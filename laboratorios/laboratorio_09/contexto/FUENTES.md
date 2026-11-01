# Fuentes primarias del laboratorio

Consulta efectiva: **1 de noviembre de 2026**. Selección de la documentación oficial consultada durante esta entrega. El contrato sintético, las diferencias y los JSON de pruebas son la fuente de los comportamientos específicos del ejercicio.

## OWASP Input Validation Cheat Sheet

Validar sintaxis y semántica; límites antes del procesamiento; comprobación en servidor; aceptar datos legítimos según contrato. Validación, parametrización y presentación segura son controles diferentes. [Documentación oficial](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html).

Límite de la referencia: No atribuir al simple rechazo de caracteres una protección integral frente a SQL o XSS.

## Python 3.11 sqlite3 — How to use placeholders to bind values in SQL queries

La API admite placeholders y parámetros separados para valores SQL. El context manager de conexión controla commit/rollback, pero no cierra la conexión. [Documentación oficial](https://docs.python.org/3.11/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries).

Límite de la referencia: Los parámetros representan valores; no reemplazan nombres de columnas u otras partes estructurales ni decisiones de autorización.

## Python 3.11 http.server

La documentación desaconseja http.server para producción y describe sus comprobaciones básicas. [Documentación oficial](https://docs.python.org/3.11/library/http.server.html).

Límite de la referencia: Mantener el laboratorio local; no llamar a la solución lista para producción.

## Python 3.11 urllib.parse — parse_qsl and URL parsing security

parse_qsl devuelve una lista de pares; keep_blank_values preserva vacíos; strict_parsing rechaza determinados errores de estructura; errors=strict exige decodificación UTF-8 estricta. urlsplit no valida por sí solo la entrada. [Documentación oficial](https://docs.python.org/3.11/library/urllib.parse.html).

Límite de la referencia: No equiparar strict_parsing con validación completa de percent-encoding. El límite y la política de duplicados son decisiones explícitas de la aplicación.

## RFC 9110 — HTTP Semantics, 15.5.15: 414 URI Too Long

414 informa que el servidor rechaza interpretar un URI de destino por su longitud. [Documentación oficial](https://www.rfc-editor.org/rfc/rfc9110.html#name-414-uri-too-long).

Límite de la referencia: El RFC no impone el umbral didáctico de 2.048 bytes. El laboratorio restringe la representación de la query, no acredita protección global frente a agotamiento de recursos.

## RFC 3986 — Uniform Resource Identifier, 2.1: Percent-Encoding

La sintaxis de percent-encoding requiere el signo de porcentaje seguido por dos dígitos hexadecimales. Sintaxis válida y secuencia UTF-8 válida son comprobaciones diferentes. [Documentación oficial](https://www.rfc-editor.org/rfc/rfc3986.html#section-2.1).

Límite de la referencia: No atribuir a RFC 3986 la política específica de claves o duplicados de la aplicación ni el significado de + en formularios.

## Límites elegidos por el libro

La query de 2.048 bytes y el nombre de 80 puntos de código son decisiones del contrato de este ejercicio. No son límites generales impuestos por Python, HTTP u OWASP. Las pruebas acreditan las peticiones y respuestas observadas, no una certificación de seguridad ni una auditoría completa.
