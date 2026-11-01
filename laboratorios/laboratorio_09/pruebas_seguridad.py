"""S01–S08: contrato de entrada por HTTP real; S06 vive en navegador."""
import argparse
import json
from pathlib import Path
import tempfile
import unittest
from urllib.error import HTTPError
from urllib.parse import urlencode

from pruebas_resumen import ResultadoRegistrado
from soporte_procesos import BASE, Escenario, HTTP, snapshot, huella_bytes, BloqueoEntorno

CASOS = ["S01", "S02.a", "S02.b", "S02.c", "S03", "S04.a", "S04.b",
         "S05.a", "S05.b", "S07", "S08"]
DIRECTORIO = None
ACTUALIZADO = {"almacen": "ALFA", "total": 2, "codigos": ["A01", "A03"]}


class ResultadoSeguridad(ResultadoRegistrado):
    def addError(self, test, err):
        if isinstance(err[1], BloqueoEntorno):
            self.registrar(test, "BLOQUEADO", str(err[1]), type(err[1]).__name__)
        else:
            super().addError(test, err)


class SeguridadTests(unittest.TestCase):
    def setUp(self):
        temporal = tempfile.TemporaryDirectory(prefix="lab09_http_")
        self.addCleanup(temporal.cleanup)
        self.trabajo = Path(temporal.name)
        self.base = self.trabajo / "principal.sqlite"
        self.escenario = Escenario(DIRECTORIO, self.trabajo)
        self.observado = {"operaciones": self.escenario.operaciones, "peticiones": []}
        self.assertEqual(0, self.escenario.cli("iniciar", self.base)[0])
        rc, informe = self.escenario.cli("importar", self.base,
            "--archivo", BASE / "datos/actualizacion_valida.csv")
        self.assertEqual(0, rc)
        self.assertEqual("APLICADO", informe["estado"])
        self.huella_inicial = huella_bytes(self.base)
        self.estado_inicial = snapshot(self.base)
        self.servidor = self.escenario.servidor(self.base)
        self.url, _ = self.servidor.__enter__()
        self.addCleanup(self.servidor.__exit__, None, None, None)

    def tearDown(self):
        # Todas las consultas, también las rechazadas, deben conservar el estado.
        if hasattr(self, "huella_inicial") and self.base.exists():
            iguales = (self.huella_inicial == huella_bytes(self.base)
                       and self.estado_inicial == snapshot(self.base))
            self.observado["base_sin_modificaciones"] = iguales
            self.assertTrue(iguales, "La consulta alteró la base de práctica.")

    def pedir(self, query):
        try:
            respuesta = HTTP.open(self.url + "/api/resumen?" + query, timeout=10)
        except HTTPError as error:
            respuesta = error
        with respuesta:
            cuerpo = respuesta.read()
            estado = respuesta.code
            datos = json.loads(cuerpo)
            tipo = respuesta.headers.get("Content-Type")
        self.observado["peticiones"].append({
            "metodo": "GET", "ruta": "/api/resumen", "query_bytes": len(query.encode("utf-8")),
            "query": query if len(query) <= 120 else "<CONSULTA_SINTETICA_LARGA>",
            "http": estado, "content_type": tipo, "respuesta": datos,
        })
        self.assertEqual("application/json; charset=utf-8", tipo)
        self.assertNotIn(str(self.trabajo), cuerpo.decode("utf-8"))
        return estado, datos

    def rechazo(self, query, http, codigo):
        self.entrada = {"query": query if len(query) <= 120 else "<CONSULTA_SINTETICA_LARGA>",
                        "query_bytes": len(query.encode("utf-8"))}
        self.esperado = {"http": http, "codigo": codigo, "sin_modificar_base": True}
        observado, datos = self.pedir(query)
        self.assertEqual(http, observado)
        self.assertEqual({"error"}, set(datos))
        self.assertEqual({"codigo", "mensaje"}, set(datos["error"]))
        self.assertEqual(codigo, datos["error"]["codigo"])
        self.assertTrue(datos["error"]["mensaje"])

    def test_s01_consulta_valida_y_borde(self):
        """S01: consultar datos importados conserva búsqueda y acepta 80 puntos de código."""
        self.entrada = {"archivo": "datos/actualizacion_valida.csv", "almacen": "ALFA",
                        "nombre_normalizado": " AGOTADO ", "nombre_en_limite": "é × 80"}
        self.esperado = {"catalogo": ACTUALIZADO, "busqueda": ["A03"],
                         "nombre_80_http": 200, "almacen_desconocido": []}
        self.assertEqual((200, ACTUALIZADO), self.pedir("almacen=ALFA"))
        http, datos = self.pedir(urlencode({"almacen": "ALFA", "nombre": " AGOTADO "}))
        self.assertEqual(200, http)
        self.assertEqual(["A03"], datos["codigos"])
        http, datos = self.pedir(urlencode({"almacen": "ALFA", "nombre": "é" * 80}))
        self.assertEqual(200, http)
        self.assertEqual([], datos["codigos"])
        http, datos = self.pedir("almacen=alfa")
        self.assertEqual(200, http)
        self.assertEqual([], datos["codigos"])

    def test_s02a_dos_almacenes(self):
        """S02.a: dos valores de almacén se rechazan sin elegir uno."""
        self.rechazo("almacen=ALFA&almacen=BETA", 400, "PARAMETRO_REPETIDO")

    def test_s02b_nombre_igual_repetido(self):
        """S02.b: repetir nombre se rechaza incluso con valores iguales."""
        self.rechazo("almacen=ALFA&nombre=local&nombre=local", 400, "PARAMETRO_REPETIDO")

    def test_s02c_clave_codificada_equivalente(self):
        """S02.c: las claves equivalentes tras decodificar se reconocen como repetidas."""
        self.rechazo("almacen=ALFA&%61lmacen=ALFA", 400, "PARAMETRO_REPETIDO")

    def test_s03_clave_adicional(self):
        """S03: una clave adicional no se ignora silenciosamente."""
        self.rechazo("almacen=ALFA&debug=1", 400, "PARAMETRO_DESCONOCIDO")

    def test_s04a_nombre_largo_antes_de_strip(self):
        """S04.a: 81 puntos de código, también espacios, exceden el límite."""
        self.rechazo(urlencode({"almacen": "ALFA", "nombre": " " * 81}),
                     400, "NOMBRE_DEMASIADO_LARGO")
        self.rechazo(urlencode({"almacen": "ALFA", "nombre": "é" * 81}),
                     400, "NOMBRE_DEMASIADO_LARGO")

    def test_s04b_query_larga_y_recuperacion(self):
        """S04.b: 2048 bytes son el borde; 2049 se rechazan y la siguiente consulta funciona."""
        borde = "almacen=" + "A" * (2048 - len("almacen="))
        self.assertEqual(2048, len(borde.encode("utf-8")))
        http, datos = self.pedir(borde)
        self.assertEqual(200, http)
        self.assertEqual([], datos["codigos"])
        self.rechazo(borde + "A", 414, "CONSULTA_DEMASIADO_LARGA")
        self.assertEqual((200, ACTUALIZADO), self.pedir("almacen=ALFA"))

    def test_s05a_percent_invalido(self):
        """S05.a: percent-encoding mal formado se rechaza, no se convierte en texto válido."""
        self.rechazo("almacen=ALFA&nombre=%ZZ", 400, "CONSULTA_INVALIDA")

    def test_s05b_utf8_invalido(self):
        """S05.b: bytes UTF-8 inválidos se rechazan sin carácter de sustitución."""
        self.rechazo("almacen=ALFA&nombre=%FF", 400, "CONSULTA_INVALIDA")

    def test_s07_texto_parecido_a_sql(self):
        """S07: una cadena parecida a SQL sigue siendo un valor de búsqueda."""
        nombre = "%' OR 1=1 --"
        self.entrada = {"almacen": "ALFA", "nombre": nombre}
        self.esperado = {"http": 200, "total": 0, "codigos": [], "base_sin_modificaciones": True}
        http, datos = self.pedir(urlencode({"almacen": "ALFA", "nombre": nombre}))
        self.assertEqual(200, http)
        self.assertEqual({"almacen": "ALFA", "total": 0, "codigos": []}, datos)
        self.assertEqual((200, ACTUALIZADO), self.pedir("almacen=ALFA"))

    def test_s08_error_interno_generico_y_recuperacion(self):
        """S08: una base temporalmente ausente produce un error genérico y se recupera."""
        self.entrada = {"fallo_controlado": "Renombrar la base aislada después de iniciar el servidor."}
        self.esperado = {"http": 500, "codigo": "CONSULTA_FALLIDA", "recuperacion": ACTUALIZADO}
        desplazada = self.trabajo / "base_apartada.sqlite"
        self.base.rename(desplazada)
        try:
            http, datos = self.pedir("almacen=ALFA")
            self.assertEqual(500, http)
            self.assertEqual({"error": {"codigo": "CONSULTA_FALLIDA",
                "mensaje": "No fue posible consultar el catálogo."}}, datos)
            self.assertFalse(self.base.exists(), "La consulta no debe crear otra base.")
        finally:
            desplazada.rename(self.base)
        self.assertEqual((200, ACTUALIZADO), self.pedir("almacen=ALFA"))


