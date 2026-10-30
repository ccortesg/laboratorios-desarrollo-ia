"""Primera implementacion didactica de la busqueda por nombre."""

from laboratorio import consultar_catalogo


def buscar_catalogo(almacen, texto):
    """Filtra nombres dentro de los articulos disponibles del almacen."""
    articulos = consultar_catalogo("solucion", almacen)
    termino = texto.strip().casefold()
    resultado = []
    for articulo in articulos:
        if termino in articulo["nombre"].casefold():
            resultado.append(articulo)
    return resultado
