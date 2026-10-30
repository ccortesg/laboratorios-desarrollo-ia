"""Imprime diferencias de los estados sin modificar archivos."""

import argparse
import difflib
from pathlib import Path


BASE = Path(__file__).resolve().parent
PASOS = {
    "generar": (None, "estados/generado.py"),
    "refactorizar": ("estados/generado.py", "estados/refactorizado.py"),
    "introducir-defecto": ("estados/refactorizado.py", "estados/defecto.py"),
    "corregir": ("estados/defecto.py", "estados/corregido.py"),
}


def diferencia(paso):
    anterior, siguiente = PASOS[paso]
    lineas_antes = ((BASE / anterior).read_text(encoding="utf-8").splitlines(True)
                    if anterior else [])
    lineas_despues = (BASE / siguiente).read_text(encoding="utf-8").splitlines(True)
    return "".join(difflib.unified_diff(
        lineas_antes, lineas_despues, fromfile=anterior or "/dev/null",
        tofile=siguiente,
    ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paso", choices=PASOS, required=True)
    opciones = parser.parse_args()
    print(diferencia(opciones.paso), end="")


if __name__ == "__main__":
    main()
