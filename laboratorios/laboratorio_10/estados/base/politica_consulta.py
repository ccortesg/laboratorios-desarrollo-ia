"""Contrato de entrada HTTP: sintaxis, ambigüedad y límites antes del dominio."""
import re
from urllib.parse import parse_qsl

MAX_QUERY_BYTES = 2048
MAX_NOMBRE = 80


class ErrorConsulta(ValueError):
    def __init__(self, estado_http, codigo, mensaje):
        super().__init__(mensaje)
        self.estado_http = estado_http
        self.publico = {"error": {"codigo": codigo, "mensaje": mensaje}}


def leer_consulta(query):
    if len(query.encode("utf-8")) > MAX_QUERY_BYTES:
        raise ErrorConsulta(414, "CONSULTA_DEMASIADO_LARGA", "La consulta supera el tamaño permitido.")
    if re.search(r"%(?![0-9A-Fa-f]{2})", query):
        raise ErrorConsulta(400, "CONSULTA_INVALIDA", "La consulta no tiene una codificación válida.")
    try:
        pares = parse_qsl(query, keep_blank_values=True, strict_parsing=True,
                          encoding="utf-8", errors="strict")
    except (ValueError, UnicodeError):
        raise ErrorConsulta(400, "CONSULTA_INVALIDA", "La consulta no tiene una codificación válida.") from None
    # La lista conserva cada aparición; todavía no se colapsan claves.
    vistos = set()
    for clave, _ in pares:
        if clave in vistos:
            raise ErrorConsulta(400, "PARAMETRO_REPETIDO", "Cada parámetro debe aparecer una sola vez.")
        vistos.add(clave)
    if vistos - {"almacen", "nombre"}:
        raise ErrorConsulta(400, "PARAMETRO_DESCONOCIDO", "La consulta contiene un parámetro no admitido.")
    parametros = dict(pares)
    almacen = parametros.get("almacen", "")
    if not almacen.strip():
        raise ErrorConsulta(400, "ALMACEN_REQUERIDO", "Selecciona un almacén.")
    nombre = parametros.get("nombre", "")
    if len(nombre) > MAX_NOMBRE:
        raise ErrorConsulta(400, "NOMBRE_DEMASIADO_LARGO", "El nombre admite hasta 80 puntos de código Unicode.")
    return almacen, nombre
