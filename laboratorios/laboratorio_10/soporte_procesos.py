"""Procesos y observaciones controlados; sólo HTTP en loopback."""
from contextlib import closing, contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import queue
import sqlite3
import subprocess
import sys
import threading
from urllib.parse import urlencode
from urllib.request import build_opener, ProxyHandler

BASE = Path(__file__).resolve().parent
HTTP = build_opener(ProxyHandler({}))  # Sólo loopback; no modifica el entorno global.


class BloqueoEntorno(Exception):
    """Dependencia o permiso del entorno impide iniciar el proceso local."""


def snapshot(ruta):
    # El contexto de Connection gestiona transacciones, pero no cierra el archivo.
    with closing(sqlite3.connect(Path(ruta).resolve().as_uri() + "?mode=ro", uri=True)) as c:
        return {
            "articulos": [list(r) for r in c.execute("SELECT codigo,nombre,habilitado FROM articulos ORDER BY codigo")],
            "almacenes": [list(r) for r in c.execute("SELECT codigo FROM almacenes ORDER BY codigo")],
            "existencias": [list(r) for r in c.execute("SELECT articulo,almacen,cantidad FROM existencias ORDER BY articulo,almacen")],
        }


class Escenario:
    def __init__(self, codigo, trabajo):
        self.codigo = Path(codigo).resolve()
        self.trabajo = Path(trabajo).resolve()
        self.operaciones = []
        self.entorno = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")

    def sanear(self, texto):
        return str(texto).replace(str(self.codigo), "<CODIGO>").replace(
            str(self.trabajo), "<TRABAJO>").replace(str(BASE), "<LABORATORIO>").replace(
            sys.executable, "python")

    def cli(self, operacion, base, *argumentos, cwd=None):
        comando = [sys.executable, "-B", str(self.codigo / "persistencia.py"),
                   operacion, "--base", str(base), *map(str, argumentos)]
        inicio = datetime.now(timezone.utc).isoformat()
        r = subprocess.run(comando, cwd=cwd or self.codigo, env=self.entorno,
                           capture_output=True, timeout=20)
        salida = r.stdout.decode("utf-8")
        error = r.stderr.decode("utf-8")
        self.operaciones.append({
            "proceso": "cli_" + str(len(self.operaciones) + 1),
            "inicio_utc": inicio, "comando": [self.sanear(v) for v in comando],
            "directorio": self.sanear(cwd or self.codigo),
            "codigo_salida": r.returncode,
            "stdout": self.sanear(salida), "stderr": self.sanear(error),
        })
        try:
            datos = json.loads(salida)
        except ValueError:
            datos = {"salida_no_json": self.sanear(salida)}
        return r.returncode, datos

    def servidor_rechazado(self, base, *argumentos):
        comando = [sys.executable, "-B", str(self.codigo / "servidor.py"),
                   "--puerto", "0", "--base", str(base), *map(str, argumentos)]
        r = subprocess.run(comando, cwd=self.codigo, env=self.entorno,
                           capture_output=True, timeout=10)
        self.operaciones.append({
            "proceso": "servidor_rechazado",
            "comando": [self.sanear(v) for v in comando],
            "codigo_salida": r.returncode,
            "stdout": self.sanear(r.stdout.decode("utf-8")),
            "stderr": self.sanear(r.stderr.decode("utf-8")),
        })
        return r.returncode, json.loads(r.stdout)

    @contextmanager
    def servidor(self, base, *, alias="principal", cwd=None):
        numero = len(self.operaciones) + 1
        diagnostico = self.trabajo / ("diagnostico_" + str(numero) + ".jsonl")
        stderr = self.trabajo / ("servidor_" + str(numero) + ".stderr")
        comando = [sys.executable, "-B", str(self.codigo / "servidor.py"),
                   "--puerto", "0", "--base", str(base), "--alias", alias,
                   "--diagnostico", str(diagnostico)]
        with stderr.open("wb") as errores:
            p = subprocess.Popen(comando, cwd=cwd or self.codigo, env=self.entorno,
                                 stdout=subprocess.PIPE, stderr=errores)
            cola = queue.Queue()
            lector = threading.Thread(target=lambda: cola.put(p.stdout.readline()), daemon=True)
            lector.start()
            registro = {
                "proceso": "servidor_" + str(numero),
                "comando": [self.sanear(v) for v in comando],
                "directorio": self.sanear(cwd or self.codigo),
                "inicio_utc": datetime.now(timezone.utc).isoformat(),
            }
            self.operaciones.append(registro)
            try:
                primera = cola.get(timeout=10)
                listo = json.loads(primera)
                if listo.get("estado") == "BLOQUEADO":
                    raise BloqueoEntorno("No se pudo iniciar el servidor local en este entorno.")
                url = listo["url"]
                if not url.startswith("http://127.0.0.1:"):
                    raise RuntimeError("El servidor no anunció una dirección local.")
                registro["disponibilidad"] = {"servidor": "local", "url": "<URL_LOCAL>"}
                yield url, diagnostico
            finally:
                if p.poll() is None:
                    p.terminate()
                    try:
                        p.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        p.kill()
                        p.wait(timeout=5)
                registro["codigo_salida_al_cerrar"] = p.returncode
                registro["cierre"] = "Proceso terminado por el controlador de la prueba."
                errores.flush()
                registro["stderr"] = self.sanear(stderr.read_text(encoding="utf-8"))
                p.stdout.close()
                lector.join(timeout=1)
        registro["stderr"] = self.sanear(stderr.read_text(encoding="utf-8"))
        registro["diagnostico"] = ([
            json.loads(linea) for linea in diagnostico.read_text(encoding="utf-8").splitlines()
        ] if diagnostico.exists() else [])

    def consultar_http(self, url, almacen, nombre=""):
        ruta = "/api/resumen?" + urlencode({"almacen": almacen, "nombre": nombre})
        with HTTP.open(url + ruta, timeout=10) as r:
            datos = json.loads(r.read())
            codigo = r.status
        self.operaciones.append({"componente": "cliente_http", "metodo": "GET",
                                 "url": "<URL_LOCAL>" + ruta,
                                 "codigo_http": codigo, "json": datos})
        return codigo, datos


def huella_bytes(ruta):
    return hashlib.sha256(Path(ruta).read_bytes()).hexdigest()
