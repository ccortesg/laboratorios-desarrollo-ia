# Componentes y responsabilidades del laboratorio 10

| Componente | Responsabilidad implementada |
| --- | --- |
| `operar.py` | Prevalidar base/CSV/destino, reservar recibo, guardar instantánea, ejecutar dos CLI fijas y decidir continuación. |
| `persistencia.py` | Abrir la base explícita, inicializar sólo por orden independiente, invocar importación y consulta con conexiones cerradas. |
| `importacion.py` | Validar el CSV completo y aplicar cantidades absolutas en su transacción. |
| `resumen.py`, `catalogo.py`, `laboratorio.py` | Consultar el origen recibido y conservar las reglas del catálogo. |
| `servidor.py`, `politica_consulta.py` y `web/` | Consultar la misma SQLite mediante HTTP y mostrar resultado, vacío o error. |
| `soporte/huellas_evidencia.py` | Conservar hashes de captura y comprobar los bytes finales de las salidas guardadas. |
| Baterías de comprobación | Crear escenarios aislados y observar comportamiento sin sustituir el importador, SQLite, HTTP ni navegador por respuestas simuladas. |

El operador modifica estado sólo por el subproceso de importación. La consulta usa otra CLI y una conexión real al mismo archivo. La presentación HTTP puede seguir viva mientras se ejecuta la operación; cada petición abre el origen explícito y observa lo persistido.

Las acciones permitidas son fijas. Los argumentos de ruta, almacén y nombre se transmiten como datos. El operador no utiliza una respuesta de modelo como código ni requiere cuentas comerciales. La decisión de cambiar objetivos, recuperar un fallo o repetir una operación permanece fuera del programa.

No existe una transacción distribuida entre ambos procesos ni un servidor de automatización. Programación periódica, colas, agentes con herramientas y permisos de despliegue serían otras decisiones arquitectónicas; no están implementadas aquí.
