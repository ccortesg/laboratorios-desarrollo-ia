# Continuidad vigente · cierre del laboratorio 9 preparado

**Fecha:** 1 de noviembre de 2026. Estados vigentes de preparación: [libro 1.8.2](docs/estados/ESTADO_DEL_LIBRO_v1.8.2.md) y [repositorio 1.7.2](docs/estados/ESTADO_REPOSITORIO_v1.7.2.md). Incorporan como antecedente exacto la revisión 1.8.1/1.7.1. Maestro editorial 1.0 sin cambios; capítulos 1–9 pendientes de revisión del autor.

La ejecución funcional WSL fue auditada y aprobada sobre `251105483bc5bef040c57dc3a036d5bc3a7e0da0`. El cierre preserva íntegro ese contenido e incorpora [la revisión recibida](evidencia_integracion/revision_laboratorio_09_wsl/README.md). Las 805 ejecuciones y las pruebas 8/9/4 pertenecen a esa sesión anterior. En este cierre se comprobaron los 2.273 archivos de ese árbol, las 210 huellas declaradas y ocho pruebas nuevas del recolector con el runtime aislado; todas aprobaron.

**Operación autorizada vigente:** el autor invocó `PROMPT_CIERRE_LABORATORIO_09_v1.0.md` y autorizó commit, integración en main conservando avances y push atómico de main con únicamente `lab-09-v1.0` y `repositorio-v1.5`. Las restricciones de las preparaciones anteriores describen su momento y no cancelan este encargo expreso. La publicación sigue pendiente en este documento previo; commit, árbol documental y consultas posteriores se registran fuera del commit que acreditan, en `trabajo/cierre_lab09_wsl_20261101T231144Z/`.

No reaplicar el parche, forzar referencias, mover etiquetas históricas ni modificar código, pruebas, datos, distribuciones o evidencias anteriores. Los estados posteriores 1.8.3/1.7.3 y el comprobante confirmado sólo se emitirán según el resultado real. No redactar el capítulo 10.

## Antecedentes íntegros de preparación

El texto siguiente conserva las observaciones y restricciones de sus sesiones; la continuidad vigente es la que encabeza este documento.

# Continuidad vigente · laboratorio 9 preparado para revisión

**Fecha:** 1 de noviembre de 2026. Estados vigentes: [libro 1.8](docs/estados/ESTADO_DEL_LIBRO_v1.8.md) y [repositorio 1.7](docs/estados/ESTADO_REPOSITORIO_v1.7.md). El maestro editorial 1.0 sigue sin cambios y los capítulos 1–9 están pendientes de revisión del autor.

La base utilizada es `9212ee99b88f70f0b289837b88d6bbf34da91a52`, árbol `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0`. La reconsulta de GitHub a las 21:50:33 UTC del 1 de noviembre conservó main y las etiquetas lab-08-v1.0/repositorio-v1.4 en ese commit; las trece etiquetas siguen intactas. El cierre del 8 ya está confirmado. Se añaden sus estados posteriores 1.7.4/1.6.4 y la revisión externa exacta en `evidencia_integracion/cierre_laboratorio_08_confirmado/`.

El laboratorio 9 preserva la solución corregida del 8, sus 62 casos y el recorrido persistente real. Añade ocho criterios S con doce casos para validar la query HTTP y comprobar rechazo y recuperación. La propuesta pierde repeticiones antes de validarlas. La base falla nueve exigencias nuevas; la propuesta falla tres casos S02; la solución satisface 74/74. El alcance no incluye usuarios, permisos, exposición pública ni una auditoría productiva.

El autónomo final registró 27 baterías, 222 ejecuciones, 210 APROBADO, 12 FALLIDO didácticos y 54/54 huellas. El conjunto nuevo registró 92 baterías, 805 ejecuciones, 781 APROBADO, 24 FALLIDO previstos, 0 bloqueos, 48 NO EJECUTADO en baterías y diez ausentes aparte; 156/156 huellas. Las pruebas 8/9/4 de infraestructura se cuentan separadamente. El ZIP nuevo descomprimido reprodujo 222/210/12, conservando sus 292 archivos. Todo ello se ejecutó en Linux.

