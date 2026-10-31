# Componentes y responsabilidades

| Componente implementado | Responsabilidad |
| --- | --- |
| `datos/*.csv` | Entradas sintéticas adicionales; no sustituyen el SQL de referencia. |
| `importacion.leer_csv` | Interpretar UTF-8/BOM y la estructura CSV con el lector estándar. |
| `importacion.validar_filas` | Comprobar maestros, cantidades, columnas y duplicados sin escribir. |
| `importacion.aplicar_filas` | Sustituir cantidades dentro de una transacción. |
| `importacion.importar_existencias` | Coordinar etapas, identificar bytes y producir el informe. |
| `laboratorio.crear_conexion` | Crear la base desechable con datos originales. |
| `laboratorio.consultar_catalogo` | Consultar su conexión recibida, o una nueva si se omite. |
| `catalogo` y `resumen` | Reutilizar disponibilidad y búsqueda sobre ese origen. |
| `demostrar.py` | Mantener una conexión durante importación, repetición y consulta. |
| `pruebas_integracion.py` | Observar resultado de negocio y estado de las tablas. |
| `verificar.py` | Ejecutar referencias por capas y conservar evidencia nueva. |

La frontera externa termina en tuplas internas validadas. Las consultas SQL
utilizan parámetros; no se construyen fragmentos SQL con campos recibidos.
`aplicar_filas` inicia `BEGIN` explícitamente y deja que una excepción salga del contexto transaccional antes de
convertirla en un informe de rechazo. El importador no cierra la conexión del
llamador ni ejecuta scripts de esquema dentro de la transacción de importación.

**Evolución propuesta, no implementada:** persistir una base entre procesos,
recibir archivos por web, coordinar múltiples productores o controlar versiones
de intercambio. Ninguno de esos componentes forma parte de la evidencia actual.
