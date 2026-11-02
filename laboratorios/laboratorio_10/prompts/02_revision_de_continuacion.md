# Encargo didáctico: revisar la decisión de continuación

Ejemplo preparado para el libro. No representa una interacción comercial ejecutada.

```text
Revisa diferencias/propuesta_a_solucion.diff y contexto/TRAZABILIDAD.md.
Explica qué observación autoriza la consulta posterior y qué significa
el código de salida global. Sigue T02 desde el CSV inválido hasta la
importación, el paso consulta y resultado.json.

Comprueba que una consulta exitosa no oculte un rechazo anterior y que
NO EJECUTADO no tenga stdout, stderr ni hashes inventados. Comprueba
también la distinción entre BLOQUEADO sin captura e integridad FALLIDA.

Coteja el input efectivo: entrada.csv debe ser el archivo usado por la
CLI y el SHA-256 debe corresponder a esos bytes. Revisa que las rutas
con espacios y un directorio de trabajo ajeno no elijan otro script.

Conserva los 74 casos heredados y exige sólo T02 FALLIDO en propuesta.
La solución debe aprobar T01–T08. No agregues tolerancias a otros fallos.
No deduzcas atomicidad global: si la importación ya se confirmó y luego
falla consultar, explica qué permanece y qué debe investigar una persona.

Devuelve hallazgos con archivo, comportamiento observable, evidencia y
límite. No reescribas la evidencia para producir un resultado esperado.
```
