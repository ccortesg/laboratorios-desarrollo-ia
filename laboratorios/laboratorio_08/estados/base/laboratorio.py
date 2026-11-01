"""Catálogo sintético con conexión opcional para consultar la integración."""

import argparse
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
VERSIONES = ("solucion",)


def crear_conexion():
    """Crea una base desechable con los datos sintéticos de referencia."""
    conexion = sqlite3.connect(":memory:")
    conexion.row_factory = sqlite3.Row
    try:
        for nombre in ("esquema.sql", "ejemplos.sql"):
            conexion.executescript((BASE / "datos" / nombre).read_text(encoding="utf-8"))
        return conexion
    except Exception:
        conexion.close()
        raise


def consultar_catalogo(version, almacen="ALFA", *, conexion=None):
    """Consulta la conexión recibida; sin ella conserva la base nueva anterior."""
    if version not in VERSIONES:
        raise ValueError("Version desconocida: use solucion.")
    propia = conexion is None
    if propia:
        conexion = crear_conexion()
    try:
        consulta = (BASE / version / "consulta.sql").read_text(encoding="utf-8")
        cursor = conexion.execute(consulta, {"almacen": almacen})
        columnas = [columna[0] for columna in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    finally:
        if propia:
            conexion.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", choices=VERSIONES, required=True)
    parser.add_argument("--almacen", default="ALFA")
    opciones = parser.parse_args()
    filas = consultar_catalogo(opciones.version, opciones.almacen)
    codigos = ", ".join(fila["codigo"] for fila in filas) or "(ninguno)"
    print("Version: " + opciones.version)
    print("Almacen seleccionado: " + opciones.almacen)
    print("Articulos: " + codigos)


if __name__ == "__main__":
    main()
