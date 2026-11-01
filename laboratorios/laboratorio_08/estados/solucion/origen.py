"""Diagnóstico opcional del origen efectivo; sin rutas publicables."""
from contextlib import contextmanager
from contextvars import ContextVar
import json
from pathlib import Path
from threading import Lock

_OBSERVACION = ContextVar("origen_catalogo", default=None)
_OTROS = {}
_CERROJO = Lock()


class ErrorDiagnostico(ValueError):
    pass


def validar_destino(base, destino):
    if destino is None:
        return
    base, destino = Path(base).resolve(), Path(destino).resolve()
    coincide = base == destino
    if base.exists() and destino.exists():
        coincide = coincide or base.samefile(destino)
    if coincide:
        raise ErrorDiagnostico("El diagnóstico debe usar un archivo distinto de la base.")


def alias_otro(archivo):
    with _CERROJO:
        if archivo not in _OTROS:
            _OTROS[archivo] = "archivo_no_configurado:origen_" + str(len(_OTROS) + 1)
        return _OTROS[archivo]


@contextmanager
def registrar_origen(base_configurada, alias, destino):
    validar_destino(base_configurada, destino)
    token = _OBSERVACION.set((Path(base_configurada).resolve(), alias, destino))
    try:
        yield
    finally:
        _OBSERVACION.reset(token)


def observar(conexion, almacen, articulos):
    configuracion = _OBSERVACION.get()
    if configuracion is None:
        return
    base, alias, destino = configuracion
    filas = conexion.execute("PRAGMA database_list").fetchall()
    archivo = next((f[2] for f in filas if f[1] == "main"), "")
    efectivo = ("memoria" if not archivo else
                "archivo:" + alias if Path(archivo).resolve() == base else alias_otro(str(Path(archivo).resolve())))
    registro = {
        "evento": "consulta_catalogo",
        "origen_configurado": "archivo:" + alias,
        "origen_efectivo": efectivo,
        "almacen": almacen,
        "codigos_disponibles": [a["codigo"] for a in articulos],
    }
    if destino is not None:
        with Path(destino).open("a", encoding="utf-8", newline="\n") as archivo_salida:
            archivo_salida.write(json.dumps(registro, ensure_ascii=False) + "\n")
