# Mapa mínimo de responsabilidades

| Componente | Responsabilidad implementada | Límite |
| --- | --- | --- |
| `persistencia.py` | Inicializar un archivo nuevo, importar con la CLI y consultar una conexión real | No recrea una base al consultar; conserva el archivo elegido |
| `importacion.py` | Leer y validar CSV, adaptar pares y aplicar cantidades absolutas de forma transaccional | No cambia artículos, almacenes ni habilitación |
| `servidor.py` | Adaptar GET, abrir la base seleccionada y responder HTTP | La respuesta no expone errores internos |
| `politica_consulta.py` | Validar tamaño, sintaxis, repeticiones, claves y nombre; devolver almacén/nombre | No consulta SQL ni modifica datos |
| `resumen.py` / `catalogo.py` / `laboratorio.py` | Conservar filtros de disponibilidad y búsqueda; consultar la conexión recibida | La normalización de nombres no se aplica al identificador del almacén |
| `web/app.js` | Mostrar resultado, vacío o error y recuperar controles | La pantalla consume la política, no la sustituye |
| Comprobaciones | Crear bases aisladas, iniciar procesos/HTTP/navegador y contrastar resultados | No acreditan producción ni servicios externos |

La nueva frontera se sitúa entre la query recibida y la llamada al resumen. La lista de pares conserva una información que el diccionario perdería: cuántas veces llegó cada clave. La validación actúa mientras esa información todavía existe.

El catálogo usa SQLite persistente cuando se indica `--base`; el comportamiento predeterminado sin base sigue siendo la demostración en memoria heredada. Las pruebas S indican siempre el archivo y demuestran el efecto del CSV con A03 visible. El diagnóstico de origen del laboratorio 8 sigue disponible y no se usa para aceptar datos erróneos.

No hay arquitectura productiva nueva. Autenticación, identidad, servicio externo de importación, colas y despliegue son posibles evoluciones fuera del ejercicio; este mapa describe exclusivamente lo implementado.
