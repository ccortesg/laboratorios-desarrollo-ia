"""Ejecuta seis baterías y distingue fallos didácticos de problemas nuevos."""

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

BASE = Path(__file__).resolve().parent
ESTADOS = ("base", "propuesta", "solucion")
HEREDADOS = [f"C{i:02}" for i in range(1, 5)] + [
    f"B{i:02}" for i in range(1, 7)] + [f"N{i:02}" for i in range(1, 11)]
NUEVOS = [f"P{i:02}" for i in range(1, 7)]


def ahora():
    return datetime.now(timezone.utc).isoformat()


def guardar(ruta, datos):
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def huella(ruta):
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def conservar_heredados():
    origen = json.loads((BASE / "PROCEDENCIA.json").read_text(encoding="utf-8"))
    registros = []
    for estado in ESTADOS:
        for nombre, esperada in origen["archivos_heredados"].items():
            archivo = BASE / "estados" / estado / nombre
            observada = huella(archivo) if archivo.is_file() else None
            registros.append({"archivo": f"estados/{estado}/{nombre}",
                              "sha256_esperado": esperada,
                              "sha256_observado": observada,
                              "estado": "APROBADO" if observada == esperada
                              else "FALLIDO"})
    return {"estado": "APROBADO" if all(r["estado"] == "APROBADO"
                                          for r in registros) else "FALLIDO",
            "archivos": registros}


