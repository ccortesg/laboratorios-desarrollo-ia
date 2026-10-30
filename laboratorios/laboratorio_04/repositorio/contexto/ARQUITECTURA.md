# Responsabilidades del repositorio con consulta exacta

## Implementado

| Componente | Responsabilidad |
| --- | --- |
| `laboratorio.py` | Crear SQLite en memoria, cargar datos y ejecutar la consulta parametrizada |
| `datos/` | Esquema y cuatro artículos sintéticos |
| `solucion/consulta.sql` | Disponibilidad por habilitación, almacén y cantidad positiva |
| `catalogo.py` | Consultar disponibilidad y filtrar por subcadena del nombre |
| `detalle.py` | Seleccionar un registro disponible por código exacto, o devolver `None` |
| `pruebas.py` y `pruebas_detalle.py` | Evaluar C01–C04, B01–B06 y N01–N10 contra resultados públicos |
| `contexto/` y `AGENTS.md` | Expresar contratos, responsabilidades y continuidad |

`catalogo.py` es una copia exacta de `estados/corregido.py` del laboratorio 3. La consulta sigue siendo `consultar_catalogo(version, almacen="ALFA")`, con única versión `solucion`; cada llamada reconstruye los datos y devuelve diccionarios `codigo` y `nombre` ordenados por código. No hay persistencia.

La búsqueda transmite el almacén, consulta disponibilidad y filtra nombres. Su helper devuelve una lista nueva con diccionarios por referencia; no promete copia profunda. Los diez escenarios no prueban orden entre múltiples artículos disponibles ni Unicode exhaustivo.

## Flujo de la consulta exacta

`obtener_articulo(almacen, codigo)` llama a `consultar_catalogo("solucion", almacen)`. Compara el código con cada registro disponible y devuelve el que coincide, o `None`. Reutilizar la consulta conserva habilitación, cantidad positiva y ubicación en un único lugar. La función no usa el filtro de nombres porque la normalización textual no forma parte del contrato del identificador.

No se añadió una interfaz de terminal propia: las pruebas llaman a la función pública. El recorrido no demuestra rendimiento bajo volumen; recorre la lista disponible generada por la consulta. No se mide eficiencia ni se cambia la arquitectura para resolver necesidades aún no definidas.

## Evolución propuesta

**PROPUESTA, NO IMPLEMENTADA:** una interfaz y un servicio para solicitudes requerirían definir usuarios, errores, autorizaciones, persistencia, concurrencia y volumen. D03 conserva esa posibilidad. Este laboratorio no elige un framework ni despliega servicios.
