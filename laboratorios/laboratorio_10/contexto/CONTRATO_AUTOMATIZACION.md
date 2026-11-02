# Contrato previo del laboratorio 10

Registro anterior a la implementación: **2026-11-02 00:02:55 UTC**. El proyecto y sus datos son exclusivamente sintéticos. Este documento define expectativas; no constituye evidencia de ejecución.

## Incremento y propósito

Crear una operación repetible de actualización local: leer una instantánea del CSV elegido, importar sus existencias mediante la CLI existente, consultar la misma base persistente mediante otro proceso CLI y conservar un recibo de la operación. La secuencia está fijada por el programa. No ejecuta instrucciones arbitrarias, no recibe comandos ni planes de un modelo y no se presenta como agente comercial.

El catálogo, las reglas de importación, la base, la política HTTP y la web conservan la solución del laboratorio 9. Una prueba nueva de navegador observará el mismo servidor antes y después de invocar el operador: CSV → operador → importador CLI → SQLite persistente → HTTP → navegador. El operador no necesita navegador ni instala dependencias.

## Interfaz y precondiciones

`operar.py` recibe `--base`, `--archivo`, `--almacen` y `--salida`, obligatorios; admite `--nombre` y `--alias` sintético opcionales. No admite URL, host, código, comando, script alternativo, plan o indicador de sobrescritura. Utiliza el intérprete Python de la ejecución y el `persistencia.py` de su propio estado, con argumentos en lista, `shell=False`, UTF-8 y un límite de 20 segundos por hijo.

Antes de cualquier importación:

- La base debe existir como archivo, tener el esquema heredado y poder abrirse mediante `abrir_base()`. La conexión de validación se cierra explícitamente. El operador no inicializa ni recrea bases.
- El CSV debe existir como archivo y ser distinto de la base. Los identificadores y las cantidades conservan exactamente el contrato de importación; el operador no normaliza códigos.
- La salida debe ser una carpeta nueva. Rechaza cualquier destino existente, la raíz del laboratorio y los descendientes de `estados`, `datos`, `contexto`, `prompts`, `diferencias`, `soporte`, `evidencia` y `node_modules`, antes de importar. No borra ni reutiliza recibos.
- Las rutas del CSV y de la base se resuelven explícitamente; los scripts no se buscan en el directorio actual del invocador.

Tras validar, crea la carpeta nueva con exclusión de existencia y guarda los bytes leídos una sola vez del CSV como `entrada.csv`. El importador recibe esa instantánea. Su SHA-256 y tamaño identifican exactamente los bytes empleados en esta ejecución, sin prometer identidad con una segunda lectura del archivo original. El modelo supone ejecución local secuencial: no intenta proteger archivos frente a otro proceso con permisos para modificarlos concurrentemente.

## Secuencia y decisiones

1. Invocar `persistencia.py importar --base BASE --archivo RECIBO/entrada.csv`.
2. Sólo si el hijo devuelve código 0 y JSON `APLICADO`, invocar `persistencia.py consultar --base BASE --almacen ALMACEN --nombre NOMBRE --alias ALIAS`.
3. Si la consulta devuelve código 0 y JSON `CONSULTADO`, registrar su resumen real y terminar APROBADO con código 0.

Un rechazo o fallo del importador detiene la solución: importación FALLIDO, consulta NO EJECUTADO, resultado FALLIDO y código 1. Un paso no ejecutado no tiene capturas ni huellas inventadas. Si un ejecutable no puede iniciarse o vence el tiempo, el paso se clasifica BLOQUEADO, se detiene la secuencia y termina con código 2. Un JSON inválido o un resultado incompatible con el código de salida se registra FALLIDO. Una precondición inválida produce RECHAZADO/código 2 sin importar.

No hay reintentos automáticos. La importación tiene su propia transacción. Si se confirmó y falla la consulta posterior, los datos ya aplicados permanecen; el recibo debe indicar `importacion_confirmada=true` y el punto alcanzado. Detenerse no equivale a revertir toda la operación. La recuperación requiere revisar el recibo y decidir si basta consultar de nuevo; el programa no ejecuta rollback genérico ni reinicialización.

## Recibo e integridad

El recibo contiene `entrada.csv`, `resultado.json`, `comandos.json`, las capturas de pasos ejecutados y `huellas.json`. Se emplea la copia exacta del recolector corregido para conservar huellas capturadas y comprobar bytes finales después del saneamiento. Las capturas se guardan primero como bytes; no se convierten saltos LF/CRLF para hacer coincidir hashes.

