"""Servidor didáctico local: HTTP adapta el resumen existente, sin reescribirlo."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from resumen import resumir_catalogo
from persistencia import abrir_base, ErrorBase, validar_alias
from origen import registrar_origen, validar_destino, ErrorDiagnostico

BASE = Path(__file__).resolve().parent
RECURSOS = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
    "/estilos.css": ("estilos.css", "text/css; charset=utf-8"),
}
ERROR_ALMACEN = {"error": {"codigo": "ALMACEN_REQUERIDO",
                            "mensaje": "Selecciona un almacén."}}


class Manejador(BaseHTTPRequestHandler):
    server_version = "LaboratorioHTTP"
    sys_version = ""

    def log_message(self, formato, *argumentos):
        # La aplicación no registra direcciones ni consultas del lector.
        pass

    def responder(self, estado, contenido, tipo):
        self.send_response(estado)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(contenido)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; "
                         "script-src 'self'; style-src 'self'; "
                         "connect-src 'self'; img-src 'self' data:; "
                         "base-uri 'none'; form-action 'self'")
        self.end_headers()
        self.wfile.write(contenido)

    def responder_json(self, estado, datos):
        contenido = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.responder(estado, contenido, "application/json; charset=utf-8")

    def do_GET(self):
        partes = urlsplit(self.path)
        if partes.path == "/api/resumen":
            parametros = parse_qs(partes.query, keep_blank_values=True)
            almacen = parametros.get("almacen", [""])[0]
            if not almacen.strip():
                self.responder_json(400, ERROR_ALMACEN)
                return
            nombre = parametros.get("nombre", [""])[0]
            try:
                if self.server.base_persistente is None:
                    datos = resumir_catalogo(almacen, nombre)
                else:
                    conexion = abrir_base(self.server.base_persistente)
                    try:
                        with registrar_origen(self.server.base_persistente,
                                              self.server.alias, self.server.diagnostico):
                            datos = resumir_catalogo(almacen, nombre)
                    finally:
                        conexion.close()
            except Exception:
                self.responder_json(500, {"error": {
                    "codigo": "CONSULTA_FALLIDA",
                    "mensaje": "No fue posible consultar el catálogo."}})
                return
            self.responder_json(200, datos)
        elif partes.path in RECURSOS:
            nombre, tipo = RECURSOS[partes.path]
            self.responder(200, (BASE / "web" / nombre).read_bytes(), tipo)
        else:
            self.responder_json(404, {"error": {
                "codigo": "RUTA_NO_ENCONTRADA", "mensaje": "Ruta no encontrada."}})


def crear_servidor(puerto=8000, *, base=None, alias="principal", diagnostico=None):
    validar_alias(alias)
    base_fija = Path(base).resolve() if base is not None else None
    if base_fija is not None:
        validar_destino(base_fija, diagnostico)
        conexion = abrir_base(base_fija)
        conexion.close()
    servidor = ThreadingHTTPServer(("127.0.0.1", puerto), Manejador)
    servidor.base_persistente = base_fija
    servidor.alias = alias
    servidor.diagnostico = diagnostico
    return servidor


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--puerto", type=int, default=8000)
    parser.add_argument("--base", type=Path)
    parser.add_argument("--alias", default="principal")
    parser.add_argument("--diagnostico", type=Path)
    opciones = parser.parse_args()
    if not 0 <= opciones.puerto <= 65535:
        parser.error("El puerto debe estar entre 0 y 65535.")
    try:
        instancia = crear_servidor(opciones.puerto, base=opciones.base,
                                  alias=opciones.alias, diagnostico=opciones.diagnostico)
    except ErrorDiagnostico as error:
        print(json.dumps({"estado": "RECHAZADO", "error": {
            "codigo": "DIAGNOSTICO_INVALIDO", "mensaje": str(error)}}, ensure_ascii=False))
        return 2
    except ErrorBase as error:
        print(json.dumps({"estado": "RECHAZADO", "error": {
            "codigo": error.codigo, "mensaje": str(error)}}, ensure_ascii=False))
        return 2
    except OSError:
        print(json.dumps({"estado": "BLOQUEADO", "error": {
            "codigo": "SERVIDOR_NO_DISPONIBLE", "mensaje": "No fue posible iniciar el servidor local."}}, ensure_ascii=False))
        return 2
    with instancia as servidor:
        print(json.dumps({"servidor": "local",
                          "url": "http://127.0.0.1:" + str(servidor.server_port)}),
              flush=True)
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
