"""Comprueba comportamiento publico; no inspecciona la estructura del codigo."""

import argparse
import json
import unittest
from pathlib import Path

from catalogo import buscar_catalogo
from pruebas_detalle import DetalleTests


A01 = [{"codigo": "A01", "nombre": "Articulo local"}]
A04 = [{"codigo": "A04", "nombre": "Articulo de otra ubicacion"}]


class DisponibilidadTests(unittest.TestCase):
    def setUp(self):
        filas = buscar_catalogo("ALFA", "")
        self.codigos = [fila["codigo"] for fila in filas]

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


class BusquedaTests(unittest.TestCase):
    def setUp(self):
        self.buscar = buscar_catalogo

    def comprobar(self, almacen, texto, esperado):
        self.entrada = {"almacen": almacen, "texto": texto}
        self.esperado = esperado
        self.observado = self.buscar(almacen, texto)
        self.assertEqual(esperado, self.observado)

    def test_b01_normaliza_espacios_y_mayusculas(self):
        """B01: buscar LoCaL con espacios en ALFA devuelve A01."""
        self.comprobar("ALFA", "  LoCaL  ", A01)

    def test_b02_termino_blanco_devuelve_disponibles(self):
        """B02: termino blanco en ALFA devuelve A01."""
        self.comprobar("ALFA", " \t ", A01)

    def test_b03_sin_coincidencias_devuelve_lista_vacia(self):
        """B03: termino inexistente en ALFA devuelve lista vacia."""
        self.comprobar("ALFA", "inexistente", [])

    def test_b04_nombre_remoto_no_amplia_disponibilidad(self):
        """B04: buscar otra en ALFA no incorpora el articulo remoto."""
        self.comprobar("ALFA", "otra", [])

    def test_b05_almacen_beta_con_termino_vacio(self):
        """B05: termino vacio en BETA devuelve A04."""
        self.comprobar("BETA", "", A04)

    def test_b06_busqueda_normalizada_en_beta(self):
        """B06: buscar OTRA con espacios en BETA devuelve A04."""
        self.comprobar("BETA", " OTRA ", A04)


class ResultadoRegistrado(unittest.TestResult):
    """Conserva evidencia util sin imprimir trazas con rutas del equipo."""

    def __init__(self):
        super().__init__()
        self.registros = []

    def registrar(self, prueba, estado, detalle="", tipo_error=None):
        descripcion = prueba.shortDescription() or prueba._testMethodName
        self.registros.append({
            "id": descripcion.split(":", 1)[0],
            "prueba": prueba._testMethodName,
            "criterio": descripcion,
            "estado": estado,
            "detalle": detalle,
            "tipo_error": tipo_error,
            "entrada": getattr(prueba, "entrada", None),
            "esperado": getattr(prueba, "esperado", None),
            "observado": getattr(prueba, "observado", None),
            "codigos_catalogo": getattr(prueba, "codigos", None),
        })

    def addSuccess(self, test):
        super().addSuccess(test)
        self.registrar(test, "APROBADO")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.registrar(test, "FALLIDO", str(err[1]), type(err[1]).__name__)

    def addError(self, test, err):
        super().addError(test, err)
        self.registrar(test, "FALLIDO", "Error inesperado durante la prueba.",
                       type(err[1]).__name__)

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.registrar(test, "NO EJECUTADO", reason)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    opciones = parser.parse_args()
    suite = unittest.TestSuite([
        unittest.defaultTestLoader.loadTestsFromTestCase(DisponibilidadTests),
        unittest.defaultTestLoader.loadTestsFromTestCase(BusquedaTests),
        unittest.defaultTestLoader.loadTestsFromTestCase(DetalleTests),
    ])
    resultado = ResultadoRegistrado()
    suite.run(resultado)
    registro = {
        "bateria": "catalogo",
        "criterios_registrados": len(resultado.registros),
        "ejecutados": resultado.testsRun - len(resultado.skipped),
        "aprobados": sum(p["estado"] == "APROBADO" for p in resultado.registros),
        "fallidos": len(resultado.failures) + len(resultado.errors),
        "fallos_de_asercion": len(resultado.failures),
        "errores_de_ejecucion": len(resultado.errors),
        "bloqueados": 0,
        "no_ejecutados": len(resultado.skipped),
        "pruebas": resultado.registros,
    }
    print("Bateria: catalogo")
    for prueba in resultado.registros:
        print(prueba["id"] + ": " + prueba["estado"])
        if prueba["detalle"]:
            print(prueba["detalle"])
    print("Ejecutados: {ejecutados}; aprobados: {aprobados}; fallidos: {fallidos}; "
          "no ejecutados: {no_ejecutados}.".format(**registro))
    if opciones.json:
        opciones.json.parent.mkdir(parents=True, exist_ok=True)
        opciones.json.write_text(json.dumps(registro, ensure_ascii=False, indent=2)
                                 + "\n", encoding="utf-8")
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
