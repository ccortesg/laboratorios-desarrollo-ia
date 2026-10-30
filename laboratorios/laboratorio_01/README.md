# Laboratorio 01 Disponibilidad de inventario por almacén

Este ejercicio permite observar un defecto de lógica, formular criterios de aceptación y comprobar una corrección. Todos los artículos, almacenes y cantidades se crearon para el libro. No hay conexiones a servicios externos ni datos de producción.

## Qué necesitas

- Entorno de referencia: Python 3.12 con los módulos estándar `sqlite3` y `unittest` disponibles.
- Un editor de texto y una terminal.

La ejecución incluida se realizó con CPython 3.12.14. Otras versiones no se han verificado exhaustivamente; la evidencia acredita únicamente el entorno indicado en `evidencia/entorno.json`.

No es necesario instalar paquetes con `pip`, crear cuentas, configurar un servidor de bases de datos ni usar una herramienta comercial de IA. La base SQLite se construye en memoria y se cierra después de cada consulta. Los scripts no crean una base persistente.

Los comandos siguientes utilizan `python` como nombre genérico del intérprete. En macOS o Linux puede corresponder a `python3`; en Windows, a `py -3`. Comprueba tu instalación con `python --version`, `python3 --version` o `py -3 --version` y utiliza la variante disponible en todos los comandos. Una compilación de Python que omita `sqlite3` necesita ese módulo para ejecutar el ejercicio.

Descomprime el laboratorio y abre una terminal dentro de la carpeta que contiene este archivo y `laboratorio.py`. Los comandos se ejecutan desde esa carpeta. Conserva juntos los archivos y las subcarpetas.

Comprueba los módulos antes de comenzar:

```text
python -c "import sqlite3, unittest; print('Modulos disponibles; SQLite', sqlite3.sqlite_version)"
```

Si el import falla, esa instalación de Python todavía no cumple el requisito. Registra la precondición como **BLOQUEADO** y utiliza una instalación que incluya los módulos; el fallo de preparación es distinto del defecto intencional del catálogo.

## Datos y regla esperada

La ubicación seleccionada en los cuatro criterios es **ALFA**. ALFA y BETA son etiquetas ficticias.

| Artículo | Habilitado | Almacén con registro | Cantidad | ¿Debe aparecer en ALFA? |
| --- | --- | --- | --- | --- |
| A01 | Sí | ALFA | 7 | Sí |
| A02 | No | ALFA | 4 | No |
| A03 | Sí | ALFA | 0 | No |
| A04 | Sí | BETA | 9 | No |

La regla es: un artículo aparece si está habilitado y tiene una cantidad mayor que cero en el almacén solicitado. Un registro en otra ubicación no satisface esa condición. Para este ejercicio, «disponible» significa exactamente cantidad positiva; no hay reservas, compromisos de venta ni unidades en tránsito.

## Archivos

| Ruta relativa | Función |
| --- | --- |
| `datos/esquema.sql` | Define tablas, claves y restricciones del laboratorio. |
| `datos/ejemplos.sql` | Carga los cuatro artículos y sus existencias ficticias. |
| `inicial/consulta.sql` | Consulta con el defecto intencional. |
| `solucion/consulta.sql` | Consulta con la condición de ubicación incorporada. |
| `laboratorio.py` | Prepara la base en memoria y ejecuta la consulta seleccionada. |
| `pruebas.py` | Aplica los mismos cuatro criterios de aceptación a ambas versiones. |
| `verificar.py` | Ejecuta el recorrido completo y guarda evidencia saneada. |
| `evidencia/` | Resultados observados durante la preparación del paquete. |

## 1 Observar el comportamiento inicial

```text
python laboratorio.py --version inicial --almacen ALFA
```

Resultado esperado del estado defectuoso:

```text
Version: inicial
Almacen seleccionado: ALFA
Articulos: A01, A04
```

La consulta inicial comprueba que el artículo esté habilitado y que exista algún registro de cantidad positiva. Omite exigir que ese registro pertenezca al almacén seleccionado. Por eso incluye A04.

## 2 Ejecutar los criterios sobre el estado inicial

```text
python pruebas.py --version inicial
```

La suite contiene exactamente cuatro pruebas: C01 valida la inclusión de A01; C02, la exclusión de A02; C03, la exclusión de A03; y C04, la exclusión de A04.

**Se espera un fallo en C04 y un código de salida 1.** Ese fallo intencional demuestra que las comprobaciones detectan el defecto. Los otros tres criterios deben pasar. Un fallo diferente o una excepción de entorno requieren investigación; no deben clasificarse automáticamente como parte del ejercicio.

## 3 Revisar la corrección

Compara `inicial/consulta.sql` con `solucion/consulta.sql`. La consulta corregida añade esta condición dentro de la subconsulta que comprueba existencias:

