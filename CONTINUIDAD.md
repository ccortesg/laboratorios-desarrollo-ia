# Continuidad de los laboratorios

**Fecha:** 30 de octubre de 2026 · **Integración:** 1.0.

## Punto de partida

Se importaron los laboratorios 1, 2 y 3 v1.0 y el laboratorio 4 v1.1. Los cuatro ZIP originales se conservan en `distribuciones/`. Los 120 archivos visibles coinciden byte a byte con esos paquetes; `PROCEDENCIA.json` identifica cada huella. La incorporación al repositorio no modifica los originales del libro.

El documento maestro editorial v1.0 sigue vigente. El estado editorial más reciente es `ESTADO_DEL_LIBRO_v1.3.1.md`, conservado con las entregas editoriales. Los capítulos 1–4 continúan pendientes de revisión del autor; no se escribió el capítulo 5.

## Decisiones de integración

- Un repositorio general con los cuatro laboratorios visibles, instrucciones comunes y evidencia trazable.
- El manuscrito y sus Word permanecen en el flujo editorial. Aquí se reúne lo necesario para ejecutar, revisar y continuar los laboratorios.
- Datos sintéticos, Python estándar, SQLite en memoria y Git. Esto no determina el stack de la aplicación futura del libro.
- El Git del laboratorio 4 se conserva mediante un bundle autónomo. La copia de práctica se crea en `trabajo/`, ignorada por el Git general. Las etiquetas `inicio` y `solucion` mantienen sus identificadores.
- Evidencias históricas importadas sin alterar; cada ejecución nueva tiene su propia carpeta.
- Preparación para repositorio privado; licencia pública pendiente. Los materiales no se publican abiertamente por esta decisión.
- Automatización local con un comando común. No se configura ni se presenta como ejecutada una batería de GitHub Actions.

## Verificación efectivamente realizada

Comando observado desde la raíz:

```bash
python3 herramientas/verificar_todo.py --salida trabajo/verificacion_inicial
```

**APROBADO**, código 0. Evidencia nueva: [resumen](evidencia_integracion/2026-10-30/resumen.json), [entorno](evidencia_integracion/2026-10-30/entorno.json) y [registro de integración](evidencia_integracion/2026-10-30/EJECUCION.json).

Entorno observado: Linux, CPython 3.12.14, SQLite 3.53.1 y Git 2.51.1. Once baterías, 106 ejecuciones: 103 aprobaciones y tres fallos intencionales exactos. C04 falla en el inicial del laboratorio 1; B05 y B06 fallan en el defecto del laboratorio 3. No se detectaron fallos funcionales inesperados.

Seis criterios B01–B06 en la base del laboratorio 3 permanecen **NO EJECUTADO**. N01–N10 no existen en `inicio` del laboratorio 4 y se registran aparte como **NO EJECUTADO**. Las referencias del laboratorio 4 obtuvieron diez y veinte aprobaciones; el árbol actual recién reconstruido obtuvo veinte.

Las herramientas también se comprobaron sobre copias de ensayo: rechazo de destinos ocupados sin alterar su contenido, detección de desacuerdo entre instantánea y bundle, y propagación de un fallo adicional ajeno al patrón didáctico. Son comprobaciones de integración, no nuevos criterios de negocio.

La revisión de confidencialidad de los insumos y los nuevos resultados no encontró detalles identificables en el alcance inspeccionado. No equivale a una garantía universal ni a una evaluación de seguridad productiva.

## Evidencia de Codex que permanece delimitada

El informe saneado recibido describe una sesión de Codex desktop con Bash en Linux sobre la solución existente. Declara resultados funcionales aprobados y 17 diferencias de modos preexistentes, conservadas; no atribuye a Codex la implementación original. La revisión documental v1.1 permanece en el laboratorio 4.

**BLOQUEADO:** cotejo de `evidencia_codex_04_20261030/`, porque esa carpeta no se recibió. Las pruebas nuevas de integración no acreditan los comandos de aquella sesión ni explican el origen de sus diferencias de modos.

**NO EJECUTADO en esta integración:** una nueva sesión de Codex, Copilot o Grok Build; Windows nativo; GitHub Actions; los retos opcionales. La subida a un servidor, si se realiza, debe acreditarse mediante su URL y commit remoto; los resultados locales anteriores no la demuestran por sí mismos.

## Pendientes y siguiente trabajo

Primero, completar y acreditar el alojamiento privado del repositorio general. Después, aportar y contrastar los registros faltantes de Codex si se desea cerrar ese pendiente documental. La revisión del autor debe evaluar voz, profundidad técnica y utilidad práctica de los borradores.

La siguiente entrega de contenido prevista es el capítulo 5, «GitHub Copilot: de la sugerencia al trabajo delegado». Partirá de la solución del laboratorio 4, conservará C01–C04, B01–B06 y N01–N10 y definirá un incremento pequeño antes de implementarlo. Verificará el acceso real a Copilot y consultará documentación oficial vigente. Esa entrega todavía no comenzó.

Para cualquier siguiente sesión, lee `README.md`, `AGENTS.md`, este documento y el contexto del laboratorio pertinente. Registra qué versión utilizas y qué evidencia recibiste; no presupongas aprobaciones o ejecuciones ausentes.
