#!/usr/bin/env python3
"""Comprueba bytes y cobertura del paquete, sin red ni escrituras."""
import argparse
import hashlib
import re
from pathlib import Path, PurePosixPath


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    raiz = Path(__file__).resolve().parent
    manifiesto = raiz / "SHA256SUMS"
    declarados = {}
    for linea in manifiesto.read_text(encoding="utf-8").splitlines():
        huella, nombre = linea.split("  ", 1)
        partes = PurePosixPath(nombre)
        if (not re.fullmatch(r"[a-f0-9]{64}", huella)
                or not nombre or nombre != partes.as_posix()
                or nombre in declarados or partes.is_absolute()
                or ".." in partes.parts or "\\" in nombre or ":" in nombre
                or nombre == "SHA256SUMS"):
            raise ValueError("Declaracion de manifiesto invalida")
        declarados[nombre] = huella
    if not declarados:
        raise ValueError("El manifiesto no declara archivos")
    reales = set()
    for archivo in raiz.rglob("*"):
        if archivo.is_symlink():
            raise ValueError("El paquete no admite enlaces simbolicos")
        if archivo.is_file() and archivo != manifiesto:
            reales.add(archivo.relative_to(raiz).as_posix())
    if reales != set(declarados):
        raise ValueError("La cobertura del manifiesto no coincide con los archivos")
    diferentes = [nombre for nombre, huella in declarados.items()
                  if hashlib.sha256((raiz / nombre).read_bytes()).hexdigest() != huella]
    if diferentes:
        raise ValueError("Huellas divergentes: " + ", ".join(diferentes))
    print("APROBADO: {} archivos; SHA256 coincidente y cobertura completa.".format(len(declarados)))
    print("Verificacion de lectura, sin red ni cambios de archivos.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        print("FALLIDO: " + str(error))
        raise SystemExit(1)
