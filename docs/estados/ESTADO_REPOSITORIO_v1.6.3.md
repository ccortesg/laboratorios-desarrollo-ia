# Estado operativo · cierre documental del laboratorio 8 preparado

**Versión documental:** 1.6.3. **Fecha:** 31 de octubre de 2026, UTC-07:00.
**Antecedente:** `ESTADO_REPOSITORIO_v1.6.2.md`, conservado sin cambios.

Repositorio autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

## Base y evidencia

- Commit de partida: `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`.
- Rama Windows registrada: `integracion/laboratorio-08`.
- Árbol corregido aprobado en Windows: `9ea6109fe8e89a2785bdce255252ffaabea1d122`.
- Evidencia: `EVIDENCIA_CORRECCION_LAB08_WINDOWS_02.zip`.
- SHA-256: `2e8503f199f85184ef55de2c8808cda7b358e4dd75554a03371be51b4d7b1445`.

La revisión confirma APROBADO, salida 0: 65 baterías, 583 ejecuciones, 571 aprobaciones, doce fallos didácticos, cero bloqueos y cero errores de ejecución; 48 NO EJECUTADO y diez ausentes aparte. Coinciden 102/102 huellas del conjunto, 10/10 auxiliares y los 244 archivos del antecedente. Las pruebas auxiliares 8/4/9 se cuentan por separado. Esta evidencia procede de Windows del autor; no de una simulación de ese entorno.

## Incremento de cierre

El parche documental incorpora la revisión recibida bajo `evidencia_integracion/cierre_laboratorio_08_windows/revision_recibida/`, conservando su estructura y manifiesto. Los estados de revisión se copian a `docs/estados/` y se añaden los de preparación actuales. README, continuidad, versiones, instrucciones de trabajo y metadatos de procedencia se actualizan para reconocer Windows aprobado y la autorización de cierre.

No se modifica ningún archivo de `laboratorios/`, `distribuciones/`, `historiales/`, `herramientas/` ni evidencia previa. El parche sólo admite una lista explícita de documentos y adiciones de evidencia. `BASE_CIERRE.json` del paquete registra el árbol documental resultante y un mapa de huellas de los archivos protegidos. El auxiliar compara el código, los archivos preparados y las referencias antes de cada fase.

La documentación nueva es otro árbol Git. El auxiliar de la corrección anterior, que exige el árbol 9ea6109..., no debe usarse para validar este árbol documental. La comprobación de cierre conserva la atribución de las 583 ejecuciones a su pase Windows original.

## Referencias y publicación prevista

La consulta de preparación confirma main en `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`, once etiquetas históricas y ausencia de las dos nuevas. Se conserva el registro fechado en `evidencia_integracion/cierre_laboratorio_08_windows/REFERENCIAS_PREPARACION_CIERRE.json`. Reconsultar antes de publicar y después.

El autor autorizó crear únicamente `lab-08-v1.0` y `repositorio-v1.4`. La primera etiqueta identifica la primera publicación del laboratorio 8 y contiene `LABORATORIO_08_v1.0.1.zip`, revisión técnica corregida. No sustituye ni mueve etiquetas anteriores. Las versiones documentales, de distribución y de integración tienen funciones distintas.

El procedimiento crea primero un commit en la rama de integración. Después conserva los avances de main local y origin/main, revisa el resultado y realiza un avance rápido de main. La subida utiliza referencias completas, `--atomic` y `--no-follow-tags`, sin `--force` ni publicación indiscriminada de etiquetas.

Si una referencia prevista ya existe o main cambia después de crear las etiquetas, conservar esas referencias y revisar su identidad; no moverlas automáticamente. Si una integración incorpora cambios de código, la conservación documental por sí sola ya no basta y deben ejecutarse las comprobaciones correspondientes.

## Estado y comprobante posterior

Este documento describe la preparación previa al commit/publicación del autor. **NO EJECUTADO en esa copia:** aplicación del cierre documental, commit, integración main, etiquetas nuevas y push. La preparación y prueba local del parche se registran separadamente en el paquete; no equivalen a acciones sobre Windows o GitHub.

Tras la publicación, el auxiliar consulta las referencias reales y genera `RESULTADO_CIERRE.json`, el manifiesto y un ZIP nuevo dentro de `trabajo/`. También produce los estados observados `ESTADO_DEL_LIBRO_v1.7.4.md` y `ESTADO_REPOSITORIO_v1.6.4.md`. Quedan fuera del commit que identifican para evitar autorreferencia y movimientos de etiquetas. Su auditoría remota posterior cerrará la continuidad.

Los manuscritos 1–8 permanecen pendientes de revisión editorial del autor. No se redacta el capítulo 9.
