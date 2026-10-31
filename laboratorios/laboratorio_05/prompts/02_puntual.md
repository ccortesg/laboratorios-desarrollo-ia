# Encargo puntual

**Prompt didáctico preparado para el libro. No enviado a Copilot.**

Contexto: en esta copia sintética existe `buscar_catalogo(almacen, texto)` en
`catalogo.py`. Devuelve diccionarios `codigo` y `nombre` de artículos habilitados
con existencias positivas en ese almacén y filtra el nombre mediante
`strip().casefold()` del término. Lee su implementación y el contrato de `ALCANCE.md`.

Propón únicamente `resumir_catalogo(almacen, texto="")` para un módulo nuevo
`resumen.py`. Entradas: cadenas. Salida: diccionario con `almacen` recibido, `total`
de artículos coincidentes y lista `codigos` en el orden recibido. Reutiliza
`buscar_catalogo(almacen, texto)`; no cambies SQL, datos, búsqueda ni consulta exacta.

Ejemplos de aceptación: ALFA sin texto da total 1 y A01; BETA sin texto da total 1
y A04; BETA con `" OTRA "` conserva A04; ALFA con `"otra"` da total 0 y códigos
vacíos. No implementes todavía la terminal. Explica la función propuesta y qué
criterios permite revisar. No afirmes que ejecutaste pruebas si no las ejecutaste.

## Qué conserva el desarrollador como responsabilidad inmediata

Revisar que se transmita el nombre y el almacén, que el total cuente artículos,
que la función cumpla P01–P04 y que la integración posterior aún no está comprobada.
Aceptar este fragmento no completa P05 ni P06.
