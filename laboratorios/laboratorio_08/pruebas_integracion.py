"""I01-I08: comportamiento observable del adaptador CSV, 17 casos."""

import argparse
import hashlib
import importlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

from pruebas_resumen import ResultadoRegistrado

BASE = Path(__file__).resolve().parent
ESTADO = None
DIRECTORIO = None
MODULO = None
LABORATORIO = None
RESUMEN = None
CABECERA = b"codigo_articulo,almacen,existencias\n"
CASOS = ["I01", "I02.a", "I02.b", "I02.c", "I02.d", "I02.e", "I03.a",
         "I03.b", "I03.c", "I04.a", "I04.b", "I04.c", "I04.d",
         "I05", "I06", "I07", "I08"]


def estado_completo(conexion):
    return {
        "articulos": [list(f) for f in conexion.execute("SELECT codigo, nombre, habilitado FROM articulos ORDER BY codigo")],
        "almacenes": [list(f) for f in conexion.execute("SELECT codigo FROM almacenes ORDER BY codigo")],
        "existencias": [list(f) for f in conexion.execute("SELECT articulo, almacen, cantidad FROM existencias ORDER BY articulo, almacen")],
    }


class IntegracionTests(unittest.TestCase):
    def setUp(self):
        if ESTADO == "base":
            self.skipTest("La base conserva el catálogo web anterior sin importador CSV.")
        self.conexion = LABORATORIO.crear_conexion()
        self.addCleanup(self.conexion.close)
        self.temporal = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporal.cleanup)
        self.archivo = Path(self.temporal.name) / "entrada.csv"

    def importar(self, contenido):
        self.archivo.write_bytes(contenido)
        return MODULO.importar_existencias(self.conexion, self.archivo)

    def rechazo(self, contenido, codigo, fila=None, campo=None):
        antes = estado_completo(self.conexion)
        informe = self.importar(contenido)
        despues = estado_completo(self.conexion)
        self.entrada = {"sha256": hashlib.sha256(contenido).hexdigest()}
        self.esperado = {"estado": "RECHAZADO", "codigo_error": codigo,
                         "filas_aplicadas": 0, "sin_cambios": True}
        self.observado = {"informe": informe, "sin_cambios": antes == despues}
        self.assertEqual("RECHAZADO", informe["estado"])
        self.assertEqual(0, informe["filas_aplicadas"])
        self.assertEqual(antes, despues)
        encontrados = [e for e in informe["errores"] if e["codigo"] == codigo]
        self.assertTrue(encontrados)
        if fila is not None:
            self.assertEqual(fila, encontrados[0]["fila"])
        if campo is not None:
            self.assertEqual(campo, encontrados[0]["campo"])
        return informe

    def test_i01_archivo_valido_y_catalogo_misma_base(self):
        """I01: la actualización absoluta cambia la disponibilidad real del catálogo."""
        informe = self.importar((BASE / "datos/actualizacion_valida.csv").read_bytes())
        self.esperado = {"ALFA": {"almacen": "ALFA", "total": 2, "codigos": ["A01", "A03"]},
                         "BETA": {"almacen": "BETA", "total": 0, "codigos": []},
                         "existencias": [["A01", "ALFA", 5], ["A02", "ALFA", 8],
                                         ["A03", "ALFA", 3], ["A04", "BETA", 0]],
                         "habilitado_A02": 0}
        self.observado = {"ALFA": RESUMEN.resumir_catalogo("ALFA", conexion=self.conexion),
                          "BETA": RESUMEN.resumir_catalogo("BETA", conexion=self.conexion),
                          "existencias": estado_completo(self.conexion)["existencias"],
                          "habilitado_A02": self.conexion.execute("SELECT habilitado FROM articulos WHERE codigo='A02'").fetchone()[0]}
        self.assertEqual("APLICADO", informe["estado"])
        self.assertEqual(self.esperado, self.observado)

    def test_i02a_cabecera_incorrecta(self):
        """I02.a: encabezado con campo incorrecto o en otro orden se rechaza."""
        self.rechazo(b"almacen,codigo_articulo,existencias\nALFA,A01,5\n", "CABECERA", 1)

    def test_i02b_columnas_extra_o_ausentes(self):
        """I02.b: una fila debe tener exactamente tres columnas."""
        for fila in (b"A01,ALFA,5,extra\n", b"A01,ALFA\n"):
            self.rechazo(CABECERA + fila, "COLUMNAS", 2)

    def test_i02c_codificacion_invalida(self):
        """I02.c: bytes que no representan UTF-8 se rechazan."""
        self.rechazo(CABECERA + b"A01,ALFA,\xff\n", "CODIFICACION")

    def test_i02d_archivo_sin_datos(self):
        """I02.d: vacío y encabezado sin registros no producen un éxito vacío."""
        self.rechazo(b"", "CABECERA", 1)
        self.rechazo(CABECERA, "SIN_DATOS", 1)

    def test_i02e_fila_vacia(self):
        """I02.e: una fila vacía se rechaza y no se omite silenciosamente."""
        self.rechazo(CABECERA + b"A01,ALFA,5\n\n", "COLUMNAS", 3)

    def test_i03a_articulo_desconocido(self):
        """I03.a: no se crea un artículo desconocido al importar."""
        self.rechazo(CABECERA + b"Z99,ALFA,5\n", "ARTICULO_DESCONOCIDO", 2, "codigo_articulo")

    def test_i03b_almacen_desconocido(self):
        """I03.b: no se crea un almacén desconocido al importar."""
        self.rechazo(CABECERA + b"A01,GAMMA,5\n", "ALMACEN_DESCONOCIDO", 2, "almacen")

    def test_i03c_identificadores_exactos(self):
        """I03.c: los códigos no heredan strip o casefold de la búsqueda por nombre."""
        for codigo in (b" a01 ", b"a01", b"A1"):
            self.rechazo(CABECERA + codigo + b",ALFA,5\n", "ARTICULO_DESCONOCIDO", 2)

    def test_i04a_cantidad_negativa(self):
        """I04.a: una cantidad negativa se rechaza antes de escribir."""
        self.rechazo(CABECERA + b"A01,ALFA,-1\n", "CANTIDAD_INVALIDA", 2)

    def test_i04b_cantidad_fraccionaria(self):
        """I04.b: una cantidad fraccionaria no se redondea silenciosamente."""
        self.rechazo(CABECERA + b"A01,ALFA,1.5\n", "CANTIDAD_INVALIDA", 2)

    def test_i04c_cantidad_no_numerica(self):
        """I04.c: texto y campos vacíos no se convierten a cero."""
        for cantidad in (b"muchas", b"", b" 5 ", b"+5", b"1e2"):
            self.rechazo(CABECERA + b"A01,ALFA," + cantidad + b"\n", "CANTIDAD_INVALIDA", 2)

    def test_i04d_cantidad_fuera_de_rango(self):
        """I04.d: el rango contractual se comprueba antes de SQLite."""
        self.rechazo(CABECERA + b"A01,ALFA,2147483648\n", "CANTIDAD_INVALIDA", 2)

    def test_i05_par_duplicado(self):
        """I05: se rechaza el par repetido sin escoger primera o última fila."""
        self.rechazo((BASE / "datos/par_duplicado.csv").read_bytes(), "PAR_DUPLICADO", 3)

    def test_i06_error_tardio_sin_cambio_parcial(self):
        """I06: validación tardía y escritura rechazada conservan las tres tablas."""
        informe = self.rechazo((BASE / "datos/error_tardio.csv").read_bytes(), "CANTIDAD_INVALIDA", 3)
        self.assertEqual(2, informe["filas_leidas"])
        self.assertEqual(1, informe["filas_validadas"])
        validacion = self.observado
        self.conexion.isolation_level = None
        self.conexion.execute(
            "CREATE TEMP TRIGGER rechazo_sintetico BEFORE UPDATE OF cantidad ON existencias "
            "WHEN NEW.articulo = 'A02' BEGIN SELECT RAISE(ABORT, 'rechazo sintetico'); END")
        informe = self.rechazo((BASE / "datos/actualizacion_valida.csv").read_bytes(), "ESCRITURA")
        self.assertEqual(4, informe["filas_leidas"])
        self.assertEqual(4, informe["filas_validadas"])
        self.assertFalse(self.conexion.in_transaction)
        self.observado = {"validacion_tardia": validacion,
                          "fallo_escritura_controlado": self.observado,
                          "isolation_level": None, "transaccion_cerrada": True}

    def test_i07_repeticion_y_pares_omitidos(self):
        """I07: dos importaciones sobre la misma base son idempotentes."""
        entrada = CABECERA + b"A01,ALFA,5\n"
        antes = estado_completo(self.conexion)
        primero = self.importar(entrada)
        estado_primero = estado_completo(self.conexion)
        segundo = self.importar(entrada)
        estado_segundo = estado_completo(self.conexion)
        self.esperado = {"cantidad_A01": 5, "mismo_estado": True,
                         "pares_omitidos_intactos": True, "cambios_segunda": 0}
        self.observado = {"cantidad_A01": estado_segundo["existencias"][0][2],
                          "mismo_estado": estado_primero == estado_segundo,
                          "pares_omitidos_intactos": antes["existencias"][1:] == estado_segundo["existencias"][1:],
                          "cambios_segunda": segundo["filas_aplicadas"]}
        self.assertEqual("APLICADO", primero["estado"])
        self.assertEqual("APLICADO", segundo["estado"])
        self.assertEqual(self.esperado, self.observado)

    def test_i08_informe_y_error_localizable(self):
        """I08: SHA-256 y conteos describen los bytes leídos y el resultado real."""
        contenido = b"\xef\xbb\xbfcodigo_articulo,almacen,existencias\r\nA03,ALFA,3\r\n"
        informe = self.importar(contenido)
        self.esperado = {"estado": "APLICADO", "sha256_fuente": hashlib.sha256(contenido).hexdigest(),
                         "filas_leidas": 1, "filas_validadas": 1, "filas_aplicadas": 1,
                         "filas_sin_cambio": 0, "errores": []}
        self.observado = informe
        self.assertEqual(self.esperado, informe)
        rechazo = self.importar(CABECERA + b"A01,ALFA,5\nA03,ALFA,no\n")
        self.assertEqual("RECHAZADO", rechazo["estado"])
        self.assertEqual(3, rechazo["errores"][0]["fila"])
        self.assertEqual("existencias", rechazo["errores"][0]["campo"])
        self.assertNotIn(str(self.archivo), json.dumps(rechazo))


