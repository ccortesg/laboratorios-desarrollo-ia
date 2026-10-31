"""Muestra diferencias de texto entre estados, sin modificar sus archivos."""

import argparse
import difflib
from pathlib import Path

BASE = Path(__file__).resolve().parent
ESTADOS = ("base", "propuesta", "solucion")


def comparar(desde, hasta):
    izquierda, derecha = BASE / "estados" / desde, BASE / "estados" / hasta
    nombres = set()
    for raiz in (izquierda, derecha):
        nombres.update(p.relative_to(raiz).as_posix() for p in raiz.rglob("*")
                       if p.is_file() and "__pycache__" not in p.parts)
    partes = []
    for nombre in sorted(nombres):
        a, b = izquierda / nombre, derecha / nombre
        contenido_a = a.read_text(encoding="utf-8").splitlines(keepends=True) if a.is_file() else []
        contenido_b = b.read_text(encoding="utf-8").splitlines(keepends=True) if b.is_file() else []
        partes.extend(difflib.unified_diff(contenido_a, contenido_b,
                      fromfile=f"{desde}/{nombre}", tofile=f"{hasta}/{nombre}"))
    return "".join(partes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--desde", choices=ESTADOS, required=True)
    parser.add_argument("--hasta", choices=ESTADOS, required=True)
    opciones = parser.parse_args()
    print(comparar(opciones.desde, opciones.hasta), end="")


if __name__ == "__main__":
    main()