Los dos TimeoutExpired del primer autónomo se conservan como problemas reales del instrumento, no como fallos didácticos. La corrección S06 mantiene HTTP, DOM, controles y recuperación; S04.a verifica el cuerpo JSON. Los diagnósticos y la diferencia están incluidos. La causa interna completa de la espera no se atribuye a una versión del navegador.

La evidencia histórica de 583 ejecuciones Windows y el cierre posterior WSL del laboratorio 8 siguen separados. Las nuevas ejecuciones no autorizan una aprobación editorial ni acreditan sesiones comerciales. El recolector y sus ocho pruebas permanecen idénticos a la base; ninguna evidencia histórica se reescribe.

**Siguiente operación:** usar el paquete de integración y su prompt para Codex para aplicar y verificar localmente, conservando avances de main. Terminar con evidencia nueva para revisión. No crear commit, no integrar main, no crear ni mover etiquetas y no hacer push. `lab-09-v1.0` y `repositorio-v1.5` son únicamente nombres previstos. No redactar todavía el capítulo 10.

## Antecedentes conservados

Los textos siguientes mantienen sus fechas y estados originales. Sus pendientes de publicación del laboratorio 8 ya quedaron cerrados; no describen el estado vigente que encabeza este documento.

# Continuidad vigente · cierre del laboratorio 8

Estados de preparación: [libro 1.7.3](docs/estados/ESTADO_DEL_LIBRO_v1.7.3.md) y [repositorio 1.6.3](docs/estados/ESTADO_REPOSITORIO_v1.6.3.md). La ejecución corregida del autor en Windows es **APROBADO** y su [revisión completa](evidencia_integracion/cierre_laboratorio_08_windows/revision_recibida/REVISION_LABORATORIO_08_WINDOWS_v1.0.md) ya está incorporada. Los estados 1.7.2/1.6.2 se conservan como antecedentes de esa revisión.

El árbol Windows verificado es `9ea6109fe8e89a2785bdce255252ffaabea1d122`, sobre HEAD `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`. Este incremento sólo añade documentación y evidencia y actualiza referencias operativas; conserva el código, distribuciones y evidencia histórica. El árbol documental nuevo se registra en el paquete de cierre.

Se acreditan 65 baterías, 583 ejecuciones, 571 aprobaciones y doce fallos didácticos; cero bloqueos, 48 NO EJECUTADO y diez ausentes aparte. Huellas: 102/102 conjunto y 10/10 auxiliares. Las pruebas 8/4/9 se cuentan separadamente. Los resultados anteriores FALLIDO y BLOQUEADO siguen siendo antecedentes con su estado original.

El autor autorizó el commit, integración main y publicación de main con sólo `lab-08-v1.0` y `repositorio-v1.4`, sin forzar referencias. La primera etiqueta corresponde a la publicación inicial del laboratorio 8 con distribución técnica 1.0.1. La publicación continúa pendiente hasta verificar las referencias reales. Después se generarán los estados 1.7.4/1.6.4 observados en el ZIP de cierre; no se insertan anticipadamente en el commit que acreditan.

Si main avanza, conservarlo y revisar los cambios. Si cambia código, la evidencia funcional anterior por sí sola no acredita ese código nuevo. Los manuscritos 1–8 siguen pendientes de revisión editorial. El maestro permanece en 1.0 y el capítulo 9 queda fuera del cierre.

## Antecedentes conservados

Los textos siguientes conservan sus estados y fechas históricos. Sus pendientes de ejecución Windows del laboratorio 8 quedaron resueltos por la revisión incorporada arriba; no describen la continuidad vigente.

# Continuidad vigente · corrección SQLite del laboratorio 8

Estados vigentes: [libro 1.7.1](docs/estados/ESTADO_DEL_LIBRO_v1.7.1.md) y [repositorio 1.6.1](docs/estados/ESTADO_REPOSITORIO_v1.6.1.md). La ejecución Windows original del laboratorio 8 resultó FALLIDO por conexiones de prueba sin cerrar; su auditoría y captura se conservan. La distribución 1.0.1 corrige ese soporte y añade cuatro regresiones, sin cambiar contratos ni estados de aplicación. La nueva ejecución Windows sigue pendiente.

