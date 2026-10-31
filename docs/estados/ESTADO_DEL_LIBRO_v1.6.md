# Estado del libro — capítulo 7 preparado para revisión

**Versión de continuidad:** 1.6 · **Fecha:** 31 de octubre de 2026
**Libro:** Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro
**Estado operativo relacionado:** ESTADO_REPOSITORIO_v1.5.md.

## 1. Decisiones vigentes

Este estado sucede a ESTADO_DEL_LIBRO_v1.5.2.md, que se conserva como antecedente. El documento maestro editorial v1.0 permanece intacto: no hubo un cambio editorial que justificara actualizarlo.

Se mantienen la promesa del libro, el principio rector, el público, el índice, CLARO, la plantilla y la anonimización. Los capítulos **1–7 son borradores pendientes de revisión editorial del autor**. Las pruebas técnicas no constituyen aprobación de los manuscritos. No se incorporaron observaciones editoriales que el autor no haya proporcionado y no se redactó el capítulo 8.

## 2. Contenido y materiales de esta entrega

El capítulo 7, «Datos e integraciones: cuando los sistemas deben ponerse de acuerdo», desarrolla un contrato CSV y su aplicación al catálogo sintético. El Markdown completo tiene aproximadamente 4.700 palabras; la crónica contiene 466 palabras narrativas y está rotulada como reconstrucción sintética.

La entrega comprende:

- CAPITULO_07_v1.0.md y CAPITULO_07_v1.0.docx.
- LABORATORIO_07_v1.0.zip.
- ESTADO_DEL_LIBRO_v1.6.md.
- ESTADO_REPOSITORIO_v1.5.md.
- INTEGRACION_LABORATORIO_07_v1.0.zip.

El laboratorio añade lectura, validación y aplicación de cantidades absolutas por artículo y almacén. Conserva pares omitidos, rechaza duplicados y entradas inválidas, y consulta la misma conexión que actualizó. Se distinguen base, propuesta defectuosa y solución; los únicos fallos previstos de la propuesta nueva son I01 e I07.

El incremento es local, por terminal y en una base desechable. La web conserva su recorrido y sus datos predeterminados; no se añadió importación web ni persistencia entre procesos. La revisión añadió BEGIN explícito y una observación de rollback a I06, sin alterar el contrato previo ni su huella. El reto de previsualización permanece NO EJECUTADO.

## 3. Base y continuidad técnica

La consulta de lectura del 31 de octubre de 2026 confirmó main en 6382e05846e149a9a72f7fdc56da48c37a873833 y árbol 680fa6135ed0aae40e962ec3f893d72ece1389c1. Esa base ya contiene la corrección del recolector.

Las etiquetas lab-06-v1.0 y repositorio-v1.2 permanecen en 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd. La integración 1.3 se prepara localmente; no se presenta como publicada. El estado operativo detalla la consulta y las referencias.

H01 sigue cerrado para ejecuciones nuevas. Se conservan los registros históricos con discrepancias, sin modificar sus bytes para hacerlos aprobar. La evidencia Windows de los laboratorios 1–6 y de la corrección pertenece a las ejecuciones anteriores aportadas por el autor; no acredita el laboratorio 7.

## 4. Resultados efectivamente observados

La producción local utilizó Linux, Python 3.12.14, SQLite 3.53.1, Node 24.22.1, Playwright 1.62.1 y Chromium 156.0.8078.80.

| Alcance | Resultado observado |
| --- | --- |
| Laboratorio 7 autónomo, con navegador | APROBADO: 15 baterías, 136 ejecuciones, 134 aprobaciones, dos fallos didácticos y cero bloqueos. |
| Solución del laboratorio 7 | 51/51 casos APROBADO: 34 heredados y 17 I, correspondientes a cuarenta criterios. |
| Huellas del verificador autónomo | 30/30 APROBADO sobre los bytes finales. |
| Conjunto de siete laboratorios, con navegador | APROBADO: 44 baterías, 408 ejecuciones, 400 aprobaciones, ocho fallos didácticos y cero bloqueos. |
| Huellas del conjunto | 64/64 APROBADO sobre los bytes finales. |

