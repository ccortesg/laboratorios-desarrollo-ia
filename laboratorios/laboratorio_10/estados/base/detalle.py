"""Consulta exacta de un articulo dentro del catalogo disponible."""

from laboratorio import consultar_catalogo


def obtener_articulo(almacen, codigo, *, conexion=None):
    """Devuelve el registro disponible con codigo exacto, o None."""
    for articulo in consultar_catalogo("solucion", almacen, conexion=conexion):
        if articulo["codigo"] == codigo:
            return articulo
    return None
