# Estado del repositorio · laboratorio 10 auditado y pendiente de cierre

**Versión:** 1.8.1. **Fecha:** 2026-11-01 18:48:53 -0700 · America/Hermosillo. Registro UTC: 2026-11-02T01:48:53.445285+00:00.

**Antecedente conservado:** ESTADO_REPOSITORIO_v1.8.md. **Continuidad editorial:** ESTADO_DEL_LIBRO_v1.9.1.md. Repositorio sintético autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

## Identidad comprobada

| Elemento | Valor |
| --- | --- |
| Rama de la ejecución recibida | codex/integracion-laboratorio-10 |
| HEAD, main local y main remoto observado | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| Árbol de partida | `790e875fc95495c39ea2b5ebe7621a4ae1afa30f` |
| Árbol preparado aprobado | `78b136a253cb3cb79143a0c81ee09f7892efa40f` |
| SHA-256 del parche original | `60a0f636ebb254fb5e1a98724127780069209ee9d0f690966566dd8f80e2a808` |
| Rutas preparadas | 1.372: 1.363 altas, nueve modificaciones y ninguna baja. |
| Archivos del índice | 3.660; identidad cotejada con los objetos Git confiables. |

Consulta remota independiente: 1 de noviembre de 2026, 18:43:25 America/Hermosillo (`2026-11-02 01:43:25 UTC`). Main no avanzó. Quince etiquetas históricas conservadas; lab-09-v1.0 y repositorio-v1.5 permanecen en la base. Lab-10-v1.0 y repositorio-v1.6 no existen: son nombres previstos, no publicaciones realizadas.

## Resultado de la ejecución WSL y de su revisión

APROBADO: conjunto con navegador, 125 baterías, 1.043 ejecuciones, 1.018 aprobaciones y 25 fallos didácticos exactos. Cero bloqueos y errores. Los 56 NO EJECUTADO históricos y los diez criterios ausentes se registran aparte. Solución 10: 82/82, con T08 real. El único fallo de propuesta 10 es T02 por aserción.

APROBADO: infraestructura 8/9/9/4/1 métodos, separada de los resultados funcionales. Integridad independiente del envío: 665/665 entradas y cobertura de 666 archivos contando manifiesto; 340/340 huellas finales en sesión, de las cuales 284 pertenecen al auxiliar y 272 al conjunto. No sumar esos alcances anidados.

Entorno aportado: WSL2/Linux, Python 3.12.16, SQLite 3.53.1, Git 2.34.1, Node 22.23.1, npm 10.9.8, Playwright 1.62.1 y Chromium 151.0.7922.34. Se utilizó el intérprete aislado existente del proyecto; Python del sistema no fue sustituido. Windows nativo permanece NO EJECUTADO. En esta auditoría no se repitió la batería funcional ni se ejecutaron scripts adjuntos.

## Conservación y precisión de evidencia

Los 2.297 hashes iniciales se contrastaron con HEAD; 2.288 archivos protegidos conservan sus bytes y modos. Incluyen los 2.285 de producción y tres comprobaciones adicionales. Los inventarios de 3.156 archivos históricos de trabajo concuerdan, con el límite de que sus bytes no se incluyeron individualmente en el ZIP. Se conserva la precisión temporal del inventario; no fue una captura atómica.

La distribución autónoma conserva sus 450 archivos y SHA-256 `5e39d5fb92e2408684003809d65f753b16929c7ad649e70f1c8eec0e26eb54f3`. El cotejo no representa una segunda ejecución autónoma.

El observador adicional de capturas quedó documentado y revisado como texto. No modifica fuentes versionadas ni resultados según el código inspeccionado; añade operaciones de archivo. El almacén original externo de 95 blobs no se reabrió durante esta revisión. Los registros capturados y finales se mantienen distintos; tres saneamientos externos explican cambios de huella y sus finales coinciden.

## Punto de cierre y siguiente operación

**APROBADO para preparar el cierre técnico; publicación NO EJECUTADO.** No se ha creado un commit nuevo, integrado en main, creado o movido etiquetas ni hecho push. Los capítulos 1–10 permanecen pendientes de revisión editorial.

Utilizar REVISION_LABORATORIO_10_WSL_v1.0.zip y PROMPT_CIERRE_LABORATORIO_10_v1.0.md en el próximo encargo. Antes de cualquier escritura futura comprobar de nuevo estado, árbol, base y referencias. Incorporar documentos nuevos sin reescribir antecedentes. Tras añadir documentación, el árbol cambiará: contrastar explícitamente las rutas documentales permitidas y conservar el contenido técnico del árbol auditado. No exigir que ese árbol documental nuevo sea idéntico a `78b136a253cb3cb79143a0c81ee09f7892efa40f`.

Si main avanzó, conservar sus cambios y adaptar la integración; verificar cualquier cambio funcional antes de cerrar. Publicar sólo main y las etiquetas nuevas previstas, mediante un push atómico sin forzar. Registrar después las referencias efectivamente observadas y conservar las capturas posteriores fuera del commit que describen, evitando autorreferencias.
