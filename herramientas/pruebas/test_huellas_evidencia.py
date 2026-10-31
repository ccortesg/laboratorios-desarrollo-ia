"""Comprueba el contrato observable de la evidencia nueva con datos sintéticos.

No ejecuta navegadores ni modifica evidencias históricas. Los casos LF/CRLF
comprueban bytes concretos en la plataforma que ejecuta unittest; no simulan
una ejecución completa de Windows.
"""

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from huellas_evidencia import (  # noqa: E402
    ErrorHuellas, cerrar_evidencia, comprobar_huellas,
)


def sha256(datos):
    return hashlib.sha256(datos).hexdigest()


class HuellasEvidenciaTests(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory(prefix="prueba_huellas_")
        self.addCleanup(self.temporal.cleanup)
        self.base = Path(self.temporal.name)
        self.salida = self.base / "evidencia_nueva"
        self.salida.mkdir()

    def guardar_json(self, archivo, documento):
        archivo.write_bytes((json.dumps(documento, ensure_ascii=False, indent=2)
                             + "\n").encode("utf-8"))

    def crear_captura(self, salida=None, stdout=b"APROBADO\n", stderr=b""):
        salida = salida or self.salida
        carpeta = salida / "laboratorio_sintetico"
        carpeta.mkdir(parents=True)
        (carpeta / "caso.stdout.txt").write_bytes(stdout)
        (carpeta / "caso.stderr.txt").write_bytes(stderr)
        documento = {
            "convenciones": "Captura original como bytes sin transformación.",
            "registros": [{
                "id": "caso_sintetico", "codigo_salida": 0,
                "inicio_utc": "2026-01-01T00:00:00Z",
                "stdout": "caso.stdout.txt", "stderr": "caso.stderr.txt",
                "sha256_stdout": sha256(stdout), "sha256_stderr": sha256(stderr),
            }],
        }
        self.guardar_json(carpeta / "comandos.json", documento)
        return carpeta, documento

    def leer_comandos(self, carpeta):
        return json.loads((carpeta / "comandos.json").read_bytes())

    def instantanea(self):
        return {p.relative_to(self.base).as_posix(): p.read_bytes()
                for p in self.base.rglob("*") if p.is_file()}

    def test_preserva_lf_crlf_unicode_y_salida_vacia(self):
        """H01/H02: sin sustituciones, los bytes deben conservarse exactamente."""
        casos = [b"uno\ndos\n", b"uno\r\ndos\r\n",
                 "catálogo: acción\r\n".encode("utf-8"), b""]
        for numero, original in enumerate(casos):
            with self.subTest(caso=numero):
                salida = self.salida / str(numero)
                carpeta, _ = self.crear_captura(salida=salida, stdout=original)
                resultado = cerrar_evidencia(salida, lambda texto: texto)
                self.assertEqual(resultado["estado"], "APROBADO")
                self.assertEqual((carpeta / "caso.stdout.txt").read_bytes(), original)
                registro = self.leer_comandos(carpeta)["registros"][0]
                self.assertEqual(registro["sha256_stdout"], sha256(original))
                self.assertEqual(registro["sha256_stdout_capturado"], sha256(original))
                self.assertEqual(registro["sha256_stderr"], sha256(b""))

    def test_saneamiento_actualiza_huella_final_y_conserva_captura(self):
        """H03/H08: una sustitución real cambia la huella final, no la capturada."""
        original = "RUTA_SINTETICA/datos.txt\r\nEstado: válido\r\n".encode("utf-8")
        esperado = "TEMPORAL/datos.txt\r\nEstado: válido\r\n".encode("utf-8")
        carpeta, _ = self.crear_captura(stdout=original)
        historico = self.base / "registro_historico.txt"
        historico.write_bytes(original)
        cerrar_evidencia(self.salida,
                         lambda texto: texto.replace("RUTA_SINTETICA", "TEMPORAL"))
        registro = self.leer_comandos(carpeta)["registros"][0]
        self.assertEqual((carpeta / "caso.stdout.txt").read_bytes(), esperado)
        self.assertEqual(registro["sha256_stdout"], sha256(esperado))
        self.assertEqual(registro["sha256_stdout_capturado"], sha256(original))
        self.assertNotEqual(registro["sha256_stdout"], registro["sha256_stdout_capturado"])
        self.assertEqual(historico.read_bytes(), original)

    def test_conserva_resultados_y_aclara_convenciones(self):
        """H04: sanear no cambia criterios, estados, totales ni códigos de salida."""
        carpeta, anterior = self.crear_captura()
        resultados = {"estado": "APROBADO", "totales": {"aprobados": 1, "fallidos": 1},
                      "pruebas": [{"id": "W05", "estado": "FALLIDO"}],
                      "nota": "Resultado didáctico con acentos"}
        self.guardar_json(carpeta / "resumen.json", resultados)
        cerrar_evidencia(self.salida, lambda texto: texto)
        posterior = self.leer_comandos(carpeta)
        self.assertEqual(json.loads((carpeta / "resumen.json").read_bytes()), resultados)
        for clave in ("id", "codigo_salida", "inicio_utc"):
            self.assertEqual(posterior["registros"][0][clave], anterior["registros"][0][clave])
        self.assertEqual(posterior["convenciones_del_productor"], anterior["convenciones"])
        self.assertNotEqual(posterior["convenciones"], anterior["convenciones"])

    def test_no_ejecutado_sin_salidas_no_inventa_huellas(self):
        """H05: el registro sin proceso mantiene su ausencia de stdout y stderr."""
        carpeta, documento = self.crear_captura()
        omitido = {"id": "caso_omitido", "comando": None, "codigo_salida": None,
                   "estado": "NO EJECUTADO", "motivo": "Estado didáctico sin interfaz."}
        documento["registros"].append(omitido)
        self.guardar_json(carpeta / "comandos.json", documento)
        nombres_antes = sorted(p.name for p in carpeta.iterdir())
        resultado = cerrar_evidencia(self.salida, lambda texto: texto)
        self.assertEqual(resultado["comprobadas"], 2)
        self.assertEqual(self.leer_comandos(carpeta)["registros"][1], omitido)
        self.assertEqual(sorted(p.name for p in carpeta.iterdir()), nombres_antes)

    def test_huella_inicial_incorrecta_rechaza_sin_reescritura(self):
        """H06: no debe ocultar una alteración previa recalculando las huellas."""
        carpeta, documento = self.crear_captura(stdout=b"RUTA_SINTETICA\n")
        documento["registros"][0]["sha256_stdout"] = "0" * 64
        self.guardar_json(carpeta / "comandos.json", documento)
        antes = self.instantanea()
        with self.assertRaises(ErrorHuellas):
            cerrar_evidencia(self.salida,
                             lambda texto: texto.replace("RUTA_SINTETICA", "TEMPORAL"))
        self.assertEqual(self.instantanea(), antes)

    def test_referencia_externa_se_rechaza_sin_escribir(self):
        """H07: el contrato sólo admite nombres simples dentro de la evidencia."""
        carpeta, documento = self.crear_captura()
        (self.salida / "fuera.txt").write_bytes(b"contenido sintetico\n")
        documento["registros"][0]["stdout"] = "../fuera.txt"
        documento["registros"][0]["sha256_stdout"] = sha256(b"contenido sintetico\n")
        self.guardar_json(carpeta / "comandos.json", documento)
        antes = self.instantanea()
        with self.assertRaises(ErrorHuellas):
            cerrar_evidencia(self.salida, lambda texto: texto)
        self.assertEqual(self.instantanea(), antes)

    def test_registro_incompleto_no_se_omite_silenciosamente(self):
        """H06/H07: una salida declarada sin huella es un registro incompleto."""
        carpeta, documento = self.crear_captura()
        del documento["registros"][0]["sha256_stderr"]
        self.guardar_json(carpeta / "comandos.json", documento)
        antes = self.instantanea()
        with self.assertRaises(ErrorHuellas):
            cerrar_evidencia(self.salida, lambda texto: texto)
        self.assertEqual(self.instantanea(), antes)

    def test_comprobador_detecta_modificacion_posterior_sin_escribir(self):
        """H09: la inspección debe aprobar bytes válidos y detectar su cambio."""
        carpeta, _ = self.crear_captura()
        cerrar_evidencia(self.salida, lambda texto: texto)
        antes = self.instantanea()
        resultado = comprobar_huellas(self.salida)
        self.assertEqual(resultado["estado"], "APROBADO")
        self.assertEqual(resultado["comprobadas"], 2)
        self.assertEqual(resultado["coincidentes"], 2)
        self.assertEqual(self.instantanea(), antes)
        (carpeta / "caso.stdout.txt").write_bytes(b"contenido modificado\n")
        alterada = self.instantanea()
        resultado = comprobar_huellas(self.salida)
        self.assertEqual(resultado["estado"], "FALLIDO")
        self.assertEqual(resultado["comprobadas"], 2)
        self.assertEqual(resultado["coincidentes"], 1)
        self.assertEqual(len(resultado["discrepancias"]), 1)
        self.assertEqual(self.instantanea(), alterada)


if __name__ == "__main__":
    unittest.main(verbosity=2)
