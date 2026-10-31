# Estado operativo del repositorio — cierre de la corrección de huellas

**Versión del estado:** 1.4.1 · **Fecha:** 31 de octubre de 2026  
**Repositorio autorizado:** https://github.com/ccortesg/laboratorios-desarrollo-ia  
**Situación:** corrección del recolector integrada en main, verificada en Windows y auditada. **H01 cerrado para las ejecuciones nuevas.**

Este estado actualiza `ESTADO_REPOSITORIO_v1.4.md`, que se conserva como antecedente. La entrega técnica etiquetada sigue siendo `repositorio-v1.2`; la corrección es un commit posterior y no crea una etiqueta de versión nueva. La continuidad del libro pasa a `ESTADO_DEL_LIBRO_v1.5.2.md`. El maestro editorial permanece en 1.0.

## 1. Punto de partida vigente confirmado

La consulta independiente de lectura a GitHub confirmó:

| Referencia | Commit |
| --- | --- |
| main | 6382e05846e149a9a72f7fdc56da48c37a873833 |
| lab-06-v1.0 | 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd |
| repositorio-v1.2 | 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd |

El commit actual tiene como único padre `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd` y árbol `680fa6135ed0aae40e962ec3f893d72ece1389c1`, idéntico al del parche preparado y probado. La fecha Git es `2026-10-31T16:28:05Z`; es un dato del commit, no la fecha de las pruebas. Las nueve etiquetas existentes conservan sus referencias y no se añadieron otras en este cierre.

