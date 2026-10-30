# Responsabilidades y contratos del laboratorio 3

## Componentes implementados

| Parte | Responsabilidad | Relación |
| --- | --- | --- |
| `laboratorio.py` | Preparar una base SQLite en memoria, ejecutar la consulta y devolver artículos | Lee esquema, datos y SQL; cada llamada reconstruye el estado |
| `datos/` y `solucion/consulta.sql` | Expresar los datos sintéticos y la disponibilidad por almacén | Se conservan desde el capítulo 2 |
| `estados/generado.py` | Consultar disponibilidad y filtrar nombres en una función | Primera implementación nueva |
| `estados/refactorizado.py` | Separar acceso a datos y filtro puro | Misma interfaz pública de búsqueda |
| `estados/defecto.py` | Exhibir la omisión intencional del almacén | Activa el valor por defecto ALFA de la consulta |
| `estados/corregido.py` | Restituir la transmisión del almacén | Implementación final del incremento |
| `recorrido.py` | Elegir un estado explícito y presentar registros como JSON | No decide la disponibilidad ni sustituye el filtro |
| `pruebas.py` | Comparar diez criterios con expectativas | Usa la interfaz pública de la búsqueda |
| `comparar.py` | Mostrar diferencias de texto sin modificar archivos | Usa `difflib`; no ejecuta parches |
| `verificar.py` | Ejecutar baterías, observaciones y guardar evidencia | Comprueba el patrón esperado de cada estado |

## Flujo vigente

En un estado de búsqueda, la terminal o las pruebas entregan almacén y texto a `buscar_catalogo`. La función llama a `consultar_catalogo("solucion", almacen)`. El ejecutor construye la base en memoria, aplica la consulta y devuelve artículos disponibles. El filtro de nombre selecciona coincidencias de esa lista. La terminal serializa el resultado a JSON.

El estado `base` termina después de consultar disponibilidad: no tiene función de búsqueda. En `refactorizado` y `corregido`, `filtrar_por_nombre(articulos, texto)` separa la transformación de una lista del acceso a datos. La función pura no cambia los diccionarios ni la lista recibida; los devuelve por referencia en una lista nueva. No se promete una copia profunda.

`defecto` conserva las piezas, pero omite el segundo argumento al consultar. El defecto está en la transmisión de la entrada, no en el SQL que recibe un valor ya equivocado para la petición original.

## Contratos y alcance de evidencia

El contrato base sigue siendo `consultar_catalogo(version, almacen="ALFA")`, con la única versión `solucion`. Devuelve una lista de diccionarios `codigo` y `nombre`, ordenada por código; los cambios en memoria no persisten. La CLI base original sigue disponible.

La búsqueda recibe dos cadenas y devuelve un subconjunto ordenado de esos registros, según la regla de normalización documentada en CONTEXTO. Los comportamientos fuera del contrato no se normalizan ni validan en este incremento. Las pruebas conservan C01 a C04 y agregan B01 a B06, sin llamar a los helpers internos.

La ausencia de mutación, el orden conservado por el bucle y la separación de responsabilidades se revisan por lectura del código; no constituyen pruebas adicionales ejecutadas. Los ejemplos con un único artículo disponible por almacén no prueban el orden de una salida múltiple.

## Evolución propuesta

**PROPUESTA, NO IMPLEMENTADA:** una interfaz podría presentar la búsqueda antes de crear solicitudes. Haría falta decidir entradas, errores, autorizaciones, persistencia, actualización de datos y requisitos de volumen. No se ha elegido framework ni desplegado servicio alguno. D03 mantiene visible esta posibilidad sin convertirla en parte del laboratorio.
