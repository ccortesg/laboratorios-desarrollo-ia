"""W01-W04: verifica respuestas HTTP reales, con cinco casos explícitos."""

import argparse
import json
from pathlib import Path
import unittest
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen

from pruebas_resumen import ResultadoRegistrado
from soporte_web import servidor_local

BASE = Path(__file__).resolve().parent
ESTADO = None
URL = None
CASOS = ("W01", "W02", "W03", "W04.a", "W04.b")


class HttpTests(unittest.TestCase):
    def setUp(self):
        if ESTADO == "base":
            self.skipTest("El estado base todavía no tiene servidor ni interfaz web.")

    def comprobar(self, parametros, estado_http, cuerpo):
        ruta = "/api/resumen?" + urlencode(parametros)
        self.entrada = {"metodo": "GET", "ruta": ruta}
        self.esperado = {"estado_http": estado_http,
                         "tipo_contenido": "application/json; charset=utf-8",
                         "json": cuerpo}
        try:
            respuesta = urlopen(URL + ruta, timeout=5)
        except HTTPError as error:
            respuesta = error
        with respuesta:
            self.observado = {"estado_http": respuesta.code,
                              "tipo_contenido": respuesta.headers.get("Content-Type"),
                              "json": json.loads(respuesta.read().decode("utf-8"))}
        self.assertEqual(self.esperado, self.observado)

    def test_w01_alfa_sin_nombre(self):
        """W01: ALFA sin nombre devuelve un artículo local por HTTP."""
        self.comprobar({"almacen": "ALFA"}, 200,
                       {"almacen": "ALFA", "total": 1, "codigos": ["A01"]})

    def test_w02_beta_nombre_normalizado(self):
        """W02: BETA y OTRA con espacios conservan nombre y almacén."""
        self.comprobar({"almacen": "BETA", "nombre": " OTRA "}, 200,
                       {"almacen": "BETA", "total": 1, "codigos": ["A04"]})

    def test_w03_consulta_valida_vacia(self):
        """W03: ALFA y otra devuelven 200 y un resumen vacío."""
        self.comprobar({"almacen": "ALFA", "nombre": "otra"}, 200,
                       {"almacen": "ALFA", "total": 0, "codigos": []})

    def test_w04a_almacen_omitido(self):
        """W04.a: omitir el almacén devuelve 400 con error explícito."""
        self.comprobar({}, 400, {"error": {"codigo": "ALMACEN_REQUERIDO",
                                         "mensaje": "Selecciona un almacén."}})

    def test_w04b_almacen_vacio(self):
        """W04.b: almacén vacío devuelve 400 sin elegir un valor implícito."""
        self.comprobar({"almacen": ""}, 400,
                       {"error": {"codigo": "ALMACEN_REQUERIDO",
                                  "mensaje": "Selecciona un almacén."}})


def main():
    global ESTADO, URL
    parser = argparse.ArgumentParser(description=__doc__)
    origen = parser.add_mutually_exclusive_group(required=True)
    origen.add_argument("--estado", choices=("base", "propuesta", "solucion"))
    origen.add_argument("--directorio", type=Path,
                        help="Copia propia que contiene servidor.py y los módulos del catálogo.")
    parser.add_argument("--json", type=Path)
    opciones = parser.parse_args()
    ESTADO = opciones.estado
    directorio = (BASE / "estados" / ESTADO if ESTADO
                  else opciones.directorio.resolve())
    resultado = ResultadoRegistrado()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(HttpTests)
    bloqueado = None
    try:
        if ESTADO == "base":
            suite.run(resultado)
        else:
            with servidor_local(directorio) as url:
                URL = url
                suite.run(resultado)
    except OSError as error:
        bloqueado = {"tipo_error": type(error).__name__,
                     "detalle": "No fue posible iniciar el servidor local de pruebas."}
    if bloqueado:
        registros = [{"id": caso, "estado": "BLOQUEADO", **bloqueado}
                     for caso in CASOS]
    else:
        registros = resultado.registros
    registro = {
        "bateria": "http", "estado_codigo": ESTADO or "copia_del_lector",
        "casos_registrados": len(registros), "criterios_distintos": 4,
        "ejecutados": sum(p["estado"] in ("APROBADO", "FALLIDO") for p in registros),
        "aprobados": sum(p["estado"] == "APROBADO" for p in registros),
        "fallidos": sum(p["estado"] == "FALLIDO" for p in registros),
        "fallos_de_asercion": len(resultado.failures),
        "errores_de_ejecucion": len(resultado.errors),
        "bloqueados": sum(p["estado"] == "BLOQUEADO" for p in registros),
        "no_ejecutados": sum(p["estado"] == "NO EJECUTADO" for p in registros),
        "pruebas": registros,
        "alcance": "Peticiones HTTP contra un servidor real local; no prueba el navegador.",
    }
    for prueba in registros:
        print(prueba["id"] + ": " + prueba["estado"])
    print(json.dumps({k: registro[k] for k in
                      ("ejecutados", "aprobados", "fallidos", "bloqueados", "no_ejecutados")}))
    if opciones.json:
        opciones.json.parent.mkdir(parents=True, exist_ok=True)
        opciones.json.write_text(json.dumps(registro, ensure_ascii=False, indent=2)
                                 + "\n", encoding="utf-8")
    return 2 if bloqueado else (0 if resultado.wasSuccessful() else 1)


if __name__ == "__main__":
    raise SystemExit(main())
