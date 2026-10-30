"""Ejecuta ambas versiones y guarda evidencia local sin rutas ni identidad del host."""

import argparse
import hashlib
import json
import os
import platform
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from laboratorio import BASE, VERSIONES, consultar_catalogo


def escribir_json(ruta, contenido):
    ruta.write_text(
        json.dumps(contenido, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sanear(texto):
    texto = texto.replace(str(BASE), ".")
    # Un traceback conserva el nombre del archivo, nunca la ruta del equipo.
    return re.sub(
        r'File "([^\"]+)"',
        lambda m: 'File "' + m.group(1).replace("\\", "/").split("/")[-1] + '"',
        texto,
    )


def ejecutar(argumentos):
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
    return proceso.returncode, sanear(proceso.stdout + proceso.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, default=Path("evidencia"))
    opciones = parser.parse_args()
    salida = opciones.salida.resolve()
    salida.mkdir(parents=True, exist_ok=True)
    zona = timezone(timedelta(hours=-7))
    fecha = datetime.now(zona).isoformat(timespec="seconds")

    entorno = {
        "fecha_hora": fecha,
        "desfase_utc": "-07:00",
        "python": platform.python_version(),
        "implementacion_python": platform.python_implementation(),
        "sqlite": sqlite3.sqlite_version,
        "sistema": platform.system(),
        "dependencias": "Solo biblioteca estandar de Python",
        "base_de_datos": "SQLite en memoria, reconstruida en cada consulta",
        "red": "No utilizada por el laboratorio",
    }
    escribir_json(salida / "entorno.json", entorno)

    versiones = {}
    for version in VERSIONES:
        resultado_json = salida / ("pruebas_" + version + ".json")
        codigo, texto = ejecutar(
            ["pruebas.py", "--version", version, "--json", str(resultado_json)]
        )
        (salida / ("pruebas_" + version + ".txt")).write_text(
            texto, encoding="utf-8"
        )
        datos = json.loads(resultado_json.read_text(encoding="utf-8"))
        codigo_demo, texto_demo = ejecutar(
            ["laboratorio.py", "--version", version, "--almacen", "ALFA"]
        )
        (salida / ("catalogo_" + version + ".txt")).write_text(
            texto_demo, encoding="utf-8"
        )
        versiones[version] = {
            "estado": "APROBADO" if codigo == 0 else "FALLIDO",
            "fallo_intencional": False,
            "comando_pruebas": "python pruebas.py --version " + version,
            "codigo_salida_pruebas": codigo,
            "comando_demostracion": (
                "python laboratorio.py --version " + version + " --almacen ALFA"
            ),
            "codigo_salida_demostracion": codigo_demo,
            "articulos_observados": [
                fila["codigo"] for fila in consultar_catalogo(version, "ALFA")
            ],
            "total": datos["total"],
            "aprobados": datos["aprobados"],
            "fallidos": datos["fallidos"],
            "fallos_de_asercion": datos["fallos_de_asercion"],
            "errores_de_ejecucion": datos["errores_de_ejecucion"],
            "bloqueados": datos["bloqueados"],
            "no_ejecutados": datos["no_ejecutados"],
            "detalle_pruebas": "pruebas_" + version + ".json",
        }

    inicial = versiones["inicial"]
    solucion = versiones["solucion"]
    casos_iniciales = json.loads(
        (salida / "pruebas_inicial.json").read_text(encoding="utf-8")
    )["pruebas"]
    fallo_c04 = [p["prueba"] for p in casos_iniciales if p["estado"] == "FALLIDO"]
    inicial_esperado = (
        inicial["codigo_salida_pruebas"] == 1
        and inicial["total"] == 4
        and inicial["aprobados"] == 3
        and inicial["fallidos"] == 1
        and inicial["fallos_de_asercion"] == 1
        and inicial["errores_de_ejecucion"] == 0
        and inicial["bloqueados"] == 0
        and inicial["no_ejecutados"] == 0
        and fallo_c04 == ["test_c04_existencias_en_otra_ubicacion_se_excluyen"]
        and inicial["articulos_observados"] == ["A01", "A04"]
        and inicial["codigo_salida_demostracion"] == 0
    )
    solucion_esperada = (
        solucion["codigo_salida_pruebas"] == 0
        and solucion["total"] == 4
        and solucion["aprobados"] == 4
        and solucion["fallidos"] == 0
        and solucion["fallos_de_asercion"] == 0
        and solucion["errores_de_ejecucion"] == 0
        and solucion["bloqueados"] == 0
        and solucion["no_ejecutados"] == 0
        and solucion["articulos_observados"] == ["A01"]
        and solucion["codigo_salida_demostracion"] == 0
    )
    inicial["fallo_intencional"] = inicial_esperado
    esperado = inicial_esperado and solucion_esperada
    resumen = {
        "fecha_hora": fecha,
        "desfase_utc": "-07:00",
        "estado_del_recorrido_didactico": "APROBADO" if esperado else "FALLIDO",
        "criterio_del_recorrido": (
            "El defecto inicial incumple solo C04; la solucion satisface los cuatro "
            "criterios usando la misma suite y los mismos datos."
        ),
        "versiones": versiones,
        "limite": (
            "Evidencia de ejecucion local del laboratorio sintetico. "
            "No acredita uso de Codex, Copilot o Grok Build ni validacion productiva."
        ),
        "herramientas_comerciales": {
            "Codex": "NO EJECUTADO",
            "GitHub Copilot": "NO EJECUTADO",
            "Grok Build": "NO EJECUTADO",
        },
    }
    escribir_json(salida / "resumen.json", resumen)

    fuentes = [
        BASE / "README.md",
        BASE / "laboratorio.py",
        BASE / "pruebas.py",
        BASE / "verificar.py",
        BASE / "datos" / "esquema.sql",
        BASE / "datos" / "ejemplos.sql",
        BASE / "inicial" / "consulta.sql",
        BASE / "solucion" / "consulta.sql",
    ]
    hashes = {
        fuente.relative_to(BASE).as_posix(): hashlib.sha256(fuente.read_bytes()).hexdigest()
        for fuente in fuentes
    }
    escribir_json(salida / "sha256_fuentes.json", hashes)
    print("Recorrido didactico: " + resumen["estado_del_recorrido_didactico"])
    for version, datos in versiones.items():
        print(
            "{}: {} | {} aprobados, {} fallidos | codigo {}".format(
                version,
                datos["estado"],
                datos["aprobados"],
                datos["fallidos"],
                datos["codigo_salida_pruebas"],
            )
        )
    print("Evidencia guardada en el directorio de salida indicado.")
    return 0 if esperado else 1


if __name__ == "__main__":
    sys.exit(main())
