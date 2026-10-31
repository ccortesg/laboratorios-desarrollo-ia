# Corrección del recolector de evidencia

**Fecha:** 31 de octubre de 2026 (UTC). **Versión del cambio:** 1.0.

## Problema y alcance

La integración del laboratorio 6 quedó publicada en el commit
`31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd`. Su ejecución completa en Windows fue
aportada y auditada: 29 baterías, 272 ejecuciones, 266 aprobaciones, seis fallos
didácticos y cero bloqueos. El estado operativo que registra ese cierre es
`ESTADO_REPOSITORIO_v1.4.md`, entregado por separado; prevalece sobre las notas
históricas de preparación que quedaron dentro de la distribución.

La auditoría detectó cuatro huellas históricas de stdout que coinciden sólo tras
normalizar CRLF a LF. El verificador conjunto reescribía textos para sanear rutas
después de calcular las huellas. La conversión implícita de saltos y cualquier
sustitución de rutas podían cambiar los bytes sin actualizar sus hashes.

Este incremento corrige únicamente el cierre de evidencia nueva. Los laboratorios
1–6, sus reglas C/B/N/P/W, distribuciones, evidencias históricas y etiquetas
permanecen intactos. No cambia la aplicación ni se redacta el capítulo 7.

## Contrato del cierre nuevo

1. Antes de escribir, las huellas de captura deben coincidir con los archivos
   recibidos. Una discrepancia se declara FALLIDO; no se recalcula para ocultarla.
2. Se sanean textos UTF-8 mediante lectura y escritura de bytes. LF y CRLF se
   conservan si no hay una sustitución explícita necesaria.
3. `sha256_stdout_capturado` y `sha256_stderr_capturado` conservan las huellas de
   captura. `sha256_stdout` y `sha256_stderr` identifican los bytes finales saneados.
4. Las convenciones del productor se conservan por separado; las vigentes explican
   el posprocesamiento de integración. Los resultados, estados, códigos y criterios
   conservan su significado.
5. Los registros sin salidas no adquieren archivos ni hashes. Las referencias deben
   ser nombres simples dentro de su carpeta; no se aceptan rutas ni enlaces.
6. El verificador conjunto sigue exigiendo una carpeta de salida nueva. La CLI de
   comprobación de huellas es de lectura y no repara evidencia antigua.

## Comprobaciones para una copia del lector

Desde la raíz del repositorio:

```bash
python -m unittest discover -s herramientas/pruebas -p test_huellas_evidencia.py -v
python herramientas/verificar_todo.py --navegador --salida trabajo/correccion_huellas_windows_01
python herramientas/huellas_evidencia.py trabajo/correccion_huellas_windows_01 --esperadas 34
```

Expectativas: ocho pruebas específicas OK; verificación conjunta APROBADO con
272/266/6 y cero bloqueos; 34/34 huellas APROBADO. Los seis fallos didácticos siguen
siendo C04 del inicial 1, B05/B06 del defecto 3, P04/P05 de propuesta 5 y W05 de
propuesta 6. Hay 20 NO EJECUTADO en baterías y diez N ausentes aparte.

La preparación local acreditó las ocho pruebas y una regresión sintética que falla
con el bucle antiguo y aprueba con el nuevo. Una prueba de bytes CRLF en Linux no
es una ejecución Windows. La descarga de Chromium devolvió una página de sitio
no disponible en el entorno de preparación; la comprobación completa con navegador
corregida en Windows queda pendiente de la ejecución nueva del autor. El paquete
de corrección registra los comandos efectivamente realizados y sus límites.

## Continuidad y conservación

La verificación histórica de Windows permanece conservada con sus discrepancias
de huellas documentadas. Cada ejecución nueva usa otro directorio. La corrección
se integra mediante un commit nuevo de main; `lab-06-v1.0` y `repositorio-v1.2`
siguen identificando la entrega original, sin mover ni forzar etiquetas.

El maestro editorial 1.0 y los capítulos 1–6 continúan pendientes de revisión del
autor. Una ejecución local no acredita una sesión de Grok Build ni de otra
herramienta comercial.

Fuentes de semántica técnica consultadas el 31 de octubre de 2026 UTC:
[Python 3.11, Path.read_bytes/write_bytes](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path.write_bytes),
[Git merge --ff-only](https://git-scm.com/docs/git-merge) y
[Git push --no-follow-tags](https://git-scm.com/docs/git-push).
