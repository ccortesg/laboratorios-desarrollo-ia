# Instrucciones de trabajo para el laboratorio sintético

Lee explícitamente `ALCANCE.md`, `contexto/CONTEXTO.md` y
`contexto/ARQUITECTURA.md` antes de proponer un cambio. Este archivo se entrega
como contexto legible; su presencia no acredita que un producto lo haya cargado
automáticamente.

Conserva las tres referencias de `estados/`, los ocho archivos heredados y las
expectativas C01–C04, B01–B06 y N01–N10. Los cambios experimentales se hacen en una
copia nueva. No añadas dependencias, servicios, datos reales ni conexiones.

Para comprobar las referencias: `python verificar.py --salida nueva_evidencia`.
El destino debe ser nuevo. Distingue P04/P05 fallidos en la propuesta del resultado
corregido. No describas una ejecución local como uso de Copilot.

Al cerrar, entrega los archivos cambiados, su motivo, criterios comprobados,
comandos, resultados observados y límites. No borres fallos para mejorar un resumen.
