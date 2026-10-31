# Estado del libro — corrección del recolector cerrada

**Libro:** Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro  
**Versión de continuidad:** 1.5.2 · **Fecha:** 31 de octubre de 2026  
**Etapa:** capítulo 6 entregado; laboratorio 6 integrado; corrección del recolector verificada y publicada.

## 1. Decisiones vigentes y precedencia

Este estado actualiza `ESTADO_DEL_LIBRO_v1.5.1.md`, que se conserva. La versión 1.5.2 representa el cierre técnico posterior al capítulo 6; no añade contenido de otro capítulo. El estado operativo vigente es `ESTADO_REPOSITORIO_v1.4.1.md`.

**DOCUMENTO_MAESTRO_EDITORIAL_v1.0.md permanece intacto.** Se mantienen promesa, principio rector, público, índice aprobado, método CLARO, plantilla y anonimización. Los capítulos **1–6 siguen pendientes de revisión editorial del autor**. El proceso técnico aportado no contiene una aprobación editorial ni observaciones nuevas sobre los manuscritos.

El capítulo 6, su Markdown y Word, el laboratorio autónomo y las distribuciones anteriores conservan sus versiones. El cambio afecta al recolector común de evidencia, sus pruebas y una nota de mantenimiento. No se redactó el capítulo 7.

## 2. Estado técnico confirmado

La revisión independiente de GitHub confirmó main en:

`6382e05846e149a9a72f7fdc56da48c37a873833`

Su padre es `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd` y el árbol es `680fa6135ed0aae40e962ec3f893d72ece1389c1`, igual al del parche probado. `lab-06-v1.0` y `repositorio-v1.2` permanecen en el padre, identificando la entrega original. Las nueve etiquetas existentes se conservan. No hay una nueva etiqueta de versión para esta corrección.

Se modificó un archivo común y se añadieron tres: auxiliar de huellas, ocho pruebas y nota de mantenimiento. Los otros 584 archivos anteriores conservan contenido y modo, incluidos los seis laboratorios, las distribuciones y sus evidencias.

Fuente: [commit publicado](https://github.com/ccortesg/laboratorios-desarrollo-ia/commit/6382e05846e149a9a72f7fdc56da48c37a873833) y la auditoría de este cierre. Estos identificadores se limitan a la continuidad operativa y no identifican al protagonista de las crónicas.

## 3. Nueva evidencia del autor

Se recibió y auditó `EVIDENCIA_CORRECCION_HUELLAS_WINDOWS_v1.0.zip` junto con la transcripción del procedimiento. El ZIP tiene 118 archivos, CRC correcto y SHA-256:

`001cd08e94f9b9a00c400368cdedfc7072955c4beb3ac44b017af2eb11878707`

Resultados observados en la evidencia aportada:

- **Ocho pruebas específicas: APROBADO**, código 0, según la transcripción de Windows.
- **Conjunto de seis laboratorios: APROBADO**, 29 baterías, 272 ejecuciones, 266 aprobaciones, seis fallos didácticos y cero bloqueos; cifras conciliadas con los casos del ZIP.
- **Huellas finales: 34/34 APROBADO**, recalculadas sobre los bytes recibidos sin normalizar LF/CRLF.
- **Solución del laboratorio 6: 34/34 casos APROBADO**.
- **Fuentes: 60/60 hashes del laboratorio 6 coincidentes** y 28 comprobaciones heredadas coherentes.

Los 20 NO EJECUTADO en baterías y diez criterios N ausentes aparte siguen correctamente diferenciados. Los fallos intencionales son C04 del inicial 1, B05/B06 del defecto 3, P04/P05 de la propuesta 5 y W05 de la propuesta 6. Los códigos global y del comprobador final son 0 en la transcripción. No se suman la auditoría, los ocho tests específicos o ejecuciones anteriores a las 272 para inflar la cobertura del catálogo.

El entorno registrado es Windows, Python 3.11.9, SQLite 3.45.1, Git 2.45.1.windows.1, Node v20.20.0, Playwright 1.62.1 y Chromium 151.0.7922.34. Los sellos técnicos de la ejecución abarcan `2026-10-31T16:25:31Z`–`2026-10-31T16:25:48Z`, según los registros del entorno. La ejecución, el commit y la subida corresponden al autor; el asistente revisó los archivos y consultó GitHub.

## 4. Pendiente resuelto y conservación histórica

La corrección de huellas H01 queda **cerrada para las ejecuciones nuevas**. El recolector conserva el hash capturado, sanea sin traducción implícita de finales de línea y calcula el hash final sobre los bytes guardados. En la evidencia nueva los 34 hashes finales coinciden directamente; los 34 campos capturados están presentes y también coinciden con esos valores.

Las cuatro diferencias documentadas en el ZIP Windows anterior permanecen como hallazgo histórico. Se conservaron ambos adjuntos y sus hashes; no se reescribió evidencia para borrar el incidente. El resultado Linux bloqueado durante la preparación también se conserva. La ejecución posterior del autor acredita ahora el recorrido completo corregido en Windows.

Esta observación aporta un aprendizaje transferible: la evidencia debe verificarse después de cualquier transformación que cambie sus bytes. Puede recuperarse como ejemplo didáctico en un encargo editorial posterior, sin inventar una conversación, sesión comercial o ahorro de tiempo. No se añadió ese contenido al manuscrito en este cierre.

## 5. Límites que continúan

La aprobación se limita al contrato sintético y a los entornos registrados. No acredita otros navegadores, accesibilidad exhaustiva, rendimiento, seguridad integral, despliegue, Word nativo ni los retos opcionales. La ejecución local no acredita una sesión comercial de Grok Build; su situación histórica de acceso y uso permanece sin cambios. Continúa separado el cotejo de la carpeta histórica de evidencia de Codex del capítulo 4 que no estuvo disponible.

Los estados nuevos y el paquete de revisión se entregan por separado y no se presentan como contenido ya incluido en main. La siguiente sesión debe utilizar estos estados por encima de los pendientes históricos y consultar de nuevo las referencias remotas.

## 6. Próxima tarea

Ya puede prepararse el encargo del capítulo 7, **«Datos e integraciones: cuando los sistemas deben ponerse de acuerdo»**, utilizando el maestro 1.0, este estado, el estado operativo 1.4.1, el capítulo 6 y el laboratorio 6. El punto de partida confirmado es el commit `6382e05846e149a9a72f7fdc56da48c37a873833`.

El siguiente incremento deberá declarar su contrato antes de implementarse y conservar C01–C04, B01–B06, N01–N10, P01–P06 y W01–W06, incluidos sus subcasos. Se mantendrán materiales sintéticos, evidencias nuevas por ejecución, historial intacto y separación entre resultados observados y ejemplos didácticos. La revisión del autor sigue pendiente sobre voz, profundidad técnica y utilidad práctica de los borradores.
