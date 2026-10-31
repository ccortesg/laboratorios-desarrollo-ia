# Estado operativo del repositorio — integración 1.3 preparada

**Versión del estado:** 1.5 · **Fecha:** 31 de octubre de 2026
**Repositorio autorizado:** https://github.com/ccortesg/laboratorios-desarrollo-ia
**Situación:** laboratorio 7 construido y verificado localmente; integración remota pendiente.

Este estado sucede a ESTADO_REPOSITORIO_v1.4.1.md. La versión técnica preparada es repositorio 1.3; la continuidad editorial pasa a ESTADO_DEL_LIBRO_v1.6.md. Los tres números corresponden a documentos o entregas diferentes.

## 1. Base confirmada y procedencia

La consulta de lectura a GitHub se registró a las 17:45:34 UTC del 31 de octubre de 2026:

| Referencia | Commit |
| --- | --- |
| main | 6382e05846e149a9a72f7fdc56da48c37a873833 |
| lab-06-v1.0 | 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd |
| repositorio-v1.2 | 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd |

El árbol de partida es 680fa6135ed0aae40e962ec3f893d72ece1389c1 y el padre de main es 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd. La copia local coincide con el árbol confirmado. La consulta y su método se conservan en evidencia_integracion/laboratorio_07_v1.0/BASE_REMOTA.json.

Las nueve etiquetas anteriores mantienen las referencias observadas. No se crearon ni se movieron etiquetas remotas. Las denominaciones lab-07-v1.0 y repositorio-v1.3 son **previstas**, no publicaciones realizadas.

La corrección de huellas ya forma parte de la base. No debe restaurarse el recolector anterior desde la distribución del laboratorio 6. Los pendientes históricos de subida del laboratorio 6 y cierre de H01 quedaron resueltos en los estados anteriores, que se conservan.

## 2. Alcance preparado

El laboratorio 7 añade un adaptador CSV, una demostración por terminal, datos de intercambio, contrato, contexto, diferencias y comprobaciones. Conserva C01–C04, B01–B06, N01–N10, P01–P06 y W01–W06, incluidos sus subcasos. Incorpora I01–I08 mediante diecisiete casos registrados.

La propuesta suma cantidades y conserva I01 e I07 como FALLIDO. La solución sustituye existencias absolutas y mantiene el mismo estado al repetir una entrada sobre la misma base. I06 comprueba tanto el rechazo previo de un archivo inválido como el rollback de una segunda escritura rechazada por SQLite mediante un trigger temporal de prueba.

Las consultas de la demostración reciben la conexión actualizada. La web conserva su comportamiento predeterminado. No se añade un servicio externo, importación web ni persistencia entre procesos.

La infraestructura común incluye el laboratorio 7 en verificar_todo.py y añade documentación de continuidad. El algoritmo corregido de huellas se conserva; sólo se actualiza el texto de ayuda que mencionaba un total fijo de 34. Las ocho pruebas específicas permanecen como batería independiente.

Los archivos de laboratorios 1–6, historiales y evidencias anteriores no presentan cambios en la comparación local con la base. Las nuevas evidencias se añaden en su propio directorio; los antecedentes no se sobrescriben.

## 3. Verificación conjunta observada

La ejecución de Linux terminó APROBADO con código cero y navegador real:

| Medida | Resultado |
| --- | ---: |
| Laboratorios | 7 |
| Baterías | 44 |
| Casos ejecutados | 408 |
| APROBADO | 400 |
| FALLIDO didácticos | 8 |
| BLOQUEADO | 0 |
| NO EJECUTADO en baterías | 37 |
| Criterios N ausentes, registrados aparte | 10 |
| Huellas de salidas coincidentes | 64/64 |

La fuente es evidencia_integracion/laboratorio_07_v1.0/verificacion_conjunta/resumen.json. El registro tiene fecha técnica 2026-10-31T17:58:08+00:00. La aprobación corresponde a los patrones previstos, no convierte los ocho fallos individuales en aprobaciones.

Los únicos fallos admitidos son C04 en inicial 1; B05/B06 en defecto 3; P04/P05 en propuesta 5; W05 en propuesta 6; I01/I07 en propuesta 7. Cualquier fallo adicional debe producir FALLIDO.

