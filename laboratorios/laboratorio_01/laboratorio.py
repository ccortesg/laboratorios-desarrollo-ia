"""Catalogo sintetico para observar una regla de disponibilidad por almacen."""

import argparse
import sqlite3
from pathlib import Path


BASE = Path(__file__).resolve().parent
VERSIONES = ("inicial", "solucion")


def consultar_catalogo(version, almacen="ALFA"):
    """Devuelve registros de una base nueva en memoria; no modifica archivos."""
    if version not in VERSIONES:
        raise ValueError("Version desconocida: use inicial o solucion.")

    conexion = sqlite3.connect(":memory:")
    conexion.row_factory = sqlite3.Row
    try:
        conexion.executescript(
            (BASE / "datos" / "esquema.sql").read_text(encoding="utf-8")
        )
        conexion.executescript(
            (BASE / "datos" / "ejemplos.sql").read_text(encoding="utf-8")
        )
        consulta = (BASE / version / "consulta.sql").read_text(encoding="utf-8")
        # El parametro se enlaza en SQLite; no se concatena al texto SQL.
        # La version inicial lo recibe pero omite utilizarlo en la consulta.
        filas = conexion.execute(consulta, {"almacen": almacen}).fetchall()
        return [dict(fila) for fila in filas]
    finally:
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
