"""Variante con defecto intencional para el recorrido de depuracion."""

from laboratorio import consultar_catalogo


def filtrar_por_nombre(articulos, texto):
    """Devuelve coincidencias sin consultar datos ni modificar la lista."""
    termino = texto.strip().casefold()
    resultado = []
    for articulo in articulos:
        if termino in articulo["nombre"].casefold():
            resultado.append(articulo)
    return resultado


def buscar_catalogo(almacen, texto):
    """Filtra nombres; este estado contiene un defecto didactico conocido."""
    articulos = consultar_catalogo("solucion")
    return filtrar_por_nombre(articulos, texto)
