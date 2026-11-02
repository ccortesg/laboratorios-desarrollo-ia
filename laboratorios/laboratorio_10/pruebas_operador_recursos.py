"""Regresión de infraestructura del operador; no pertenece a T01–T08.

La imposibilidad de iniciar el hijo se inyecta de forma controlada. No es
un incidente real del entorno ni una nueva ejecución funcional de negocio.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

LABORATORIO = Path(__file__).resolve().parent


class RecursosOperadorTests(unittest.TestCase):
    def test_no_inicio_del_hijo_conserva_bloqueo_sin_inventar_capturas(self):
        """RO01: fallo controlado de inicio permanece BLOQUEADO sin huellas ficticias."""
        anteriores = list(sys.path)
        try:
            for estado in ("propuesta", "solucion"):
                with self.subTest(estado=estado), tempfile.TemporaryDirectory(prefix="lab10_recurso_") as temporal:
                    carpeta = Path(temporal)
                    codigo = LABORATORIO / "estados" / estado
                    sys.path.insert(0, str(codigo))
                    spec = importlib.util.spec_from_file_location("operador_recursos_" + estado, codigo / "operar.py")
                    modulo = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(modulo)
                    from persistencia import inicializar
                    base = carpeta / "principal.sqlite"
                    inicializar(base)
                    antes = base.read_bytes()
                    salida = carpeta / "recibo"
                    opciones = argparse.Namespace(base=base,
                        archivo=LABORATORIO / "datos/actualizacion_valida.csv",
                        salida=salida, almacen="ALFA", nombre="", alias="principal")
                    with patch.object(modulo.subprocess, "run", side_effect=OSError("Fallo sintético de inicio")):
                        resultado = modulo.operar(opciones)
                    self.assertEqual("BLOQUEADO", resultado["estado"])
                    self.assertEqual(2, resultado["codigo_salida"])
                    self.assertFalse(resultado["importacion_confirmada"])
                    self.assertEqual(["BLOQUEADO", "NO EJECUTADO"], [p["estado"] for p in resultado["pasos"]])
                    self.assertEqual(antes, base.read_bytes())
                    comandos = json.loads((salida / "comandos.json").read_bytes())
                    self.assertTrue(all("stdout" not in p and "sha256_stdout" not in p for p in comandos["registros"]))
                    huellas = json.loads((salida / "huellas.json").read_bytes())
                    self.assertEqual("NO EJECUTADO", huellas["estado"])
                    self.assertEqual(0, huellas["comprobadas"])
        finally:
            sys.path[:] = anteriores


if __name__ == "__main__":
    unittest.main(verbosity=2)
