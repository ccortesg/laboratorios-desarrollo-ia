"""Regresiones del evaluador común del laboratorio 10, separadas de las funcionales.

Se construyen registros de ejemplo para comprobar la interpretación de contratos,
no para acreditar una ejecución del catálogo. No se inicia HTTP ni un navegador.
"""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verificar_todo import conservar_herencia_laboratorio_10, evaluar_laboratorio_web
from test_evaluador_laboratorio_09 import CONTEOS, GRUPOS as GRUPOS_HEREDADOS, conteos


GRUPOS = dict(GRUPOS_HEREDADOS,
              automatizacion=["T%02d" % i for i in range(1, 8)],
              automatizacion_navegador=["T08"])


class EvaluadorLaboratorio10Tests(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory(prefix="evaluador_lab10_")
        self.addCleanup(self.temporal.cleanup)
        self.raiz = Path(self.temporal.name)
        self.registros = {}
        self.navegador = True

    def crear_fixture(self, navegador=True):
        self.navegador = navegador
        self.registros = {}
        for estado in ("base", "propuesta", "solucion"):
            for grupo, ids in GRUPOS.items():
                sin_incremento = estado == "base" and grupo.startswith("automatizacion")
                sin_navegador = grupo.endswith("navegador") and not navegador
                casos = []
                for identificador in ids:
                    resultado = ("NO EJECUTADO" if sin_incremento or sin_navegador else
                                 "FALLIDO" if estado == "propuesta" and identificador == "T02"
                                 else "APROBADO")
                    caso = {"id": identificador, "estado": resultado}
                    if resultado == "FALLIDO":
                        caso["tipo_error"] = "AssertionError"
                    casos.append(caso)
                self.registros[estado + "_" + grupo] = {
                    "estado_codigo": estado, "grupo": grupo, "pruebas": casos,
                }

    def guardar_fixture(self, estado_global=None):
        """Recalcula los totales tras cada alteración para exigir identidad de casos."""
        comandos, baterias = [], []
        for nombre, fuente in self.registros.items():
            casos = fuente["pruebas"]
            numeros = conteos(casos)
            codigo = (2 if numeros["bloqueados"] else 1 if numeros["fallidos"] else
                      None if numeros["no_ejecutados"] == len(casos) else 0)
            registro = dict(numeros, casos_registrados=len(casos), pruebas=casos)
            (self.raiz / (nombre + ".json")).write_text(json.dumps(registro), encoding="utf-8")
            comandos.append({"id": nombre, "codigo_salida": codigo})
            baterias.append({
                "estado_codigo": fuente["estado_codigo"], "bateria": fuente["grupo"],
                "resultado": nombre + ".json",
                "patron": {"estado": "BLOQUEADO" if numeros["bloqueados"] else "APROBADO"},
                **{k: numeros[k] for k in CONTEOS},
            })
        bloqueado = any(b["bloqueados"] for b in baterias)
        estado = estado_global or ("BLOQUEADO" if bloqueado else
                                   "APROBADO" if self.navegador else "NO EJECUTADO")
        resumen = {
            "estado": estado, "extremo_a_extremo": estado,
            "alcance_ejecutado": "BLOQUEADO" if bloqueado else "APROBADO",
            "conservacion_heredados": "APROBADO",
            "base_sin_incremento_automatizacion": "APROBADO",
            "navegador_solicitado": self.navegador, "baterias": baterias,
            "totales": {k: sum(b[k] for b in baterias) for k in CONTEOS},
        }
        (self.raiz / "resumen.json").write_text(json.dumps(resumen), encoding="utf-8")
        (self.raiz / "comandos.json").write_text(
            json.dumps({"registros": comandos}), encoding="utf-8")
        return resumen

    def evaluar(self):
        return evaluar_laboratorio_web(self.raiz, self.navegador, numero=10)

    def caso(self, bateria, identificador):
        return next(c for c in self.registros[bateria]["pruebas"] if c["id"] == identificador)

    def test_patron_completo_con_un_fallo_y_base_sin_operador(self):
        """E10.01: heredar la solución 9 obliga a aprobar los 74 casos previos."""
        self.crear_fixture()
        resumen = self.guardar_fixture()
        correcto, baterias, estado = self.evaluar()
        self.assertTrue(correcto)
        self.assertEqual(estado, "APROBADO")
        self.assertEqual(len(baterias), 33)
        self.assertEqual(resumen["totales"], {
            "ejecutados": 238, "aprobados": 237, "fallidos": 1,
            "bloqueados": 0, "no_ejecutados": 8, "errores_de_ejecucion": 0,
        })

    def test_no_arrastra_excepciones_didacticas_de_la_seguridad_anterior(self):
        """E10.02: los fallos admitidos en estados del laboratorio 9 no pasan al 10."""
        for bateria, identificador in (("base_seguridad", "S02.a"),
                                       ("propuesta_seguridad", "S02.a"),
                                       ("base_seguridad_navegador", "S06")):
            with self.subTest(bateria=bateria):
                self.crear_fixture()
                self.caso(bateria, identificador).update(estado="FALLIDO", tipo_error="AssertionError")
                self.guardar_fixture()
                correcto, _, estado = self.evaluar()
                self.assertFalse(correcto)
                self.assertEqual(estado, "FALLIDO")

    def test_t02_exige_asercion_salida_uno_y_presencia_del_defecto(self):
        """E10.03: una excepción de infraestructura o un éxito no prueban el defecto."""
        for alteracion in ("tipo_error", "codigo", "desaparece"):
            with self.subTest(alteracion=alteracion):
                self.crear_fixture()
                caso = self.caso("propuesta_automatizacion", "T02")
                if alteracion == "tipo_error":
                    caso["tipo_error"] = "OSError"
                elif alteracion == "desaparece":
                    caso.clear()
                    caso.update(id="T02", estado="APROBADO")
                self.guardar_fixture()
                if alteracion == "codigo":
                    archivo = self.raiz / "comandos.json"
                    comandos = json.loads(archivo.read_text("utf-8"))
                    next(c for c in comandos["registros"]
                         if c["id"] == "propuesta_automatizacion")["codigo_salida"] = 0
                    archivo.write_text(json.dumps(comandos), encoding="utf-8")
                self.assertFalse(self.evaluar()[0])

    def test_rechaza_caso_ausente_o_duplicado_con_totales_recalculados(self):
        """E10.04: los conteos coherentes no reemplazan la identidad de cada caso."""
        self.crear_fixture()
        self.registros["solucion_automatizacion"]["pruebas"] = [
            c for c in self.registros["solucion_automatizacion"]["pruebas"] if c["id"] != "T04"]
        self.guardar_fixture()
        self.assertFalse(self.evaluar()[0])
        self.crear_fixture()
        self.caso("solucion_automatizacion", "T04")["id"] = "T03"
        self.guardar_fixture()
        with self.assertRaisesRegex(ValueError, "duplicado"):
            self.evaluar()

    def test_no_acredita_automatizacion_inexistente_en_la_base(self):
        """E10.05: base no tiene operar.py; T01–T08 deben seguir NO EJECUTADO."""
        self.crear_fixture()
        self.caso("base_automatizacion", "T01")["estado"] = "APROBADO"
        self.guardar_fixture()
        self.assertFalse(self.evaluar()[0])

    def test_sin_navegador_conserva_no_ejecutado_global(self):
        """E10.06: T08 se comprueba en navegador y no se infiere de la CLI."""
        self.crear_fixture(navegador=False)
        self.guardar_fixture()
        correcto, _, estado = self.evaluar()
        self.assertTrue(correcto)
        self.assertEqual(estado, "NO EJECUTADO")
        self.guardar_fixture(estado_global="APROBADO")
        self.assertFalse(self.evaluar()[0])

    def test_bloqueo_parcial_cli_se_conserva_sin_aprobarlo(self):
        """E10.07: un impedimento de ejecución en T04 no se convierte en éxito."""
        self.crear_fixture()
        self.caso("solucion_automatizacion", "T04")["estado"] = "BLOQUEADO"
        self.guardar_fixture()
        correcto, baterias, estado = self.evaluar()
        self.assertTrue(correcto)
        self.assertEqual(estado, "BLOQUEADO")
        self.assertEqual(next(b["evaluacion_del_recorrido"] for b in baterias
                              if b["bateria"] == "laboratorio_10/solucion_automatizacion"), "BLOQUEADO")
        self.guardar_fixture(estado_global="APROBADO")
        self.assertFalse(self.evaluar()[0])

    def test_navegador_solicitado_pero_bloqueado_no_aprueba_extremo_a_extremo(self):
        """E10.08: la petición de navegador no acredita su ejecución efectiva."""
        self.crear_fixture()
        self.caso("solucion_automatizacion_navegador", "T08")["estado"] = "BLOQUEADO"
        self.guardar_fixture()
        correcto, _, estado = self.evaluar()
        self.assertTrue(correcto)
        self.assertEqual(estado, "BLOQUEADO")
        self.guardar_fixture(estado_global="APROBADO")
        self.assertFalse(self.evaluar()[0])

    def test_cotejo_heredado_rechaza_bytes_cambiados_y_archivos_extra_en_base(self):
        """E10.09: el manifiesto propio no puede ocultar cambios al material heredado."""
        repo = self.raiz / "repositorio_sintetico"
        fuente = repo / "laboratorios" / "laboratorio_09" / "estados" / "solucion"
        fuente.mkdir(parents=True)
        original = b"def catalogo():\n    return []\n"
        (fuente / "catalogo.py").write_bytes(original)
        raiz_estados = repo / "laboratorios" / "laboratorio_10" / "estados"
        for estado in ("base", "propuesta", "solucion"):
            carpeta = raiz_estados / estado
            carpeta.mkdir(parents=True)
            (carpeta / "catalogo.py").write_bytes(original)
            if estado != "base":
                (carpeta / "operar.py").write_bytes(b"# Incremento sint\xc3\xa9tico.\n")
        self.assertEqual(conservar_herencia_laboratorio_10(repo)["estado"], "APROBADO")
        (raiz_estados / "solucion" / "catalogo.py").write_bytes(original + b"# Cambio.\n")
        self.assertEqual(conservar_herencia_laboratorio_10(repo)["estado"], "FALLIDO")
        (raiz_estados / "solucion" / "catalogo.py").write_bytes(original)
        (raiz_estados / "base" / "operar.py").write_bytes(b"# No corresponde a la base.\n")
        self.assertEqual(conservar_herencia_laboratorio_10(repo)["estado"], "FALLIDO")


if __name__ == "__main__":
    unittest.main(verbosity=2)