def main():
    global ESTADO, DIRECTORIO, MODULO, LABORATORIO, RESUMEN
    parser = argparse.ArgumentParser(description=__doc__)
    origen = parser.add_mutually_exclusive_group(required=True)
    origen.add_argument("--estado", choices=("base", "propuesta", "solucion"))
    origen.add_argument("--directorio", type=Path)
    parser.add_argument("--json", type=Path)
    opciones = parser.parse_args()
    ESTADO = opciones.estado
    DIRECTORIO = BASE / "estados" / ESTADO if ESTADO else opciones.directorio.resolve()
    if not DIRECTORIO.is_dir():
        parser.error("El directorio de código no existe.")
    sys.path.insert(0, str(DIRECTORIO))
    if ESTADO != "base":
        MODULO = importlib.import_module("importacion")
        LABORATORIO = importlib.import_module("laboratorio")
        RESUMEN = importlib.import_module("resumen")
    resultado = ResultadoRegistrado()
    unittest.defaultTestLoader.loadTestsFromTestCase(IntegracionTests).run(resultado)
    registros = resultado.registros
    registro = {"bateria": "integracion", "estado_codigo": ESTADO or "copia_del_lector",
        "casos_registrados": len(registros), "criterios_distintos": 8,
        "ejecutados": resultado.testsRun - len(resultado.skipped),
        "aprobados": sum(p["estado"] == "APROBADO" for p in registros),
        "fallidos": len(resultado.failures) + len(resultado.errors),
        "fallos_de_asercion": len(resultado.failures), "errores_de_ejecucion": len(resultado.errors),
        "bloqueados": 0, "no_ejecutados": len(resultado.skipped), "pruebas": registros}
    for prueba in registros:
        print(prueba["id"] + ": " + prueba["estado"])
    print(json.dumps({k: registro[k] for k in ("ejecutados", "aprobados", "fallidos", "bloqueados", "no_ejecutados")}, ensure_ascii=False))
    if opciones.json:
        opciones.json.parent.mkdir(parents=True, exist_ok=True)
        opciones.json.write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
