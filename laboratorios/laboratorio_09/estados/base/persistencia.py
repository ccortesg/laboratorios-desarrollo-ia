"""Inicialización explícita y CLI sobre una base sintética persistente."""
import argparse
import json
import os
from pathlib import Path
import re
import sqlite3

from importacion import importar_existencias
from resumen import resumir_catalogo
from origen import registrar_origen, validar_destino, ErrorDiagnostico

BASE = Path(__file__).resolve().parent
ESQUEMA = {
    "articulos": [("codigo", "TEXT", 0, 1), ("nombre", "TEXT", 1, 0),
                  ("habilitado", "INTEGER", 1, 0)],
    "almacenes": [("codigo", "TEXT", 0, 1)],
    "existencias": [("articulo", "TEXT", 1, 1), ("almacen", "TEXT", 1, 2),
                    ("cantidad", "INTEGER", 1, 0)],
}


class ErrorBase(Exception):
    def __init__(self, codigo, mensaje):
        super().__init__(mensaje)
        self.codigo = codigo


def validar_alias(alias):
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,32}", alias):
        raise ErrorBase("ALIAS_INVALIDO", "Usa un alias sintético de letras, números, guion o subrayado.")
    return alias


def abrir_base(ruta, *, escritura=False):
    ruta = Path(ruta).resolve()
    if not ruta.is_file():
        raise ErrorBase("BASE_INEXISTENTE", "La base seleccionada no existe como archivo.")
    conexion = None
    try:
        modo = "rw" if escritura else "ro"
        conexion = sqlite3.connect(ruta.as_uri() + "?mode=" + modo, uri=True)
        conexion.row_factory = sqlite3.Row
        conexion.execute("PRAGMA foreign_keys = ON")
        for tabla, esperado in ESQUEMA.items():
            observado = [(r[1], r[2].upper(), r[3], r[5])
                         for r in conexion.execute("PRAGMA table_info(" + tabla + ")")]
            if observado != esperado:
                raise ErrorBase("ESQUEMA_INCOMPATIBLE", "La base no contiene el esquema requerido.")
        relaciones = {(r[2], r[3], r[4])
                      for r in conexion.execute("PRAGMA foreign_key_list(existencias)")}
        if relaciones != {("articulos", "articulo", "codigo"),
                          ("almacenes", "almacen", "codigo")}:
            raise ErrorBase("ESQUEMA_INCOMPATIBLE", "Las relaciones de la base son incompatibles.")
        return conexion
    except (sqlite3.Error, ErrorBase) as error:
        if conexion is not None:
            conexion.close()
        if isinstance(error, ErrorBase):
            raise
        raise ErrorBase("ESQUEMA_INCOMPATIBLE", "No fue posible abrir el esquema requerido.") from error


def inicializar(ruta):
    ruta = Path(ruta).absolute()
    try:
        descriptor = os.open(ruta, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise ErrorBase("BASE_EXISTENTE", "El destino ya existe; no se sobrescribe.") from error
    except OSError as error:
        raise ErrorBase("DESTINO_INVALIDO", "No fue posible crear el destino solicitado.") from error
    os.close(descriptor)
    conexion = None
    try:
        conexion = sqlite3.connect(ruta)
        for nombre in ("esquema.sql", "ejemplos.sql"):
            conexion.executescript((BASE / "datos" / nombre).read_text(encoding="utf-8"))
        conexion.commit()
    except Exception:
        if conexion is not None:
            conexion.close()
            conexion = None
        ruta.unlink(missing_ok=True)
        raise
    finally:
        if conexion is not None:
            conexion.close()
    return {"estado": "INICIALIZADO"}


def estado_completo(conexion):
    return {
        "articulos": [list(r) for r in conexion.execute(
            "SELECT codigo,nombre,habilitado FROM articulos ORDER BY codigo")],
        "almacenes": [list(r) for r in conexion.execute(
            "SELECT codigo FROM almacenes ORDER BY codigo")],
        "existencias": [list(r) for r in conexion.execute(
            "SELECT articulo,almacen,cantidad FROM existencias ORDER BY articulo,almacen")],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operacion", choices=("iniciar", "importar", "consultar"))
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--archivo", type=Path)
    parser.add_argument("--almacen", default="ALFA")
    parser.add_argument("--nombre", default="")
    parser.add_argument("--alias", default="principal")
    parser.add_argument("--diagnostico", type=Path)
    opciones = parser.parse_args()
    if opciones.operacion == "importar" and opciones.archivo is None:
        parser.error("importar requiere --archivo")
    try:
        validar_alias(opciones.alias)
        validar_destino(opciones.base, opciones.diagnostico)
        if opciones.operacion == "iniciar":
            resultado = inicializar(opciones.base)
        else:
            conexion = abrir_base(opciones.base, escritura=opciones.operacion == "importar")
            try:
                if opciones.operacion == "importar":
                    resultado = importar_existencias(conexion, opciones.archivo)
                else:
                    with registrar_origen(opciones.base, opciones.alias, opciones.diagnostico):
                        resumen = resumir_catalogo(opciones.almacen, opciones.nombre,
                                                   conexion=conexion)
                    resultado = {"estado": "CONSULTADO", "origen": "archivo:" + opciones.alias,
                                 "resumen": resumen, "datos": estado_completo(conexion)}
            finally:
                conexion.close()
        print(json.dumps(resultado, ensure_ascii=False))
        return 1 if resultado.get("estado") == "RECHAZADO" else 0
    except ErrorDiagnostico as error:
        print(json.dumps({"estado": "RECHAZADO", "error": {
            "codigo": "DIAGNOSTICO_INVALIDO", "mensaje": str(error)}}, ensure_ascii=False))
        return 2
    except ErrorBase as error:
        print(json.dumps({"estado": "RECHAZADO",
                          "error": {"codigo": error.codigo, "mensaje": str(error)}},
                         ensure_ascii=False))
        return 2
    except (OSError, sqlite3.Error):
        print(json.dumps({"estado": "RECHAZADO", "error": {
            "codigo": "OPERACION_FALLIDA", "mensaje": "No fue posible completar la operación local."}},
            ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
