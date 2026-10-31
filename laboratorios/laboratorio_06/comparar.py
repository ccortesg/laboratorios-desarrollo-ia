"""Genera diferencias legibles entre los estados, sin modificar su contenido."""

import argparse
import difflib
from pathlib import Path

BASE = Path(__file__).resolve().parent
PARES = (("base", "propuesta"), ("propuesta", "solucion"), ("base", "solucion"))


def archivos(directorio):
    return {p.relative_to(directorio).as_posix(): p
            for p in directorio.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, required=True)
    opciones = parser.parse_args()
    destino = opciones.salida.resolve()
    if destino.exists():
        parser.error("La carpeta de salida ya existe; elige una nueva.")
    estados = BASE / "estados"
    if destino == estados or estados in destino.parents:
        parser.error("Las diferencias no deben guardarse dentro de los estados.")
    destino.mkdir(parents=True)
    for anterior, posterior in PARES:
        a = archivos(estados / anterior)
        b = archivos(estados / posterior)
        lineas = []
        for nombre in sorted(a.keys() | b.keys()):
            antes = a[nombre].read_text(encoding="utf-8").splitlines(keepends=True) if nombre in a else []
            despues = b[nombre].read_text(encoding="utf-8").splitlines(keepends=True) if nombre in b else []
            lineas.extend(difflib.unified_diff(
                antes, despues,
                fromfile=f"estados/{anterior}/{nombre}" if nombre in a else "/dev/null",
                tofile=f"estados/{posterior}/{nombre}" if nombre in b else "/dev/null"))
        salida = destino / f"{anterior}_a_{posterior}.diff"
        salida.write_text("".join(lineas), encoding="utf-8")
        print(salida.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