La integración continúa en una rama local con cambios preparados, sin commit, main, etiquetas nuevas ni push. Usa el paquete correctivo sobre el árbol preparado 2ea01dea2aa0c8907eba54ef65efcb44d547b9d7; los resultados y el árbol posterior están en su BASE_CORRECCION.json y evidencia. Maestro editorial 1.0 y manuscritos sin cambios; revisión del autor pendiente.

## Antecedentes conservados de preparación v1.0

# Continuidad vigente · Integración 1.4 preparada para revisión

**Fecha:** 1 de noviembre de 2026, UTC. Estados vigentes: [libro 1.7](docs/estados/ESTADO_DEL_LIBRO_v1.7.md) y [repositorio 1.6](docs/estados/ESTADO_REPOSITORIO_v1.6.md). Maestro editorial 1.0 sin cambios. Los capítulos 1–8 siguen pendientes de revisión del autor.

## Cierre del laboratorio 7 conservado

La ejecución Windows del autor y la publicación del laboratorio 7 están confirmadas. Los estados 1.6.2 y 1.5.2, recuperados de la entrega separada, prevalecen sobre pendientes históricos. Su cierre se incorpora bajo `evidencia_integracion/cierre_laboratorio_07_confirmado/`, sin modificar sus archivos.

GitHub se consultó el 31 de octubre de 2026 a las 23:47:03 UTC: main, lab-07-v1.0 y repositorio-v1.3 apuntaban a `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`, árbol `b123b5969e8077ba0cb3c4eedc9b348f94294652`. Se conservaron las once etiquetas. Esa base contiene la corrección del recolector.

## Incremento nuevo y evidencia

El laboratorio 8 añade persistencia explícita y el recorrido CSV→importador CLI→SQLite en archivo→HTTP→navegador. Conserva 51 casos anteriores; ocho criterios D añaden once casos. La propuesta omite transmitir la conexión y falla exactamente D03, D04, D05 y D08.a. La solución aprueba 62/62. El diagnóstico del origen efectivo existe en ambos estados y se comprueba por separado de la corrección funcional.

El laboratorio se ejecutó con navegador: 21 baterías, 175 ejecuciones, 171 aprobaciones, cuatro fallos didácticos, cero bloqueos y once NO EJECUTADO de base; 38/38 huellas finales. El pase desde un ZIP nuevo descomprimido reprodujo el resultado y conservó sus 142 archivos.

El conjunto nuevo de ocho laboratorios registró APROBADO: 65 baterías, 583 ejecuciones, 571 aprobaciones, doce fallos didácticos, cero bloqueos, 48 NO EJECUTADO en baterías y diez criterios ausentes aparte. Coincidieron 102/102 huellas finales. Las ocho pruebas del recolector y nueve pruebas focales del evaluador se contabilizan por separado. La evidencia está en `evidencia_integracion/laboratorio_08_v1.0/`; no sustituye los registros históricos.

La producción y la prueba del parche son Linux. Windows del laboratorio 8, herramientas comerciales, Actions, producción, concurrencia, carga y el reto comparador están NO EJECUTADO. Cambiar el directorio de trabajo no equivale a cambiar de sistema operativo.

## Siguiente operación autorizada en esta preparación

El paquete `INTEGRACION_LABORATORIO_08_v1.0.zip` permite verificar, aplicar y probar sobre una rama local de Windows. Su `BASE_INTEGRACION.json` registra el árbol preparado y la huella del parche; las instrucciones conservan avances posteriores de main y terminan con evidencia nueva para revisión.

No se creó commit, no se integró main, no se crearon ni movieron etiquetas y no se hizo push en esta producción. `lab-08-v1.0` y `repositorio-v1.4` son sólo nombres previstos. La siguiente tarea es revisar la aplicación y ejecución Windows antes del cierre. El capítulo 9 permanece fuera de alcance.

## Antecedentes íntegros

El texto siguiente conserva los estados tal como se documentaron. Sus pendientes de Windows y publicación del laboratorio 7 ya quedaron cerrados por los estados vigentes indicados arriba.

# Continuidad histórica · Integración 1.3 preparada

**Fecha:** 31 de octubre de 2026. El maestro editorial v1.0 sigue vigente. Los estados actuales son [ESTADO_DEL_LIBRO_v1.6.md](docs/estados/ESTADO_DEL_LIBRO_v1.6.md) y [ESTADO_REPOSITORIO_v1.5.md](docs/estados/ESTADO_REPOSITORIO_v1.5.md). Los capítulos 1–7 permanecen pendientes de revisión editorial del autor.

