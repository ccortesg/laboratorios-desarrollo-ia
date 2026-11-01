"""Pruebas focales del evaluador; los registros son sintéticos, no ejecuciones del catálogo."""

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "repositorio" / "herramientas"))
from verificar_todo import evaluar_bateria


IDS = ["D01", "D02", "D03", "D05", "D06.a", "D06.b", "D07.a", "D07.b", "D08.a", "D08.b"]
FALLOS = {"D03", "D05", "D08.a"}


def registro():
    return {
        "casos_registrados": 10, "ejecutados": 10, "aprobados": 7,
        "fallidos": 3, "fallos_de_asercion": 3, "errores_de_ejecucion": 0,
        "bloqueados": 0, "no_ejecutados": 0,
        "pruebas": [{"id": i, "estado": "FALLIDO" if i in FALLOS else "APROBADO",
                     "tipo_error": "AssertionError" if i in FALLOS else None} for i in IDS],
    }


class EvaluadorOchoTests(unittest.TestCase):
    def evaluar(self, r):
        return evaluar_bateria(r, "laboratorio_08/propuesta_depuracion", IDS, 1, fallos=FALLOS)

    def test_patron_exacto_conserva_fallidos_individuales(self):
        observado = self.evaluar(registro())
        self.assertEqual(observado["evaluacion_del_recorrido"], "APROBADO")
        self.assertEqual(observado["fallidos"], 3)
        self.assertEqual({i for i, estado in observado["criterios_observados"].items()
                          if estado == "FALLIDO"}, FALLOS)

    def test_fallo_adicional_no_se_admite_con_totales_coherentes(self):
        r = registro()
        r["pruebas"][0].update(estado="FALLIDO", tipo_error="AssertionError")
        r.update(aprobados=6, fallidos=4, fallos_de_asercion=4)
        self.assertEqual(self.evaluar(r)["evaluacion_del_recorrido"], "FALLIDO")

    def test_caso_ausente_no_se_admite_con_totales_coherentes(self):
        r = registro()
        r["pruebas"].pop(0)
        r.update(casos_registrados=9, ejecutados=9, aprobados=6)
        self.assertEqual(self.evaluar(r)["evaluacion_del_recorrido"], "FALLIDO")

    def test_excepcion_ajena_no_se_acepta_como_defecto_didactico(self):
        r = registro()
        next(p for p in r["pruebas"] if p["id"] == "D03")["tipo_error"] = "RuntimeError"
        r.update(fallos_de_asercion=2, errores_de_ejecucion=1)
        self.assertEqual(self.evaluar(r)["evaluacion_del_recorrido"], "FALLIDO")

    def test_caso_duplicado_se_rechaza(self):
        r = registro()
        r["pruebas"][1] = copy.deepcopy(r["pruebas"][0])
        with self.assertRaises(ValueError):
            self.evaluar(r)

    def parcial(self, id_bloqueado="D02"):
        r = registro()
        next(p for p in r["pruebas"] if p["id"] == id_bloqueado).update(
            estado="BLOQUEADO", tipo_error="PermissionError")
        r.update(ejecutados=9, aprobados=6, bloqueados=1)
        return r

    def evaluar_parcial(self, r):
        return evaluar_bateria(r, "laboratorio_08/propuesta_depuracion", IDS, 2,
                               fallos=FALLOS, permitir_bloqueo=True,
                               bloqueos_parciales={"D02", "D03", "D05", "D08.a"})

    def test_bloqueo_parcial_autorizado_no_aprueba_recorrido_completo(self):
        r = self.evaluar_parcial(self.parcial())
        self.assertEqual(r["evaluacion_del_recorrido"], "BLOQUEADO")
        self.assertEqual(r["ejecutados"], 9)
        self.assertEqual(r["bloqueados"], 1)
        self.assertEqual(r["fallidos"], 3)
        sin_codigo = evaluar_bateria(self.parcial(), "sin_codigo", IDS, None,
                                      fallos=FALLOS, permitir_bloqueo=True,
                                      bloqueos_parciales={"D02", "D03", "D05", "D08.a"})
        self.assertEqual(sin_codigo["evaluacion_del_recorrido"], "FALLIDO")

    def test_bloqueo_parcial_no_oculta_fallo_adicional(self):
        r = self.parcial()
        r["pruebas"][0].update(estado="FALLIDO", tipo_error="AssertionError")
        r.update(aprobados=5, fallidos=4, fallos_de_asercion=4)
        self.assertEqual(self.evaluar_parcial(r)["evaluacion_del_recorrido"], "FALLIDO")

    def test_bloqueo_parcial_fuera_de_casos_permitidos_se_rechaza(self):
        self.assertEqual(self.evaluar_parcial(self.parcial("D01"))["evaluacion_del_recorrido"], "FALLIDO")

    def test_bloqueo_parcial_no_altera_politica_heredada(self):
        r = evaluar_bateria(self.parcial(), "sin_habilitar_mezcla", IDS, 2,
                             fallos=FALLOS, permitir_bloqueo=True)
        self.assertEqual(r["evaluacion_del_recorrido"], "FALLIDO")


if __name__ == "__main__":
    unittest.main(verbosity=2)
