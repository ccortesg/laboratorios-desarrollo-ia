"""D01–D08: persistencia y diagnóstico entre procesos, sin navegador en esta batería."""
import argparse
from contextlib import closing
import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from pruebas_resumen import ResultadoRegistrado
from soporte_procesos import BASE, Escenario, snapshot, huella_bytes, BloqueoEntorno

CASOS = ["D01", "D02", "D03", "D05", "D06.a", "D06.b", "D07.a", "D07.b", "D08.a", "D08.b"]
DIRECTORIO = None
ESTADO = None
ACTUALIZADO = {"almacen": "ALFA", "total": 2, "codigos": ["A01", "A03"]}
REFERENCIA = {"almacen": "ALFA", "total": 1, "codigos": ["A01"]}
VACIO_BETA = {"almacen": "BETA", "total": 0, "codigos": []}
CANTIDADES = [["A01", "ALFA", 5], ["A02", "ALFA", 8],
              ["A03", "ALFA", 3], ["A04", "BETA", 0]]


class ResultadoDepuracion(ResultadoRegistrado):
    def addError(self, test, err):
        if isinstance(err[1], BloqueoEntorno):
            self.registrar(test, "BLOQUEADO", str(err[1]), type(err[1]).__name__)
        else:
            super().addError(test, err)


