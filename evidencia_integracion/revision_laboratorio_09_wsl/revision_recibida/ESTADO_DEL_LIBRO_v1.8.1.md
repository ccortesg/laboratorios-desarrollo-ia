# Estado del libro · laboratorio 9 verificado en WSL

**Versión:** 1.8.1. **Fecha:** 1 de noviembre de 2026. **Antecedente conservado:** `ESTADO_DEL_LIBRO_v1.8.md`. **Sustento nuevo:** `REVISION_LABORATORIO_09_WSL_v1.0.zip`.

## Decisiones editoriales vigentes

El maestro editorial v1.0, la promesa, el principio rector, el público, el índice y el método CLARO permanecen vigentes. El capítulo 9 conserva sus diez secciones, 4.236 palabras y crónica sintética de 523 palabras; el Word completo de once páginas no se modifica en esta revisión.

Los capítulos 1–8 siguen pendientes de revisión editorial del autor y el capítulo 9 sigue siendo otro borrador pendiente. La verificación técnica del laboratorio no equivale a aprobación del manuscrito. No hay observaciones editoriales nuevas aportadas en este intercambio ni una autorización para redactar el capítulo 10.

## Nuevo resultado acreditado

El autor aportó la ejecución de Codex en Linux/WSL2 mediante `EVIDENCIA_LABORATORIO_09_WSL_v1.0.zip`, SHA-256 `6aaeb6ce9e0cf781239499fae2f57bb147b5b2b07b7a20d5cfbd5d61a4ffb239`. La auditoría de ese envío es **APROBADO**, sin discrepancias pendientes.

La sesión utilizó Python 3.12.16, SQLite 3.53.1, Git 2.34.1, Node 22.23.1, Playwright 1.62.1 y Chromium 151.0.7922.34. El intérprete funcional quedó aislado bajo `trabajo/`; el Python inicial 3.10.12 se usó para preparación y observaciones. La atribución correcta es WSL/Linux, no Windows nativo.

Se verificaron 92 baterías y 805 ejecuciones: 781 APROBADO y 24 FALLIDO didácticos exactos, cero bloqueos y cero errores de ejecución. Se conservan 48 NO EJECUTADO en baterías y diez ausentes aparte. La solución 9 aprueba 74/74 casos, incluidos los 62 heredados. Las pruebas 8/9/4 de infraestructura permanecen separadas del total funcional.

El envío contiene 453 archivos y un manifiesto que cubre 452, excluyéndose a sí mismo. Las 210 huellas finales coinciden: 156 funcionales, ocho de auxiliares y 46 de operaciones. Las 164 de la revisión contienen las 156 funcionales; no se suman como grupos independientes. Los 387 registros de fuentes cotejados coinciden con el contenido preparado.

La auditoría no ejecutó una batería nueva: revisó la evidencia aportada, cotejó bytes y consultó referencias remotas. Las ejecuciones Linux de producción, esta sesión WSL, las 583 ejecuciones históricas Windows y el cierre WSL anterior del laboratorio 8 siguen separados. Ninguna se convierte retroactivamente en otra.

## Estado técnico y pendientes

HEAD y main permanecen en `9212ee99b88f70f0b289837b88d6bbf34da91a52`, árbol de base `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0`. La rama del autor es `codex/integracion-laboratorio-09` y su índice coincide con `251105483bc5bef040c57dc3a036d5bc3a7e0da0`. La reconsulta remota del 1 de noviembre a las 15:37:39 de Hermosillo, 22:37:39 UTC, mantiene main y las trece etiquetas históricas. Las etiquetas nuevas aún están ausentes.

No se necesita una nueva versión del laboratorio ni una corrección del capítulo a partir de esta auditoría. Queda resuelto el pendiente de ejecutar la integración en el entorno WSL del autor. Permanecen pendientes el cierre documental, el commit, la integración en main y la publicación, que requieren el siguiente encargo. No se ha ejecutado ese cierre durante esta revisión.

El alcance de seguridad sigue siendo una aplicación sintética local; no acredita una evaluación productiva integral, autenticación, autorización ni exposición pública. El reto de cabeceras no se implementó. Los bytes originales de dos capturas saneadas permanecen fuera del ZIP: se verificaron sus bytes finales, sin poder reconstruir los originales desde sus hashes.

## Siguiente tarea recomendada

Usar `PROMPT_CIERRE_LABORATORIO_09_v1.0.md` para incorporar esta revisión, preservar las evidencias y realizar el cierre con Codex cuando el autor invoque ese encargo. El futuro cierre debe registrar lo efectivamente publicado y conservar cualquier avance de main, sin referencias forzadas. Antes de otro capítulo, conviene revisar la voz, la profundidad técnica y la utilidad práctica del borrador.
