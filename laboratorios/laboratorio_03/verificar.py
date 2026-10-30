"""Ejecuta los estados y conserva evidencia local en una carpeta nueva."""

import argparse
import hashlib
import json
import os
import platform
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent
ESTADOS = ("base", "generado", "refactorizado", "defecto", "corregido")
CRITERIOS = ("C01", "C02", "C03", "C04", "B01", "B02", "B03", "B04", "B05", "B06")
FUENTES = (
    "README.md", "ALCANCE.md", "laboratorio.py", "recorrido.py",
    "comparar.py", "pruebas.py", "verificar.py",
    "datos/esquema.sql", "datos/ejemplos.sql", "solucion/consulta.sql",
    "estados/__init__.py", "estados/generado.py", "estados/refactorizado.py",
    "estados/defecto.py", "estados/corregido.py",
    "contexto/CONTEXTO.md", "contexto/ARQUITECTURA.md",
    "contexto/DECISIONES.md", "contexto/CONTINUIDAD.md",
    "prompts/01_generar.md", "prompts/02_refactorizar.md", "prompts/03_depurar.md",
    "diferencias/01_generar.diff", "diferencias/02_refactorizar.diff",
    "diferencias/03_introducir_defecto.diff", "diferencias/04_corregir.diff",
)
A01 = [{"codigo": "A01", "nombre": "Articulo local"}]
A04 = [{"codigo": "A04", "nombre": "Articulo de otra ubicacion"}]


def escribir_json(ruta, datos):
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def sanear(texto, salida):
    texto = texto.replace(str(salida), "SALIDA").replace(str(BASE), ".")
    return re.sub(
        r'File "([^\"]+)"',
        lambda m: 'File "' + m.group(1).replace("\\", "/").split("/")[-1] + '"',
        texto,
    )


