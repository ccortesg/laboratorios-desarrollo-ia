"""Muestra la consulta base o una busqueda de un estado del ejercicio."""

import argparse
import importlib
import json

from laboratorio import consultar_catalogo


ESTADOS = ("base", "generado", "refactorizado", "defecto", "corregido")


def cargar_busqueda(estado):
    """Selecciona una implementacion explicita; base no tiene busqueda."""
    if estado not in ESTADOS[1:]:
        raise ValueError("El estado debe incluir una implementacion de busqueda.")
    return importlib.import_module("estados." + estado).buscar_catalogo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--estado", choices=ESTADOS, required=True)
    parser.add_argument("--almacen", default="ALFA")
    parser.add_argument("--texto", default="")
    opciones = parser.parse_args()
    if opciones.estado == "base":
        if opciones.texto:
            parser.error("base no implementa busqueda; omite --texto.")
        articulos = consultar_catalogo("solucion", opciones.almacen)
    else:
        buscar = cargar_busqueda(opciones.estado)
        articulos = buscar(opciones.almacen, opciones.texto)
    print(json.dumps({"estado": opciones.estado,
                      "almacen": opciones.almacen,
                      "texto": opciones.texto,
                      "articulos": articulos}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
