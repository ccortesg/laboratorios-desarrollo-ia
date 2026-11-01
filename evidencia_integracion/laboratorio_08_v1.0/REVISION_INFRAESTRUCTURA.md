# Revisión de la infraestructura común para el laboratorio 8

**Resultado:** APROBADO. La modificación se limita a `herramientas/verificar_todo.py`; el recolector y sus ocho pruebas conservan exactamente los bytes de la base.

## Cambio revisado

El verificador común incorpora las siete baterías de cada estado del laboratorio 8: heredados, resumen, HTTP, navegador, integración CSV, depuración entre procesos y depuración en navegador. Conserva las expectativas de C/B/N/P/W/I y evalúa los nuevos casos D por identificador, estado, código de salida y tipo de error.

Los únicos fallos nuevos admitidos son D03, D05 y D08.a en `propuesta_depuracion`, y D04 en `propuesta_depuracion_navegador` cuando se ejecuta el navegador. Los casos conservan FALLIDO; la aprobación del recorrido significa que se observó exactamente el patrón didáctico acordado.

La batería D permite registrar un impedimento del servidor en D02, D03, D05 o D08.a mientras las comprobaciones CLI independientes se completan. Esta posibilidad sólo se habilita para esa batería del laboratorio 8. Un bloqueo parcial mantiene BLOQUEADO en la evaluación y nunca oculta otro fallo. Las baterías anteriores conservan su política. Un registro con casos ejecutados debe conservar su código de salida; no se admite `None` para el bloqueo parcial.

## Verificación funcional observada

La ejecución conjunta completa con navegador terminó con código **0** y estado **APROBADO**. El entorno fue Linux; no se ejecutó Windows. Los registros de fecha y hora UTC están en `COMANDO_CONJUNTO_01.json`.

| Medida | Conjunto 1–8 | Subconjunto conservado 1–7 |
| --- | ---: | ---: |
| Baterías | 65 | 44 |
| Ejecuciones funcionales | 583 | 408 |
| APROBADO | 571 | 400 |
| FALLIDO didácticos | 12 | 8 |
| BLOQUEADO | 0 | 0 |
| NO EJECUTADO en baterías | 48 | 37 |

Diez criterios ausentes de la referencia inicial del laboratorio 4 continúan registrados aparte. El laboratorio 8 aporta 21 baterías y 175 ejecuciones: 171 aprobaciones, cuatro fallos previstos y once casos D de la base NO EJECUTADO. La solución satisface 62 casos, incluidos sus 51 heredados.

Los ocho fallos históricos mantienen sus identificadores: C04 del inicial 1; B05/B06 del defecto 3; P04/P05 de la propuesta 5; W05 de la propuesta 6; I01/I07 de la propuesta 7. No apareció ningún fallo adicional fuera de ese patrón y de los cuatro D declarados.

La comparación de fuentes antes y después de ejecutar indicó conservación de las ocho referencias. `git diff HEAD` confirmó que los laboratorios 1–7, `huellas_evidencia.py` y `test_huellas_evidencia.py` permanecían sin modificaciones.

## Integridad y pruebas del evaluador

El cierre del verificador comprobó **102/102 huellas finales stdout/stderr**. Después se calculó el número de referencias declaradas en los archivos de comandos y se ejecutó el comprobador de sólo lectura con ese número: 102 coincidencias, salida 0. No se fijó una cantidad heredada como total del conjunto nuevo ni se modificó evidencia histórica.

El cotejo independiente de fuentes aprobó **333/333 declaraciones** de los manifiestos `sha256_fuentes.json`, `sha256_herramientas.json` y `sha256_referencias.json`: 258 corresponden al subconjunto 1–7 y 75 al laboratorio 8. En el laboratorio 4 se leyeron los bytes de 32 blobs de las referencias `inicio` y `solucion` del bundle local; no se confundieron identificadores Git con hashes SHA-256 de contenido. Las dos referencias declaradas coincidieron con las anunciadas en el bundle.

También se cotejaron 18 declaraciones del registro de preparación y 222 campos esperado/observado de conservación. Estas repeticiones se contaron como declaraciones independientes: **573/573 declaraciones de fuentes** aprobadas, sin deduplicación. No son 573 archivos únicos ni casos funcionales adicionales. `COTEJO_FUENTES_DECLARADAS.json` registra cada declaración, origen, valor esperado y valor observado; `auditar_fuentes_declaradas.py` permite reproducir el cotejo. El comando terminó con salida 0. El análisis lee las fuentes, los blobs y la evidencia sin modificarlos; su único producto persistente es un informe nuevo. Los hashes de bases y CSV temporales incrustados en las salidas funcionales quedan fuera de esta auditoría de fuentes; su alcance corresponde a las comprobaciones de comportamiento que generaron esos datos aislados.

Las verificaciones auxiliares se mantienen separadas del recuento funcional:

- **Ocho pruebas del recolector:** APROBADO, salida 0; `recolector_01/`.
- **Nueve pruebas focales del evaluador:** APROBADO, salida 0; `evaluador_02/`. Comprueban rechazo de un fallo adicional, caso ausente, duplicado, excepción ajena al defecto, bloqueo parcial ilegítimo y ausencia de código en una ejecución parcial. También comprueban conservación de los FALLIDO esperados y que un bloqueo legítimo no aprueba la cobertura completa.
- `evaluador_01/` conserva un ensayo previo de cinco pruebas anterior a la ampliación del bloqueo parcial. No se suma a las nueve como cobertura adicional.

Estas pruebas del evaluador usan registros sintéticos para verificar el mecanismo de aceptación. No son nuevas ejecuciones de casos de negocio. Sus archivos identifican las huellas del verificador y de las pruebas utilizados.

## Evidencia y límites

`conjunto_01/resumen.json` contiene los resultados completos; `COMANDO_CONJUNTO_01.json` conserva el comando, las horas y el código de salida; `REVISION_CONJUNTO_01.json` documenta la comparación independiente de totales y huellas. `CONSERVACION_RECOLECTOR.json` conserva las huellas de la base y de los dos archivos protegidos.

No se crearon commits ni etiquetas, no se modificó main y no se publicó en GitHub. Esta revisión no acredita una sesión comercial, una ejecución Windows, GitHub Actions, rendimiento o seguridad integral. Las pruebas desde un ZIP y desde el parche corresponden a los controles adicionales de empaquetado que realizará la producción.
