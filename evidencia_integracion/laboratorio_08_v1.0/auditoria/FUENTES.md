# Fuentes y preparación editorial del capítulo 8

**Fecha efectiva de consulta:** 31 de octubre de 2026, 23:49:46 UTC.

**Uso:** notas de producción; todavía no describen resultados del laboratorio 8.

Se consultaron seis fuentes primarias. Las afirmaciones propuestas se expresan en paráfrasis y deben citarse junto a su uso. La documentación no sustituye las pruebas del laboratorio ni acredita sus resultados.

## F1 — Python sqlite3

**Título:** sqlite3 — DB-API 2.0 interface for SQLite databases. Documentación Python 3.11.

**URL:** https://docs.python.org/3.11/library/sqlite3.html

**Secciones:** parámetros de connect; How to use the connection context manager; How to work with SQLite URIs.

**Referencias recuperadas:** turn94view0, turn95view0, turn95view1, turn95view2.

Afirmaciones respaldadas: con `uri=True`, `mode=rw` permite abrir un archivo existente sin crearlo implícitamente; `mode=ro` permite apertura de sólo lectura. Por defecto, usar una conexión desde otro hilo produce `ProgrammingError`. El gestor `with conexion` confirma o revierte una transacción abierta, pero no abre por sí solo una transacción ni cierra la conexión.

Aplicación editorial: justificar la separación entre inicializar y abrir, y la conexión por petición. No extender estas garantías a validación de esquema, rechazo de sobrescritura, saneamiento de rutas o concurrencia: esas propiedades deben implementarse y comprobarse en el ejercicio.

## F2 — SQLite en memoria

**Título:** In-Memory Databases.

**URL:** https://www.sqlite.org/inmemorydb.html

**Referencia recuperada:** turn94view1; pasaje preciso turn95view3.

Una conexión que abre el nombre especial `:memory:` crea una base que desaparece al cerrarse. Dos aperturas de ese nombre generan bases independientes. El documento también describe otros mecanismos para compartir memoria; no deben confundirse con la llamada simple que utiliza el proyecto.

Aplicación editorial: explicar por qué compartir una conexión en un proceso no equivale a compartir datos entre el importador y un proceso HTTP. Esta afirmación no convierte el laboratorio 7 en defectuoso: su alcance en memoria estaba declarado.

## F3 — Origen de la conexión SQLite

**Título:** PRAGMA Statements — database_list.

**URL:** https://www.sqlite.org/pragma.html#pragma_database_list

**Referencias recuperadas:** turn94view2; pasaje preciso turn95view4.

`PRAGMA database_list` devuelve información de las bases asociadas a la conexión actual. Incluye el nombre del esquema y el archivo; cuando no hay archivo asociado, ese campo queda vacío.

Aplicación editorial: observar la conexión efectiva, no repetir sólo una ruta configurada. La traducción a alias sintéticos es una decisión del laboratorio. El origen registrado ayuda a investigar, pero no reemplaza la comparación de datos. No describir este PRAGMA como una garantía universal de identidad, integridad o ausencia de efectos de otros componentes.

## F4 — Procesos y resultados

**Título:** subprocess — Subprocess management. Documentación Python 3.11.

**URL:** https://docs.python.org/3.11/library/subprocess.html

**Referencia recuperada:** turn94view3.

`subprocess` permite iniciar procesos y recoger sus salidas y códigos de terminación. `run` cubre ejecuciones que se esperan hasta concluir; `Popen` permite control más directo. En `run`, un timeout de comunicación termina el hijo y espera su salida; la creación inicial del proceso puede no ser interrumpible de inmediato.

Aplicación editorial: explicar procesos reales de importación y servicio y la captura de evidencia. No afirmar que la existencia de un código cero demuestra el resultado de negocio. El cierre de un servidor iniciado con `Popen` debe comprobarse en el auxiliar concreto, no inferirse automáticamente del comportamiento de `run`.

## F5 — Servidor HTTP del ejercicio

**Título:** http.server — HTTP servers. Documentación Python 3.11.

**URL:** https://docs.python.org/3.11/library/http.server.html

**Referencia recuperada:** turn94view4.

`ThreadingHTTPServer` utiliza hilos para atender peticiones. La documentación indica que `http.server` no se recomienda para producción y sólo implementa comprobaciones básicas de seguridad.

Aplicación editorial: justificar la conexión creada y cerrada dentro de la petición y el alcance de demostración local. No presentar este servidor como arquitectura productiva ni atribuirle pruebas de carga, seguridad o múltiples escritores.

## F6 — Esperas de navegador

**Título:** Auto-waiting. Documentación Playwright.

**URL:** https://playwright.dev/docs/actionability

**Referencias recuperadas:** turn94view5, turn95view5.

Playwright espera condiciones de interacción antes de ciertas acciones, con un timeout; por ejemplo, visibilidad y disponibilidad del elemento antes de pulsarlo. La documentación también describe aserciones con reintentos hasta que se cumple una condición.

Aplicación editorial: preferir condiciones observables y límites de espera a pausas arbitrarias. La espera de un clic no demuestra por sí sola que la operación de negocio haya terminado. Citar la función realmente utilizada en el laboratorio; no afirmar que éste usa Playwright Test o `expect` si sólo utiliza la biblioteca y otro mecanismo de espera.

## Plan narrativo propuesto

El capítulo debe abrir con el importador satisfecho y una pantalla que conserva otro resultado. Presentar después las fronteras: proceso, conexión, origen, HTTP y representación visible. Mantener el protagonismo en la elección del experimento, no en una lista de herramientas.

La crónica será sintética, de 400–700 palabras. Un desarrollador experimentado comprueba que registrar la ruta solicitada no demuestra que esa conexión llegue a la consulta. La observación decisiva combina persistencia confirmada, respuesta HTTP y origen efectivo. No inventar un descubrimiento histórico ni conversaciones literales.

Distribución orientativa para 4.400–4.700 palabras:

| Sección | Función |
| --- | --- |
| 1 | Síntoma reconocible y pregunta concreta. |
| 2 | Crónica sintética; primer intento, dificultad, observación y aprendizaje. |
| 3 | Entregable y contratos conservados. |
| 4 | Conceptos de proceso, conexión, hipótesis y experimento discriminante. |
| 5 | Entorno, archivos y comandos exactos, tras confirmar su implementación. |
| 6 | CLARO, encargo insuficiente y mejorado, registro de investigación. |
| 7 | Por qué HTTP 200 y pruebas heredadas aprobadas pueden coexistir con el defecto nuevo. |
| 8 | Resultados realmente observados y límites de cobertura. |
| 9 | Adaptar la investigación a otros contextos sin copiar datos privados. |
| 10 | Reto de comparar informes en sólo lectura, NO EJECUTADO. |

Esperar la evidencia de producción antes de redactar comandos, resultados, tabla de casos y explicación del cambio real. Usar los nombres y salidas que efectivamente existan.

El maestro 1.0 permanece vigente. Los capítulos anteriores y el nuevo borrador siguen pendientes de revisión del autor. El capítulo 7 no requiere corrección retroactiva: su sección 6 delimita la conexión en memoria y su sección 9 propone seguir el origen que consulta el consumidor.