## Cierres anteriores confirmados

El laboratorio 6 ya fue integrado y verificado en Windows por el autor. Las etiquetas lab-06-v1.0 y repositorio-v1.2 conservan el commit 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd. La corrección del recolector fue integrada después: main está confirmado en 6382e05846e149a9a72f7fdc56da48c37a873833, árbol 680fa6135ed0aae40e962ec3f893d72ece1389c1.

H01 está cerrado para ejecuciones nuevas. La evidencia Windows corregida acreditó 34/34 huellas finales; las divergencias del registro anterior se conservan como antecedentes. La producción del laboratorio 7 parte del recolector corregido. Las notas antiguas de subida del laboratorio 6 o de corrección pendiente no describen el estado vigente.

## Incremento preparado

El laboratorio 7 añade importación CSV de existencias absolutas, validación completa, aplicación transaccional y consulta sobre la misma conexión. Conserva C/B/N/P/W y añade I01–I08 con diecisiete casos. El defecto didáctico de propuesta suma cantidades y produce exactamente los fallos I01 e I07.

La ejecución autónoma con navegador obtuvo APROBADO: quince baterías, 136 ejecuciones, 134 aprobaciones y dos fallos didácticos; diecisiete casos I de base NO EJECUTADO. La solución satisfizo 51/51 casos y coincidieron 30/30 huellas.

La verificación conjunta local obtuvo APROBADO: 44 baterías, 408 ejecuciones, 400 aprobaciones, ocho fallos didácticos y cero bloqueos; 37 NO EJECUTADO en baterías y diez criterios ausentes aparte. Coincidieron 64/64 huellas finales. La evidencia nueva está en evidencia_integracion/laboratorio_07_v1.0/ y no sustituye registros históricos.

## Siguiente operación

La integración 1.3 está preparada localmente. Windows para laboratorio 7, la integración en main, la subida y las etiquetas nuevas están NO EJECUTADO. Los nombres previstos son lab-07-v1.0 y repositorio-v1.3. Antes de aplicarla, comprobar de nuevo main, preservar cambios y seguir las instrucciones del paquete. No se requiere volver a aplicar la corrección del recolector.

El capítulo 7 y su Word forman parte de la entrega editorial. No se acredita una nueva sesión comercial mediante estas pruebas ni se redactó el capítulo 8.

## Antecedentes conservados

El contenido siguiente conserva sus fechas, resultados y pendientes históricos. No sustituye las actualizaciones anteriores ni permite atribuir al laboratorio 7 una ejecución Windows previa.

# Continuidad vigente · Integración 1.2 preparada

**Fecha: 31 de octubre de 2026 (UTC).** El maestro editorial v1.0 permanece vigente. El estado del libro es v1.5 y el estado operativo del repositorio es v1.3; estas versiones son independientes de la integración técnica 1.2.

## Observaciones posteriores al cierre de la integración 1.1

**Integración remota del laboratorio 5: APROBADO.** Se volvieron a consultar las referencias del repositorio autorizado: `main`, `lab-05-v1.0` y `repositorio-v1.1` apuntan a `67edef7b44524f5f621e9b060c6b9c523c1b05a8`, árbol `a1d70872f969886c5f33f88692b61e90579a18ed`. Ese es el punto de partida de esta entrega. Las cinco etiquetas anteriores conservan su commit original. Las notas antiguas de subida pendiente no describen el estado vigente.

**Ejecución Windows aportada por el autor: APROBADO en el alcance observado.** La captura muestra Python 3.11.9 y el verificador de los laboratorios 1–5 con 17 baterías, 178 ejecuciones, 173 aprobaciones y cinco fallos intencionales. También registra 12 NO EJECUTADO en baterías y diez N ausentes aparte. No se presenta como ejecución realizada por el editor, como certificación general de Windows ni como prueba del laboratorio 6. La captura original no se incorpora a los materiales publicables porque contiene identificadores del entorno del autor.

## Incremento de esta entrega

El laboratorio 6 está completo: añade formulario, adaptador HTTP y representación del resumen real. Conserva los cuatro artículos y C/B/N/P; incorpora W01–W06 con ocho casos. La ejecución Linux con navegador obtuvo 94 ejecuciones, 93 aprobaciones y un fallo intencional W05 en propuesta; ocho casos web de base NO EJECUTADO. La solución satisfizo 34/34. La evidencia nueva no sustituye los registros históricos.

