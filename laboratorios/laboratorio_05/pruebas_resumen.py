"""P01-P06: resultados públicos de la función y de la terminal."""

import argparse
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

BASE = Path(__file__).resolve().parent
ESTADO = None
DIRECTORIO = None


class ResumenTests(unittest.TestCase):
    def setUp(self):
        if ESTADO == "base":
            self.skipTest("El incremento resumen.py no existe en el estado base.")

    def comprobar(self, almacen, texto, esperado, omitir_texto=False):
        self.entrada = {"almacen": almacen, "texto": texto,
                        "argumento_texto_omitido": omitir_texto}
        self.esperado = esperado
        funcion = importlib.import_module("resumen").resumir_catalogo
        self.observado = (funcion(almacen) if omitir_texto
                          else funcion(almacen, texto))
        self.assertEqual(esperado, self.observado)

    def ejecutar_cli(self, argumentos):
        entorno = dict(os.environ, PYTHONIOENCODING="utf-8",
                       PYTHONDONTWRITEBYTECODE="1")
        resultado = subprocess.run(
            [sys.executable, "-B", "resumen.py", *argumentos],
            cwd=DIRECTORIO, capture_output=True,
            text=True, encoding="utf-8", env=entorno, timeout=20,
        )
        self.comando = ["python", "-B", "resumen.py", *argumentos]
        return {"codigo_salida": resultado.returncode,
                "stdout": resultado.stdout, "stderr": resultado.stderr}

    def test_p01_resumen_alfa_sin_argumento_texto(self):
        """P01: ALFA sin texto cuenta un artículo, no siete unidades."""
        self.comprobar("ALFA", "", {"almacen": "ALFA", "total": 1,
                                   "codigos": ["A01"]}, omitir_texto=True)

    def test_p02_resumen_beta_vacio(self):
        """P02: BETA con texto vacío devuelve únicamente A04."""
        self.comprobar("BETA", "", {"almacen": "BETA", "total": 1,
                                   "codigos": ["A04"]})

    def test_p03_nombre_normalizado(self):
        """P03: BETA y OTRA con espacios conservan la coincidencia."""
        self.comprobar("BETA", " OTRA ", {"almacen": "BETA", "total": 1,
                                         "codigos": ["A04"]})

    def test_p04_nombre_sin_coincidencia_local(self):
        """P04: ALFA y otra producen un resumen vacío."""
        self.comprobar("ALFA", "otra", {"almacen": "ALFA", "total": 0,
                                       "codigos": []})

    def test_p05_terminal_filtra_nombre(self):
        """P05: la terminal devuelve JSON vacío para BETA e inexistente."""
        self.entrada = {"almacen": "BETA", "nombre": "inexistente"}
        self.esperado = {"codigo_salida": 0, "stderr": "",
                         "json": {"almacen": "BETA", "total": 0,
                                  "codigos": []}}
        self.observado = self.ejecutar_cli(
            ["--almacen", "BETA", "--nombre", "inexistente"])
        self.assertEqual(0, self.observado["codigo_salida"])
        self.assertEqual("", self.observado["stderr"])
        contenido = json.loads(self.observado["stdout"])
        self.observado["json"] = contenido
        self.assertEqual(self.esperado["json"], contenido)

    def test_p06_terminal_exige_almacen(self):
        """P06: omitir almacén produce salida 2 y ningún JSON de éxito."""
        self.entrada = {"argumentos": []}
        self.esperado = {"codigo_salida": 2, "stdout": "",
                         "stderr_menciona": "--almacen"}
        self.observado = self.ejecutar_cli([])
        self.assertEqual(2, self.observado["codigo_salida"])
        self.assertEqual("", self.observado["stdout"])
        self.assertTrue(self.observado["stderr"].strip())
        self.assertIn("--almacen", self.observado["stderr"])


class ResultadoRegistrado(unittest.TestResult):
    """Registra expectativas y observaciones sin trazas con rutas del equipo."""

    def __init__(self):
        super().__init__()
        self.registros = []

    def registrar(self, test, estado, detalle="", tipo_error=None):
        descripcion = test.shortDescription() or test._testMethodName
        self.registros.append({
            "id": descripcion.split(":", 1)[0],
            "prueba": test._testMethodName, "criterio": descripcion,
            "estado": estado, "detalle": detalle, "tipo_error": tipo_error,
            "entrada": getattr(test, "entrada", None),
            "esperado": getattr(test, "esperado", None),
            "observado": getattr(test, "observado", None),
            "comando_terminal": getattr(test, "comando", None),
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
    global ESTADO, DIRECTORIO
    parser = argparse.ArgumentParser(description=__doc__)
    origen = parser.add_mutually_exclusive_group(required=True)
    origen.add_argument("--estado", choices=("base", "propuesta", "solucion"))
    origen.add_argument("--directorio", type=Path,
                        help="Copia propia que contiene catalogo.py y resumen.py.")
    parser.add_argument("--json", type=Path)
    opciones = parser.parse_args()
    ESTADO = opciones.estado
    DIRECTORIO = (BASE / "estados" / ESTADO if ESTADO
                  else opciones.directorio.resolve())
    if not DIRECTORIO.is_dir():
        parser.error("El directorio de código no existe.")
    sys.path.insert(0, str(DIRECTORIO))
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ResumenTests)
    resultado = ResultadoRegistrado()
    suite.run(resultado)
    registro = {
        "bateria": "resumen", "estado_codigo": ESTADO or "copia_del_lector",
        "criterios_registrados": len(resultado.registros),
        "ejecutados": resultado.testsRun - len(resultado.skipped),
        "aprobados": sum(p["estado"] == "APROBADO"
                         for p in resultado.registros),
        "fallidos": len(resultado.failures) + len(resultado.errors),
        "fallos_de_asercion": len(resultado.failures),
        "errores_de_ejecucion": len(resultado.errors),
        "bloqueados": 0, "no_ejecutados": len(resultado.skipped),
        "pruebas": resultado.registros,
    }
    print("Bateria: resumen; estado: " + (ESTADO or "copia_del_lector"))
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
