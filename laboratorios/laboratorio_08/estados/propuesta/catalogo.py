"""Correccion didactica: vuelve a transmitir el almacen seleccionado."""

from laboratorio import consultar_catalogo


def filtrar_por_nombre(articulos, texto):
    """Devuelve coincidencias sin consultar datos ni modificar la lista."""
    termino = texto.strip().casefold()
    resultado = []
    for articulo in articulos:
        if termino in articulo["nombre"].casefold():
            resultado.append(articulo)
    return resultado


def buscar_catalogo(almacen, texto, *, conexion=None):
    """Filtra nombres dentro de los articulos disponibles del almacen."""
    articulos = consultar_catalogo("solucion", almacen, conexion=conexion)
    return filtrar_por_nombre(articulos, texto)
