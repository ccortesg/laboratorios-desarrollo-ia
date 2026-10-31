# Fuentes técnicas del laboratorio 7

Consulta efectiva: 31 de octubre de 2026. Las afirmaciones se presentan como
paráfrasis. La revisión documental es distinta de las ejecuciones del laboratorio.

## CSV y validación del contrato

Python 3.11 documenta `newline=''` al leer archivos CSV, devuelve campos como
cadenas y permite declarar el dialecto. `strict=True` detecta errores del analizador,
pero no comprueba por sí mismo encabezados, maestros o cantidades válidas. Esas
reglas pertenecen al contrato sintético del ejercicio.

Fuente: [Python Software Foundation, csv](https://docs.python.org/3.11/library/csv.html).

## UTF-8 con firma inicial

`utf-8-sig` omite la firma UTF-8 inicial al decodificar. El laboratorio la admite
por una decisión expresa; no presupone que sea obligatoria ni que toda exportación
de Windows la incorpore. Se calcula el SHA-256 antes de decodificar: archivos con
bytes distintos pueden representar los mismos registros.

Fuente: [Python Software Foundation, codecs](https://docs.python.org/3.11/library/codecs.html#encodings-and-unicode).

## Parámetros SQL y conexión

Los parámetros de una sentencia se pasan separados del texto SQL. En Python 3.11,
el contexto de una conexión confirma o revierte una transacción abierta, pero no
la abre por sí mismo ni cierra la conexión. El importador utiliza `BEGIN` explícito;
la excepción de escritura sale del contexto antes de producir un informe de rechazo.
Los scripts de esquema se ejecutan al preparar la base, fuera de esa aplicación.
La parametrización no acredita una evaluación integral de seguridad.

Fuente: [Python Software Foundation, sqlite3](https://docs.python.org/3.11/library/sqlite3.html).

## Atomicidad y alcance de la evidencia

La atomicidad trata los cambios de una transacción como un conjunto. SQLite
documenta sus mecanismos y supuestos de almacenamiento. Las pruebas del libro
observan rechazo de entrada y una escritura rechazada de forma controlada; no
experimentan con cortes eléctricos, fallos físicos ni escritores concurrentes.

Fuente: [SQLite, Atomic Commit In SQLite](https://www.sqlite.org/atomiccommit.html).

## Propiedad de la transacción

`BEGIN` no se anida dentro de otra transacción. Algunos errores revierten sólo
una sentencia y no toda la transacción, por lo que el importador declara quién
confirma o revierte. Rechaza una conexión con cambios pendientes y controla la
aplicación del lote. Los savepoints y la concurrencia quedan fuera del ejercicio.

Fuente: [SQLite, Transaction](https://www.sqlite.org/lang_transaction.html).