La verificación conjunta de esta integración obtuvo APROBADO, salida 0: 29 baterías, 272 ejecuciones, 266 aprobaciones y seis fallos didácticos; 20 NO EJECUTADO en baterías y diez N ausentes aparte. Una extracción nueva del ZIP reprodujo el patrón 94/93/1 del laboratorio 6. Los registros están en `evidencia_integracion/laboratorio_06_v1.0/COMPROBACION.json` y sus subdirectorios.

El capítulo 6 y su Word permanecen fuera del repositorio técnico. Los capítulos 1–6 siguen pendientes de revisión editorial del autor. El reto de limpiar la búsqueda no se implementó. No se redactó el capítulo 7.

**Acceso utilizable a Grok Build: BLOQUEADO. Interacciones comerciales: NO EJECUTADO.** Se inspeccionaron los accesos disponibles sin enviar prompts al servicio. El código y las comprobaciones son locales. Los ejemplos del laboratorio no constituyen sesiones de Grok Build.

La integración 1.2 se prepara y verifica en una copia aislada. GitHub se utilizó solo para lectura. No se hizo push ni se crearon ramas, pull requests o etiquetas remotas. Las etiquetas nuevas previstas son `lab-06-v1.0` y `repositorio-v1.2`, únicamente después de revisar y aplicar el cambio. Las instrucciones exactas están en el paquete de integración entregado por separado.

Siguiente paso: aplicar el parche en una rama local, ejecutar el verificador completo con navegador en Windows, revisar el cambio y realizar la subida como operación posterior. Conservar la evidencia de esa ejecución como nueva observación. La revisión del autor debe centrarse en voz, profundidad técnica y utilidad práctica.

## Antecedente conservado de la integración 1.1

El texto siguiente conserva la situación y las observaciones anteriores. Sus pendientes de subida y Windows quedaron complementados por las observaciones vigentes de arriba; no se reinterpretan sus ejecuciones originales.

# Continuidad de los laboratorios

**Fecha:** 30 de octubre de 2026 · **Integración:** 1.1.

## Punto de partida

Se conservan los laboratorios 1, 2 y 3 v1.0 y el laboratorio 4 v1.1; se incorpora el laboratorio 5 v1.0. Los cinco ZIP originales se conservan en `distribuciones/`. Los 198 archivos visibles coinciden byte a byte con esos paquetes; `PROCEDENCIA.json` identifica cada huella. La incorporación al repositorio no modifica los originales del libro.

El documento maestro editorial v1.0 sigue vigente. El estado editorial más reciente es `ESTADO_DEL_LIBRO_v1.4.md`, conservado con las entregas editoriales. Los capítulos 1–5 continúan pendientes de revisión del autor. El capítulo 5 y su Word están completos en las entregas editoriales; no se redactó el capítulo 6.

## Decisiones de integración

- Un repositorio general con los cinco laboratorios visibles, instrucciones comunes y evidencia trazable.
- El manuscrito y sus Word permanecen en el flujo editorial. Aquí se reúne lo necesario para ejecutar, revisar y continuar los laboratorios.
- Datos sintéticos, Python estándar, SQLite en memoria y Git. Esto no determina el stack de la aplicación futura del libro.
- El Git del laboratorio 4 se conserva mediante un bundle autónomo. La copia de práctica se crea en `trabajo/`, ignorada por el Git general. Las etiquetas `inicio` y `solucion` mantienen sus identificadores.
- Evidencias históricas importadas sin alterar; cada ejecución nueva tiene su propia carpeta.
- Preparación para repositorio privado; licencia pública pendiente. Los materiales no se publican abiertamente por esta decisión.
- Automatización local con un comando común. No se configura ni se presenta como ejecutada una batería de GitHub Actions.

## Verificación histórica de la primera integración

Comando observado desde la raíz:

```bash
python3 herramientas/verificar_todo.py --salida trabajo/verificacion_inicial
```

**APROBADO**, código 0. Evidencia nueva: [resumen](evidencia_integracion/2026-10-30/resumen.json), [entorno](evidencia_integracion/2026-10-30/entorno.json) y [registro de integración](evidencia_integracion/2026-10-30/EJECUCION.json).