class DepuracionTests(unittest.TestCase):
    def setUp(self):
        if not (DIRECTORIO / "persistencia.py").is_file():
            self.skipTest("La base conserva el alcance en memoria; no implementa persistencia entre procesos.")
        temporal = tempfile.TemporaryDirectory(prefix="lab08_")
        self.addCleanup(temporal.cleanup)
        self.trabajo = Path(temporal.name)
        self.base = self.trabajo / "principal.sqlite"
        self.escenario = Escenario(DIRECTORIO, self.trabajo)
        self.observado = {"operaciones": self.escenario.operaciones}
        self.assertEqual(0, self.escenario.cli("iniciar", self.base)[0])

    def importar_valido(self, base=None, cwd=None):
        resultado = self.escenario.cli("importar", base or self.base,
            "--archivo", BASE / "datos/actualizacion_valida.csv", cwd=cwd)
        self.assertEqual(0, resultado[0])
        self.assertEqual("APLICADO", resultado[1]["estado"])
        return resultado[1]

    def test_d01_persistencia_y_proceso_nuevo(self):
        """D01: importar y consultar en procesos separados conserva cantidades y catálogo."""
        self.entrada = {"archivo": "datos/actualizacion_valida.csv",
                        "sha256": huella_bytes(BASE / "datos/actualizacion_valida.csv")}
        informe = self.importar_valido()
        codigo, consulta = self.escenario.cli("consultar", self.base)
        self.esperado = {"cantidades": CANTIDADES, "resumen": ACTUALIZADO,
                         "filas_aplicadas": 4}
        self.observado.update({"consulta": consulta, "estado_independiente": snapshot(self.base),
                               "informe": informe})
        self.assertEqual(0, codigo)
        self.assertEqual(CANTIDADES, snapshot(self.base)["existencias"])
        self.assertEqual(ACTUALIZADO, consulta["resumen"])
        self.assertEqual(4, informe["filas_aplicadas"])
        self.assertEqual(0, snapshot(self.base)["articulos"][1][2])

    def test_d02_origen_efectivo_fiel(self):
        """D02: el diagnóstico distingue el origen efectivo, sin alterar el estado."""
        self.importar_valido()
        antes = snapshot(self.base)
        bytes_antes = huella_bytes(self.base)
        rechazo_cli = self.escenario.cli("consultar", self.base, "--diagnostico", self.base)
        rechazo_http = self.escenario.servidor_rechazado(self.base, "--diagnostico", self.base)
        self.observado["colision_diagnostico"] = {"cli": rechazo_cli, "servidor": rechazo_http,
                                                "bytes_intactos": bytes_antes == huella_bytes(self.base)}
        for rc, respuesta in (rechazo_cli, rechazo_http):
            self.assertEqual(2, rc)
            self.assertEqual("DIAGNOSTICO_INVALIDO", respuesta["error"]["codigo"])
        self.assertEqual(bytes_antes, huella_bytes(self.base))
        archivo = self.trabajo / "consulta.jsonl"
        codigo, directa = self.escenario.cli("consultar", self.base,
            "--diagnostico", archivo, "--alias", "principal")
        with self.escenario.servidor(self.base) as (url, log):
            http, respuesta = self.escenario.consultar_http(url, "ALFA")
        trazas_cli = [json.loads(l) for l in archivo.read_text().splitlines()]
        trazas_http = [json.loads(l) for l in log.read_text().splitlines()]
        self.esperado = {"diagnostico_corresponde_al_resultado": True,
                         "estado_sin_cambios": True, "sin_rutas": True}
        self.observado.update({"directa": directa, "http": respuesta,
                               "diagnostico_cli": trazas_cli, "diagnostico_http": trazas_http,
                               "estado_sin_cambios": antes == snapshot(self.base)})
        self.assertEqual(0, codigo)
        self.assertEqual(200, http)
        self.assertEqual(ACTUALIZADO, directa["resumen"])
        self.assertEqual("archivo:principal", trazas_cli[-1]["origen_efectivo"])
        # Oracle observacional: la procedencia registrada debe explicar los datos leídos.
        posibles = {"memoria": REFERENCIA, "archivo:principal": ACTUALIZADO}
        self.assertIn(trazas_http[-1]["origen_efectivo"], posibles)
        self.assertEqual(posibles[trazas_http[-1]["origen_efectivo"]], respuesta)
        self.assertEqual(respuesta["codigos"], trazas_http[-1]["codigos_disponibles"])
        self.assertEqual("archivo:principal", trazas_http[-1]["origen_configurado"])
        self.assertEqual(antes, snapshot(self.base))
        self.assertNotIn(str(self.trabajo), json.dumps(trazas_cli + trazas_http))

    def test_d03_http_sobre_importado(self):
        """D03: HTTP refleja almacén, búsqueda y habilitación después de importar."""
        self.importar_valido()
        with self.escenario.servidor(self.base) as (url, _):
            observado = {
                "alfa": self.escenario.consultar_http(url, "ALFA")[1],
                "beta": self.escenario.consultar_http(url, "BETA")[1],
                "busqueda": self.escenario.consultar_http(url, "ALFA", " AGOTADO ")[1],
                "deshabilitado": self.escenario.consultar_http(url, "ALFA", "deshabilitado")[1],
            }
        self.esperado = {"alfa": ACTUALIZADO, "beta": VACIO_BETA,
            "busqueda": {"almacen": "ALFA", "total": 1, "codigos": ["A03"]},
            "deshabilitado": {"almacen": "ALFA", "total": 0, "codigos": []}}
        self.observado["http"] = observado
        self.assertEqual(self.esperado, observado)

    def test_d05_otro_directorio_y_reinicio(self):
        """D05: una ruta explícita conserva la base entre directorios y reinicios."""
        uno = self.trabajo / "directorio uno"; dos = self.trabajo / "directorio dos"
        uno.mkdir(); dos.mkdir()
        self.importar_valido(cwd=uno)
        antes = snapshot(self.base)
        with self.escenario.servidor(self.base, cwd=uno) as (url, _):
            primero = self.escenario.consultar_http(url, "ALFA")[1]
        with self.escenario.servidor(self.base, cwd=dos) as (url, _):
            segundo = self.escenario.consultar_http(url, "ALFA")[1]
        self.esperado = {"antes_reinicio": ACTUALIZADO, "despues_reinicio": ACTUALIZADO,
                         "sin_resembrado": True}
        self.observado["resultado"] = {"antes_reinicio": primero, "despues_reinicio": segundo,
                                      "sin_resembrado": antes == snapshot(self.base)}
        self.assertEqual(self.esperado, self.observado["resultado"])

    def rechazar_base(self, ruta, codigo):
        observado = []
        for operacion in ("consultar", "importar"):
            args = ("--archivo", BASE / "datos/actualizacion_valida.csv") if operacion == "importar" else ()
            rc, datos = self.escenario.cli(operacion, ruta, *args)
            observado.append({"operacion": operacion, "codigo": rc, "respuesta": datos})
        rc, datos = self.escenario.servidor_rechazado(ruta)
        observado.append({"operacion": "servir", "codigo": rc, "respuesta": datos})
        self.observado["rechazos"] = observado
        for item in observado:
            self.assertEqual(2, item["codigo"])
            self.assertEqual("RECHAZADO", item["respuesta"]["estado"])
            self.assertEqual(codigo, item["respuesta"]["error"]["codigo"])
            self.assertNotIn(str(self.trabajo), json.dumps(item))

    def test_d06a_base_inexistente(self):
        """D06.a: una ruta inexistente se rechaza sin crear una base."""
        ruta = self.trabajo / "ausente.sqlite"
        self.esperado = {"error": "BASE_INEXISTENTE", "archivo_creado": False}
        self.rechazar_base(ruta, "BASE_INEXISTENTE")
        self.observado["archivo_creado"] = ruta.exists()
        self.assertFalse(ruta.exists())

    def test_d06b_esquema_incompatible(self):
        """D06.b: un esquema incompatible se rechaza sin modificar sus bytes."""
        ruta = self.trabajo / "incompatible.sqlite"
        # Primero confirmar/revertir la transacción y después cerrar la conexión.
        with closing(sqlite3.connect(ruta)) as c, c:
            c.execute("CREATE TABLE marcador(valor TEXT)")
            c.execute("INSERT INTO marcador VALUES ('sintetico')")
        antes = huella_bytes(ruta)
        self.esperado = {"error": "ESQUEMA_INCOMPATIBLE", "bytes_intactos": True}
        self.rechazar_base(ruta, "ESQUEMA_INCOMPATIBLE")
        self.observado["bytes_intactos"] = antes == huella_bytes(ruta)
        self.assertEqual(antes, huella_bytes(ruta))

    def test_d07a_rechazo_sin_cambio(self):
        """D07.a: una entrada inválida posterior conserva las tres tablas persistidas."""
        self.importar_valido()
        antes = snapshot(self.base)
        rc, informe = self.escenario.cli("importar", self.base,
            "--archivo", BASE / "datos/error_tardio.csv")
        _, consulta = self.escenario.cli("consultar", self.base)
        self.esperado = {"codigo_salida": 1, "estado": "RECHAZADO",
                         "filas_aplicadas": 0, "sin_cambios": True}
        self.observado["rechazo"] = {"codigo_salida": rc, "estado": informe["estado"],
            "filas_aplicadas": informe["filas_aplicadas"],
            "sin_cambios": antes == snapshot(self.base) == consulta["datos"]}
        self.assertEqual(self.esperado, self.observado["rechazo"])

    def test_d07b_repetir_y_conservar_omitidos(self):
        """D07.b: repetir desde otro proceso no acumula y conserva pares omitidos."""
        archivo = self.trabajo / "solo_a01.csv"
        archivo.write_bytes(b"codigo_articulo,almacen,existencias\nA01,ALFA,5\n")
        antes = snapshot(self.base)
        r1, primera = self.escenario.cli("importar", self.base, "--archivo", archivo)
        intermedio = snapshot(self.base)
        r2, segunda = self.escenario.cli("importar", self.base, "--archivo", archivo)
        final = snapshot(self.base)
        self.esperado = {"primera_aplicadas": 1, "segunda_aplicadas": 0,
                         "idempotente": True, "omitidos_intactos": True, "a01": 5}
        self.observado["repeticion"] = {"primera_aplicadas": primera["filas_aplicadas"],
            "segunda_aplicadas": segunda["filas_aplicadas"], "idempotente": intermedio == final,
            "omitidos_intactos": antes["existencias"][1:] == final["existencias"][1:],
            "a01": final["existencias"][0][2]}
        self.assertEqual((0, 0), (r1, r2))
        self.assertEqual(self.esperado, self.observado["repeticion"])

    def test_d08a_dos_bases_aisladas(self):
        """D08.a: seleccionar dos archivos conserva sus resultados independientes."""
        otra = self.trabajo / "segunda.sqlite"
        self.assertEqual(0, self.escenario.cli("iniciar", otra)[0])
        control = snapshot(otra)
        self.importar_valido()
        with self.escenario.servidor(self.base, alias="primera") as (url, _):
            primera = self.escenario.consultar_http(url, "ALFA")[1]
        with self.escenario.servidor(otra, alias="segunda") as (url, _):
            segunda = self.escenario.consultar_http(url, "ALFA")[1]
        self.esperado = {"primera": ACTUALIZADO, "segunda": REFERENCIA,
                         "segunda_sin_cambios": True}
        self.observado["bases"] = {"primera": primera, "segunda": segunda,
                                  "segunda_sin_cambios": control == snapshot(otra)}
        self.assertEqual(self.esperado, self.observado["bases"])

    def test_d08b_no_reinicializar(self):
        """D08.b: inicializar una base existente no sobrescribe datos ni bytes."""
        self.importar_valido()
        antes = snapshot(self.base)
        huella = huella_bytes(self.base)
        codigo, respuesta = self.escenario.cli("iniciar", self.base)
        self.esperado = {"codigo": 2, "error": "BASE_EXISTENTE",
                         "datos_intactos": True, "bytes_intactos": True}
        self.observado["reinicializar"] = {"codigo": codigo, "error": respuesta["error"]["codigo"],
            "datos_intactos": antes == snapshot(self.base), "bytes_intactos": huella == huella_bytes(self.base)}
        self.assertEqual(self.esperado, self.observado["reinicializar"])


