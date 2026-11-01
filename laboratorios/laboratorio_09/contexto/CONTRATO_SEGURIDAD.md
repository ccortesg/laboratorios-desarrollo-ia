# Contrato previo del laboratorio 9

Fecha de decisión: 1 de noviembre de 2026. Se registra antes de escribir la implementación nueva. Proyecto y datos exclusivamente sintéticos.

## Incremento elegido

Añadir una frontera de validación explícita y acotada para las consultas GET de `/api/resumen`. La aplicación del laboratorio 8 ya conserva disponibilidad, búsqueda, importación transaccional, persistencia y presentación mediante texto. Sin embargo, su adaptador HTTP acepta parámetros repetidos eligiendo el primer valor, ignora claves adicionales y no declara un límite pequeño de consulta o búsqueda. El incremento define esas decisiones en el servidor, conservando las interfaces y los contratos anteriores para sus entradas válidas.

No se añade autenticación, pantalla de importación, servicio externo, autorización por usuario, infraestructura productiva, escáner ni nuevo origen de datos. El servidor permanece ligado a loopback y el recorrido CSV → CLI → SQLite persistente → HTTP → navegador sigue siendo real. Las comprobaciones de seguridad sólo envían peticiones al servidor sintético levantado por cada prueba.

## Riesgos y límites de confianza

1. Una consulta con dos valores para la misma clave es ambigua: dos componentes podrían elegir valores distintos. El contrato la rechaza antes de consultar; no elige el primero ni el último.
2. Valores mal codificados o demasiado grandes no deben convertirse silenciosamente en otra entrada ni seguir hasta el dominio sin un límite definido.
3. El rechazo debe ser distinguible de un catálogo vacío y la pantalla debe recuperarse para una nueva consulta. La respuesta no debe exponer rutas, SQL interno ni el texto recibido.
4. Las cadenas parecidas a SQL siguen siendo datos. La validación de forma y longitud no sustituye el tratamiento seguro de valores en las capas existentes. El error interno controlado conserva el mensaje público genérico ya disponible.

La petición HTTP cruza una frontera de entrada aunque el formulario normalmente genere una URL correcta. El navegador es un consumidor; las reglas nuevas se aplican en el servidor. SQLite y los archivos de diagnóstico pertenecen al entorno de práctica y no se asumen protegidos frente a un usuario local que pueda editarlos. No se demuestra resistencia global a denegación de servicio, ataques de red o procesos concurrentes.

## Reglas de entrada y respuesta

- Alcance: únicamente la query de `/api/resumen` con GET. Recursos estáticos y ruta desconocida conservan su comportamiento.
- Claves admitidas, comparadas exactamente después de decodificar: `almacen` y `nombre`.
- `almacen` es obligatorio, una sola vez. Su ausencia o valor vacío/sólo espacios mantiene HTTP 400 y el error histórico `ALMACEN_REQUERIDO`. El valor no se recorta ni cambia de mayúsculas para consultar: no se altera la coincidencia exacta del almacén.
- `nombre` es opcional y aparece como máximo una vez. Ausente equivale a cadena vacía. La búsqueda sigue usando su `strip()` y `casefold()` existentes dentro del dominio; no se aplican a los identificadores.
- Cualquier clave repetida se rechaza con HTTP 400 y `PARAMETRO_REPETIDO`, incluso si sus valores son iguales o si la clave repetida usa percent-encoding equivalente. No se colapsan pares a diccionario antes de detectar repeticiones.
- Una clave adicional se rechaza con HTTP 400 y `PARAMETRO_DESCONOCIDO`.
- La query URL recibida se limita a 2.048 bytes en su representación UTF-8, antes de decodificar valores. Sobrepasarlo produce HTTP 414 y `CONSULTA_DEMASIADO_LARGA`. Es un límite didáctico del adaptador, no un ensayo de carga ni una garantía de protección frente a toda denegación de servicio.
- Tras decodificar, `nombre` admite hasta 80 puntos de código Unicode, inclusive. Se cuenta antes de recortar espacios o normalizar la búsqueda. Excederlo produce HTTP 400 y `NOMBRE_DEMASIADO_LARGO`.
- Se utiliza percent-encoding bien formado y decodificación UTF-8 estricta; `+` representa espacio. Secuencias `%` incompletas/no hexadecimales, bytes UTF-8 inválidos o campos sin estructura `clave=valor` producen HTTP 400 y `CONSULTA_INVALIDA`. No se aplica doble decodificación.
- Orden de validación: límite de query, sintaxis/decodificación, repeticiones, claves admitidas, almacén requerido, longitud de nombre. Una petición con varios errores tiene el diagnóstico de la primera regla incumplida.
- Las respuestas nuevas utilizan el sobre `{"error":{"codigo":...,"mensaje":...}}` con mensajes estáticos comprensibles. No repiten la petición, rutas ni información interna. Conservan los encabezados existentes.
- Una petición válida conserva HTTP 200 y el resumen de negocio real de la base seleccionada. Un almacén desconocido no vacío mantiene la consulta exacta y el resultado vacío anterior; no se introduce una lista distinta de almacenes autorizados.
- Los fallos internos de consulta conservan HTTP 500 y `CONSULTA_FALLIDA`, sin detalles internos. La aplicación no registra la query del lector.

