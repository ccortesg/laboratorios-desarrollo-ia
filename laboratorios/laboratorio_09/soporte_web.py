"""Inicia el servidor real del estado elegido en un puerto local libre."""

from contextlib import contextmanager
import importlib.util
from pathlib import Path
import sys
import threading


@contextmanager
def servidor_local(directorio):
    directorio = Path(directorio).resolve()
    anteriores = list(sys.path)
    for nombre in ("resumen", "catalogo", "laboratorio"):
        sys.modules.pop(nombre, None)
    sys.path.insert(0, str(directorio))
    try:
        especificacion = importlib.util.spec_from_file_location(
            "servidor_del_estado", directorio / "servidor.py")
        modulo = importlib.util.module_from_spec(especificacion)
        especificacion.loader.exec_module(modulo)
        servidor = modulo.crear_servidor(0)
    finally:
        sys.path[:] = anteriores
    hilo = threading.Thread(target=servidor.serve_forever, daemon=True)
    hilo.start()
    try:
        yield "http://127.0.0.1:" + str(servidor.server_port)
    finally:
        servidor.shutdown()
        servidor.server_close()
        hilo.join(timeout=5)
