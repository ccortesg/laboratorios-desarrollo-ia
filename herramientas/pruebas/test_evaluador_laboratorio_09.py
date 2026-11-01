"""Regresiones del evaluador de evidencia; no son casos funcionales del catálogo.

Las fixtures expresan el contrato de 74 casos por estado y se alteran para
comprobar que una declaración de aprobación no sustituye evidencia consistente.
No se ejecutan servidores ni se accede a red.
"""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verificar_todo import evaluar_laboratorio_web


GRUPOS = {
    "heredados": (["C%02d" % i for i in range(1, 5)]
                  + ["B%02d" % i for i in range(1, 7)]
                  + ["N%02d" % i for i in range(1, 11)]),
    "resumen": ["P%02d" % i for i in range(1, 7)],
    "http": ["W01", "W02", "W03", "W04.a", "W04.b"],
    "navegador": ["W05", "W06.a", "W06.b"],
    "integracion": (["I01"] + ["I02." + c for c in "abcde"]
                    + ["I03." + c for c in "abc"]
                    + ["I04." + c for c in "abcd"]
                    + ["I05", "I06", "I07", "I08"]),
    "depuracion": ["D01", "D02", "D03", "D05", "D06.a", "D06.b",
                   "D07.a", "D07.b", "D08.a", "D08.b"],
    "depuracion_navegador": ["D04"],
    "seguridad": ["S01", "S02.a", "S02.b", "S02.c", "S03", "S04.a",
                  "S04.b", "S05.a", "S05.b", "S07", "S08"],
    "seguridad_navegador": ["S06"],
}
FALLOS = {
    ("base", "seguridad"): {"S02.a", "S02.b", "S02.c", "S03", "S04.a",
                            "S04.b", "S05.a", "S05.b"},
    ("base", "seguridad_navegador"): {"S06"},
    ("propuesta", "seguridad"): {"S02.a", "S02.b", "S02.c"},
}
CONTEOS = ("ejecutados", "aprobados", "fallidos", "bloqueados",
           "no_ejecutados", "errores_de_ejecucion")


def conteos(casos):
    return {
        "ejecutados": sum(c["estado"] in {"APROBADO", "FALLIDO"} for c in casos),
        "aprobados": sum(c["estado"] == "APROBADO" for c in casos),
        "fallidos": sum(c["estado"] == "FALLIDO" for c in casos),
        "fallos_de_asercion": sum(c["estado"] == "FALLIDO"
                                 and c.get("tipo_error") == "AssertionError" for c in casos),
        "bloqueados": sum(c["estado"] == "BLOQUEADO" for c in casos),
        "no_ejecutados": sum(c["estado"] == "NO EJECUTADO" for c in casos),
        "errores_de_ejecucion": sum(c["estado"] == "FALLIDO"
                                    and c.get("tipo_error") != "AssertionError" for c in casos),
    }


