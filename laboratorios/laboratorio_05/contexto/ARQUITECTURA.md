# Componentes y responsabilidades

## Implementado

| Componente | Responsabilidad |
| --- | --- |
| `laboratorio.py` de cada estado | Crear datos en memoria y consultar disponibilidad |
| `datos/` y `solucion/consulta.sql` | Dataset sintético y regla parametrizada por almacén |
| `catalogo.py` | Filtrar el catálogo disponible por nombre |
| `detalle.py` | Consultar un código exacto dentro de lo disponible |
| `resumen.py` en solución | Proyectar resultados a almacén, total y códigos; exponer CLI |
| `pruebas.py` y `pruebas_detalle.py` | Comprobar los veinte criterios heredados |
| `pruebas_resumen.py` | Evaluar P01–P06 mediante función y subproceso |
| `verificar.py` | Ejecutar procesos por estado, capturar evidencia y contrastar el patrón |

El flujo correcto es: entrada de terminal → `resumir_catalogo` → `buscar_catalogo`
→ consulta de disponibilidad → filtro de nombre → resumen → JSON. Una llamada
directa a la función comienza en el segundo paso. La propuesta didáctica salta
`buscar_catalogo` y pierde el filtro de nombre. Esa diferencia explica P04 y P05.

La estructura de carpetas mantiene puntos comparables sin requerir Git para ejecutar
el ejercicio. `comparar.py` regenera diferencias de texto entre estados. Las huellas
de procedencia identifican los archivos heredados. Esto no inventa un historial de
contribuciones de una herramienta.

## Propuesto, no implementado

Una interfaz web y un servicio de solicitudes requerirían definir usuarios, errores,
persistencia, autorización y concurrencia. No se selecciona un framework ni se
incorpora ese trabajo a la solución actual. La capa de resumen no es una API remota.