Entorno observado: Linux, CPython 3.12.14, SQLite 3.53.1 y Git 2.51.1. Once baterías, 106 ejecuciones: 103 aprobaciones y tres fallos intencionales exactos. C04 falla en el inicial del laboratorio 1; B05 y B06 fallan en el defecto del laboratorio 3. No se detectaron fallos funcionales inesperados.

Seis criterios B01–B06 en la base del laboratorio 3 permanecen **NO EJECUTADO**. N01–N10 no existen en `inicio` del laboratorio 4 y se registran aparte como **NO EJECUTADO**. Las referencias del laboratorio 4 obtuvieron diez y veinte aprobaciones; el árbol actual recién reconstruido obtuvo veinte.

Las herramientas también se comprobaron sobre copias de ensayo: rechazo de destinos ocupados sin alterar su contenido, detección de desacuerdo entre instantánea y bundle, y propagación de un fallo adicional ajeno al patrón didáctico. Son comprobaciones de integración, no nuevos criterios de negocio.

La revisión de confidencialidad de los insumos y los nuevos resultados no encontró detalles identificables en el alcance inspeccionado. No equivale a una garantía universal ni a una evaluación de seguridad productiva.

## Verificación de la integración 1.1

El comando común ahora incluye los cinco laboratorios. La comprobación local del parche
se documenta en `evidencia_integracion/laboratorio_05_v1.0/COMPROBACION.json`, con su
procedencia, comandos y resultados. No acredita una ejecución en Windows ni uso de Copilot.

El patrón esperado es 17 baterías y 178 ejecuciones: 173 APROBADO y cinco FALLIDO didácticos.
Los seis P de la base 5 se suman a los seis B omitidos de base 3; los diez N ausentes de
la referencia inicio del laboratorio 4 siguen fuera de las baterías. La solución del laboratorio 5 satisface 26/26.

Los materiales y la evidencia importados del laboratorio 5 conservan sus bytes y su
contexto histórico, incluso cuando describen su integración remota como pendiente.
La copia del lector y sus resultados deben permanecer en `trabajo/`.

## Evidencia de Codex que permanece delimitada

El informe saneado recibido describe una sesión de Codex desktop con Bash en Linux sobre la solución existente. Declara resultados funcionales aprobados y 17 diferencias de modos preexistentes, conservadas; no atribuye a Codex la implementación original. La revisión documental v1.1 permanece en el laboratorio 4.

**BLOQUEADO:** cotejo de `evidencia_codex_04_20261030/`, porque esa carpeta no se recibió. Las pruebas nuevas de integración no acreditan los comandos de aquella sesión ni explican el origen de sus diferencias de modos.

**NO EJECUTADO en esta integración:** una nueva sesión de Codex, Copilot o Grok Build; Windows nativo; GitHub Actions; los retos opcionales. La subida a un servidor, si se realiza, debe acreditarse mediante su URL y commit remoto; los resultados locales anteriores no la demuestran por sí mismos.

## Pendientes y siguiente trabajo

El alojamiento privado del repositorio general ya quedó acreditado en ESTADO_REPOSITORIO_v1.2.md. Esta actualización se prepara localmente; su subida debe contrastarse con el commit remoto después de ejecutarla. La nueva evidencia Codex auditada es distinta de la carpeta histórica faltante; puede cerrarse ese pendiente si se aportan sus registros. La revisión del autor debe evaluar voz, profundidad técnica y utilidad práctica de los borradores.

El capítulo 5 y su laboratorio están terminados para revisión. La nueva función resume el catálogo y añade una terminal JSON; conserva C01–C04, B01–B06 y N01–N10, y agrega P01–P06. Copilot quedó BLOQUEADO por falta de interfaz invocable en su producción; las interacciones comerciales siguen NO EJECUTADO. La implementación y las pruebas fueron locales.

El siguiente contenido del índice es el capítulo 6, que requiere un nuevo encargo. No se presupone aprobación de los borradores anteriores.

Para cualquier siguiente sesión, lee `README.md`, `AGENTS.md`, este documento y el contexto del laboratorio pertinente. Registra qué versión utilizas y qué evidencia recibiste; no presupongas aprobaciones o ejecuciones ausentes.
