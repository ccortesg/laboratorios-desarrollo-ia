# Encargo delegado con CLARO

**Prompt didáctico preparado para el libro. No enviado a Copilot.**

## C — Contextualiza

Trabaja en una copia nueva de `estados/base/`, exclusivamente con el catálogo
sintético. Lee `ALCANCE.md`, `contexto/CONTEXTO.md` y `contexto/ARQUITECTURA.md` del
paquete, además de `catalogo.py`, `laboratorio.py`, `detalle.py` y sus pruebas.
Existen disponibilidad por almacén, búsqueda por nombre y consulta por código exacto.
Falta resumir el resultado de búsqueda para revisarlo desde una terminal.

## L — Limita

Añade `resumen.py` con `resumir_catalogo(almacen, texto="")` y su terminal.
No modifiques los ocho archivos heredados ni la coincidencia exacta de códigos.
No cambies datos, SQL, dependencias ni contratos existentes. No uses red, servicios,
cuentas ni repositorios externos. Trabaja en la copia, conservando las referencias.

## A — Acuerda aceptación

Conserva C01–C04, B01–B06 y N01–N10. Aplica P01–P06 de `ALCANCE.md`: cuenta artículos
coincidentes; conserva almacén y normalización del nombre; devuelve resumen vacío
cuando no hay coincidencias; terminal con JSON válido, salida 0 y stderr vacío;
omitir `--almacen` produce salida 2 y stdout vacío. Usa expectativas literales.

## R — Resuelve en incrementos

Primero identifica el contrato y explica qué archivo vas a añadir. Implementa la
función utilizando `buscar_catalogo(almacen, texto)`. Después añade la terminal y
comprueba su conexión con la función. Revisa las diferencias y ejecuta los veinte
criterios heredados y los seis nuevos en la copia de trabajo. Si falta una capacidad,
registra el impedimento sin simular la ejecución.

Si la copia se llama `mi_practica`, ejecuta desde la raíz del paquete
`python mi_practica/pruebas.py` y
`python pruebas_resumen.py --directorio mi_practica`.
El verificador de referencias no comprueba automáticamente esta copia.

## O — Observa y documenta

Entrega el cambio revisable, los comandos realmente ejecutados, códigos de salida,
resultados por criterio y límites. Relaciona cada cambio con P01–P06. No declares
terminado el trabajo sólo porque la suite anterior pasa. Distingue tu sesión real
de los ejemplos de referencia distribuidos en este paquete. No publiques cambios.

## Qué debe revisar el desarrollador

Al delegar este alcance, revisa función, terminal, pruebas y archivos añadidos.
Confirma que los criterios negativos descubren el filtro omitido y que las
veinte expectativas heredadas permanecen intactas. La revisión y la aceptación
del resultado siguen siendo una decisión del desarrollador.
