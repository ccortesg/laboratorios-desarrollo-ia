# Estado operativo · laboratorio 9 auditado y pendiente de cierre

**Versión documental:** 1.7.1. **Fecha:** 1 de noviembre de 2026. **Antecedente conservado:** `ESTADO_REPOSITORIO_v1.7.md`. **Integración técnica prevista:** repositorio v1.5, aún no publicado.

## Identidad vigente

Repositorio sintético autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

| Referencia o contenido | Identidad |
| --- | --- |
| HEAD y main de la ejecución WSL | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |
| main remoto reconsultado | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |
| Árbol de la base | `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0` |
| Rama local del autor | `codex/integracion-laboratorio-09` |
| Árbol del índice preparado y auditado | `251105483bc5bef040c57dc3a036d5bc3a7e0da0` |
| Etiquetas previstas, ausentes | `lab-09-v1.0`, `repositorio-v1.5` |

Consulta independiente de sólo lectura: 1 de noviembre de 2026 a las 15:37:39 de Hermosillo, 22:37:39 UTC. Las trece etiquetas históricas mantienen los hashes de la base documental. Main no había avanzado y no fue necesaria una adaptación. Una consulta posterior prevalecerá si registra un avance real; no se debe retroceder una rama para conservar estas identidades.

## Ejecución y revisión

Evidencia aportada: `EVIDENCIA_LABORATORIO_09_WSL_v1.0.zip`, SHA-256 `6aaeb6ce9e0cf781239499fae2f57bb147b5b2b07b7a20d5cfbd5d61a4ffb239`. Revisión nueva: `REVISION_LABORATORIO_09_WSL_v1.0.zip` y su informe homónimo.

El paquete original aprobó 373 archivos y cobertura completa en la sesión del autor. Se aplicó una vez el parche, SHA-256 `219e9b2f2353c0b55c3418d3af3277f643ce5ce151deebafcd4f425d31cc8f42`. Las 771 rutas y el árbol del índice coinciden con el paquete probado. Las advertencias de espacios finales no alteraron esos bytes; `git diff --cached --check` terminó con cero.

Los 1.502 hashes protegidos del registro previo coinciden con la base conocida. El cotejo final local aportado conserva esos archivos y las trece etiquetas. No hay cambios sin preparar ni nuevos archivos no ignorados. Los estados y evidencias de la revisión actual todavía no forman parte del índice del autor: deberán añadirse como incremento documental del cierre y producirán otro árbol, que se registrará por separado.

| Comprobación | Resultado auditado |
| --- | --- |
| Conjunto funcional 1–9 | APROBADO; 92 baterías; 805 ejecuciones; 781 aprobaciones, 24 fallos didácticos, cero bloqueos y cero errores de ejecución |
| Omisiones históricas | 48 NO EJECUTADO en baterías y diez criterios ausentes aparte |
| Solución 9 | 74/74 APROBADO, incluidos 62 casos heredados |
| Infraestructura separada | Recolector 8/8; evaluador 9/9; recursos SQLite 4/4 |
| Fuentes | 387/387 referencias coincidentes; laboratorio 4 cotejado mediante sus manifiestos propios |
| Manifiesto del envío | 452/452 archivos; 453 archivos contando el manifiesto |
| Huellas finales | 210/210: 156 funcionales + ocho de auxiliares + 46 de operaciones |

Los fallos didácticos conservan sus IDs y tipo de aserción. No se admitió un TimeoutExpired, error de infraestructura o fallo adicional. Las 23 operaciones de preparación documentadas terminaron con código cero.

Entorno funcional: Linux/WSL2, Python 3.12.16, SQLite 3.53.1, Git 2.34.1, Node 22.23.1, npm 10.9.8, Playwright 1.62.1 y Chromium 151.0.7922.34. Se utilizó un runtime Python aislado bajo `trabajo/`. El navegador arrancó realmente. Esta evidencia no es Windows nativo ni una ejecución remota de CI.

## Conservación y límites de atribución

No se modificaron laboratorios, distribuciones ni evidencias históricas durante esta auditoría. El ZIP recibido se conserva exacto. Las dos capturas originales cuyos hashes difieren de los finales no están en el envío; sus bytes finales sí coinciden. Su conservación original fuera del ZIP queda atribuida a la sesión del productor.

La auditoría verificó los archivos recibidos y el contenido conocido; no accedió directamente al disco WSL del autor ni repitió las 805 ejecuciones. La consulta GitHub de esta revisión es nueva. Las ejecuciones Windows históricas, el cierre anterior WSL, la producción Linux del 9 y la ejecución WSL ahora aportada permanecen diferenciados.

Las URL del repositorio autorizado se mantienen únicamente en documentación operativa y copias exactas de sus insumos. Los manuscritos siguen fuera del repositorio técnico. El maestro editorial no cambia y los capítulos 1–9 continúan pendientes de revisión del autor.

## Próximo paso y prohibiciones vigentes

La integración está **APROBADA para continuar con el cierre**, pero aún no existe un commit del laboratorio 9. En esta revisión no se integró main, no se crearon ni movieron etiquetas y no se hizo push. No se redactó el capítulo 10.

El siguiente encargo puede autorizar incorporar estos documentos y la evidencia, preparar un árbol documental nuevo, crear el commit, conservar avances de main y publicar sólo main con `lab-09-v1.0` y `repositorio-v1.5`. `PROMPT_CIERRE_LABORATORIO_09_v1.0.md` describe ese trabajo futuro. No reaplicar el parche de integración ya incorporado. No afirmar una publicación hasta comprobar las referencias remotas y registrar el resultado real.