`resultado.json` identifica entrada por SHA-256/tamaño, base por alias sintético, pasos y estado final, si la importación se confirmó y el resumen sólo si una consulta válida lo produjo. `comandos.json` declara los códigos de salida, estados, comandos con alias de rutas y los nombres simples de stdout/stderr existentes. Se omiten rutas del equipo y datos de identidad. El recibo es evidencia operativa local, no una firma digital ni prueba de uso comercial.

## Estados y defecto acotado

`base` copia exactamente la solución 9 y no incorpora `operar.py`. Sus 74 casos heredados deben aprobar; los ocho T se registran NO EJECUTADO.

`propuesta` añade el operador y sus precondiciones, pero ignora una importación rechazada con código 1 y continúa consultando. El resultado global toma el éxito de la consulta aunque los datos sigan antiguos. Conserva la captura y el rechazo del importador. Es un defecto didáctico preparado para el libro.

`solucion` exige importación confirmada antes de consultar. La única diferencia funcional de la propuesta es esa decisión de continuación. Ambas detienen errores de infraestructura y comparten precondiciones, formato, tiempos y protección de salidas. Sólo T02 debe fallar en la propuesta; los demás fallos impedirán aprobar el laboratorio.

## Criterios y casos nuevos

| Criterio/caso | Comportamiento observable |
| --- | --- |
| T01 | CSV válido por el operador: la CLI real aplica cantidades absolutas y la consulta de la misma base muestra A01/A03 en ALFA, A03=3, A02 deshabilitado. Resultado APROBADO/código 0. |
| T02 | Primera fila válida seguida de una inválida: estado completo sin cambios, importación rechazada, consulta NO EJECUTADO y código no cero. La propuesta falla este caso al continuar y devolver el catálogo antiguo. |
| T03 | Repetir el mismo CSV con dos carpetas de recibo conserva el estado y los pares omitidos; ambos recibos existen y el primero conserva sus bytes. |
| T04 | Base ausente: rechazo previo, no se crea la base ni se importa; ningún catálogo de referencia sustituye al archivo elegido. |
| T05 | Salida existente o dentro de componentes protegidos: rechazo previo, base y CSV intactos y recibo anterior conservado. Se incluyen ambas entradas como observaciones del mismo criterio de protección de salida. |
| T06 | Recibo trazable: instantánea idéntica al CSV leído, SHA-256/tamaño correctos, códigos reales y pasos coherentes, resumen consultado y huellas finales verificables; no hay rutas personales. |
| T07 | Cwd ajeno y rutas con espacios: operación correcta sobre la base explícita, sin buscar scripts en el cwd ni interpretar argumentos como instrucciones. |
| T08 | Navegador real sobre el mismo servidor: resultado inicial A01, operador en proceso separado, resultado posterior A01/A03 y búsqueda A03. La base HTTP es la modificada por la operación. |

Son ocho criterios y ocho casos: siete de CLI y uno de navegador. Los 74 casos anteriores corresponden a 56 criterios; la solución tendrá 82 casos y 64 criterios. Las expectativas son base 74 APROBADO y ocho NO EJECUTADO, propuesta 81 APROBADO y T02 FALLIDO, solución 82 APROBADO. Las cifras de la ejecución se calcularán de los registros y se distinguirán de estas expectativas.

Los 74 heredados se ejecutan en los tres estados, con datos de referencia intactos. No se arrastran fallos S de base/propuesta9 a laboratorio10: los tres estados reutilizan la solución de seguridad. Los T usan bases y recibos aislados. El fallo didáctico debe ser una aserción; un error de infraestructura no acredita T02.

## Alcance y límites

Implementado: operador fijo, snapshot del CSV, dos CLI reales, parada ante fallo, recibo nuevo, huellas y observación real en navegador. Fuera de alcance: planificador, demonio, cola, reintentos, agentes que elijan acciones, proveedores comerciales, credenciales, servicios externos, concurrencia, autenticación, exposición pública, despliegue y recuperación ante fallo físico de almacenamiento.

La aprobación de las pruebas no aprueba el manuscrito. El reto editorial podrá ampliar una propiedad concreta, pero no se implementará en esta entrega. Si el comportamiento observado exige revisar el contrato, la decisión se registrará expresamente antes de declarar resultados; no se alterará una expectativa para ocultar un error.
