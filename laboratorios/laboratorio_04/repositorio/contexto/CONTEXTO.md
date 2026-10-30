# Contexto del repositorio con consulta exacta

**Estado:** laboratorio 4, implementación de referencia `solucion`. Se conserva el estado corregido del laboratorio 3 y se añade el incremento de `ALCANCE.md`; las entregas anteriores permanecen intactas.

## Regla que se conserva

Un artículo aparece si está habilitado y existe un registro de existencias del mismo artículo, en el almacén seleccionado, con cantidad mayor que cero. Las condiciones de artículo, almacén y cantidad corresponden al mismo registro. Disponible significa cantidad positiva; no se calculan reservas. La habilitación del artículo no representa autorización de usuarios.

`laboratorio.py` conserva `consultar_catalogo(version, almacen="ALFA")` y carga `solucion/consulta.sql`. La llamada con `"solucion"` y el almacén elegido enlaza `:almacen`. El SQL, el esquema, los datos y el ejecutor se conservan byte a byte desde el laboratorio 2.

## Incremento de búsqueda

`buscar_catalogo(almacen, texto)` consulta primero los artículos disponibles y filtra después por subcadena del nombre. Las entradas del contrato son cadenas. El término usa `strip().casefold()`; el nombre usa `casefold()`. El texto vacío o blanco conserva todos los resultados disponibles. No se retiran acentos ni se realiza búsqueda aproximada.

La salida conserva los diccionarios `codigo` y `nombre` y su orden de entrada. Este contrato se inspecciona en el código y se comprueba mediante los ejemplos siguientes. Los datos de la práctica no permiten acreditar orden entre varios artículos disponibles del mismo almacén.

## Trazabilidad funcional

| Criterio | Datos o entrada | Expectativa | Archivo de comprobación |
| --- | --- | --- | --- |
| C01 | A01 habilitado, ALFA, 7 unidades | Aparece en ALFA | `pruebas.py`, `test_c01_...` |
| C02 | A02 deshabilitado, ALFA, 4 unidades | Se excluye | `pruebas.py`, `test_c02_...` |
| C03 | A03 habilitado, ALFA, 0 unidades | Se excluye | `pruebas.py`, `test_c03_...` |
| C04 | A04 habilitado, BETA, 9 unidades | Se excluye de ALFA | `pruebas.py`, `test_c04_...` |
| B01 | ALFA, `"  LoCaL  "` | A01 completo | `test_b01_normaliza_espacios_y_mayusculas` |
| B02 | ALFA, espacio, tabulación y espacio | A01 completo | `test_b02_termino_blanco_devuelve_disponibles` |
| B03 | ALFA, `"inexistente"` | Lista vacía | `test_b03_sin_coincidencias_devuelve_lista_vacia` |
| B04 | ALFA, `"otra"` | Lista vacía | `test_b04_nombre_remoto_no_amplia_disponibilidad` |
| B05 | BETA, `""` | A04 completo | `test_b05_almacen_beta_con_termino_vacio` |
| B06 | BETA, `" OTRA "` | A04 completo | `test_b06_busqueda_normalizada_en_beta` |

C01 a C04 y B01 a B06 conservan literalmente sus métodos y expectativas. La preparación importa `buscar_catalogo` de `catalogo.py`, copia byte a byte de `estados/corregido.py` del laboratorio 3. Los C consultan ALFA con término vacío y los B comparan registros completos con expectativas explícitas. Los cuatro artículos y sus existencias están en `datos/ejemplos.sql`; no se agregaron registros al dataset.

## Consulta exacta implementada y límites

`detalle.py` implementa `obtener_articulo(almacen, codigo)`. Recibe cadenas, consulta disponibilidad del almacén y devuelve el primer registro cuyo código coincide exactamente, o `None`. La clave primaria del esquema hace únicos los códigos. No retira espacios ni transforma mayúsculas. Su contrato previo está en `ALCANCE.md`.

N01 y N02 cubren artículos disponibles en ALFA y BETA. N03 y N04 excluyen deshabilitado y agotado. N05 y N06 excluyen el artículo remoto en ambas direcciones. N07 comprueba un código inexistente; N08, N09 y N10 comprueban otra caja, espacios y prefijo. Las entradas y expectativas explícitas están en `pruebas_detalle.py`. `pruebas.py` ejecuta los veinte criterios sobre el árbol actual.

La evidencia del recorrido se guarda fuera del repositorio, en la carpeta `evidencia` del paquete. Este contexto expresa requisitos y no sustituye una ejecución. No hay frontend, API, persistencia de solicitudes ni conexión a inventarios reales.
