# Repositorio sintético del capítulo 4

Este directorio es un repositorio Git local autónomo. La etiqueta `inicio` identifica el catálogo corregido del laboratorio 3, adaptado a un árbol único. La etiqueta `solucion` incorpora la consulta por código exacto. El directorio se entrega situado en `solucion`, dentro de la rama `main`.

Desde este directorio ejecuta `python pruebas.py` para evaluar el árbol de trabajo actual. En `inicio` se esperan diez criterios C01–C04 y B01–B06; en `solucion`, esos diez más N01–N10. Si tu intérprete se llama `python3` o `py -3`, sustituye el comando de forma consistente.

```text
git status --short
git log --oneline --decorate
git diff --stat inicio solucion --
git diff inicio solucion -- detalle.py pruebas_detalle.py pruebas.py
python pruebas.py
```

Lee `ALCANCE.md`, `AGENTS.md` y `contexto/`. Los prompts de `prompts/` se prepararon para enseñar, no son transcripciones de una sesión comercial. La función `obtener_articulo` no existe en `inicio`; no uses ese estado como implementación del incremento.

Para practicar desde la base, crea primero una copia del paquete descomprimido. En esa copia, comprueba que `git status --short` no muestre cambios y ejecuta `git switch -c practica inicio`. Si ya tienes cambios, no fuerces el cambio de rama ni los borres. La copia distribuida sirve como referencia para comparar tu solución.

El README del directorio superior explica las verificaciones históricas y la evidencia. El verificador superior prueba los commits etiquetados; para comprobar tus ediciones sin commit ejecuta las pruebas en este directorio.
