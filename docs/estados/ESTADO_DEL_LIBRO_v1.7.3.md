# Estado del libro · cierre documental del laboratorio 8 preparado

**Versión documental:** 1.7.3. **Fecha:** 31 de octubre de 2026, UTC-07:00.
**Antecedente:** `ESTADO_DEL_LIBRO_v1.7.2.md`, conservado sin cambios.

## Decisiones editoriales

El documento maestro editorial v1.0, CLARO, el índice y la promesa siguen vigentes. Los capítulos 1–8 y sus Word permanecen pendientes de revisión expresa del autor. No se modificaron los manuscritos ni se redactó el capítulo 9.

## Ejecución Windows acreditada

La revisión `REVISION_LABORATORIO_08_WINDOWS_v1.0.md` confirma la ejecución corregida aportada por el autor: 65 baterías, 583 ejecuciones funcionales, 571 aprobaciones y doce fallos didácticos exactos; cero bloqueos y cero errores de ejecución. Los 48 NO EJECUTADO en baterías y diez criterios ausentes se registran aparte. Las ocho pruebas del recolector, cuatro de recursos y nueve del evaluador aprueban, sin sumarse a las ejecuciones funcionales.

Se comprobaron 102/102 huellas del conjunto, 10/10 auxiliares y 253/253 archivos del manifiesto del ZIP recibido; el propio manifiesto completa sus 254 archivos. El antecedente Windows fallido se conserva íntegro. El recorrido CSV→CLI→SQLite→HTTP→navegador funciona con la base importada y el mismo servidor activo.

## Incorporación documental preparada

El nuevo incremento incorpora la revisión completa, su evidencia saneada, los estados 1.7.2/1.6.2 y este registro de preparación. Actualiza las referencias de continuidad y documenta que la etiqueta prevista `lab-08-v1.0` identificará la primera publicación del laboratorio 8, que incluye la distribución técnica corregida 1.0.1. La distribución 1.0 continúa como antecedente.

El código, datos, contratos, distribuciones, herramientas comunes y evidencias anteriores conservan sus bytes respecto del árbol Windows verificado `9ea6109fe8e89a2785bdce255252ffaabea1d122`. La incorporación documental cambia el árbol Git; la nueva identidad se registra en `BASE_CIERRE.json` del paquete y en la ejecución del auxiliar. La conservación del código justifica reutilizar la evidencia funcional existente; no se declara una ejecución funcional nueva.

## Autorización y estado real

El autor autorizó expresamente el cierre: commit, integración en main, creación exclusiva de `lab-08-v1.0` y `repositorio-v1.4`, y publicación sin forzar referencias. Esa autorización permite completar el procedimiento, pero no acredita que las operaciones ya se hayan ejecutado.

En esta preparación: Windows funcional **APROBADO**; documentación y procedimiento **PREPARADOS**; commit de la integración, main, etiquetas nuevas y push **NO EJECUTADO en la copia del autor**. La sesión de preparación utiliza una copia Linux aislada y no tiene acceso al Git Bash de Windows del autor.

El cierre confirmado se generará después de comprobar las referencias publicadas, fuera del commit que acredita, como `ESTADO_DEL_LIBRO_v1.7.4.md` y su estado operativo correspondiente. No añadir ese comprobante a un nuevo commit implícito ni mover las etiquetas para incluirlo.

## Siguiente operación

Aplicar el parche documental mediante el auxiliar del paquete de cierre, revisar las diferencias, crear el commit y seguir los pasos de integración/publicación. Si main avanzó, conservarlo y revisar su relación con el material aprobado; si cambia código, realizar las comprobaciones pertinentes. Después, aportar el ZIP de cierre para la revisión final del estado remoto. La revisión editorial de los capítulos 1–8 sigue pendiente.
