# Ejemplo didáctico preparado para el libro

**C — Contextualiza.** Lee contexto/CONTRATO_INTEGRACION.md, ARQUITECTURA.md y
TRAZABILIDAD.md. Trabaja sobre una copia de estados/solucion. El CSV contiene
cantidades absolutas y el catálogo consulta existencias locales de artículos
habilitados. Conserva la búsqueda por nombre y los códigos exactos.

**L — Limita.** Implementa lectura, validación, aplicación transaccional e informe
con Python estándar. No añadas web de importación, servicios ni datos reales.
La demostración debe importar y consultar en la misma conexión desechable.

**A — Acuerda.** Conserva C/B/N/P/W y satisface I01–I08 con los subcasos del contrato.
Un error rechaza el archivo completo. Dos aplicaciones sobre la misma base deben
conservar el resultado; los pares omitidos no cambian.

**R — Resuelve.** Propón archivos y diferencias antes de editar. Implementa un
incremento pequeño y revisa la propagación de la conexión hasta la consulta real.

**O — Observa.** Ejecuta pruebas de la copia modificada y registra comandos,
resultados y límites. Separa informe APLICADO de comprobación APROBADO. No atribuyas
pruebas locales a una herramienta comercial ni sustituyas evidencia anterior.
