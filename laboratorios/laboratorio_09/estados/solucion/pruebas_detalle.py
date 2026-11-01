"""Criterios nuevos del contrato de consulta exacta."""

import unittest

from detalle import obtener_articulo


class DetalleTests(unittest.TestCase):
    def comprobar(self, almacen, codigo, esperado):
        self.entrada = {"almacen": almacen, "codigo": codigo}
        self.esperado = esperado
        self.observado = obtener_articulo(almacen, codigo)
        self.assertEqual(esperado, self.observado)

    def test_n01_articulo_disponible_en_alfa(self):
        """N01: A01 disponible en ALFA devuelve su registro."""
        self.comprobar("ALFA", "A01", {"codigo": "A01", "nombre": "Articulo local"})

    def test_n02_articulo_disponible_en_beta(self):
        """N02: A04 disponible en BETA devuelve su registro."""
        self.comprobar("BETA", "A04", {"codigo": "A04", "nombre": "Articulo de otra ubicacion"})

    def test_n03_articulo_deshabilitado(self):
        """N03: A02 deshabilitado en ALFA devuelve None."""
        self.comprobar("ALFA", "A02", None)

    def test_n04_articulo_agotado(self):
        """N04: A03 sin existencias en ALFA devuelve None."""
        self.comprobar("ALFA", "A03", None)

    def test_n05_articulo_remoto_en_alfa(self):
        """N05: A04 con existencias en BETA se excluye de ALFA."""
        self.comprobar("ALFA", "A04", None)

    def test_n06_articulo_remoto_en_beta(self):
        """N06: A01 con existencias en ALFA se excluye de BETA."""
        self.comprobar("BETA", "A01", None)

    def test_n07_codigo_inexistente(self):
        """N07: A99 inexistente devuelve None."""
        self.comprobar("ALFA", "A99", None)

    def test_n08_codigo_con_otra_caja(self):
        """N08: a01 no coincide exactamente con A01."""
        self.comprobar("ALFA", "a01", None)

    def test_n09_codigo_con_espacios(self):
        """N09: espacios exteriores no se retiran del codigo."""
        self.comprobar("ALFA", " A01 ", None)

    def test_n10_prefijo_del_codigo(self):
        """N10: A0 no coincide exactamente con A01."""
        self.comprobar("ALFA", "A0", None)