def ejecutar(argumentos, salida):
    entorno = os.environ.copy()
    entorno["PYTHONDONTWRITEBYTECODE"] = "1"
    entorno["PYTHONIOENCODING"] = "utf-8"
    proceso = subprocess.run(
        [sys.executable] + argumentos, cwd=BASE, env=entorno,
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    return proceso.returncode, sanear(proceso.stdout + proceso.stderr, salida)


def cumple_patron(registro, estado, codigo):
    """Exige el patron exacto; no acepta cualquier fallo como demostracion."""
    esperados = {criterio: "APROBADO" for criterio in CRITERIOS}
    if estado == "base":
        esperados.update({criterio: "NO EJECUTADO" for criterio in CRITERIOS[4:]})
    elif estado == "defecto":
        esperados.update({"B05": "FALLIDO", "B06": "FALLIDO"})
    try:
        casos = registro["pruebas"]
        conteos = {
            "criterios_registrados": 10,
            "ejecutados": 4 if estado == "base" else 10,
            "aprobados": 4 if estado == "base" else (8 if estado == "defecto" else 10),
            "fallidos": 2 if estado == "defecto" else 0,
            "fallos_de_asercion": 2 if estado == "defecto" else 0,
            "errores_de_ejecucion": 0,
            "bloqueados": 0,
            "no_ejecutados": 6 if estado == "base" else 0,
        }
        return (
            codigo == (1 if estado == "defecto" else 0)
            and registro["estado_codigo"] == estado
            and len(casos) == 10
            and sorted(p["id"] for p in casos) == sorted(CRITERIOS)
            and all(p["estado"] == esperados[p["id"]] for p in casos)
            and all(registro[k] == valor for k, valor in conteos.items())
            and all(p["tipo_error"] == "AssertionError"
                    for p in casos if p["estado"] == "FALLIDO")
        )
    except (KeyError, TypeError):
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, required=True,
                        help="Carpeta nueva para esta ejecucion.")
    opciones = parser.parse_args()
    salida = opciones.salida.resolve()
    try:
        salida.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("BLOQUEADO: la carpeta de salida ya existe; utiliza un nombre nuevo.")
        return 2
    except OSError as error:
        print("BLOQUEADO: no se pudo crear la carpeta de salida ({}).".format(
            type(error).__name__))
        return 2

    fecha = datetime.now(timezone.utc).isoformat(timespec="seconds")
    escribir_json(salida / "entorno.json", {
        "fecha_hora_utc": fecha,
        "python": platform.python_version(),
        "implementacion_python": platform.python_implementation(),
        "sqlite": sqlite3.sqlite_version,
        "sistema": platform.system(),
        "dependencias": "Solo biblioteca estandar de Python",
        "base_de_datos": "SQLite en memoria, reconstruida en cada consulta",
        "red": "No utilizada por el laboratorio",
    })
    faltantes = [ruta for ruta in FUENTES if not (BASE / ruta).is_file()]
    if faltantes:
        escribir_json(salida / "resumen.json", {
            "fecha_hora_utc": fecha, "estado": "BLOQUEADO",
            "motivo": "Faltan archivos del paquete; no comenzaron las comprobaciones.",
            "archivos_faltantes": faltantes,
            "pruebas": {"estado": "NO EJECUTADO"},
        })
        print("BLOQUEADO: faltan archivos; consulta el resumen de evidencia.")
        return 2

    baterias = []
    for estado in ESTADOS:
        archivo = salida / ("pruebas_" + estado + ".json")
        codigo, texto = ejecutar(
            ["pruebas.py", "--estado", estado, "--json", str(archivo)], salida)
        (salida / ("pruebas_" + estado + ".txt")).write_text(texto, encoding="utf-8")
        try:
            registro = json.loads(archivo.read_text(encoding="utf-8"))
            if not isinstance(registro, dict):
                registro = None
            aprobado = cumple_patron(registro, estado, codigo)
        except (OSError, ValueError):
            registro, aprobado = None, False
        baterias.append({
            "estado_codigo": estado,
            "evaluacion_del_recorrido": "APROBADO" if aprobado else "FALLIDO",
            "comando": "python pruebas.py --estado " + estado,
            "codigo_salida": codigo,
            "criterios_registrados": registro.get("criterios_registrados") if registro else None,
            "ejecutados": registro.get("ejecutados") if registro else None,
            "aprobados": registro.get("aprobados") if registro else None,
            "fallidos": registro.get("fallidos") if registro else None,
            "no_ejecutados": registro.get("no_ejecutados") if registro else None,
            "fallos_intencionales_esperados": ["B05", "B06"] if estado == "defecto" else [],
            "detalle": archivo.name if registro else None,
        })

    observaciones = []
    experimentos = (
        ("base_beta", "base", "", A04),
        ("defecto_beta_vacio", "defecto", "", A01),
        ("defecto_beta_nombre", "defecto", " OTRA ", []),
        ("corregido_beta_vacio", "corregido", "", A04),
        ("corregido_beta_nombre", "corregido", " OTRA ", A04),
    )
    for identificador, estado, termino, previsto in experimentos:
        argumentos = ["recorrido.py", "--estado", estado, "--almacen", "BETA"]
        if estado != "base":
            argumentos += ["--texto", termino]
        codigo, texto = ejecutar(argumentos, salida)
        (salida / (identificador + ".txt")).write_text(texto, encoding="utf-8")
        try:
            respuesta = json.loads(texto)
            observado = respuesta["articulos"]
            legible = (respuesta["estado"] == estado and respuesta["almacen"] == "BETA"
                       and respuesta["texto"] == termino)
        except (ValueError, KeyError, TypeError):
            observado, legible = None, False
        cumple_experimento = codigo == 0 and legible and observado == previsto
        observaciones.append({
            "id": identificador,
            "estado_codigo": estado,
            "comando": "python recorrido.py --estado " + estado + " --almacen BETA"
                       + (' --texto "' + termino + '"' if estado != "base" else ""),
            "codigo_salida": codigo,
            "entrada": {"almacen": "BETA", "texto": termino},
            "esperado_por_regla": A04,
            "esperado_en_este_estado_didactico": previsto,
            "observado": observado,
            "estado_del_comportamiento": "APROBADO" if codigo == 0 and legible and observado == A04 else "FALLIDO",
            "evaluacion_del_experimento": "APROBADO" if cumple_experimento else "FALLIDO",
        })
    escribir_json(salida / "observacion_diagnostica.json", {
        "fecha_hora_utc": fecha,
        "metodo": "Ejecucion local de la consulta base y de dos variantes de busqueda.",
        "observaciones": observaciones,
        "interpretacion": ("Las cinco salidas coinciden con el experimento previsto; contrastar la causa con la llamada a la consulta."
                           if all(o["evaluacion_del_experimento"] == "APROBADO" for o in observaciones)
                           else "Una o mas salidas difieren del experimento previsto; investigar antes de atribuir una causa."),
        "limite": "Cinco ejecuciones sinteticas, no una prueba productiva ni evaluacion de herramientas comerciales.",
    })

    aprobado = (all(b["evaluacion_del_recorrido"] == "APROBADO" for b in baterias)
                and all(o["evaluacion_del_experimento"] == "APROBADO" for o in observaciones))
    estado_final = "APROBADO" if aprobado else "FALLIDO"
    escribir_json(salida / "sha256_fuentes.json", {
        ruta: hashlib.sha256((BASE / ruta).read_bytes()).hexdigest()
        for ruta in FUENTES
    })
    escribir_json(salida / "resumen.json", {
        "fecha_hora_utc": fecha,
        "estado": estado_final,
        "criterio": "Patron exacto de las cinco baterias y cinco observaciones diagnosticas.",
        "baterias": baterias,
        "observaciones_diagnosticas": {
            "total": len(observaciones),
            "evaluacion_del_experimento": "APROBADO" if all(o["evaluacion_del_experimento"] == "APROBADO" for o in observaciones) else "FALLIDO",
            "detalle": "observacion_diagnostica.json",
        },
        "revision_documental_automatica": {
            "estado": "NO EJECUTADO",
            "motivo": "El script no evalua semanticamente prompts ni documentos.",
        },
        "herramientas_comerciales": {
            "Codex": "NO EJECUTADO",
            "GitHub Copilot": "NO EJECUTADO",
            "Grok Build": "NO EJECUTADO",
        },
        "limite": "Escenarios locales sinteticos; no prueba equivalencia universal, eficacia de prompts ni preparacion productiva.",
    })
    print("Verificacion del recorrido: " + estado_final)
    for bateria in baterias:
        print("{estado_codigo}: {aprobados} aprobados; {fallidos} fallidos; "
              "{no_ejecutados} no ejecutados; salida {codigo_salida}.".format(**bateria))
    print("Los fallos B05 y B06 de defecto son intencionales; no se aceptan otros fallos.")
    print("Evidencia guardada en la carpeta nueva indicada.")
    return 0 if aprobado else 1


if __name__ == "__main__":
    raise SystemExit(main())