## Estados y defecto intencional

`base` es una copia exacta de la solución corregida del laboratorio 8. Sus 62 casos heredados siguen siendo el contrato anterior y deben aprobar.

`propuesta` introduce la política nueva, pero convierte la lista de pares a `dict` antes de buscar claves repetidas. Esta única decisión defectuosa borra la evidencia de duplicidad y conserva silenciosamente el último valor. No se atribuye a una herramienta comercial ni a una conversación histórica.

`solucion` detecta las repeticiones mientras conserva la lista de pares y construye después el diccionario. No modifica filtros, datos, importación, persistencia, interfaz ni expectativas para obtener aprobación.

Las comprobaciones nuevas se ejecutan sobre los tres estados. La base se evalúa contra una exigencia que su contrato anterior no incluía: sus fallos esperados se registran como brechas respecto de la política nueva, no como fallos de los contratos heredados. La propuesta debe fallar exclusivamente en la regla de repetición. Los errores de infraestructura nunca cuentan como fallos didácticos.

## Criterios nuevos y casos

| Criterio | Caso | Comportamiento observable |
| --- | --- | --- |
| S01 | S01 | Consultas válidas y límite de 80 caracteres se aceptan; consulta tras importación devuelve el resumen persistido correcto y conserva la búsqueda normalizada existente. |
| S02 | S02.a | `almacen=ALFA&almacen=BETA` se rechaza con 400/PARAMETRO_REPETIDO. |
| S02 | S02.b | Dos apariciones de `nombre`, incluso con el mismo valor, se rechazan con 400/PARAMETRO_REPETIDO. |
| S02 | S02.c | `almacen=ALFA&%61lmacen=ALFA` se reconoce como repetición y se rechaza. |
| S03 | S03 | Una clave adicional como `debug=1` se rechaza con 400/PARAMETRO_DESCONOCIDO. |
| S04 | S04.a | Un nombre de 81 puntos de código se rechaza; los espacios también cuentan antes de normalizar. |
| S04 | S04.b | Una query de 2.049 bytes se rechaza con 414 antes de decodificar; el servicio atiende correctamente otra petición posterior. |
| S05 | S05.a | Una secuencia percent inválida se rechaza con 400/CONSULTA_INVALIDA. |
| S05 | S05.b | Bytes que no forman UTF-8 válido se rechazan con 400/CONSULTA_INVALIDA. |
| S06 | S06 | Navegador real: resultado válido, nombre de 81 caracteres, error visible y resultados previos ocultos, controles recuperados, nueva consulta válida sobre la misma base. |
| S07 | S07 | Una búsqueda corta parecida a SQL se trata como dato: 200 con el resultado literal esperado, sin ampliar el catálogo ni cambiar la base. No se usa una lista de palabras prohibidas. |
| S08 | S08 | Un fallo real y controlado de apertura de la base tras iniciar el servidor produce 500/CONSULTA_FALLIDA genérico, sin ruta ni SQL; restaurado el recurso, una consulta vuelve a funcionar. |

Son ocho criterios y doce casos: once HTTP y uno de navegador. La solución conserva 62 casos anteriores y añade estos doce: 74 casos por recorrido completo de un estado.

Patrón esperado de la base respecto de la política nueva: FALLIDO únicamente en S02.a, S02.b, S02.c, S03, S04.a, S04.b, S05.a, S05.b y S06. S01/S07/S08 deben aprobar. La propuesta debe FALLAR únicamente en S02.a/S02.b/S02.c. La solución debe aprobar todos. Los 62 heredados deben aprobar en los tres estados.

Si una observación contradice estas expectativas, se investigará y se corregirá la implementación o el diseño de la prueba, documentando cualquier decisión contractual revisada antes de cerrar resultados. No se cambiará una expectativa sólo para ocultar un error.

## Evidencia y conservación

Se conservan los datos de referencia y las pruebas heredadas. Las importaciones nuevas utilizan bases desechables aisladas; no se cambian las expectativas históricas. Se registra comparación de la base copiada contra la solución 8 y diferencias base→propuesta→solución. Los resultados esperados de este documento no son evidencia de ejecución.

Se reutiliza el saneamiento de salidas con huellas capturadas y finales. Se ejecutan por separado las ocho pruebas comunes del recolector y las regresiones pertinentes de recursos/evaluación. La batería funcional nueva no se suma a auditorías para aparentar cobertura adicional. El conjunto completo incluye navegador cuando puede ejecutarse y conserva exactamente los fallos esperados.

Los límites del ejercicio incluyen autenticación, permisos por usuario, concurrencia de escritores, límites globales de memoria/CPU, pruebas de carga, hardening productivo, auditoría general de dependencias y seguridad integral. El reto editorial podrá proponer una extensión acotada, pero no se implementará en esta entrega.
