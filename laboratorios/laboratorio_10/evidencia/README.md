# Cómo leer la evidencia del laboratorio 10

Las carpetas conservan ejecuciones diferentes. Sus resultados no se suman para declarar una cobertura mayor. El entorno efectivo de esta producción fue Linux, Python 3.12.14 y SQLite 3.53.1; el navegador real fue Chromium 151 con Playwright 1.62.1 y Node 24.22.1. No se acredita una ejecución Windows ni una sesión comercial de agente.

## Desarrollo inicial: `desarrollo_01`

Se ejecutaron las focales T contra base, propuesta y solución antes de la aclaración final de infraestructura. Son 16 ejecuciones funcionales: 15 aprobaciones y el fallo didáctico T02; los ocho T de base están NO EJECUTADO. Hay seis comandos de prueba y recibos anidados de operaciones reales. Las 66/66 huellas de capturas coinciden. El manifiesto de fuentes identifica aquella versión; se conserva sin recalcularlo para atribuirle una versión posterior.

Esta fase detectó el defecto intencional de continuación. No es el registro de ejecución completa de la entrega.

## Infraestructura focal: `infraestructura_01`

RO01 inyecta una imposibilidad de iniciar el hijo. Es un método unittest con dos estados, no dos criterios nuevos: debe conservar BLOQUEADO/código 2 y consulta NO EJECUTADO, sin inventar capturas. El resultado observado es `Ran 1 test`, `OK`, código 0 y 2/2 huellas de las salidas de la prueba. La inyección es explícita; no se presenta como una incidencia histórica del equipo del autor.

## Ejecución autónoma completa: `ejecucion_local`

La ejecución completa se realizó después de la corrección del tratamiento de BLOQUEADO. `resumen.json` registró APROBADO el 2 de noviembre de 2026 UTC: 33 baterías, 238 ejecuciones, 237 aprobaciones, un fallo didáctico T02 en propuesta, cero bloqueos y ocho NO EJECUTADO en base. La solución aprobó sus 82 casos. Las 116/116 huellas de salidas coinciden con los bytes finales.

El recorrido T08 ejecutó el operador mediante un proceso real mientras un mismo servidor atendía la misma SQLite. Se comprobaron las respuestas HTTP y la presentación en Chromium. Los recibos conservados permiten seguir el CSV utilizado, el importador, la consulta y los códigos de cada paso.

La carpeta incluye entorno, comandos, resultados por batería, recibos de las operaciones y huellas de fuentes. Su comprobador valida exactamente los fallos didácticos definidos. FALLIDO permanece en T02 de propuesta; la aprobación del recorrido no elimina ni renombra ese fallo.

La verificación común de los laboratorios 1–10, las ocho pruebas del recolector y las auditorías de integración pertenecen al paquete de integración, no al total autónomo. Las ejecuciones históricas de Windows y los cierres posteriores desde WSL se conservan en la documentación operativa; no se reclasifican como ejecuciones de este laboratorio.

## Comprobación de las huellas

Desde la carpeta del laboratorio:

```bash
python -B soporte/huellas_evidencia.py evidencia/ejecucion_local
```

Esta orden es de lectura. Comprueba las huellas declaradas en los registros de comandos; no atribuye autoría, no audita todos los requisitos ni cambia la evidencia. Una nueva ejecución debe guardarse en una carpeta distinta de `evidencia/` y de los recibos anteriores.