Fuente operativa: [commit publicado](https://github.com/ccortesg/laboratorios-desarrollo-ia/commit/6382e05846e149a9a72f7fdc56da48c37a873833). La consulta completa y la comparación de árboles constan en `AUDITORIA_REMOTA.json` del paquete de revisión.

## 2. Alcance exacto y conservación

El cambio modifica `herramientas/verificar_todo.py` y añade tres archivos:

- `herramientas/huellas_evidencia.py`.
- `herramientas/pruebas/test_huellas_evidencia.py`.
- `docs/CORRECCION_RECOLECTOR_v1.0.md`.

El árbol pasa de 585 a 588 archivos: uno modificado, tres nuevos y ninguno eliminado. Los otros **584 archivos anteriores conservan contenido y modo**. La comparación confirma íntegros los 310 archivos de laboratorios, los siete archivos de distribuciones, los dos de historiales y los 257 de evidencia de integración. No cambia la aplicación ni los contratos C/B/N/P/W.

Los cuatro archivos del cambio coinciden por objeto Git con los bytes del parche probado. `COTEJO_PARCHE_PUBLICADO.json` registra además sus SHA-256. El autor realizó el commit, la integración fast-forward y el push; el asistente sólo leyó GitHub durante esta revisión.

## 3. Evidencia Windows nueva y comprobaciones

Fuente original: `EVIDENCIA_CORRECCION_HUELLAS_WINDOWS_v1.0.zip`, **82.204 bytes**, 118 archivos y siete entradas de directorio. CRC correcto, sin duplicados ni rutas inseguras detectadas. SHA-256 recibido:

`001cd08e94f9b9a00c400368cdedfc7072955c4beb3ac44b017af2eb11878707`

Los registros conservan el intervalo técnico `2026-10-31T16:25:31Z`–`2026-10-31T16:25:48Z`. Son tiempos consignados por el entorno registrador. El entorno acreditado es Windows, Python 3.11.9, SQLite 3.45.1, Git 2.45.1.windows.1, Node v20.20.0, Playwright 1.62.1 y Chromium 151.0.7922.34.

| Comprobación | Resultado y procedencia |
| --- | --- |
| Ocho pruebas específicas del recolector | APROBADO, salida 0, según la transcripción del autor. |
| Verificación conjunta completa | APROBADO: 29 baterías, 272 ejecuciones, 266 aprobaciones, seis fallos didácticos y cero bloqueos; casos conciliados en el ZIP. |
| Código global y comprobador de huellas | Ambos 0, según la transcripción aportada. |
| Huellas finales stdout/stderr | 34/34 APROBADO, recalculadas independientemente sobre los bytes recibidos, sin normalización. |
| Solución del laboratorio 6 | 34/34 casos APROBADO. |
| Fuentes del laboratorio 6 | 60/60 hashes coinciden con la distribución final de referencia. |
| Conservación heredada del laboratorio 6 | 28/28 comprobaciones coherentes con las fuentes. |

Permanecen 20 NO EJECUTADO en estados didácticos y diez criterios N ausentes aparte. Los seis fallos exactos son C04 en inicial 1; B05/B06 en defecto 3; P04/P05 en propuesta 5; W05 en propuesta 6. Conservan su clasificación FALLIDO. No se detectaron fallos inesperados en la ejecución aportada.

Los ocho tests específicos no se suman a las 272 ejecuciones del catálogo para aparentar una sola batería mayor. El ZIP no incluye una nueva ejecución de unittest por el asistente: su resultado está acreditado por la transcripción del autor. La revisión de archivos y de GitHub constituye una auditoría separada.

## 4. Cierre de H01 y tratamiento de los históricos

El recolector valida la captura antes de transformar archivos, escribe bytes sin conversión implícita de LF/CRLF y calcula las huellas finales leyendo lo efectivamente guardado. Conserva las huellas de captura en `sha256_stdout_capturado` y `sha256_stderr_capturado`, y distingue las convenciones originales de las finales.

En esta ejecución los **34 campos capturados están presentes y sus valores coinciden también con los hashes finales**. No fue necesario normalizar saltos para aprobar los hashes recibidos. La auditoría no presupone acceso a una captura original adicional distinta de los archivos aportados.

H01 queda **cerrado como defecto del recolector para ejecuciones nuevas**. Las cuatro divergencias del ZIP Windows anterior permanecen documentadas como hallazgo histórico; no se alteraron sus bytes ni sus huellas para convertirlas retroactivamente en aprobaciones. El adjunto actual y el anterior se conservaron intactos.

La orden de creación de rama pegada por duplicado falló, y la siguiente orden creó correctamente la rama. El árbol preparado, el commit publicado y la limpieza final aportada acreditan la recuperación; ese incidente no deja un pendiente de integración.

## 5. Precedencia, límites y continuidad

Este documento sustituye como estado vigente el pendiente «corregir el recolector» del estado 1.4 y el pendiente «Windows corregido por confirmar» del paquete de preparación. Los resultados Linux bloqueados por falta de Chromium se conservan como tales; la evidencia nueva acredita el recorrido completo realizado por el autor en Windows.

La revisión independiente no ejecutó las pruebas en Windows ni hizo otra subida. La transcripción aporta un estado local limpio al cierre. Las comprobaciones remotas acreditan las referencias en el momento de la consulta, no garantizan que main no avance después.

Los estados actualizados y la auditoría se entregan por separado; no se afirma que estén incluidos en el commit revisado. Los documentos antiguos de preparación conservan su contexto histórico. Para continuar, usar este estado y comprobar nuevamente main.

El maestro 1.0 y los capítulos 1–6 mantienen su situación editorial: borradores pendientes de revisión del autor. Grok Build continúa sin sesión comercial acreditada. Persisten los límites de producto y documentación ya registrados, incluido el cotejo separado de evidencia histórica de Codex que no estuvo disponible. No se redactó el capítulo 7.

**Siguiente tarea recomendada:** preparar el encargo del capítulo 7 desde `6382e05846e149a9a72f7fdc56da48c37a873833`, conservar C01–C04, B01–B06, N01–N10, P01–P06 y W01–W06, y definir el siguiente incremento antes de implementarlo. La corrección de huellas ya no bloquea esa etapa.
