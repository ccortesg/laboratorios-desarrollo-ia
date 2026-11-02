# Decisiones del laboratorio 10

## Decisiones previas

El contrato previo define una operación fija de importación y consulta. Se conserva como bytes exactos y su SHA-256 figura en PROCEDENCIA.json. Se eligió Python estándar para reutilizar las CLI existentes y mantener separadas automatización de negocio y baterías de prueba.

La entrada se lee una vez y se guarda como `entrada.csv` en el recibo. El importador usa esa instantánea. La carpeta se reserva antes de iniciar la importación y se rechaza cualquier destino ya existente o protegido.

El fallo didáctico consiste únicamente en continuar tras un rechazo de datos del importador. Los errores de precondición y de infraestructura se detienen en ambos estados. Esto permite que T02 detecte una decisión incorrecta sin confundirla con una dependencia ausente.

## Aclaración surgida durante revisión

Se detectó por lectura que un hijo imposible de iniciar no produce capturas. El recolector devuelve NO EJECUTADO cuando no hay huellas; ese estado no debe transformar el bloqueo de la operación en un fallo de integridad. Se corrigieron ambos operadores y se añadió RO01, una regresión de infraestructura con fallo de inicio inyectado. Conserva BLOQUEADO/código 2, consulta NO EJECUTADO y cero huellas; no añade un criterio funcional T.

`importacion_confirmada` significa confirmación observada mediante código 0 y JSON APLICADO. Si un proceso se interrumpe antes de devolver esa confirmación, false no demuestra que la base conserve el estado anterior. La práctica no ofrece recuperación ante interrupción abrupta ni fallo físico. Después de una importación confirmada, un fallo de consulta no revierte la importación.

Las focales iniciales T preceden a esta aclaración de infraestructura y conservan su huella de fuentes. Sus archivos no se reescriben. La comprobación completa posterior corresponde a las fuentes corregidas y se registra por separado.

## Decisiones de continuidad

Los 74 casos heredados y las 71 fuentes declaradas se conservan. La nueva base mantiene la solución 9; no hereda sus defectos didácticos. La interfaz web permanece como componente heredado, con la misma presentación.

El reto de revisión previa no se implementa. Tampoco se añade un planificador, una cola, un agente comercial ni despliegue. El capítulo 10 es un borrador sujeto a revisión del autor, al igual que los capítulos anteriores.
