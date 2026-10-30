# Encargo con CLARO

**Prompt didáctico preparado para el libro.** Su texto es reutilizable; no representa una sesión ejecutada dentro de una herramienta comercial.

```text
OBJETIVO
Prepara una nota de continuidad del catálogo local usando sólo los
archivos de este laboratorio. Debe permitir retomar el trabajo en
otra sesión y conservar su comportamiento actual.

C — CONTEXTUALIZA
Lee README.md y contexto/CONTEXTO.md. Inspecciona los tres SQL,
laboratorio.py y pruebas.py. Usa contexto/ARQUITECTURA.md para
seguir las responsabilidades y contrástalas con los archivos.
Distingue requisitos, implementación, expectativas y evidencia.

L — LIMITA
No cambies la regla, los datos ni las cuatro comprobaciones.
No construyas interfaz, API, persistencia ni servicios externos.
La arquitectura futura es una propuesta, no código existente.

A — ACUERDA
La nota debe identificar la regla del almacén y C01 a C04,
las rutas que la implementan y verifican, los comandos de ejecución,
las decisiones vigentes y propuestas y los pendientes concretos.
No puede depender de recordar una conversación anterior.

R — RESUELVE
Revisa contexto/DECISIONES.md y contexto/CONTINUIDAD.md.
Primero señala contradicciones o información ausente. Después
redacta la nota con referencias precisas, sin repetir todo el código.
Si propones ampliar funciones, sepáralo del encargo actual.

O — OBSERVA
Ejecuta python verificar.py --salida mi_evidencia en una carpeta nueva.
Informa los resultados realmente observados y su alcance.
Si no puedes ejecutar, indica qué precondición falta y qué queda
BLOQUEADO o NO EJECUTADO; no conviertas expectativas en resultados.
Identifica por separado cualquier revisión documental realizada.
```

Si una herramienta no puede leer archivos, suministra los fragmentos pertinentes y sus nombres relativos; registra esa limitación. La existencia de un archivo no demuestra que una herramienta lo haya leído. La nota debe justificar sus afirmaciones con materiales concretos del paquete.
