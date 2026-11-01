"""Verifica los contratos heredados y la frontera HTTP; navegador real para el alcance completo."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import sqlite3
import subprocess
import sys

from soporte_web import servidor_local
from soporte.huellas_evidencia import cerrar_evidencia, ErrorHuellas
from pruebas_integracion import CASOS as CASOS_INTEGRACION
from pruebas_depuracion import CASOS as CASOS_DEPURACION
from pruebas_seguridad import CASOS as CASOS_SEGURIDAD

BASE = Path(__file__).resolve().parent
ESTADOS = ("base", "propuesta", "solucion")
CASOS = {
    "heredados": [f"C{i:02}" for i in range(1, 5)]
                 + [f"B{i:02}" for i in range(1, 7)]
                 + [f"N{i:02}" for i in range(1, 11)],
    "resumen": [f"P{i:02}" for i in range(1, 7)],
    "http": ["W01", "W02", "W03", "W04.a", "W04.b"],
    "navegador": ["W05", "W06.a", "W06.b"],
    "integracion": CASOS_INTEGRACION,
    "depuracion": CASOS_DEPURACION,
    "depuracion_navegador": ["D04"],
    "seguridad": CASOS_SEGURIDAD,
    "seguridad_navegador": ["S06"],
}
FALLOS_BASE = {"S02.a", "S02.b", "S02.c", "S03", "S04.a", "S04.b", "S05.a", "S05.b", "S06"}
FALLOS_PROPUESTA = {"S02.a", "S02.b", "S02.c"}
CONTEOS = ("ejecutados", "aprobados", "fallidos", "bloqueados",
           "no_ejecutados", "errores_de_ejecucion")


def ahora():
    return datetime.now(timezone.utc).isoformat()


def guardar(ruta, datos):
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def huella(ruta):
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def conservar_heredados():
    origen = json.loads((BASE / "PROCEDENCIA.json").read_text(encoding="utf-8"))
    filas = []
    for nombre, esperado in origen["archivos_heredados"].items():
        ruta = BASE / nombre
        actual = huella(ruta) if ruta.is_file() else None
        filas.append({"archivo": nombre, "esperado": esperado, "observado": actual,
                      "estado": "APROBADO" if actual == esperado else "FALLIDO"})
    return {"estado": "APROBADO" if all(p["estado"] == "APROBADO" for p in filas)
            else "FALLIDO", "archivos_comprobados": len(filas), "registros": filas}


def registro_sin_ejecucion(estado, bateria, clasificacion, detalle):
    return {
        "bateria": bateria, "estado_codigo": estado,
        "casos_registrados": len(CASOS[bateria]), "ejecutados": 0,
        "aprobados": 0, "fallidos": 0, "fallos_de_asercion": 0,
        "errores_de_ejecucion": 0,
        "bloqueados": len(CASOS[bateria]) if clasificacion == "BLOQUEADO" else 0,
        "no_ejecutados": len(CASOS[bateria]) if clasificacion == "NO EJECUTADO" else 0,
        "pruebas": [{"id": caso, "estado": clasificacion, "detalle": detalle,
                     "tipo_error": None} for caso in CASOS[bateria]],
    }


def comprobar_patron(datos, estado, bateria, codigo, con_navegador):
    esperado = {caso: "APROBADO" for caso in CASOS[bateria]}
    if bateria in ("navegador", "depuracion_navegador", "seguridad_navegador") and not con_navegador:
        esperado = {caso: "NO EJECUTADO" for caso in CASOS[bateria]}
    else:
        fallos = FALLOS_BASE if estado == "base" else FALLOS_PROPUESTA if estado == "propuesta" else set()
        for caso in set(esperado) & fallos:
            esperado[caso] = "FALLIDO"
    registros = datos.get("pruebas", [])
    observados = {p.get("id"): p.get("estado") for p in registros}
    if any(p.get("estado") == "BLOQUEADO" for p in registros):
        permitidos = ({"D02", "D03", "D05", "D08.a"} if bateria == "depuracion" else set(esperado))
        bloqueados = {p.get("id") for p in registros if p.get("estado") == "BLOQUEADO"}
        conteos = {
            "ejecutados": sum(e in ("APROBADO", "FALLIDO") for e in observados.values()),
            "aprobados": sum(e == "APROBADO" for e in observados.values()),
            "fallidos": sum(e == "FALLIDO" for e in observados.values()),
            "fallos_de_asercion": sum(e == "FALLIDO" for e in observados.values()),
            "bloqueados": len(bloqueados),
            "no_ejecutados": sum(e == "NO EJECUTADO" for e in observados.values()),
        }
        registrado = datos.get("casos_registrados", datos.get("criterios_registrados"))
        validos = (registrado == len(esperado)
                   and all(datos.get(k) == v for k, v in conteos.items())
                   and len(registros) == len(esperado) and len(observados) == len(esperado)
                   and set(observados) == set(esperado) and bloqueados <= permitidos
                   and all(e == esperado[i] for i, e in observados.items() if e != "BLOQUEADO")
                   and codigo == 2 and datos.get("errores_de_ejecucion") == 0
                   and all(p.get("tipo_error") == "AssertionError" for p in registros
                           if p.get("estado") == "FALLIDO"))
        return {"estado": "BLOQUEADO" if validos else "FALLIDO",
                "detalle": "Dependencia o servidor no disponible; los demás casos conservan su patrón.",
                "fallos_intencionales_esperados": [i for i, e in esperado.items() if e == "FALLIDO"]}
    n_fallos = sum(v == "FALLIDO" for v in esperado.values())
    n_noe = sum(v == "NO EJECUTADO" for v in esperado.values())
    n_aprobados = sum(v == "APROBADO" for v in esperado.values())
    registrado = datos.get("casos_registrados", datos.get("criterios_registrados"))
    condiciones = {
        "ids_unicos_y_completos": len(registros) == len(esperado)
        and len(observados) == len(esperado) and set(observados) == set(esperado),
        "estados_exactos": observados == esperado,
        "fallos_son_aserciones": all(p.get("tipo_error") == "AssertionError"
                                     for p in registros if p.get("estado") == "FALLIDO"),
        "sin_errores_de_ejecucion": datos.get("errores_de_ejecucion") == 0,
        "conteos_coherentes": registrado == len(esperado)
        and datos.get("ejecutados") == len(esperado) - n_noe
        and datos.get("aprobados") == n_aprobados
        and datos.get("fallidos") == n_fallos
        and datos.get("fallos_de_asercion") == n_fallos
        and datos.get("no_ejecutados") == n_noe and datos.get("bloqueados") == 0,
        "codigo_salida_esperado": codigo == (1 if n_fallos else 0),
    }
    return {"estado": "APROBADO" if all(condiciones.values()) else "FALLIDO",
            "condiciones": condiciones,
            "fallos_intencionales_esperados": [i for i, e in esperado.items() if e == "FALLIDO"],
            "no_ejecutados_esperados": [i for i, e in esperado.items() if e == "NO EJECUTADO"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, required=True)
    parser.add_argument("--navegador", action="store_true",
                        help="Añade Chromium real con Playwright; requerido para APROBADO global.")
    parser.add_argument("--node", default="node", help="Ejecutable Node para la prueba de navegador.")
    opciones = parser.parse_args()
    salida = opciones.salida.resolve()
    if salida.exists():
        parser.error("La carpeta de salida ya existe; usa una nueva.")
    for nombre in ("estados", "contexto", "prompts", "diferencias", "node_modules", "datos", "soporte", "evidencia"):
        protegido = BASE / nombre
        if salida == protegido or protegido in salida.parents:
            parser.error("La salida debe quedar fuera de los componentes del ejercicio.")
    salida.mkdir(parents=True)
    guardar(salida / "entorno.json", {
        "fecha_hora_utc": ahora(), "sistema": platform.system(),
        "python": platform.python_version(), "sqlite": sqlite3.sqlite_version,
        "navegador_solicitado": opciones.navegador,
        "dependencias_aplicacion": "Python estándar; recursos web locales.",
        "dependencias_navegador": "Node y Playwright para W05–W06, D04 y S06.",
        "atribucion": "Ejecución local; no acredita uso de una herramienta comercial.",
        "saneamiento": "Se omiten identidad, rutas del equipo y variables de entorno."
    })
    conservacion = conservar_heredados()
    guardar(salida / "conservacion_heredados.json", conservacion)
    # La procedencia declara los bytes de todos los archivos de base, además de
    # datos, auxiliares y comprobaciones heredadas. La base no añade la política.
    base_esperada = {r["archivo"] for r in conservacion["registros"]
                     if r["archivo"].startswith("estados/base/")}
    base_actual = {p.relative_to(BASE).as_posix() for p in (BASE / "estados/base").rglob("*")
                  if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}
    base_sin_seguridad = (conservacion["estado"] == "APROBADO"
                         and base_actual == base_esperada)
    fuentes = {}
    for archivo in sorted(BASE.rglob("*")):
        if not archivo.is_file() or salida in archivo.parents:
            continue
        relativo = archivo.relative_to(BASE)
        if any(p in ("__pycache__", "node_modules", "trabajo", "evidencia") for p in relativo.parts):
            continue
        if archivo.suffix != ".pyc":
            fuentes[relativo.as_posix()] = huella(archivo)
    guardar(salida / "sha256_fuentes.json", fuentes)
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    comandos, baterias = [], []

    def ejecutar(estado, bateria, argumentos, programa=None, url=None):
        nombre = f"{estado}_{bateria}"
        archivo_json = salida / f"{nombre}.json"
        es_node = programa is not None
        real = ([programa] if es_node else [sys.executable, "-B"]) + argumentos + ["--json", str(archivo_json)]
        publicado = (["node"] if es_node else ["python", "-B"]) + argumentos + ["--json", f"<SALIDA>/{nombre}.json"]
        if url:
            publicado = [p.replace(url, "<URL_LOCAL>") for p in publicado]
        registro = {"id": nombre, "inicio_utc": ahora(), "directorio": ".", "comando": publicado}
        try:
            proceso = subprocess.run(real, cwd=BASE, env=entorno, capture_output=True, timeout=120)
            stdout, stderr, codigo = proceso.stdout, proceso.stderr, proceso.returncode
        except (OSError, subprocess.TimeoutExpired) as error:
            stdout, stderr, codigo = b"", b"", 2
            registro["error"] = type(error).__name__
            guardar(archivo_json, registro_sin_ejecucion(
                estado, bateria, "BLOQUEADO", "No fue posible ejecutar el proceso de comprobación."))
        registro.update({"fin_utc": ahora(), "codigo_salida": codigo,
                         "stdout": f"{nombre}.stdout.txt", "stderr": f"{nombre}.stderr.txt",
                         "sha256_stdout": hashlib.sha256(stdout).hexdigest(),
                         "sha256_stderr": hashlib.sha256(stderr).hexdigest()})
        (salida / registro["stdout"]).write_bytes(stdout)
        (salida / registro["stderr"]).write_bytes(stderr)
        comandos.append(registro)
        try:
            return json.loads(archivo_json.read_text(encoding="utf-8")), codigo
        except (OSError, ValueError):
            return {"pruebas": [], "errores_de_ejecucion": 1}, codigo

    for estado in ESTADOS:
        for bateria in CASOS:
            nombre = f"{estado}_{bateria}"
            archivo_json = salida / f"{nombre}.json"
            if bateria == "heredados":
                datos, codigo = ejecutar(estado, bateria, [f"estados/{estado}/pruebas.py"])
            elif bateria == "resumen":
                datos, codigo = ejecutar(estado, bateria,
                                         ["pruebas_resumen.py", "--directorio", f"estados/{estado}"])
            elif bateria == "http":
                datos, codigo = ejecutar(estado, bateria, ["pruebas_http.py", "--directorio", f"estados/{estado}"])
            elif bateria == "integracion":
                datos, codigo = ejecutar(estado, bateria, ["pruebas_integracion.py", "--directorio", f"estados/{estado}"])
            elif bateria == "depuracion":
                datos, codigo = ejecutar(estado, bateria, ["pruebas_depuracion.py", "--directorio", f"estados/{estado}"])
            elif bateria == "seguridad":
                datos, codigo = ejecutar(estado, bateria, ["pruebas_seguridad.py", "--directorio", f"estados/{estado}"])
            elif not opciones.navegador:
                motivo = "No se solicitó --navegador; el recorrido completo no fue ejecutado."
                datos = registro_sin_ejecucion(estado, bateria, "NO EJECUTADO", motivo)
                codigo = 0
                guardar(archivo_json, datos)
                comandos.append({"id": nombre, "comando": None, "codigo_salida": None,
                                 "estado": "NO EJECUTADO", "motivo": motivo})
            elif bateria == "depuracion_navegador":
                datos, codigo = ejecutar(estado, bateria, ["pruebas_recorrido.py", "--directorio", f"estados/{estado}", "--node", opciones.node])
            elif bateria == "seguridad_navegador":
                datos, codigo = ejecutar(estado, bateria, ["pruebas_seguridad_navegador.py", "--directorio", f"estados/{estado}", "--node", opciones.node])
            else:
                try:
                    # Cada estado carga también sus propios adaptadores nuevos.
                    for nombre_modulo in ("persistencia", "origen", "politica_consulta"):
                        sys.modules.pop(nombre_modulo, None)
                    with servidor_local(BASE / "estados" / estado) as url:
                        datos, codigo = ejecutar(estado, bateria,
                            ["pruebas_navegador.cjs", "--url", url, "--estado", estado],
                            programa=opciones.node, url=url)
                except OSError as error:
                    datos = registro_sin_ejecucion(estado, bateria, "BLOQUEADO",
                                                   "No fue posible iniciar el servidor local.")
                    codigo = 2
                    guardar(archivo_json, datos)
                    comandos.append({"id": nombre, "comando": None, "codigo_salida": None,
                                     "estado": "BLOQUEADO", "error": type(error).__name__})
            patron = comprobar_patron(datos, estado, bateria, codigo, opciones.navegador)
            baterias.append({"estado_codigo": estado, "bateria": bateria,
                             "resultado": archivo_json.name, "patron": patron,
                             **{k: datos.get(k, 0) for k in CONTEOS}})
            print(nombre + ": patrón " + patron["estado"])
    guardar(salida / "comandos.json", {
        "convenciones": "python y node representan los ejecutables elegidos; <SALIDA> es "
        "el destino nuevo; <URL_LOCAL> es el servidor real iniciado en puerto libre. "
        "Las salidas de procesos se conservan como bytes sin transformación. "
        "Las entradas sin comando representan casos expresamente no ejecutados o bloqueados.",
        "registros": comandos,
    })
    try:
        huellas_salidas = cerrar_evidencia(salida, lambda texto: texto.replace(str(BASE), "<LABORATORIO>").replace(str(salida), "<SALIDA>"))
    except ErrorHuellas:
        huellas_salidas = {"estado": "FALLIDO", "comprobadas": 0, "coincidentes": 0,
                          "detalle": "Las huellas no pudieron cerrarse; la captura no se reinterpreta."}
    guardar(salida / "huellas_salidas.json", huellas_salidas)
    fallo = huellas_salidas["estado"] != "APROBADO" or not base_sin_seguridad or conservacion["estado"] != "APROBADO" or any(
        b["patron"]["estado"] == "FALLIDO" for b in baterias)
    bloqueo = any(b["patron"]["estado"] == "BLOQUEADO" for b in baterias)
    estado_global = ("FALLIDO" if fallo else "BLOQUEADO" if bloqueo else
                     "APROBADO" if opciones.navegador else "NO EJECUTADO")
    alcance_ejecutado = "FALLIDO" if fallo else "BLOQUEADO" if bloqueo else "APROBADO"
    resumen = {
        "estado": estado_global, "alcance_ejecutado": alcance_ejecutado,
        "extremo_a_extremo": estado_global,
        "fecha_hora_utc": ahora(), "navegador_solicitado": opciones.navegador,
        "interpretacion": "APROBADO global exige HTTP y navegador reales. Los nueve fallos S de base "
        "son brechas frente a la política nueva; S02.a/S02.b/S02.c en propuesta detectan el defecto "
        "didáctico. Conservan FALLIDO y todos los heredados deben aprobar. Sin --navegador, "
        "salida 0 solo aprueba el alcance de dominio/terminal/HTTP y no el recorrido completo.",
        "baterias": baterias,
        "totales": {k: sum(b[k] for b in baterias) for k in CONTEOS},
        "conservacion_heredados": conservacion["estado"],
        "base_sin_incremento_seguridad": "APROBADO" if base_sin_seguridad else "FALLIDO",
        "huellas_salidas": huellas_salidas,
        "criterios_solucion": 56, "casos_solucion": 74,
        "herramientas_comerciales": "NO EJECUTADO por este verificador",
        "limites": ["No demuestra una sesión comercial ni producción.",
                    "W06.b es un fallo de transporte provocado en el navegador de prueba.",
                    "I06 comprueba rechazo de entrada y escritura; no simula fallos físicos de energía.",
                    "D04 conserva el servidor vivo y ejecuta la importación CLI contra su archivo.",
                    "S06 consulta datos importados, recibe un rechazo HTTP real y recupera la pantalla.",
                    "S07 es una búsqueda sintética: no acredita ausencia general de inyección.",
                    "S08 interrumpe de forma controlada un archivo local aislado, no un sistema externo.",
                    "No demuestra autenticación, permisos por usuario, concurrencia ni resistencia global a denegación de servicio.",
                    "No acredita Windows, escritores concurrentes ni uso productivo."]
    }
    guardar(salida / "resumen.json", resumen)
    print("Estado global: " + estado_global)
    print("Alcance ejecutado: " + alcance_ejecutado)
    print("Extremo a extremo: " + estado_global)
    print(json.dumps(resumen["totales"], ensure_ascii=False))
    return 1 if fallo else 2 if bloqueo else 0


if __name__ == "__main__":
    raise SystemExit(main())
