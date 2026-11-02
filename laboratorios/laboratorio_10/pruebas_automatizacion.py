"""T01–T07: operación local real, parada y recibo conservado."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from pruebas_resumen import ResultadoRegistrado
from soporte_procesos import BASE, Escenario, snapshot, huella_bytes
from soporte.huellas_evidencia import comprobar_huellas

CASOS = [f"T{i:02}" for i in range(1, 8)]
DIRECTORIO = None
DESTINO_RECIBOS = None
ACTUALIZADO = {"almacen": "ALFA", "total": 2, "codigos": ["A01", "A03"]}


class AutomatizacionTests(unittest.TestCase):
    def setUp(self):
        if not (DIRECTORIO / "operar.py").is_file():
            self.skipTest("El estado base conserva la solución anterior y todavía no tiene operador.")
        temporal = tempfile.TemporaryDirectory(prefix="lab10_operacion_")
        self.addCleanup(temporal.cleanup)
        self.trabajo = Path(temporal.name)
        self.base = self.trabajo / "principal.sqlite"
        self.csv = BASE / "datos/actualizacion_valida.csv"
        self.escenario = Escenario(DIRECTORIO, self.trabajo)
        self.observado = {"operaciones": self.escenario.operaciones}
        self.recibos = []
        rc, _ = self.escenario.cli("iniciar", self.base)
        if rc != 0:
            raise RuntimeError("No fue posible preparar la base sintética de la prueba.")

    def tearDown(self):
        if DESTINO_RECIBOS is not None:
            for i, recibo in enumerate(self.recibos, 1):
                if recibo.is_dir():
                    destino = DESTINO_RECIBOS / self._testMethodName / str(i)
                    destino.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copytree(recibo, destino)

    def operar(self, *, base=None, csv=None, salida=None, cwd=None, nombre=""):
        base = base or self.base
        csv = csv or self.csv
        salida = salida or self.trabajo / ("recibo_" + str(len(self.recibos) + 1))
        self.recibos.append(salida)
        comando = [sys.executable, "-B", str(DIRECTORIO / "operar.py"),
                   "--base", str(base), "--archivo", str(csv), "--almacen", "ALFA",
                   "--nombre", nombre, "--salida", str(salida)]
        r = subprocess.run(comando, cwd=cwd or DIRECTORIO, env=self.escenario.entorno,
                           capture_output=True, timeout=50)
        datos = json.loads(r.stdout.decode("utf-8"))
        self.escenario.operaciones.append({
            "proceso": "operador", "comando": [self.escenario.sanear(x) for x in comando],
            "codigo_salida": r.returncode, "resultado": datos,
            "stderr": self.escenario.sanear(r.stderr.decode("utf-8"))})
        return r.returncode, datos, salida

    def registrar_recibo(self, salida):
        datos = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in salida.iterdir() if p.is_file()}
        resultado = json.loads((salida / "resultado.json").read_bytes())
        comandos = json.loads((salida / "comandos.json").read_bytes())
        self.observado["recibo"] = {"archivos_sha256": datos, "resultado": resultado,
                                   "comandos": comandos,
                                   "huellas": comprobar_huellas(salida)}
        return resultado, comandos

    def test_t01_actualiza_y_consulta_la_misma_base(self):
        """T01: la operación válida aplica el CSV y consulta realmente la misma base."""
        self.entrada = {"csv": "datos/actualizacion_valida.csv", "almacen": "ALFA"}
        self.esperado = {"codigo": 0, "estado": "APROBADO", "resumen": ACTUALIZADO,
                         "A03_ALFA": 3, "A02_habilitado": 0}
        rc, resultado, salida = self.operar()
        estado = snapshot(self.base)
        self.observado["estado_persistido"] = estado
        self.registrar_recibo(salida)
        self.assertEqual(0, rc)
        self.assertEqual("APROBADO", resultado["estado"])
        self.assertTrue(resultado["importacion_confirmada"])
        self.assertEqual(ACTUALIZADO, resultado["resumen"])
        self.assertIn(["A03", "ALFA", 3], estado["existencias"])
        self.assertEqual(0, next(a[2] for a in estado["articulos"] if a[0] == "A02"))

    def test_t02_rechazo_detiene_la_consulta(self):
        """T02: un CSV rechazado detiene el flujo y conserva toda la base."""
        csv = self.trabajo / "entrada_invalida.csv"
        csv.write_text("codigo_articulo,almacen,existencias\nA01,ALFA,9\nA03,ALFA,-1\n", encoding="utf-8")
        antes = snapshot(self.base)
        self.entrada = {"filas": "primera válida y segunda negativa"}
        self.esperado = {"codigo": 1, "estado": "FALLIDO", "consulta": "NO EJECUTADO",
                         "base_conservada": True, "resumen": None}
        rc, resultado, salida = self.operar(csv=csv)
        _, comandos = self.registrar_recibo(salida)
        self.observado["base_conservada"] = antes == snapshot(self.base)
        self.assertTrue(self.observado["base_conservada"])
        self.assertEqual(1, rc)
        self.assertEqual("FALLIDO", resultado["estado"])
        self.assertFalse(resultado["importacion_confirmada"])
        self.assertEqual("NO EJECUTADO", resultado["pasos"][1]["estado"])
        self.assertIsNone(resultado["resumen"])
        self.assertEqual("NO EJECUTADO", comandos["registros"][1]["estado"])
        self.assertNotIn("stdout", comandos["registros"][1])
        self.assertNotIn("sha256_stdout", comandos["registros"][1])
        self.assertFalse((salida / "consultar.stdout.txt").exists())

    def test_t03_repeticion_conserva_estado_y_recibo(self):
        """T03: repetir la entrada conserva estado, pares omitidos y el primer recibo."""
        antes = snapshot(self.base)
        self.entrada = {"veces": 2, "carpetas_recibo": "distintas"}
        self.esperado = {"codigos": [0, 0], "estado_repetido": True,
                         "recibo_anterior_conservado": True, "pares_omitidos_conservados": True}
        rc1, _, salida1 = self.operar()
        primero = snapshot(self.base)
        bytes1 = {p.name:p.read_bytes() for p in salida1.iterdir()}
        rc2, _, salida2 = self.operar()
        segundo = snapshot(self.base)
        actualizados = {("A01", "ALFA"), ("A02", "ALFA"), ("A03", "ALFA"), ("A04", "BETA")}
        omitidos_antes = [x for x in antes["existencias"] if tuple(x[:2]) not in actualizados]
        omitidos_despues = [x for x in segundo["existencias"] if tuple(x[:2]) not in actualizados]
        conserva = bytes1 == {p.name:p.read_bytes() for p in salida1.iterdir()}
        self.observado.update(estado_repetido=primero==segundo,
                             recibo_anterior_conservado=conserva,
                             pares_omitidos_conservados=omitidos_antes==omitidos_despues)
        self.assertEqual([0,0], [rc1,rc2])
        self.assertEqual(primero, segundo)
        self.assertEqual(omitidos_antes, omitidos_despues)
        self.assertTrue(conserva)
        self.assertNotEqual(salida1, salida2)

    def test_t04_base_ausente_no_se_recrea(self):
        """T04: una base ausente se rechaza antes de crear recibo o importar."""
        ausente = self.trabajo / "ausente.sqlite"
        self.entrada = {"base": "ausente"}
        self.esperado = {"codigo": 2, "error": "BASE_INEXISTENTE", "base_creada": False}
        rc, resultado, salida = self.operar(base=ausente)
        self.observado.update(base_creada=ausente.exists(), recibo_creado=salida.exists())
        self.assertEqual(2, rc)
        self.assertEqual("BASE_INEXISTENTE", resultado["error"]["codigo"])
        self.assertFalse(ausente.exists())
        self.assertFalse(salida.exists())

    def test_t05_salida_existente_y_protegida(self):
        """T05: los destinos existentes o protegidos se rechazan antes de importar."""
        previa = self.trabajo / "recibo_anterior"
        previa.mkdir()
        (previa / "marca.txt").write_bytes(b"recibo sintetico anterior\r\n")
        protegida = BASE / "datos" / "recibo_no_autorizado_t05"
        self.assertFalse(protegida.exists())
        base_antes, csv_antes = huella_bytes(self.base), self.csv.read_bytes()
        bytes_antes = (previa / "marca.txt").read_bytes()
        self.entrada = {"destinos": ["existente", "datos/recibo_no_autorizado_t05"]}
        self.esperado = {"codigos": [2,2], "errores": ["SALIDA_EXISTENTE", "SALIDA_PROTEGIDA"],
                         "entradas_conservadas": True}
        rc1, r1, _ = self.operar(salida=previa)
        rc2, r2, _ = self.operar(salida=protegida)
        self.observado["entradas_conservadas"] = base_antes==huella_bytes(self.base) and csv_antes==self.csv.read_bytes()
        self.assertEqual([2,2], [rc1,rc2])
        self.assertEqual(["SALIDA_EXISTENTE","SALIDA_PROTEGIDA"], [r1["error"]["codigo"],r2["error"]["codigo"]])
        self.assertTrue(self.observado["entradas_conservadas"])
        self.assertEqual(bytes_antes,(previa/"marca.txt").read_bytes())
        self.assertEqual(["marca.txt"], [p.name for p in previa.iterdir()])
        self.assertFalse(protegida.exists())

    def test_t06_recibo_corresponde_a_bytes_y_pasos(self):
        """T06: el recibo identifica el CSV usado y las salidas realmente guardadas."""
        csv = self.trabajo / "instantanea_original.csv"
        csv.write_bytes(self.csv.read_bytes())
        bytes_usados = csv.read_bytes()
        self.entrada = {"csv": "copia sintética de la actualización"}
        self.esperado = {"snapshot_exacto": True, "sha256_exacto": True,
                         "pasos": ["importar","consultar"], "huellas": "APROBADO"}
        rc, _, salida = self.operar(csv=csv)
        resultado, comandos = self.registrar_recibo(salida)
        csv.write_bytes(b"El original puede cambiar despues de terminar.\n")
        self.assertEqual(0, rc)
        self.assertEqual(bytes_usados, (salida/"entrada.csv").read_bytes())
        self.assertEqual(hashlib.sha256(bytes_usados).hexdigest(), resultado["entrada"]["sha256"])
        self.assertEqual(len(bytes_usados), resultado["entrada"]["bytes"])
        self.assertEqual(["importar","consultar"], [x["id"] for x in comandos["registros"]])
        self.assertEqual([0,0], [x["codigo_salida"] for x in comandos["registros"]])
        self.assertEqual("APROBADO", comprobar_huellas(salida)["estado"])
        for r in comandos["registros"]:
            for flujo in ("stdout","stderr"):
                self.assertEqual(hashlib.sha256((salida/r[flujo]).read_bytes()).hexdigest(),r["sha256_"+flujo])
                self.assertIn("sha256_"+flujo+"_capturado",r)
        importado=json.loads((salida/"importar.stdout.txt").read_bytes())
        consulta=json.loads((salida/"consultar.stdout.txt").read_bytes())
        self.assertEqual(resultado["entrada"]["sha256"],importado["sha256_fuente"])
        self.assertEqual(ACTUALIZADO,consulta["resumen"])
        self.assertEqual(consulta["resumen"],resultado["resumen"])
        for archivo in salida.glob("*.json"):
            texto=archivo.read_text(encoding="utf-8")
            self.assertNotIn(str(self.trabajo),texto)
            self.assertNotIn(str(DIRECTORIO),texto)

    def test_t07_directorio_ajeno_y_rutas_con_espacios(self):
        """T07: el cwd y los espacios no cambian el código ni la base elegidos."""
        carpeta=self.trabajo/"datos con espacios";carpeta.mkdir()
        base=carpeta/"catalogo principal.sqlite";csv=carpeta/"lote de entrada.csv"
        self.base.rename(base);csv.write_bytes(self.csv.read_bytes())
        ajeno=self.trabajo/"directorio ajeno";ajeno.mkdir()
        (ajeno/"persistencia.py").write_text("raise SystemExit(97)\n",encoding="utf-8")
        self.entrada={"cwd":"directorio ajeno","rutas":"con espacios","script_en_cwd":"no autorizado"}
        self.esperado={"codigo":0,"resumen":ACTUALIZADO,"A03_ALFA":3}
        rc,r,salida=self.operar(base=base,csv=csv,salida=carpeta/"recibo nuevo",cwd=ajeno)
        self.observado["estado_persistido"]=snapshot(base)
        self.registrar_recibo(salida)
        self.assertEqual(0,rc)
        self.assertEqual(ACTUALIZADO,r["resumen"])
        self.assertIn(["A03","ALFA",3],self.observado["estado_persistido"]["existencias"])


def main():
    global DIRECTORIO, DESTINO_RECIBOS
    p=argparse.ArgumentParser(description=__doc__)
    selector=p.add_mutually_exclusive_group(required=True)
    selector.add_argument("--estado",choices=("base","propuesta","solucion"))
    selector.add_argument("--directorio",type=Path)
    p.add_argument("--json",type=Path)
    a=p.parse_args()
    DIRECTORIO=(BASE/"estados"/a.estado if a.estado else a.directorio).resolve()
    if a.json:
        a.json.parent.mkdir(parents=True,exist_ok=True)
        DESTINO_RECIBOS=a.json.parent/(a.json.stem+"_recibos")
        if DESTINO_RECIBOS.exists():
            p.error("La carpeta de recibos ya existe; utiliza una salida nueva.")
    resultado=ResultadoRegistrado()
    unittest.defaultTestLoader.loadTestsFromTestCase(AutomatizacionTests).run(resultado)
    registros=resultado.registros
    datos={"bateria":"automatizacion","estado_codigo":a.estado or "copia_del_lector",
           "casos_registrados":len(registros),"criterios_distintos":7,
           "ejecutados":sum(x["estado"] in ("APROBADO","FALLIDO") for x in registros),
           "aprobados":sum(x["estado"]=="APROBADO" for x in registros),
           "fallidos":len(resultado.failures)+len(resultado.errors),
           "fallos_de_asercion":len(resultado.failures),"errores_de_ejecucion":len(resultado.errors),
           "bloqueados":0,"no_ejecutados":len(resultado.skipped),"pruebas":registros}
    if a.json:a.json.write_text(json.dumps(datos,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for r in registros:
        print(r["id"]+": "+r["estado"])
        if r["tipo_error"]:print("  "+r["tipo_error"]+": "+r["detalle"])
    return 1 if datos["fallidos"] else 0


if __name__=="__main__":
    raise SystemExit(main())
