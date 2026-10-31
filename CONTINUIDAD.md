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