class EvaluadorLaboratorio09Tests(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory(prefix="evaluador_lab09_")
        self.addCleanup(self.temporal.cleanup)
        self.raiz = Path(self.temporal.name)
        self.registros = {}
        self.navegador = True

    def crear_fixture(self, navegador=True):
        self.navegador = navegador
        for estado in ("base", "propuesta", "solucion"):
            for grupo, ids in GRUPOS.items():
                sin_navegador = grupo.endswith("navegador") and not navegador
                casos = []
                for identificador in ids:
                    resultado = ("NO EJECUTADO" if sin_navegador else
                                 "FALLIDO" if identificador in FALLOS.get((estado, grupo), ())
                                 else "APROBADO")
                    caso = {"id": identificador, "estado": resultado}
                    if resultado == "FALLIDO":
                        caso["tipo_error"] = "AssertionError"
                    casos.append(caso)
                self.registros[estado + "_" + grupo] = {
                    "estado_codigo": estado, "grupo": grupo, "pruebas": casos,
                }

    def guardar_fixture(self, estado_global=None):
        """Recalcula cantidades después de mutar: no depende de cifras obsoletas."""
        comandos, baterias = [], []
        for nombre, fuente in self.registros.items():
            casos = fuente["pruebas"]
            numeros = conteos(casos)
            codigo = (2 if numeros["bloqueados"] else 1 if numeros["fallidos"] else
                      None if numeros["no_ejecutados"] == len(casos) else 0)
            registro = dict(numeros, casos_registrados=len(casos), pruebas=casos)
            (self.raiz / (nombre + ".json")).write_text(
                json.dumps(registro), encoding="utf-8")
            comandos.append({"id": nombre, "codigo_salida": codigo})
            baterias.append({
                "estado_codigo": fuente["estado_codigo"], "bateria": fuente["grupo"],
                "resultado": nombre + ".json",
                "patron": {"estado": "BLOQUEADO" if numeros["bloqueados"] else "APROBADO"},
                **{k: numeros[k] for k in CONTEOS},
            })
        bloqueado = any(b["bloqueados"] for b in baterias)
        estado = (estado_global or ("BLOQUEADO" if bloqueado else
                                   "APROBADO" if self.navegador else "NO EJECUTADO"))
        resumen = {
            "estado": estado, "extremo_a_extremo": estado,
            "alcance_ejecutado": "BLOQUEADO" if bloqueado else "APROBADO",
            "conservacion_heredados": "APROBADO",
            "base_sin_incremento_seguridad": "APROBADO",
            "navegador_solicitado": self.navegador,
            "baterias": baterias,
            "totales": {k: sum(b[k] for b in baterias) for k in CONTEOS},
        }
        (self.raiz / "resumen.json").write_text(json.dumps(resumen), encoding="utf-8")
        (self.raiz / "comandos.json").write_text(
            json.dumps({"registros": comandos}), encoding="utf-8")
        return resumen

    def evaluar(self):
        return evaluar_laboratorio_web(self.raiz, self.navegador, numero=9)

    def caso(self, bateria, identificador):
        return next(c for c in self.registros[bateria]["pruebas"] if c["id"] == identificador)

    def test_patron_completo_conserva_heredados_y_fallos_didacticos(self):
        """E09.01: sólo el patrón exacto permite aprobar el recorrido completo."""
        self.crear_fixture()
        resumen = self.guardar_fixture()
        correcto, baterias, estado = self.evaluar()
        self.assertTrue(correcto)
        self.assertEqual(estado, "APROBADO")
        self.assertEqual(len(baterias), 27)
        self.assertEqual(resumen["totales"]["ejecutados"], 222)
        self.assertEqual(resumen["totales"]["aprobados"], 210)
        self.assertEqual(resumen["totales"]["fallidos"], 12)

    def test_rechaza_fallo_no_previsto_aunque_los_conteos_cuadren(self):
        """E09.02: S07 no pertenece a la lista de fallos admitidos."""
        self.crear_fixture()
        self.caso("propuesta_seguridad", "S07").update(
            estado="FALLIDO", tipo_error="AssertionError")
        self.guardar_fixture()
        correcto, _, estado = self.evaluar()
        self.assertFalse(correcto)
        self.assertEqual(estado, "FALLIDO")

    def test_error_de_ejecucion_no_suplanta_un_fallo_didactico(self):
        """E09.03: un OSError en S02.a no acredita el defecto intencional."""
        self.crear_fixture()
        self.caso("propuesta_seguridad", "S02.a")["tipo_error"] = "OSError"
        self.guardar_fixture()
        self.assertFalse(self.evaluar()[0])

    def test_rechaza_caso_ausente_con_totales_recalculados(self):
        """E09.04: no basta declarar una batería más corta como aprobada."""
        self.crear_fixture()
        self.registros["solucion_seguridad"]["pruebas"] = [
            c for c in self.registros["solucion_seguridad"]["pruebas"] if c["id"] != "S08"]
        self.guardar_fixture()
        self.assertFalse(self.evaluar()[0])

    def test_rechaza_identificador_duplicado(self):
        """E09.05: contar doce filas no demuestra doce casos distintos."""
        self.crear_fixture()
        self.caso("solucion_seguridad", "S08")["id"] = "S07"
        self.guardar_fixture()
        with self.assertRaisesRegex(ValueError, "duplicado"):
            self.evaluar()

    def test_sin_navegador_no_declara_recorrido_completo_aprobado(self):
        """E09.06: el alcance local puede aprobar y el global sigue NO EJECUTADO."""
        self.crear_fixture(navegador=False)
        self.guardar_fixture()
        correcto, _, estado = self.evaluar()
        self.assertTrue(correcto)
        self.assertEqual(estado, "NO EJECUTADO")
        self.guardar_fixture(estado_global="APROBADO")
        self.assertFalse(self.evaluar()[0])

    def test_bloqueo_parcial_se_conserva_y_no_equivale_a_aprobacion(self):
        """E09.07: la indisponibilidad de un servidor se conserva como BLOQUEADO."""
        self.crear_fixture()
        c = self.caso("base_seguridad", "S02.a")
        c.clear()
        c.update(id="S02.a", estado="BLOQUEADO")
        self.guardar_fixture()
        correcto, baterias, estado = self.evaluar()
        self.assertTrue(correcto)
        self.assertEqual(estado, "BLOQUEADO")
        self.assertEqual(next(b["evaluacion_del_recorrido"] for b in baterias
                              if b["bateria"] == "laboratorio_09/base_seguridad"), "BLOQUEADO")
        self.guardar_fixture(estado_global="APROBADO")
        self.assertFalse(self.evaluar()[0])

    def test_rechaza_resumen_con_cantidades_inventadas(self):
        """E09.08: los totales declarados se contrastan con las baterías."""
        self.crear_fixture()
        resumen = self.guardar_fixture()
        resumen["totales"]["aprobados"] += 1
        (self.raiz / "resumen.json").write_text(json.dumps(resumen), encoding="utf-8")
        self.assertFalse(self.evaluar()[0])

    def test_rechaza_desaparicion_del_fallo_intencional(self):
        """E09.09: una propuesta sin el fallo esperado ya no demuestra ese recorrido."""
        self.crear_fixture()
        c = self.caso("propuesta_seguridad", "S02.c")
        c.clear()
        c.update(id="S02.c", estado="APROBADO")
        self.guardar_fixture()
        self.assertFalse(self.evaluar()[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
