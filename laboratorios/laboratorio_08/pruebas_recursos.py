"""Regresiones del cierre de SQLite; se contabilizan aparte de C/B/N/P/W/I/D.

Las conexiones retenidas son reales. Comprobar que ya no admiten consultas hace
visible el defecto en Linux y Windows sin depender de la recolección de objetos.
La excepción de escritura es una inyección controlada, no un incidente real.
"""
from contextlib import closing, contextmanager
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

import pruebas_depuracion
from soporte_procesos import snapshot

BASE = Path(__file__).resolve().parent
CONECTAR = sqlite3.connect


class EscrituraInterrumpida(RuntimeError):
    """Fallo controlado después de una escritura real aún sin confirmar."""


class ConexionInterrumpida(sqlite3.Connection):
    def execute(self, sql, parameters=()):
        resultado = super().execute(sql, parameters)
        if self.in_transaction:
            raise EscrituraInterrumpida("Escritura interrumpida para comprobar rollback y cierre.")
        return resultado


@contextmanager
def conexiones_retenidas(*, interrumpir=False):
    conexiones = []

    def conectar(*args, **kwargs):
        if interrumpir:
            kwargs["factory"] = ConexionInterrumpida
        conexion = CONECTAR(*args, **kwargs)
        conexiones.append(conexion)
        return conexion

    try:
        with patch("sqlite3.connect", side_effect=conectar):
            yield conexiones
    finally:
        # La regresión también debe liberar sus recursos cuando detecta el
        # defecto original. Esta limpieza ocurre después de las aserciones.
        for conexion in conexiones:
            conexion.close()


class RecursosSQLiteTests(unittest.TestCase):
    def setUp(self):
        temporal = tempfile.TemporaryDirectory(prefix="recursos_lab08_")
        self.addCleanup(temporal.cleanup)
        self.trabajo = Path(temporal.name)

    def comprobar_cerradas(self, conexiones):
        self.assertTrue(conexiones, "La operación debe abrir una conexión real.")
        for conexion in conexiones:
            with self.assertRaises(sqlite3.ProgrammingError,
                                   msg="La conexión debe quedar cerrada antes de retornar."):
                conexion.execute("SELECT 1")

    def fixture_snapshot(self, *, completa=True):
        ruta = self.trabajo / "referencia.sqlite"
        with closing(CONECTAR(ruta)) as conexion, conexion:
            conexion.executescript(
                "CREATE TABLE articulos(codigo TEXT, nombre TEXT, habilitado INTEGER);"
                "CREATE TABLE almacenes(codigo TEXT);"
                "INSERT INTO articulos VALUES ('A01', 'Articulo sintetico', 1);"
                "INSERT INTO almacenes VALUES ('ALFA');"
            )
            if completa:
                conexion.executescript(
                    "CREATE TABLE existencias(articulo TEXT, almacen TEXT, cantidad INTEGER);"
                    "INSERT INTO existencias VALUES ('A01', 'ALFA', 3);"
                )
        return ruta

    def caso_d06b(self):
        caso = pruebas_depuracion.DepuracionTests("test_d06b_esquema_incompatible")
        caso.trabajo = self.trabajo
        caso.observado = {}
        from soporte_procesos import Escenario
        caso.escenario = Escenario(BASE / "estados/solucion", self.trabajo)
        return caso

    def test_r01_snapshot_conserva_datos_y_libera_archivo(self):
        """R01: una lectura correcta deja la conexión cerrada y el archivo liberado."""
        ruta = self.fixture_snapshot()
        antes = ruta.read_bytes()
        with conexiones_retenidas() as conexiones:
            datos = snapshot(ruta)
            self.assertEqual({
                "articulos": [["A01", "Articulo sintetico", 1]],
                "almacenes": [["ALFA"]],
                "existencias": [["A01", "ALFA", 3]],
            }, datos)
            self.assertEqual(antes, ruta.read_bytes())
            self.comprobar_cerradas(conexiones)
            ruta.unlink()
            self.assertFalse(ruta.exists())

    def test_r02_snapshot_libera_archivo_al_fallar_consulta(self):
        """R02: una consulta inválida propaga el error y libera la conexión."""
        ruta = self.fixture_snapshot(completa=False)
        antes = ruta.read_bytes()
        with conexiones_retenidas() as conexiones:
            with self.assertRaises(sqlite3.OperationalError):
                snapshot(ruta)
            self.assertEqual(antes, ruta.read_bytes())
            self.comprobar_cerradas(conexiones)
            ruta.unlink()
            self.assertFalse(ruta.exists())

    def test_r03_d06b_confirma_fixture_y_libera_conexion(self):
        """R03: D06.b confirma su dato sintético, conserva el rechazo y cierra."""
        caso = self.caso_d06b()
        ruta = self.trabajo / "incompatible.sqlite"
        with conexiones_retenidas() as conexiones:
            caso.test_d06b_esquema_incompatible()
            with closing(CONECTAR(ruta)) as independiente:
                self.assertEqual([("sintetico",)],
                                 independiente.execute("SELECT valor FROM marcador").fetchall())
            self.comprobar_cerradas(conexiones)
            ruta.unlink()
            self.assertFalse(ruta.exists())

    def test_r04_d06b_revierte_y_cierra_si_escritura_falla(self):
        """R04: una escritura interrumpida revierte el dato y libera el archivo."""
        caso = self.caso_d06b()
        ruta = self.trabajo / "incompatible.sqlite"
        with conexiones_retenidas(interrumpir=True) as conexiones:
            with self.assertRaises(EscrituraInterrumpida):
                caso.test_d06b_esquema_incompatible()
            with closing(CONECTAR(ruta)) as independiente:
                self.assertEqual([],
                                 independiente.execute("SELECT valor FROM marcador").fetchall())
            self.comprobar_cerradas(conexiones)
            ruta.unlink()
            self.assertFalse(ruta.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