El laboratorio 7, por separado, registró quince baterías y 136 ejecuciones: 134 aprobaciones, dos fallos didácticos y cero bloqueos; diecisiete casos I de base NO EJECUTADO. La solución satisfizo 51/51 casos de cuarenta criterios y el recolector comprobó 30/30 huellas. No deben sumarse de nuevo esas cifras a las 408, que ya incluyen ese recorrido.

El entorno fue Linux, Python 3.12.14, SQLite 3.53.1, Node 24.22.1, Playwright 1.62.1 y Chromium 156.0.8078.80. La comprobación de hashes utiliza los bytes finales después del saneamiento; mantiene las huellas capturadas por separado.

## 4. Cierre del paquete y comprobaciones adicionales

La presentación del Word quedó APROBADA: once páginas renderizadas e inspeccionadas, con texto, trece bloques de código, dos tablas y referencias equivalentes al Markdown de 4.677 palabras. Los metadatos personales están vacíos.

Las ocho pruebas existentes del recolector terminaron APROBADO, código 0. Se registran aparte en evidencia_integracion/laboratorio_07_v1.0/qa_recolector. El algoritmo de huellas y los ocho tests conservan su comportamiento; sólo cambia una frase de ayuda que mencionaba un total fijo.

La extracción del ZIP en una carpeta nueva y su ejecución completa con navegador terminaron APROBADO, código 0: 136 ejecuciones y 30/30 huellas. Se verificaron los 139 archivos declarados en su manifiesto antes y después; ninguno cambió. El ZIP contiene 140 archivos contando el manifiesto. Su SHA-256 es 2f579f87eb3a907e67ab195acb285543ee5997a805ff1add2e422dc7bc9b0b85.

La aplicación del parche se probó sobre una copia limpia de la base registrada y se ejecutó allí el conjunto completo. El informe independiente del paquete, evidencia/PRUEBA_PARCHE.json, identifica el parche final, su árbol, los comandos y sus resultados. El manifiesto SHA256SUMS y VERIFICAR_PAQUETE.py permiten comprobar el paquete recibido antes de aplicarlo.

Una comparación byte a byte conservó 575 archivos históricos, las seis entradas previas de PROCEDENCIA.json y los cuerpos anteriores de CONTINUIDAD.md y VERSIONES.md. Las reglas de atributos nuevas preservan los espacios significativos de los diffs y los saltos Markdown de los dos estados históricos recuperados; no se normalizaron esas evidencias. El registro está en evidencia_integracion/laboratorio_07_v1.0/CONSERVACION_HISTORICA.json.

Estas comprobaciones son ejecuciones locales de Linux. Las instrucciones Git Bash preparan una nueva verificación en Windows; no la dan por realizada.

## 5. Operaciones pendientes y límites

**NO EJECUTADO:** laboratorio 7 en Windows; aplicación de esta integración en el equipo del autor; commit e integración en main del autor; push; creación de etiquetas nuevas; GitHub Actions; sesiones comerciales nuevas; retos opcionales.

La evidencia Windows anterior permanece válida para el alcance que documenta y no sustituye las comprobaciones del laboratorio 7. Las discrepancias históricas de huellas se conservan como antecedentes. La corrección H01 sigue cerrada para nuevas ejecuciones y no necesita volver a aplicarse sobre esta base.

Las pruebas no certifican producción, concurrencia, carga, seguridad integral ni recuperación ante cortes físicos. El cotejo de la carpeta histórica ausente de Codex continúa delimitado y no bloquea este incremento local.

Antes de integrar, comprobar nuevamente main y el estado local. Si main avanzó, preservar sus cambios y adaptar la integración sin reset destructivo, retroceso de ramas ni etiquetas forzadas. Tras aprobar las pruebas de Windows, revisar el cambio, crear el commit y efectuar la subida en un paso posterior. Sólo se prevén lab-07-v1.0 y repositorio-v1.3 como etiquetas nuevas.

El maestro editorial 1.0 permanece intacto. Los capítulos 1–7 siguen pendientes de revisión editorial del autor; no se redactó el capítulo 8.