Los 17 casos I de base son NO EJECUTADO y no se suman a las 136 ejecuciones del laboratorio 7. En el conjunto hay 37 NO EJECUTADO en baterías y diez criterios N ausentes registrados aparte. Los fallos didácticos conservan FALLIDO; no representan problemas pendientes de la solución.

Las demostraciones, las pruebas del recolector y las auditorías se registran por separado. No se suman a los casos funcionales para aumentar artificialmente su cobertura. Los resultados autónomos están en laboratorio_07/evidencia/RESULTADOS.md; la ejecución conjunta está en evidencia_integracion/laboratorio_07_v1.0/verificacion_conjunta/resumen.json.

## 5. Cierre de presentación y paquetes

La presentación del Word quedó APROBADA: once páginas renderizadas e inspeccionadas, con texto, trece bloques de código, dos tablas y referencias equivalentes al Markdown de 4.677 palabras. Los metadatos personales están vacíos.

Las ocho pruebas existentes del recolector terminaron APROBADO, código 0. Se registran aparte en evidencia_integracion/laboratorio_07_v1.0/qa_recolector. El algoritmo de huellas y los ocho tests conservan su comportamiento; sólo cambia una frase de ayuda que mencionaba un total fijo.

La extracción del ZIP en una carpeta nueva y su ejecución completa con navegador terminaron APROBADO, código 0: 136 ejecuciones y 30/30 huellas. Se verificaron los 139 archivos declarados en su manifiesto antes y después; ninguno cambió. El ZIP contiene 140 archivos contando el manifiesto. Su SHA-256 es 2f579f87eb3a907e67ab195acb285543ee5997a805ff1add2e422dc7bc9b0b85.

La aplicación del parche se probó sobre una copia limpia de la base registrada y se ejecutó allí el conjunto completo. El informe independiente del paquete, evidencia/PRUEBA_PARCHE.json, identifica el parche final, su árbol, los comandos y sus resultados. El manifiesto SHA256SUMS y VERIFICAR_PAQUETE.py permiten comprobar el paquete recibido antes de aplicarlo.

Una comparación byte a byte conservó 575 archivos históricos, las seis entradas previas de PROCEDENCIA.json y los cuerpos anteriores de CONTINUIDAD.md y VERSIONES.md. Las reglas de atributos nuevas preservan los espacios significativos de los diffs y los saltos Markdown de los dos estados históricos recuperados; no se normalizaron esas evidencias. El registro está en evidencia_integracion/laboratorio_07_v1.0/CONSERVACION_HISTORICA.json.

Estas comprobaciones son ejecuciones locales de Linux. Las instrucciones Git Bash preparan una nueva verificación en Windows; no la dan por realizada.

## 6. Límites y siguiente tarea

El laboratorio 7 en Windows, su integración en main y su subida remota están **NO EJECUTADO** en esta entrega. Una sesión comercial nueva con Codex, Copilot o Grok Build y GitHub Actions tampoco se acredita mediante estas pruebas.

No se verificaron concurrencia, cortes físicos, rendimiento con archivos masivos, seguridad integral, accesibilidad exhaustiva ni despliegue. Los límites históricos de herramientas comerciales y del cotejo de evidencia de Codex ausente permanecen separados.

La siguiente tarea es verificar el paquete e integrarlo en una rama local de Windows, ejecutar las ocho pruebas del recolector y la verificación conjunta con navegador, revisar las diferencias y conservar la evidencia nueva. La subida se hará después de revisar esos resultados, con las etiquetas nuevas previstas lab-07-v1.0 y repositorio-v1.3.

La revisión editorial del autor debe valorar tres aspectos: voz y continuidad narrativa, profundidad de la explicación técnica y utilidad práctica del recorrido. El capítulo 8 necesitará un encargo posterior.
