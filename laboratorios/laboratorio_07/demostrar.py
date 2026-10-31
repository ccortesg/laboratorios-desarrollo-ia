"""Importa y consulta en una misma conexión local desechable."""

import argparse
import importlib
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent


def existencias(conexion):
    return [list(fila) for fila in conexion.execute(
        "SELECT articulo, almacen, cantidad FROM existencias ORDER BY articulo, almacen")]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    origen = parser.add_mutually_exclusive_group(required=True)
    origen.add_argument("--estado", choices=("propuesta", "solucion"))
    origen.add_argument("--directorio", type=Path, help="Copia de práctica con importacion.py.")
    parser.add_argument("--archivo", type=Path, required=True)
    parser.add_argument("--almacen", default="ALFA")
    parser.add_argument("--nombre", default="")
    parser.add_argument("--repeticiones", type=int, choices=(1, 2), default=1)
    opciones = parser.parse_args()
    directorio = opciones.directorio.resolve() if opciones.directorio else BASE / "estados" / opciones.estado
    sys.path.insert(0, str(directorio))
    laboratorio = importlib.import_module("laboratorio")
    importar = importlib.import_module("importacion").importar_existencias
    resumir = importlib.import_module("resumen").resumir_catalogo
    conexion = laboratorio.crear_conexion()
    try:
        resultado = {"estado_codigo": opciones.estado or "copia_del_lector",
                     "antes": existencias(conexion), "importaciones": []}
        for numero in range(1, opciones.repeticiones + 1):
            informe = importar(conexion, opciones.archivo)
            resultado["importaciones"].append({"numero": numero, "informe": informe,
                "existencias": existencias(conexion),
                "catalogo": resumir(opciones.almacen, opciones.nombre, conexion=conexion)})
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        return 0 if all(p["informe"]["estado"] == "APLICADO" for p in resultado["importaciones"]) else 1
    finally:
        conexion.close()


if __name__ == "__main__":
    raise SystemExit(main())