def comprobar_patron(datos, estado, bateria, codigo_salida):
    ids = HEREDADOS if bateria == "heredados" else NUEVOS
    esperados = {identificador: "APROBADO" for identificador in ids}
    if bateria == "resumen" and estado == "base":
        esperados = {identificador: "NO EJECUTADO" for identificador in ids}
    if bateria == "resumen" and estado == "propuesta":
        esperados.update({"P04": "FALLIDO", "P05": "FALLIDO"})
    registros = datos.get("pruebas", [])
    observados = {p.get("id"): p.get("estado") for p in registros}
    fallos = [p for p in registros if p.get("estado") == "FALLIDO"]
    n_fallos = sum(valor == "FALLIDO" for valor in esperados.values())
    n_omitidos = sum(valor == "NO EJECUTADO" for valor in esperados.values())
    n_aprobados = sum(valor == "APROBADO" for valor in esperados.values())
    condiciones = {
        "ids_unicos_y_completos": len(registros) == len(ids)
        and len(observados) == len(ids) and set(observados) == set(ids),
        "estados_exactos": observados == esperados,
        "fallos_son_aserciones": all(p.get("tipo_error") == "AssertionError"
                                     for p in fallos),
        "sin_errores_de_ejecucion": datos.get("errores_de_ejecucion") == 0,
        "conteos_coherentes": (
            datos.get("criterios_registrados") == len(ids)
            and datos.get("ejecutados") == len(ids) - n_omitidos
            and datos.get("aprobados") == n_aprobados
            and datos.get("fallidos") == n_fallos
            and datos.get("fallos_de_asercion") == n_fallos
            and datos.get("no_ejecutados") == n_omitidos
            and datos.get("bloqueados") == 0),
        "codigo_salida_esperado": codigo_salida == (1 if n_fallos else 0),
    }
    return {"estado": "APROBADO" if all(condiciones.values()) else "FALLIDO",
            "condiciones": condiciones,
            "fallos_intencionales_esperados": [i for i, e in esperados.items()
                                               if e == "FALLIDO"],
            "no_ejecutados_esperados": [i for i, e in esperados.items()
                                         if e == "NO EJECUTADO"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, required=True,
                        help="Carpeta nueva para conservar esta ejecución.")
    opciones = parser.parse_args()
    salida = opciones.salida.resolve()
    if salida.exists():
        parser.error("La carpeta de salida ya existe; elija una nueva.")
    for nombre in ("estados", "contexto", "prompts", "diferencias"):
        protegido = BASE / nombre
        if salida == protegido or protegido in salida.parents:
            parser.error("La evidencia debe quedar fuera de los componentes del ejercicio.")
    salida.mkdir(parents=True)
    guardar(salida / "entorno.json", {
        "fecha_utc": ahora(), "sistema": platform.system(),
        "implementacion_python": platform.python_implementation(),
        "version_python": platform.python_version(),
        "version_sqlite": sqlite3.sqlite_version,
        "dependencias_externas": [], "ejecucion": "Local",
        "sesion_copilot": "NO EJECUTADO por este verificador",
        "saneamiento": "Se omiten usuario, equipo, rutas absolutas y variables de entorno."
    })
    conservacion = conservar_heredados()
    guardar(salida / "conservacion_heredados.json", conservacion)
    base_sin_incremento = not (BASE / "estados/base/resumen.py").exists()
    fuentes = {}
    for archivo in sorted(BASE.rglob("*")):
        if not archivo.is_file() or salida in archivo.parents:
            continue
        relativo = archivo.relative_to(BASE)
        if "__pycache__" in relativo.parts or relativo.parts[0] == "evidencia":
            continue
        fuentes[relativo.as_posix()] = huella(archivo)
    guardar(salida / "sha256_fuentes.json", fuentes)
    comandos, baterias = [], []
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8",
                   PYTHONDONTWRITEBYTECODE="1")
    for estado in ESTADOS:
        for bateria in ("heredados", "resumen"):
            nombre = f"{estado}_{bateria}"
            archivo_json = salida / f"{nombre}.json"
            argumentos = ([f"estados/{estado}/pruebas.py"] if bateria == "heredados"
                          else ["pruebas_resumen.py", "--estado", estado])
            comando = [sys.executable, "-B", *argumentos, "--json", str(archivo_json)]
            registro = {"id": nombre, "inicio_utc": ahora(),
                        "directorio": ".", "comando": ["python", "-B", *argumentos,
                        "--json", f"<SALIDA>/{nombre}.json"]}
            try:
                proceso = subprocess.run(comando, cwd=BASE, capture_output=True,
                                         env=entorno, timeout=45)
                stdout, stderr = proceso.stdout, proceso.stderr
                codigo = proceso.returncode
                registro.update({"codigo_salida": codigo, "fin_utc": ahora()})
            except (OSError, subprocess.TimeoutExpired) as error:
                stdout, stderr, codigo = b"", b"", None
                registro.update({"codigo_salida": None, "fin_utc": ahora(),
                                 "error": type(error).__name__})
            (salida / f"{nombre}.stdout.txt").write_bytes(stdout)
            (salida / f"{nombre}.stderr.txt").write_bytes(stderr)
            registro.update({"stdout": f"{nombre}.stdout.txt",
                             "stderr": f"{nombre}.stderr.txt",
                             "sha256_stdout": hashlib.sha256(stdout).hexdigest(),
                             "sha256_stderr": hashlib.sha256(stderr).hexdigest()})
            comandos.append(registro)
            try:
                datos = json.loads(archivo_json.read_text(encoding="utf-8"))
                patron = comprobar_patron(datos, estado, bateria, codigo)
                baterias.append({"estado_codigo": estado, "bateria": bateria,
                                 "resultado": archivo_json.name, "patron": patron,
                                 **{k: datos[k] for k in ("ejecutados", "aprobados",
                                  "fallidos", "no_ejecutados", "errores_de_ejecucion")}})
            except (OSError, ValueError, KeyError) as error:
                baterias.append({"estado_codigo": estado, "bateria": bateria,
                                 "patron": {"estado": "FALLIDO"},
                                 "error": type(error).__name__})
            print(nombre + ": patrón " + baterias[-1]["patron"]["estado"])
    guardar(salida / "comandos.json", {
        "convenciones": "python representa el mismo intérprete que ejecutó verificar.py; "
        "<SALIDA> representa la carpeta nueva indicada. Sólo se sustituyen esas rutas. "
        "stdout y stderr se conservan como bytes sin transformación.",
        "registros": comandos,
    })
    correcto = base_sin_incremento and conservacion["estado"] == "APROBADO" and all(
        b["patron"]["estado"] == "APROBADO" for b in baterias)
    resumen = {
        "estado": "APROBADO" if correcto else "FALLIDO", "fecha_utc": ahora(),
        "alcance": "El dictamen evalúa la reproducción de los estados didácticos. "
        "Los fallos deliberados siguen siendo FALLIDO en sus respectivas pruebas.",
        "baterias": baterias,
        "totales": {k: sum(b.get(k, 0) for b in baterias) for k in
                    ("ejecutados", "aprobados", "fallidos", "no_ejecutados",
                     "errores_de_ejecucion")},
        "conservacion_heredados": conservacion["estado"],
        "base_sin_incremento": "APROBADO" if base_sin_incremento else "FALLIDO",
        "copilot": "NO EJECUTADO por este verificador",
        "limites": ["No demuestra una interacción comercial.",
                    "No acredita calidad fuera de los criterios enumerados.",
                    "Los nuevos criterios se omiten únicamente en el estado base."]
    }
    guardar(salida / "resumen.json", resumen)
    print("Verificación: " + resumen["estado"])
    print(json.dumps(resumen["totales"], ensure_ascii=False))
    return 0 if correcto else 1


if __name__ == "__main__":
    raise SystemExit(main())
