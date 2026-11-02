# Encargo didáctico: construir una operación local

Ejemplo preparado para el libro. No es una conversación histórica ni evidencia de ejecución en un producto comercial.

## Encargo insuficiente

> Automatiza la importación y muestra el catálogo al terminar.

Faltan el origen que se debe modificar, la condición de continuación, las garantías del recibo y los límites de la automatización. Una consulta correcta puede ocultar una importación rechazada.

## Encargo mejorado con CLARO

```text
C — Contextualiza
Trabaja en este laboratorio sintético. Lee README, contexto/CONTEXTO.md,
contexto/CONTRATO_AUTOMATIZACION.md y contexto/ARQUITECTURA.md.
Las CLI persistencia.py importar y consultar ya existen. La base es
explícita y persistente; las fuentes heredadas se conservan exactas.

L — Limita
Añade un operador de importación y consulta local. No inicialices bases
automáticamente, no arranques servicios, no aceptes comandos, URLs ni
planes ejecutables y no implementes programación periódica.

A — Acuerda
Respeta T01–T08 y los 74 casos heredados. Prevalida CSV, base y salida;
rechaza salida existente o protegida antes de importar. Guarda los bytes
de entrada en entrada.csv dentro de un recibo nuevo y usa esa copia para
la CLI. Sólo consulta después de observar importación confirmada.
En un rechazo, conserva FALLIDO y marca consulta NO EJECUTADO, sin
capturas inventadas. Ante imposibilidad de iniciar un proceso, conserva
BLOQUEADO aunque no existan huellas. No afirmes una transacción global.

R — Resuelve
Construye con subprocess y argumentos en listas, shell=False y tiempo
límite. Separa precondiciones, ejecución de cada paso y cierre del recibo.
Mantén un único defecto didáctico en propuesta: continuar tras una
importación rechazada. La solución debe detenerse.

O — Observa
Ejecuta las mismas comprobaciones sobre ambos estados. Registra códigos,
respuestas reales, snapshot, SHA-256 y huellas capturadas/finales. T08
debe mantener vivo un servidor sobre la misma SQLite y comprobar HTTP
y navegador antes y después de la operación. Distingue resultados nuevos,
evidencia histórica e infraestructura. No publiques ni cambies etiquetas.
```

Este encargo es una referencia para el lector. Los resultados válidos son los registrados en las carpetas de evidencia, no una respuesta ilustrativa del asistente.