```sql
AND e.almacen = :almacen
```

El parámetro se enlaza con `conexion.execute(consulta, {"almacen": almacen})`. Su valor no se concatena al texto SQL. La versión inicial recibe el mismo diccionario, pero omite utilizar el parámetro en su consulta: recibir una entrada no demuestra que la lógica la esté considerando.

La condición queda dentro del mismo `EXISTS` que relaciona las existencias con el artículo. Así, el registro que aporta una cantidad positiva también debe corresponder al almacén solicitado.

## 4 Ejecutar la solución y la misma suite

```text
python laboratorio.py --version solucion --almacen ALFA
python pruebas.py --version solucion
```

Resultado esperado del catálogo corregido:

```text
Version: solucion
Almacen seleccionado: ALFA
Articulos: A01
```

Las cuatro pruebas deben aprobarse y `pruebas.py` debe devolver código 0. La solución no modifica los datos ni las expectativas para obtener ese resultado. El tiempo mostrado por `unittest` depende del equipo y no constituye una medición de productividad.

Una aserción incumplida o una excepción inesperada durante una prueba ejecutada se clasifica como **FALLIDO**. El JSON diferencia `fallos_de_asercion` y `errores_de_ejecucion`, incluye ambos en `fallidos` y registra `tipo_error` por caso. **BLOQUEADO** corresponde a una precondición externa que impide comenzar, como la ausencia de `sqlite3` detectada en la preparación; no se utiliza para ocultar errores del código. Una prueba omitida se registra como **NO EJECUTADO**. En esta suite no hay omisiones previstas.

## 5 Generar tu propia evidencia

```text
python verificar.py --salida mi_evidencia
```

Este comando ejecuta ambas versiones, guarda las salidas y genera:

- `entorno.json`: fecha con desfase UTC, versiones de Python y SQLite y familia de sistema operativo.
- `catalogo_inicial.txt` y `catalogo_solucion.txt`: salidas observadas de las demostraciones.
- `pruebas_inicial.txt` y `pruebas_solucion.txt`: salidas de las pruebas con las rutas de los tracebacks saneadas.
- `pruebas_inicial.json` y `pruebas_solucion.json`: estado por criterio.
- `resumen.json`: resultados, códigos de salida y alcance de la evidencia.
- `sha256_fuentes.json`: hashes de los ocho archivos fuente y de instrucciones que intervienen en el laboratorio.

Los comandos del resumen emplean `python` como nombre portátil. Los subprocesos utilizan realmente el mismo intérprete con el que se inició `verificar.py`; su versión figura en `entorno.json`.

El recorrido completo se considera **APROBADO** si el estado inicial incumple únicamente C04 y la solución satisface los cuatro criterios. El estado de la versión inicial sigue siendo **FALLIDO**, con `fallo_intencional: true`. `verificar.py` devuelve 0 cuando ese recorrido didáctico se reproduce y 1 si hay una discrepancia.

La opción `--salida` escribe en la carpeta indicada y sobrescribe allí los archivos de evidencia con los mismos nombres. Usa una carpeta nueva para conservar ejecuciones anteriores. La carpeta `evidencia` incluida conserva la ejecución de preparación; `mi_evidencia` te permite compararla sin reemplazarla.

## Qué se comprueba y qué queda fuera

Las pruebas verifican resultados del catálogo mediante inclusión o exclusión de códigos. No inspeccionan el texto SQL ni exigen una implementación determinada. La misma suite y los mismos datos se aplican a ambas versiones.

El esquema usa una fila por artículo y almacén, cantidad entera no negativa y un indicador de habilitación restringido a 0 o 1. La restricción `CHECK (typeof(cantidad) = 'integer' AND cantidad >= 0)` exige que la cantidad almacenada tenga tipo entero y sea no negativa. El ejercicio no evalúa reservas, actualización concurrente del inventario, autorización, una API HTTP, interfaz gráfica, rendimiento, despliegue ni compatibilidad con todos los sistemas operativos. La ejecución registrada acredita únicamente el entorno indicado en la evidencia.

Los scripts no invocan Codex, GitHub Copilot ni Grok Build. La ejecución local de Python se distingue del uso de esas herramientas. Un prompt del capítulo puede aplicarse al laboratorio desde la herramienta que el lector tenga disponible, pero esa sesión sería una ejecución independiente que necesita su propio registro.

Los hashes permiten relacionar la evidencia con unos archivos concretos. No son una firma de un tercero ni una certificación de seguridad.

## Reto posterior

Formula la regla para una cantidad mínima solicitada por el usuario y escribe los criterios antes de modificar la solución. Decide el comportamiento cuando la cantidad solicitada sea cero, negativa o mayor que las existencias. Mantén explícito el almacén y conserva los cuatro criterios de este ejercicio. Este reto no está implementado ni verificado en el paquete inicial.