def main():
    global DIRECTORIO, ESTADO
    parser = argparse.ArgumentParser(description=__doc__)
    selector = parser.add_mutually_exclusive_group(required=True)
    selector.add_argument("--estado", choices=("base", "propuesta", "solucion"))
    selector.add_argument("--directorio", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    ESTADO = args.estado or "copia_del_lector"
    DIRECTORIO = (BASE / "estados" / args.estado if args.estado else args.directorio).resolve()
    resultado = ResultadoDepuracion()
    unittest.defaultTestLoader.loadTestsFromTestCase(DepuracionTests).run(resultado)
    registro = {"bateria": "depuracion", "estado_codigo": ESTADO,
        "casos_registrados": len(resultado.registros), "criterios_distintos": 7,
        "ejecutados": sum(r["estado"] in ("APROBADO", "FALLIDO") for r in resultado.registros),
        "aprobados": sum(r["estado"] == "APROBADO" for r in resultado.registros),
        "fallidos": len(resultado.failures) + len(resultado.errors),
        "fallos_de_asercion": len(resultado.failures), "errores_de_ejecucion": len(resultado.errors),
        "bloqueados": sum(r["estado"] == "BLOQUEADO" for r in resultado.registros), "no_ejecutados": len(resultado.skipped), "pruebas": resultado.registros}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for r in resultado.registros:
        print(r["id"] + ": " + r["estado"])
        if r["tipo_error"]: print("  " + r["tipo_error"] + ": " + r["detalle"])
    print(json.dumps({k: registro[k] for k in ("ejecutados", "aprobados", "fallidos", "bloqueados", "no_ejecutados")}))
    return 1 if registro["fallidos"] else 2 if registro["bloqueados"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
