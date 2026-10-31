# Decisiones del laboratorio 6

**Fecha editorial:** 31 de octubre de 2026. Las ejecuciones conservan su sello UTC
efectivo en los archivos de evidencia.

| ID | Decisión | Razón y límite |
| --- | --- | --- |
| D06-01 | Usar Python estándar, HTML, CSS y JavaScript | App local accesible, sin dependencias de ejecución externas. No fija el stack futuro del libro. |
| D06-02 | Copiar sin cambios los nueve archivos de la solución 5 a cada estado | Mantener los contratos y las expectativas anteriores; verificar 28 copias incluyendo la batería P. |
| D06-03 | Ejecutar P con `--directorio estados/ESTADO` | La base actual ya tiene resumen; el selector histórico `--estado base` del laboratorio 5 representaba su ausencia. |
| D06-04 | Delegar toda disponibilidad al resumen existente | Evitar dos reglas divergentes entre interfaz y servidor. |
| D06-05 | Requerir almacén en HTTP, ofrecer ALFA y BETA en el formulario | Impedir que una petición incompleta elija una ubicación implícita. No cambiar la terminal heredada. |
| D06-06 | Conservar una propuesta con ALFA capturado al cargar la página | Exhibir un defecto de integración que los tests de dominio y HTTP no detectan. No atribuirlo a una herramienta comercial. |
| D06-07 | Leer la selección dentro del evento submit | Corregir W05 sin tocar reglas de dominio ni respuesta HTTP. |
| D06-08 | Separar vacío y error; ocultar resultados anteriores durante la consulta | Evitar que una consulta fallida se interprete como ausencia de artículos o que se muestre un resultado previo. |
| D06-09 | Usar Chromium real con Playwright solo para pruebas de interfaz | W05–W06 requieren DOM e interacción reales. La aplicación funciona sin Node. |
| D06-10 | No aprobar extremo a extremo sin prueba de navegador | HTTP correcto demuestra una capa; una dependencia bloqueada debe conservar esa clasificación. |

## Supuestos explícitos

Se trabaja con cuatro artículos sintéticos y dos opciones de almacén. El navegador
y el servidor están en la misma máquina. La búsqueda responde a la acción de
consultar; no consulta en cada pulsación. Los controles permanecen deshabilitados
mientras se espera la respuesta para evitar envíos simultáneos desde este formulario.

La validación HTTP acepta cualquier cadena no vacía como almacén y conserva el
comportamiento del dominio para un código desconocido. No se certifican parámetros
duplicados, consultas Unicode exhaustivas, recuperación frente a todos los errores
posibles ni accesibilidad completa. La interfaz muestra códigos, no un listado de
nombres enriquecidos: ese es el contrato de `resumir_catalogo`.

## Atribución y evidencia

La aplicación se construyó localmente durante este encargo. Los ejemplos de
`prompts/` se prepararon para el libro. No son transcripciones de Grok Build ni
demuestran una generación comercial. La disponibilidad real de esa herramienta y
los resultados técnicos locales se documentan por separado.
