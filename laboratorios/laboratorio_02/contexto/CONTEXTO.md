# Contexto del catálogo

**Estado:** implementación local existente del laboratorio 2, versión 1.0. Este documento expresa el comportamiento requerido. El código muestra cómo se implementa y la evidencia registra una ejecución concreta. Una discrepancia entre ellos debe investigarse y quedar documentada.

## Problema y objetivo

Una aplicación ficticia de solicitudes e inventario necesita ofrecer únicamente artículos que puedan atenderse desde el almacén elegido. El piloto corrigió una consulta que aceptaba existencias de cualquier ubicación. El laboratorio 2 parte de esa solución y añade el contexto necesario para continuar sin reconstruir una conversación.

El objetivo de esta entrega es documentar, relacionar y verificar el comportamiento existente. No se ha solicitado ampliar las funciones del catálogo.

## Regla vigente

Un artículo aparece si está habilitado y existe un registro de existencias del mismo artículo, en el almacén seleccionado, con una cantidad mayor que cero. Las tres condiciones de existencias deben referirse al mismo registro. Para este ejercicio, disponible significa cantidad positiva; no se restan reservas ni compromisos de entrega.

El parámetro de almacén se recibe en `consultar_catalogo(version, almacen="ALFA")`, dentro de `laboratorio.py`, y se enlaza a `:almacen` en `solucion/consulta.sql`. Habilitación del artículo no equivale a autorización de un usuario.

## Datos sintéticos y trazabilidad

La ubicación de los cuatro criterios es ALFA. Los registros están en `datos/ejemplos.sql` y las tablas en `datos/esquema.sql`.

| Criterio | Dato preparado | Resultado esperado | Comprobación en pruebas.py |
| --- | --- | --- | --- |
| C01 | A01 habilitado, ALFA, 7 unidades | Aparece | test_c01_habilitado_con_existencias_locales_aparece |
| C02 | A02 deshabilitado, ALFA, 4 unidades | Se excluye | test_c02_deshabilitado_se_excluye |
| C03 | A03 habilitado, ALFA, 0 unidades | Se excluye | test_c03_sin_existencias_se_excluye |
| C04 | A04 habilitado, BETA, 9 unidades | Se excluye | test_c04_existencias_en_otra_ubicacion_se_excluyen |

En `solucion/consulta.sql`, `a.habilitado = 1` conserva la condición de habilitación; `e.articulo = a.codigo` relaciona el artículo; `e.almacen = :almacen` limita la ubicación; y `e.cantidad > 0` exige existencias. C01 observa su combinación favorable; C02, C03 y C04 verifican motivos de exclusión distintos.

Las pruebas evalúan códigos devueltos, no la escritura del SQL. El criterio se conserva aunque una implementación futura equivalente utilice otra estructura. Los cuatro ejemplos no cubren todas las combinaciones posibles.

## Límites y referencias

Mantener el esquema, los datos, la consulta corregida y los cuatro criterios. En este ejercicio se puede mejorar la documentación y proponer preguntas o alternativas, identificando su estado. Cualquier cambio funcional necesita un encargo propio con criterios adicionales.

Consulta [ARQUITECTURA](ARQUITECTURA.md) para conocer responsabilidades y contratos; [DECISIONES](DECISIONES.md) para entender los motivos; y [CONTINUIDAD](CONTINUIDAD.md) para retomar la verificación. Las expectativas de esta página no sustituyen los resultados de `evidencia/pruebas_solucion.json`.