def main():
    global DIRECTORIO
    parser = argparse.ArgumentParser(description=__doc__)
    origen = parser.add_mutually_exclusive_group(required=True)
    origen.add_argument("--estado", choices=("base", "propuesta", "solucion"))
    origen.add_argument("--directorio", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    DIRECTORIO = (BASE / "estados" / args.estado if args.estado else args.directorio).resolve()
    resultado = ResultadoSeguridad()
    unittest.defaultTestLoader.loadTestsFromTestCase(SeguridadTests).run(resultado)
    registro = {"bateria": "seguridad", "estado_codigo": args.estado or "copia_del_lector",
        "casos_registrados": len(resultado.registros), "criterios_distintos": 7,
        "ejecutados": sum(r["estado"] in ("APROBADO", "FALLIDO") for r in resultado.registros),
        "aprobados": sum(r["estado"] == "APROBADO" for r in resultado.registros),
        "fallidos": len(resultado.failures) + len(resultado.errors),
        "fallos_de_asercion": len(resultado.failures), "errores_de_ejecucion": len(resultado.errors),
        "bloqueados": sum(r["estado"] == "BLOQUEADO" for r in resultado.registros),
        "no_ejecutados": len(resultado.skipped), "pruebas": resultado.registros}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for r in resultado.registros:
        print(r["id"] + ": " + r["estado"])
        if r["tipo_error"]:
            print("  " + r["tipo_error"] + ": " + r["detalle"])
    return 1 if registro["fallidos"] else 2 if registro["bloqueados"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
