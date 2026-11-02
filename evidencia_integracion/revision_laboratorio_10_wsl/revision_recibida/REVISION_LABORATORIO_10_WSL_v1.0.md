# Revisión independiente de la integración del laboratorio 10 en WSL

**Dictamen: APROBADO para preparar el cierre técnico.**

**Fecha de esta revisión:** 2026-11-01 18:48:53 -0700 · America/Hermosillo. Registro UTC: 2026-11-02T01:48:53.445285+00:00.

La ejecución aportada acredita una integración local preparada y verificada. El laboratorio 10 aún no tiene un commit de cierre ni publicación confirmada. Esta revisión no integra en main, no crea etiquetas y no publica. Los capítulos 1–10 siguen pendientes de la revisión editorial del autor.

## 1. Material recibido y método

Se recibieron `EVIDENCIA_LABORATORIO_10_WSL_v1.0.zip` y `INFORME_INTEGRACION_LABORATORIO_10_WSL_v1.0.md`. El informe exterior es idéntico al incluido en el ZIP. La huella del ZIP recibido es `3a2dd4825f83056ce77cb9d2ef4a0cf5b2da205b68d2298438fd2811c4637818`; tamaño: 1.046.784 bytes.

Se revisaron el CRC, las rutas del archivo, la cobertura del manifiesto, los tamaños y SHA-256, las huellas de salida, las listas originales de casos, los contratos confiables de producción y los objetos Git disponibles de la base y del árbol preparado. Se reconsultó GitHub en lectura. No se ejecutaron los scripts recibidos ni se repitió una batería funcional para sustituir la sesión del autor. El recolector original se utilizó exclusivamente como comprobador de lectura, con aislamiento de Python.

Fuentes de la revisión: `auditoria/RECEPCION.json`, `INTEGRIDAD_INDEPENDIENTE.json`, `FUNCIONAL_INDEPENDIENTE.json`, `GIT_INDEPENDIENTE.json` y `REFERENCIAS_REMOTAS_RECONSULTADAS.json`. Se conservan sus informes desarrollados y ambos archivos recibidos sin modificaciones dentro del paquete de revisión.

## 2. Resultado funcional observado en la ejecución WSL

El recuento independiente de 125 listas de casos coincide con los informes: **1.043 ejecuciones, 1.018 APROBADO, 25 FALLIDO didácticos, cero BLOQUEADO y cero errores de ejecución**. Los 56 NO EJECUTADO de baterías históricas y los diez criterios N ausentes en el inicio del laboratorio 4 se mantienen separados. Algunas ausencias se informan mediante un proceso que sí arranca, pero no ejecuta los casos todavía inexistentes; no se cuentan como ejecuciones funcionales.

| Laboratorio 10 | APROBADO | FALLIDO | NO EJECUTADO |
| --- | ---: | ---: | ---: |
| Base | 74 | 0 | 8 |
| Propuesta | 81 | 1: T02 | 0 |
| Solución | 82 | 0 | 0 |

Los 74 casos heredados aprueban en los tres estados. T02 conserva una aserción fallida en la propuesta: el importador rechaza el CSV, pero el operador consulta el estado anterior y declara éxito indebido. La solución devuelve código 1, detiene la consulta y conserva la base ante ese rechazo. Los otros 24 fallos corresponden exactamente a los defectos anteriores permitidos por estado e identificador; los 25 son `AssertionError`, sin excepciones adicionales toleradas.

T08 contiene evidencia del recorrido real CSV → operador → importador CLI → SQLite persistente → HTTP → Chromium. En propuesta y solución se observa A01 antes, A01/A03 después y A03 al buscar; el servidor continúa siendo el mismo. El código -15 de cierre del servidor corresponde a la terminación explícita del controlador, no a un fallo oculto de la aplicación. Las 92 fuentes declaradas del laboratorio 10 coinciden con las fuentes de producción contrastadas.

Se observa un solo intento integral en el envío, con `--navegador`. Estos resultados pertenecen a la sesión WSL aportada, no a una nueva ejecución funcional durante esta revisión. Las auditorías y los casos repetidos por estado no representan requisitos únicos adicionales.

## 3. Infraestructura e integridad

| Alcance | Resultado independiente |
| --- | --- |
| Manifiesto del envío | 665/665 tamaños y SHA-256 coincidentes; 666 archivos contando el manifiesto. |
| Huellas de sesión completa | 340/340 coincidentes. |
| Huellas del auxiliar | 284/284 coincidentes. |
| Huellas del conjunto funcional | 272/272 coincidentes. |
| Recolector | Ocho métodos, OK, código 0. |
| Evaluador del laboratorio 9 | Nueve métodos, OK, código 0. |
| Evaluador del laboratorio 10 | Nueve métodos, OK, código 0. |
| Recursos SQLite | Cuatro métodos, OK, código 0. |
| Recursos del operador | Un método con dos estados como subcasos, OK, código 0. |

