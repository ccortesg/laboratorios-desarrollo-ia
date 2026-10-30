"""Cuatro criterios de aceptacion conservados para la solucion del catalogo."""

import argparse
import json
import sys
import unittest
from pathlib import Path

from laboratorio import VERSIONES, consultar_catalogo


VERSION = "solucion"


class DisponibilidadTests(unittest.TestCase):
    def setUp(self):
        self.codigos = [
            fila["codigo"] for fila in consultar_catalogo(VERSION, "ALFA")
        ]

    def test_c01_habilitado_con_existencias_locales_aparece(self):
        """C01: habilitado con existencias locales aparece."""
        self.assertIn("A01", self.codigos)

    def test_c02_deshabilitado_se_excluye(self):
        """C02: deshabilitado con existencias locales se excluye."""
        self.assertNotIn("A02", self.codigos)

    def test_c03_sin_existencias_se_excluye(self):
        """C03: habilitado sin existencias disponibles se excluye."""
        self.assertNotIn("A03", self.codigos)

    def test_c04_existencias_en_otra_ubicacion_se_excluyen(self):
        """C04: existencias solo en otra ubicacion se excluyen."""
        self.assertNotIn("A04", self.codigos)


class ResultadoRegistrado(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registros = []

    def registrar(self, prueba, estado, detalle="", tipo_error=None):
        self.registros.append(
            {
                "prueba": prueba._testMethodName,
                "criterio": prueba.shortDescription(),
                "estado": estado,
                "detalle": detalle,
                "tipo_error": tipo_error,
            }
        )

    def addSuccess(self, test):
        super().addSuccess(test)
        self.registrar(test, "APROBADO")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.registrar(test, "FALLIDO", str(err[1]), type(err[1]).__name__)

    def addError(self, test, err):
        super().addError(test, err)
        self.registrar(
            test,
            "FALLIDO",
            "Error inesperado durante la ejecucion de la prueba.",
            type(err[1]).__name__,
        )

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.registrar(test, "NO EJECUTADO", reason)


def main():
    global VERSION
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", choices=VERSIONES, required=True)
    parser.add_argument("--json", type=Path, help="Ruta opcional del resultado JSON.")
    opciones = parser.parse_args()
    VERSION = opciones.version
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DisponibilidadTests)
    resultado = unittest.TextTestRunner(
        stream=sys.stdout, verbosity=2, resultclass=ResultadoRegistrado
    ).run(suite)

    if opciones.json:
        opciones.json.parent.mkdir(parents=True, exist_ok=True)
        registro = {
            "version": VERSION,
            "total": resultado.testsRun,
            "aprobados": sum(
                p["estado"] == "APROBADO" for p in resultado.registros
            ),
            "fallidos": len(resultado.failures) + len(resultado.errors),
            "fallos_de_asercion": len(resultado.failures),
            "errores_de_ejecucion": len(resultado.errors),
            "bloqueados": 0,
            "no_ejecutados": len(resultado.skipped),
            "pruebas": resultado.registros,
        }
        opciones.json.write_text(
            json.dumps(registro, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
