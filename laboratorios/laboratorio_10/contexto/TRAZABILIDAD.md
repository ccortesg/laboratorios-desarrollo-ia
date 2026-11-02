# Trazabilidad de requisitos y comprobaciones

| Contrato | Casos por estado | Componentes | Comprobación |
| --- | ---: | --- | --- |
| C01–C04, B01–B06, N01–N10 | 20 | Catálogo, búsqueda y detalle heredados | `estados/*/pruebas.py`, `estados/*/pruebas_detalle.py` |
| P01–P06 | 6 | Resumen y CLI heredados | `pruebas_resumen.py` |
| W01–W06 y subcasos | 8 | HTTP y pantalla heredados | `pruebas_http.py`, `pruebas_navegador.cjs` |
| I01–I08 y subcasos | 17 | Importación CSV | `pruebas_integracion.py` |
| D01–D08 y subcasos | 11 | SQLite persistente, procesos y origen | `pruebas_depuracion.py`, `pruebas_recorrido.py/.cjs` |
| S01–S08 y subcasos | 12 | Política HTTP y recuperación | `pruebas_seguridad.py`, `pruebas_seguridad_navegador.py/.cjs` |
| T01–T07 | 7 | Operador, snapshot y recibo | `pruebas_automatizacion.py` |
| T08 | 1 | Operador, SQLite, HTTP y pantalla | `pruebas_automatizacion_navegador.py/.cjs` |

Los 74 heredados deben aprobar en los tres estados. Los ocho T no se ejecutan en base porque falta el operador. Propuesta falla únicamente T02; solución aprueba los 82 casos.

| Criterio T | Entrada o situación | Evidencia observable |
| --- | --- | --- |
| T01 | CSV válido | Cantidades persistidas, código del operador y resumen de consulta. |
| T02 | Fila válida seguida de negativa | Estado completo conservado, importación rechazada, paso consulta NO EJECUTADO. |
| T03 | Repetición con recibos distintos | Estado final idéntico, pares omitidos conservados y bytes del primer recibo intactos. |
| T04 | Base ausente | Rechazo previo y ausencia de archivo/base/recibo creados. |
| T05 | Salida existente o protegida | Rechazo previo y bytes de entradas/recibo conservados. |
| T06 | Operación válida y cambio posterior del CSV original | Snapshot exacto, SHA-256 del input usado y huellas de capturas reales. |
| T07 | Cwd ajeno y rutas con espacios | Script del estado elegido, base explícita y resultado correcto. |
| T08 | Mismo servidor vivo antes y después de operar | Respuestas HTTP reales y estados visibles coherentes con la actualización. |

`pruebas_recursos.py` conserva cuatro regresiones SQLite. `pruebas_operador_recursos.py` contiene RO01 con dos subejecuciones controladas. Las ocho pruebas del recolector y las regresiones del evaluador común son infraestructura aparte. Sus conteos no amplían los criterios funcionales del catálogo.
