# Contrato previo del laboratorio 5

**Versión:** 1.0. **Decisión de producción:** 31 de octubre de 2026 (UTC).
Este contrato se escribe antes de implementar el incremento. Es material sintético
preparado para el libro; no es una transcripción de una sesión de Copilot.

## Problema y punto de partida

La solución del laboratorio 4 permite buscar artículos disponibles por almacén
y nombre, y consultar un código exacto. Falta una salida breve que indique cuántos
artículos coinciden y cuáles son sus códigos. Se necesita revisar esa salida sin
construir una interfaz web ni volver a definir la disponibilidad.

Se copian sin cambios los ocho archivos funcionales del estado `solucion`:
`laboratorio.py`, `catalogo.py`, `detalle.py`, `pruebas.py`,
`pruebas_detalle.py`, `datos/esquema.sql`, `datos/ejemplos.sql` y
`solucion/consulta.sql`. Los veinte criterios C01–C04, B01–B06 y N01–N10
mantienen exactamente sus métodos, entradas y expectativas.

## Comportamiento esperado

Un módulo nuevo, `resumen.py`, expone `resumir_catalogo(almacen, texto="")`.
Las entradas son cadenas. Devuelve un diccionario con tres claves:

- `almacen`: la cadena recibida, sin normalización.
- `total`: cantidad de artículos que devuelve `buscar_catalogo(almacen, texto)`.
- `codigos`: sus códigos, en el orden recibido.

Cuenta artículos, no unidades de existencias. Reutiliza la búsqueda existente,
incluido el filtro de disponibilidad por almacén y la normalización del nombre.
No cambia la coincidencia exacta de códigos de `obtener_articulo`.

El mismo módulo incluye una interfaz de terminal:
`python resumen.py --almacen BETA --nombre " OTRA "`.
`--almacen` es obligatorio; `--nombre` es opcional y vale cadena vacía.
Una consulta válida escribe únicamente un objeto JSON en stdout y termina con 0.
La ausencia de `--almacen` termina con 2 y no produce un JSON de éxito en stdout.
No escribe archivos ni usa la red. La función no valida tipos fuera de las entradas
de cadena definidas por este contrato.

## Estados y componentes

- `estados/base/`: los ocho archivos heredados; todavía no existe `resumen.py`.
- `estados/propuesta/`: los mismos ocho archivos más una propuesta didáctica
  intencionalmente incorrecta. Consulta el almacén pero omite el filtro de nombre.
- `estados/solucion/`: los mismos ocho archivos más el módulo corregido.
- `pruebas_resumen.py`: seis comprobaciones nuevas sobre resultados públicos.
- `verificar.py`: ejecuta las baterías por estado, conserva salidas y contrasta
  el patrón esperado de aprobaciones, fallos deliberados y criterios no ejecutados.
- `contexto/`, `prompts/`, `diferencias/` y `evidencia/`: límites, encargos,
  diferencias revisables y resultados locales, con procedencia explícita.

La propuesta incorrecta es un ejemplo construido para enseñar revisión. No se
atribuirá a Copilot ni a otra herramienta comercial. Los estados de referencia
no son una prueba de una interacción comercial.

## Criterios nuevos y comprobaciones necesarias

| ID | Entrada y frontera | Resultado esperado |
| --- | --- | --- |
| P01 | Función: ALFA, texto omitido | `{"almacen":"ALFA","total":1,"codigos":["A01"]}` |
| P02 | Función: BETA, texto vacío | `{"almacen":"BETA","total":1,"codigos":["A04"]}` |
| P03 | Función: BETA, `" OTRA "` | El mismo resumen de BETA con A04 |
| P04 | Función: ALFA, `"otra"` | `{"almacen":"ALFA","total":0,"codigos":[]}` |
| P05 | Terminal: BETA, `"inexistente"` | Salida 0; stdout es exactamente un objeto JSON con BETA, total 0 y códigos vacíos; stderr vacío |
| P06 | Terminal: sin `--almacen` | Salida 2; stdout vacío; mensaje de uso en stderr |

Las expectativas se expresan literalmente. Las pruebas no llaman a la misma
implementación para calcular el resultado esperado. P01 distingue artículos de
unidades; P02 conserva selección de ubicación; P03 conserva la normalización;
P04 detecta el filtro omitido; P05 comprueba además la conexión de la terminal;
P06 obliga a elegir ubicación explícitamente en la nueva interfaz.

Los veinte criterios heredados se ejecutarán en los tres estados. P01–P06 se
registrarán como NO EJECUTADO en `base`, porque el incremento aún no existe, y se
ejecutarán sin cambios en `propuesta` y `solucion`. Se esperan fallos por aserción
en P04 y P05 de `propuesta`; la solución debe aprobar las veintiséis comprobaciones.
Esta sección describe expectativas, no resultados observados.

## Alcance y exclusiones

No se añaden artículos, dependencias externas ni servicios. Se conservan los
cuatro registros sintéticos. No se implementan cantidades solicitadas, reservas,
frontend, autenticación, autorización, concurrencia, despliegue ni persistencia.
No se evalúan orden o recuento con múltiples coincidencias, Unicode exhaustivo,
tipos de entrada ajenos al contrato ni rendimiento. El reto podrá proponer una
extensión de la evidencia sin presentarla como ya ejecutada.

Python 3.10 o posterior y su biblioteca estándar bastan. Esta elección corresponde
al laboratorio, sin fijar la tecnología de la futura aplicación del libro.
Los originales del laboratorio 4 y el repositorio remoto permanecen intactos.
