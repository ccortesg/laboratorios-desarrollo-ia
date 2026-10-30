# Instrucciones del repositorio didáctico

Este catálogo y todos sus datos son sintéticos. Lee `ALCANCE.md` y `contexto/CONTEXTO.md` antes de modificar código. `contexto/ARQUITECTURA.md`, `DECISIONES.md` y `CONTINUIDAD.md` explican responsabilidades, decisiones y estado.

Trabaja con Python estándar y SQLite en memoria. Conserva C01–C04, B01–B06, datos, SQL y la transmisión del almacén. Implementa únicamente el incremento cuyo contrato esté definido. Distingue código vigente de propuestas futuras.

Desde la raíz de este repositorio, ejecuta `python pruebas.py`. Tras cambiar, revisa `git status --short`, diferencias del árbol y del área de preparación y los archivos nuevos. Compara `inicio` y `solucion` sólo al estudiar las referencias distribuidas; esa comparación no incluye ediciones actuales. `git diff --check` revisa formato, no comportamiento.

Informa archivos cambiados, comandos ejecutados, resultados observados y límites. No presentes una expectativa como ejecución. Los prompts de `prompts/` son ejemplos didácticos.

No uses servicios externos, red, datos reales, credenciales ni repositorios ajenos. No publiques, contrates servicios, borres trabajo existente ni amplíes el incremento a una aplicación completa. Los permisos efectivos de la herramienta se configuran fuera de este archivo; estas instrucciones no sustituyen su entorno de ejecución.
