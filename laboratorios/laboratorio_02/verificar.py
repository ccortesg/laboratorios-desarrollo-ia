"""Ejecuta la solucion local y conserva evidencia en una carpeta nueva."""

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
CASOS = (
    "test_c01_habilitado_con_existencias_locales_aparece",
    "test_c02_deshabilitado_se_excluye",
    "test_c03_sin_existencias_se_excluye",
    "test_c04_existencias_en_otra_ubicacion_se_excluyen",
)
FUENTES = (
    "README.md", "laboratorio.py", "pruebas.py", "verificar.py",
    "datos/esquema.sql", "datos/ejemplos.sql", "solucion/consulta.sql",
    "contexto/ENCARGO_INSUFICIENTE.md", "contexto/CONTEXTO.md",
    "contexto/ARQUITECTURA.md", "contexto/DECISIONES.md",
    "contexto/CONTINUIDAD.md", "contexto/ENCARGO_CLARO.md",
)


def escribir_json(ruta, datos):
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def sanear(texto, salida):
    texto = texto.replace(str(BASE), ".").replace(str(salida), "SALIDA")
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
        [sys.executable] + argumentos,
        cwd=BASE,
        env=entorno,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    return proceso.returncode, sanear(proceso.stdout + proceso.stderr, salida)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, required=True,
                        help="Carpeta nueva para conservar esta ejecucion.")
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
            "fecha_hora_utc": fecha,
            "estado": "BLOQUEADO",
            "motivo": "Faltan archivos del paquete; las pruebas no comenzaron.",
            "archivos_faltantes": faltantes,
            "pruebas": {"estado": "NO EJECUTADO"},
        })
        print("BLOQUEADO: faltan archivos del paquete; consulta el resumen.")
        return 2

    codigo_demo, texto_demo = ejecutar(
        ["laboratorio.py", "--version", "solucion", "--almacen", "ALFA"], salida)
    (salida / "catalogo_solucion.txt").write_text(texto_demo, encoding="utf-8")
    lineas_codigos = [linea.removeprefix("Articulos: ")
                     for linea in texto_demo.splitlines()
                     if linea.startswith("Articulos: ")]
    observados = ([codigo.strip() for codigo in lineas_codigos[0].split(",")]
                  if len(lineas_codigos) == 1 and lineas_codigos[0] != "(ninguno)"
                  else [])
    demo_aprobada = codigo_demo == 0 and observados == ["A01"]

    resultado = salida / "pruebas_solucion.json"
    codigo_pruebas, texto_pruebas = ejecutar(
        ["pruebas.py", "--version", "solucion", "--json", str(resultado)], salida)
    (salida / "pruebas_solucion.txt").write_text(texto_pruebas, encoding="utf-8")
    try:
        registro = json.loads(resultado.read_text(encoding="utf-8"))
        casos = registro["pruebas"]
        pruebas_aprobadas = (
            codigo_pruebas == 0
            and registro["total"] == 4
            and registro["aprobados"] == 4
            and registro["fallidos"] == 0
            and registro["bloqueados"] == 0
            and registro["no_ejecutados"] == 0
            and sorted(p["prueba"] for p in casos) == sorted(CASOS)
            and all(p["estado"] == "APROBADO" for p in casos)
        )
    except (OSError, ValueError, KeyError, TypeError):
        registro = None
        pruebas_aprobadas = False

    estado = "APROBADO" if demo_aprobada and pruebas_aprobadas else "FALLIDO"
    escribir_json(salida / "resumen.json", {
        "fecha_hora_utc": fecha,
        "estado": estado,
        "criterio": "La solucion devuelve A01 en ALFA y satisface C01 a C04.",
        "demostracion": {
            "estado": "APROBADO" if demo_aprobada else "FALLIDO",
            "comando": "python laboratorio.py --version solucion --almacen ALFA",
            "codigo_salida": codigo_demo,
            "articulos_esperados": ["A01"],
            "articulos_observados": observados,
        },
        "pruebas": {
            "estado": "APROBADO" if pruebas_aprobadas else "FALLIDO",
            "comando": "python pruebas.py --version solucion",
            "codigo_salida": codigo_pruebas,
            "total": registro.get("total") if registro else None,
            "aprobados": registro.get("aprobados") if registro else None,
            "fallidos": registro.get("fallidos") if registro else None,
            "bloqueados": registro.get("bloqueados") if registro else None,
            "no_ejecutados": registro.get("no_ejecutados") if registro else None,
            "detalle": "pruebas_solucion.json" if registro else None,
            "registro_legible": registro is not None,
        },
        "revision_documental_automatica": {
            "estado": "NO EJECUTADO",
            "motivo": "El script no evalua semanticamente el contexto; la revision se registra aparte.",
        },
        "herramientas_comerciales": {
            "Codex": "NO EJECUTADO",
            "GitHub Copilot": "NO EJECUTADO",
            "Grok Build": "NO EJECUTADO",
        },
        "limite": "Ejecucion local de cuatro escenarios sinteticos; no acredita validacion productiva.",
    })
    escribir_json(salida / "sha256_fuentes.json", {
        ruta: hashlib.sha256((BASE / ruta).read_bytes()).hexdigest()
        for ruta in FUENTES
    })
    print("Verificacion local: " + estado)
    print("Catalogo ALFA: " + ", ".join(observados))
    if registro:
        print("Pruebas: {} de {} aprobadas; {} fallidas.".format(
            registro["aprobados"], registro["total"], registro["fallidos"]))
    else:
        print("FALLIDO: no se obtuvo un registro de pruebas legible.")
    print("Revision documental: fuera del alcance de este verificador.")
    print("Evidencia guardada en la carpeta nueva indicada.")
    return 0 if estado == "APROBADO" else 1


if __name__ == "__main__":
    sys.exit(main())
