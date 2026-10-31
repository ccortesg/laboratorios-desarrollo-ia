"""Resumen local del catálogo disponible; implementación didáctica."""

import argparse
import json

from catalogo import buscar_catalogo


def resumir_catalogo(almacen, texto=""):
    """Cuenta artículos disponibles que coinciden con la búsqueda por nombre."""
    articulos = buscar_catalogo(almacen, texto)
    return {
        "almacen": almacen,
        "total": len(articulos),
        "codigos": [articulo["codigo"] for articulo in articulos],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--almacen", required=True)
    parser.add_argument("--nombre", default="")
    opciones = parser.parse_args()
    resultado = resumir_catalogo(opciones.almacen, opciones.nombre)
    print(json.dumps(resultado, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
