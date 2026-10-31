# Decisiones del incremento

**Fecha:** 31 de octubre de 2026 UTC. Vigente significa aplicado al laboratorio;
no indica aprobación editorial del autor.

Se mantienen las decisiones técnicas anteriores: Python estándar, SQLite en memoria,
datos sintéticos, disponibilidad centralizada, búsqueda por nombre y consulta exacta
como contratos distintos, y evidencia nueva sin sobrescribir registros. El historial
original del laboratorio 4 permanece en aquella entrega.

## D11 Resumir el resultado de la búsqueda

**Aplicada.** La necesidad es una salida pequeña y revisable. Se añade un módulo que
usa la búsqueda existente y devuelve un diccionario; no se duplica la regla de
disponibilidad. Cuenta artículos, sin añadir unidades solicitadas ni reservas.

## D12 Añadir una terminal explícita

**Aplicada.** La entrada por terminal permite revisar el encargo completo y detectar
errores entre argumentos y función. El almacén es obligatorio en esta interfaz;
el nombre es opcional. No se altera la interfaz histórica de `laboratorio.py`.

## D13 Comparar alcances sobre el mismo incremento

**Aplicada como material didáctico.** Un prompt pide sólo la función y otro delega
función, CLI, pruebas y evidencia. Se conserva una propuesta incorrecta que omite el
nombre para enseñar por qué veinte regresiones verdes no prueban un requisito nuevo.
No se presenta la propuesta como una respuesta realmente recibida de Copilot.

## D14 Conservar referencias sin requerir Git

**Aplicada.** Tres carpetas y diferencias regenerables permiten seguir el ejercicio
en una extracción autónoma. Los ocho archivos heredados son idénticos. Las baterías
se ejecutan en procesos separados para evitar reutilizar módulos de otro estado.

## D15 Delimitar la evidencia

**Aplicada.** La base no tiene el incremento y sus seis criterios nuevos se registran
como NO EJECUTADO. En la propuesta P04 y P05 deben fallar por aserción; cualquier otro
fallo hace fallar la verificación. La solución debe aprobar veintiséis criterios.
Las observaciones de acceso comercial se registran aparte de las pruebas funcionales.

**Reto pendiente, no implementado:** omitir el argumento de nombre únicamente en
`main()` de otra copia de la solución. Se espera que falle P05 mientras la función
sigue pasando P01–P04; el lector debe corregir esa frontera y restaurar 26/26 sin
cambiar datos ni expectativas. Los recuentos mayores de uno siguen fuera de la
evidencia del dataset actual.
