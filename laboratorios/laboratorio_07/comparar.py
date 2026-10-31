"""Muestra una diferencia preparada del ejercicio sin modificar archivos."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recorrido", choices=("base_a_propuesta", "propuesta_a_solucion", "base_a_solucion"),
                        default="propuesta_a_solucion")
    opciones = parser.parse_args()
    ruta = Path(__file__).resolve().parent / "diferencias" / (opciones.recorrido + ".diff")
    print(ruta.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
