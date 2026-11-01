# Cierre confirmado del laboratorio 8

**Versión:** 1.0. **Fecha:** 1 de noviembre de 2026. **Estado:** APROBADO.

## Continuidad vigente

El laboratorio 8 está integrado en `main` y publicado. La consulta independiente realizada el 1 de noviembre de 2026 a las 20:48:55 UTC confirma:

| Referencia | Identidad |
|---|---|
| `main`, `lab-08-v1.0` y `repositorio-v1.4` | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |
| Árbol de ese commit | `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0` |
| Padre del commit | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| Árbol Windows corregido de origen | `9ea6109fe8e89a2785bdce255252ffaabea1d122` |

Fuente remota: [commit publicado](https://github.com/ccortesg/laboratorios-desarrollo-ia/commit/9212ee99b88f70f0b289837b88d6bbf34da91a52) y `auditoria/REFERENCIAS_REMOTAS_CONFIRMADAS.json`, conservada en el paquete de revisión. Las once etiquetas históricas mantienen sus valores anteriores. Las dos etiquetas nuevas identifican este cierre y no requieren recreación ni desplazamiento.

Los insumos operativos actuales son:

1. `DOCUMENTO_MAESTRO_EDITORIAL_v1.0.md`: decisiones editoriales vigentes.
2. `ESTADO_DEL_LIBRO_v1.7.4.md`: estado posterior a la publicación.
3. `ESTADO_REPOSITORIO_v1.6.4.md`: estado posterior a la publicación.
4. `REVISION_CIERRE_LABORATORIO_08_WSL_v1.0.md` y su ZIP: auditoría de la evidencia y consulta remota independiente.
5. Este documento de cierre confirmado.

Los estados 1.7.4 y 1.6.4 y los comprobantes posteriores al push están fuera del commit publicado. Se conservan en el ZIP recibido y, como copias idénticas, en el paquete de esta revisión. No debe suponerse que ya existen dentro del repositorio. Su futura incorporación será documental y preservará las versiones previas.

## Evidencia nueva y antecedente funcional

**Cierre nuevo:** WSL2/Linux, bash y Git Linux 2.34.1; Python 3.10.12 para los auxiliares. Se conservan preparación, revisión del índice, commit, integración por avance rápido, comprobación, creación de dos etiquetas, push atómico exacto y registro posterior. Las ocho pruebas del recolector tienen captura nueva aprobada en WSL. La auditoría actual revisó sus salidas; no las reejecutó.

**Antecedente funcional Windows:** 65 baterías, 583 ejecuciones, 571 aprobaciones, doce fallos didácticos previstos, cero bloqueos y errores de ejecución; 48 NO EJECUTADO y diez criterios ausentes aparte. Las ocho pruebas Windows del recolector, cuatro de recursos y nueve del evaluador se cuentan separadamente. No se ejecutó otra batería funcional completa durante este cierre WSL ni durante la revisión del ZIP.

**Precisión de entorno:** las referencias heredadas a «Git Bash» en los estados 1.7.4/1.6.4 y `metodo_subida` deben entenderse corregidas por esta aclaración: la publicación efectivamente acreditada se realizó desde WSL2/Linux. Las notas de la ejecución ya lo explican. Los originales se conservan sin cambios.

**Incidencia resuelta:** se conserva un intento de refresco del índice con `index.lock` y código 128, seguido de un reintento con código cero. No representa un fallo didáctico ni un bloqueo pendiente. El proceso propietario del lock no fue identificado independientemente por esta revisión.

## Integridad y conservación

El ZIP recibido tiene SHA-256 `0cc40f48d9ce456c9f88cc333fb5ec1a6614cc332b7ee43a10804a751198d37f`. Sus 115 declaraciones coinciden y cubren los otros 115 archivos del ZIP, que contiene 116 en total. La copia del paquete original conserva sus 27 archivos idénticos a la entrega recuperada por separado.

Los 46 flujos stdout/stderr de las 23 capturas están cubiertos por el manifiesto general; 32 cuentan además con huellas finales explícitas comprobadas. Los 14 flujos de las primeras siete capturas no incluyen hashes separados de captura y saneamiento. Esa limitación está declarada y no se reconstruye retrospectivamente.

El contrato diferencia 25 rutas documentales y 1.486 archivos protegidos. El árbol remoto coincide con el árbol documental preparado originalmente. La revisión actual cotejó esa identidad y los registros de conservación; no volvió a calcular individualmente los 1.486 blobs remotos. Se mantienen las distribuciones 1.0/1.0.1 y las evidencias históricas, incluidos los intentos fallidos. La etiqueta `lab-08-v1.0` corresponde a la primera publicación e incluye la solución corregida 1.0.1.

## Pendientes y siguiente tarea

- **Revisión editorial:** capítulos 1–8 pendientes del autor. Las pruebas aprobadas no constituyen aprobación del manuscrito.
- **Capítulo 9:** no redactado en este cierre ni en esta revisión.
- **Publicación del laboratorio 8:** completada y confirmada; no queda un push o una etiqueta pendiente de este cierre.
- **Siguiente tarea recomendada:** preparar el encargo del capítulo 9, «Confiabilidad y seguridad del software generado por IA», con esta continuidad y la solución corregida del laboratorio 8. Reconsultar antes las referencias remotas y conservar cualquier avance. Definir el incremento y sus criterios antes de implementarlo; mantener separados los resultados históricos y las futuras ejecuciones.

Este registro se entrega como documentación posterior al cierre. Esta revisión no hizo commits, merges, creación de etiquetas ni push, y no alteró la evidencia recibida.
