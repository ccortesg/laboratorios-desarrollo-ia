# Encargo didáctico para un repositorio

**Ejemplos preparados para el libro.** No son transcripciones de prompts ejecutados en Codex ni evidencia de una respuesta comercial.

## Encargo insuficiente

Añade el detalle del artículo y deja el repositorio listo.

Falta precisar entrada, respuesta, disponibilidad, archivos, comprobaciones y significado de «listo».

## Encargo con CLARO

```text
Implementa el incremento definido en ALCANCE.md.
C: Lee AGENTS.md, ALCANCE.md y contexto/. Inspecciona
   laboratorio.py, catalogo.py, los datos, el SQL y pruebas.py.
   Resume el estado actual antes de editar.
L: Añade detalle.py y pruebas_detalle.py. Conecta las pruebas
   nuevas en pruebas.py y actualiza los cuatro documentos
   de contexto. Conserva datos, SQL y catálogo existentes.
   Trabaja sólo localmente, sin dependencias nuevas ni red.
A: obtener_articulo(almacen, codigo) devuelve un registro
   disponible con código exacto o None. Conserva C01–C04
   y B01–B06 y satisface N01–N10. No normalices el código.
R: Parte de la etiqueta inicio en una copia de trabajo.
   Comprueba primero la base. Implementa el incremento
   y muestra las diferencias, incluidos archivos nuevos.
O: Ejecuta python pruebas.py sobre el árbol actual. Informa
   comandos, criterios, resultados y límites. Revisa el diff
   y cierra con un resumen que otra sesión pueda continuar.
   Si no puedes ejecutar, indica el impedimento y el estado.
```

La autoridad del encargo y los permisos de ejecución se evalúan en la sesión real. Este ejemplo no autoriza acceso a sistemas ajenos. Antes de atribuir el trabajo a Codex, verifica modalidad, acceso y ejecución efectivos. La sesión realizada durante la producción se documenta por separado en la evidencia del laboratorio.

## Encargo de revisión

```text
Revisa el cambio actual contra ALCANCE.md.
Relaciona cada archivo cambiado con el incremento autorizado.
Comprueba que el almacén llega a la consulta y que el código
se compara exactamente. Revisa expectativas de pruebas,
archivos nuevos, diferencias preparadas y sin preparar.
Ejecuta python pruebas.py; distingue observación e inferencia.
No añadas funciones nuevas. Informa hallazgos con su evidencia
u observa explícitamente que no encontraste defectos en este
alcance, sin garantizar ausencia de otros problemas.
```
