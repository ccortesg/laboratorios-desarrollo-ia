# Revisión del verificador común del laboratorio 9

**Estado de esta revisión:** APROBADO, dentro del alcance descrito.  
**Fecha efectiva:** 1 de noviembre de 2026.  
**Naturaleza:** lectura del cambio y cotejo con las ejecuciones ya conservadas; esta revisión no añade ejecuciones funcionales.

## Cambio revisado

`herramientas/verificar_todo.py` incorpora el laboratorio 9 y sus dos baterías de seguridad, conserva las baterías heredadas y exige el patrón exacto por identificador, estado, cantidad y código de salida. Los casos FALLIDO admitidos deben conservar `AssertionError`; una excepción de infraestructura no acredita el defecto didáctico. Un bloqueo permitido permanece BLOQUEADO y la ausencia de navegador conserva NO EJECUTADO global.

El estado base del laboratorio 9 ejecuta todos los contratos heredados sobre la solución corregida del laboratorio 8. Sus nueve fallos de seguridad y los tres de la propuesta se declaran expresamente; no se añaden excepciones a las listas de los laboratorios anteriores.

La revisión del diff no encontró cambios en los contratos históricos ni en el cierre de huellas. El recolector `herramientas/huellas_evidencia.py` y sus ocho pruebas son idénticos a la base `9212ee99b88f70f0b289837b88d6bbf34da91a52`. El cotejo Git de los laboratorios 1–8 y `historiales/` no mostró archivos modificados.

## Evidencia observada

La ejecución nueva completa terminó con código 0 entre `2026-11-01T21:42:50.523037+00:00` y `2026-11-01T21:44:04.998326+00:00`. Su comprobador de huellas también terminó con código 0.

| Alcance | Resultado observado |
|---|---|
| Conjunto funcional 1–9 | 92 baterías; 805 ejecuciones; 781 APROBADO; 24 FALLIDO didácticos; 0 BLOQUEADO |
| Casos sin ejecutar | 48 NO EJECUTADO en baterías; 10 criterios ausentes registrados aparte |
| Huellas funcionales declaradas | 156/156 coincidentes con los bytes finales |
| Capturas externas del conjunto y sus huellas | 4/4 coincidentes |
| Ocho pruebas originales del recolector | 8/8 aprobadas; código 0; 2/2 huellas |
| Nueve regresiones nuevas del evaluador | 9/9 aprobadas; código 0; 2/2 huellas |

Las pruebas del evaluador rechazan fallos inesperados, excepciones que suplanten aserciones, casos ausentes o duplicados, totales inventados y declaraciones de aprobación incompatibles con un bloqueo o con la ausencia de navegador. Estas pruebas son infraestructura y no se suman a las 805 ejecuciones funcionales.

Los nueve laboratorios declararon conservación de su referencia original. Las 63 fuentes registradas por la captura externa seguían idénticas al terminar. El subconjunto 1–8 de esta ejecución Linux obtuvo 583 ejecuciones, 571 aprobaciones y 12 fallos didácticos; su coincidencia con las cifras históricas de Windows no cambia la procedencia de ninguno de los registros.

## Ubicación y límites

Los resultados funcionales completos están en `conjunto_09_01/`; sus comandos, tiempos, códigos, entorno y fuentes están en `captura_conjunto_09_01/`. Las comprobaciones de infraestructura permanecen separadas en `recolector_09/` y `evaluador_09/`.

Esta revisión no prueba Windows, no equivale a una auditoría general de seguridad, no publica cambios y no aprueba editorialmente el manuscrito. Los ensayos del ZIP autónomo y del parche final corresponden a comprobaciones separadas de la entrega.