Los alcances 272, 284 y 340 están contenidos unos dentro de otros: **no se suman**. La infraestructura tampoco se suma a las 1.043 ejecuciones funcionales. La regresión RO01 inyecta un `OSError`; es un caso de prueba de infraestructura, no un incidente real de la sesión.

Tres capturas externas cambian de huella tras el saneamiento: stderr de aplicación del parche, stdout de entorno Chromium y stdout de entorno Python. Sus huellas finales coinciden con los bytes recibidos. Las 284 declaraciones capturadas del auxiliar coinciden con sus finales y con el inventario aportado.

La sesión añadió un observador en `sitecustomize.py` que copia capturas antes del saneamiento y llama a la función original con los mismos argumentos y retorno. La revisión estática no encontró alteración de expectativas o resultados ni escritura sobre las salidas declaradas. Esta instrumentación añade operaciones de archivo; no se infiere equivalencia de rendimiento. El código versionado del recolector y sus ocho pruebas permanecen exactos.

El inventario refiere 95 blobs originales conservados fuera del ZIP, que también incluyen documentos de comandos y cierres intermedios. No se inspeccionaron esos bytes externos durante esta revisión. Sí se comprobó la coherencia de las 284 referencias recibidas. SHA-256 demuestra correspondencia de bytes; por sí solo no autentica una ejecución externa.

## 4. Git, distribución y conservación

| Identidad | Valor |
| --- | --- |
| Rama documentada | `codex/integracion-laboratorio-10` |
| HEAD y main conservados | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| Árbol de la base | `790e875fc95495c39ea2b5ebe7621a4ae1afa30f` |
| Árbol preparado auditado | `78b136a253cb3cb79143a0c81ee09f7892efa40f` |
| Rutas del parche | 1.372: 1.363 altas, nueve modificaciones y cero bajas. |
| Índice preparado | 3.660 archivos. |

Se reconstruyó el árbol en memoria a partir de las 3.660 entradas recibidas y se cotejaron rutas, OID, SHA-256 y modos contra objetos Git confiables. El resultado coincide exactamente con el árbol preparado. Los 2.297 hashes iniciales corresponden a HEAD; 2.288 archivos protegidos conservan su contenido en ambos árboles. La cifra supera los 2.285 protegidos en producción porque la revisión WSL incluye tres archivos adicionales, sin retirar ninguno del conjunto anterior.

La distribución conserva el SHA-256 `5e39d5fb92e2408684003809d65f753b16929c7ad649e70f1c8eec0e26eb54f3`, el CRC y los 450 archivos esperados. Es un cotejo de contenido; no se presenta como una segunda ejecución autónoma.

Los inventarios de 3.156 archivos históricos de `trabajo/` concuerdan, pero esos archivos no se incluyen individualmente: su conservación física conserva la atribución a la comprobación local WSL. También se mantiene la precisión temporal declarada: el inventario empezó leyendo contenido antes del parche y completó sus metadatos Git después; no se describe como una captura atómica.

Las 28 operaciones documentadas tienen salida 0. Los avisos de espacios durante `git apply` no cambiaron la identidad del árbol y `git diff --cached --check` aprobó. No se reescribieron los terminadores de las evidencias para eliminar avisos.

## 5. Consulta remota independiente y punto de cierre

Consulta del **1 de noviembre de 2026, 18:43:25 de Hermosillo**, equivalente a `2026-11-02 01:43:25 UTC`: main, lab-09-v1.0 y repositorio-v1.5 siguen en el commit de partida; las quince etiquetas históricas conservan sus identidades. `lab-10-v1.0` y `repositorio-v1.6` están ausentes. No se observa avance posterior ni publicación del laboratorio 10 en esa consulta.

**No se encontraron problemas materiales pendientes dentro del alcance revisado.** La integración está lista para preparar un cierre con incorporación documental, commit, integración en main y publicación de las dos etiquetas nuevas, mediante un encargo posterior del autor. Hasta entonces esas operaciones siguen NO EJECUTADO.

## 6. Límites y continuidad

El entorno de la sesión aportada es WSL2/Linux: Python 3.12.16, SQLite 3.53.1, Git 2.34.1, Node 22.23.1, npm 10.9.8, Playwright 1.62.1 y Chromium 151.0.7922.34. Windows nativo continúa NO EJECUTADO. Tampoco se acredita CI remota, operación productiva ni una sesión nueva de Copilot o Grok Build.

La ejecución es local y secuencial. No prueba concurrencia, fallos físicos ni agotamiento del timeout. Una importación confirmada no se revierte porque falle la consulta posterior. La revisión técnica no aprueba los manuscritos: capítulos 1–10 pendientes del autor, maestro editorial 1.0 conservado. No se redactó contenido adicional.

Continuidad nueva: `ESTADO_DEL_LIBRO_v1.9.1.md` y `ESTADO_REPOSITORIO_v1.8.1.md`. El encargo propuesto para el siguiente paso se incluye en `PROMPT_CIERRE_LABORATORIO_10_v1.0.md`; no fue ejecutado en esta revisión.
