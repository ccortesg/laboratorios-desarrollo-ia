# Contexto vigente del catálogo y la búsqueda

**Estado:** laboratorio 3, implementación sintética local. Este archivo actualiza el paquete de contexto del capítulo 2 para un incremento definido en [ALCANCE](../ALCANCE.md). Los documentos anteriores permanecen sin cambios en sus entregas originales.

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

C01 a C04 conservan literalmente sus funciones de prueba. Su preparación selecciona la consulta base o la búsqueda con texto vacío, según el estado. Los B comparan registros completos con expectativas explícitas. Los cuatro artículos y sus existencias están en `datos/ejemplos.sql`; no se agregaron registros al dataset.

## Límites

Se permite implementar y comparar los cuatro módulos didácticos de búsqueda. La base y sus reglas quedan conservadas. `defecto` es un estado intencionalmente incorrecto; no representa una regresión pendiente en `corregido`. Los detalles están en [ARQUITECTURA](ARQUITECTURA.md) y [DECISIONES](DECISIONES.md).

La evidencia se consulta en `evidencia/resumen.json` y los registros por criterio. Este contexto expresa requisitos, no sustituye los resultados de una ejecución propia. No hay frontend, API, persistencia de solicitudes ni conexión a inventarios reales.
