# Contrato previo del laboratorio 7

Versión 1.0. Incremento didáctico local; datos completamente sintéticos.
Este contrato se escribió antes de implementar el importador y sus pruebas.

## Entrada y significado

CSV de actualizaciones parciales de **cantidades absolutas** por par artículo–almacén.
Encabezado exacto y en este orden: `codigo_articulo,almacen,existencias`.
Separador coma; UTF-8 estricto con BOM inicial opcional. Se admiten LF y CRLF.
El lector CSV interpreta comillas; no se implementa un parser propio.
No se recortan espacios ni se cambian mayúsculas de identificadores: son cadenas
exactas, incluidos posibles ceros iniciales. Los encabezados y campos adicionales,
ausentes o vacíos son inválidos. Se rechazan filas vacías; una última terminación
de línea no cuenta como otra fila. Un archivo sin registros de datos se rechaza.

Las existencias contienen exclusivamente dígitos ASCII y representan un entero
entre 0 y 2147483647, inclusive. Se aceptan ceros iniciales de cantidades porque
no son identificadores. No se aceptan signos, espacios, decimales ni notación
exponencial. Artículos y almacenes deben existir en los maestros sintéticos.
Un par repetido en el mismo archivo provoca rechazo, incluso con la misma cantidad.

Cada par presente sustituye su cantidad. Los pares omitidos se conservan. Puede
crearse una relación artículo–almacén antes ausente si ambos maestros existen.
No se crean maestros ni se modifica nombre o habilitación. Cero es válido.
La base del llamador debe tener sus cambios anteriores confirmados; el importador
controla la transacción de su aplicación y no cierra esa conexión.

## Resultado y rechazo

Se leen los bytes una sola vez y se identifica ese contenido con SHA-256. Se
valida el archivo completo antes de aplicar; cualquier error implica cero cambios.
La aplicación usa una transacción. El catálogo debe consultar esa misma conexión,
no recrear los datos iniciales. Los errores de escritura revierten la transacción.

El informe de negocio usa `APLICADO` o `RECHAZADO`; las comprobaciones usan
APROBADO, FALLIDO, BLOQUEADO o NO EJECUTADO. Registra huella fuente, filas leídas
(registros de datos completos, excluido encabezado), filas individualmente válidas,
filas aplicadas (pares cuyo valor realmente cambió) y filas sin cambio. Tras
rechazo hay cero filas aplicadas. Los errores identifican fila física final del
registro y campo/código; nunca incluyen rutas, identidad o mensajes internos SQL.
La segunda aplicación puede registrar cero cambios sin alterar el estado final.

## Criterios

- I01: importación válida seguida de consulta del catálogo en la misma base;
  almacén, habilitación y disponibilidad permanecen correctos.
- I02: rechazo de encabezado incorrecto, columnas extra/ausentes, codificación
  inválida, archivo vacío o sin datos y filas vacías.
- I03: rechazo de maestros desconocidos y códigos que difieran por espacios o caso.
- I04: rechazo de cantidades negativas, fraccionarias, no numéricas o fuera de rango.
- I05: rechazo de pares duplicados.
- I06: una fila válida seguida de otra inválida no modifica ninguna tabla.
- I07: repetir el mismo archivo sobre la misma base conserva el resultado y los
  pares omitidos.
- I08: informe SHA-256 y conteos coherentes; error localizable sin datos identificables.

Los subcasos definidos serán I01, I02.a–I02.e, I03.a–I03.c, I04.a–I04.d,
I05, I06, I07 e I08: 17 casos para ocho criterios nuevos. Los contratos C/B/N/P/W
se comprueban con sus datos de referencia intactos en cada estado del laboratorio.

## Estados y defecto acordado antes de implementar

`base` conserva la solución del laboratorio 6, sin importador. Sus 17 casos I son
NO EJECUTADO. `propuesta` incorpora el adaptador pero suma las existencias recibidas
al valor anterior en lugar de sustituirlo. Es un defecto intencional preparado
para el libro. Fallan exactamente I01 e I07 por AssertionError. `solucion` cambia
esa operación por sustitución absoluta y debe aprobar los 17 casos I.

Archivo didáctico válido: A01/ALFA=5, A02/ALFA=8, A03/ALFA=3 y A04/BETA=0.
Con la propuesta, A01 pasa de 7 a 12 y después a 17 al repetir; con la solución
queda en 5. La solución habilita la aparición de A03 por sus existencias, mantiene
oculto A02 por estar deshabilitado y deja vacío BETA. No cambia habilitaciones.

## Fuera de alcance

No se implementan interfaz web de importación, API externa, servicios comerciales,
reservas, cantidades solicitadas, usuarios ni plataforma completa. Las consultas
HTTP heredadas siguen usando su comportamiento predeterminado. La importación y
su consulta demostrativa se realizan por terminal y en memoria. No se acredita
concurrencia, cortes físicos de energía ni preparación productiva.
