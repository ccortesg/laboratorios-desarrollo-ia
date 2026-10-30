# Alcance previo del laboratorio 3

**Estado de este documento:** contrato didáctico escrito antes de implementar la búsqueda y sus estados. **Fecha:** 30 de octubre de 2026. Los resultados de ejecución se registrarán después, en `evidencia`; las expectativas siguientes no son resultados observados.

## Incremento elegido

Crear `buscar_catalogo(almacen, texto)` para buscar una subcadena en el nombre de los artículos disponibles del almacén indicado. La función debe reutilizar `consultar_catalogo("solucion", almacen)` del laboratorio 2 y aplicar después el filtro de nombre. La disponibilidad conserva C01 a C04.

`almacen` y `texto` son cadenas. El término se normaliza con `strip().casefold()` y se compara con el nombre transformado con `casefold()`. Un término vacío o compuesto por espacios devuelve todos los artículos disponibles en ese almacén. La salida es una lista de diccionarios con `codigo` y `nombre`, en el orden recibido del catálogo. No se modifican los datos, el SQL ni el contrato de la consulta original.

No se implementarán búsqueda aproximada, equivalencia de acentos, cantidades solicitadas, reservas, persistencia, una API, una interfaz ni servicios externos. Los tipos de entrada distintos de cadenas quedan fuera del contrato del incremento. La tecnología del ejercicio no determina el stack de una futura aplicación.

## Criterios y expectativas

| Criterio | Entrada o situación | Resultado esperado |
| --- | --- | --- |
| C01 | ALFA, término vacío; A01 habilitado con existencias locales | A01 aparece |
| C02 | ALFA, término vacío; A02 deshabilitado con existencias locales | A02 se excluye |
| C03 | ALFA, término vacío; A03 sin existencias disponibles | A03 se excluye |
| C04 | ALFA, término vacío; A04 con existencias sólo en BETA | A04 se excluye |
| B01 | ALFA, `"  LoCaL  "` | Registro completo de A01 |
| B02 | ALFA, espacio, tabulación y espacio | Registro completo de A01 |
| B03 | ALFA, `"inexistente"` | Lista vacía |
| B04 | ALFA, `"otra"` | Lista vacía |
| B05 | BETA, término vacío | Registro completo de A04 |
| B06 | BETA, `" OTRA "` | Registro completo de A04 |

Las cuatro funciones de prueba C01 a C04 conservarán sus aserciones literales. En los nuevos estados se ejecutarán a través de la búsqueda con término vacío. B01 a B06 comprobarán resultados públicos; no inspeccionarán cómo se escribió la implementación.

## Secuencia prevista

1. **Base:** conservar la consulta corregida y el ejecutor del laboratorio 2. Ejecutar C01 a C04. La búsqueda aún no existe, por lo que B01 a B06 deben figurar como NO EJECUTADO en este estado.
2. **Generado:** añadir una primera implementación pequeña de la búsqueda. Ejecutar C01 a C04 y B01 a B06.
3. **Refactorizado:** extraer un filtro puro de nombre, conservando la entrada y salida públicas. Repetir exactamente la misma batería.
4. **Defecto:** preparar una copia didáctica del estado refactorizado que omita transmitir el almacén a la consulta. El valor por defecto ALFA debe permitir observar por qué una ejecución limitada a ALFA resulta insuficiente. Se prevén fallos pertinentes en B05 y B06.
5. **Corregido:** transmitir de nuevo el almacén, repetir la batería y revisar la diferencia mínima.

Se conservarán los estados y diferencias de cada recorrido. Un resultado global APROBADO exigirá los resultados previstos para cada estado, incluidos exactamente los fallos de aserción B05 y B06 en el defecto. Un fallo distinto o un error inesperado no se aceptará como demostración correcta.

## Evidencia y límites

El verificador registrará comandos, salidas saneadas, entorno, resultados por criterio y huellas de los archivos. La versión defectuosa debe terminar su batería con código 1; ese fallo intencional se distinguirá de cualquier problema pendiente del estado corregido. APROBADO, FALLIDO, BLOQUEADO y NO EJECUTADO se interpretarán junto al objeto que describen.

La ejecución es local. No acredita uso del laboratorio dentro de Codex, GitHub Copilot o Grok Build, una comparación de prompts, productividad ni validación productiva. Los encargos serán ejemplos didácticos preparados para el libro; no transcripciones históricas.
