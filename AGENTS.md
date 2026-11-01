# Instrucciones para trabajar en los laboratorios

## Propósito y alcance

Este repositorio reúne ejercicios sintéticos del libro «Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro». El principio rector es definir bien el trabajo y reconocer con evidencia cuándo está terminado.

Lee `README.md`, `CONTINUIDAD.md` y el paquete `contexto/` del laboratorio antes de modificarlo. Los capítulos 1–9 son borradores pendientes de revisión del autor. El documento maestro editorial v1.0 sigue vigente en las entregas del libro.

## Trabajo autorizado

- Utiliza exclusivamente código y datos sintéticos. No accedas a sistemas productivos, repositorios privados ajenos a este material, credenciales ni APIs privadas.
- Conserva los originales importados en `laboratorios/`, `distribuciones/` e `historiales/`. Realiza prácticas en `trabajo/`, ignorada por Git. Una nueva versión publicada del material debe ser un incremento explícito y revisable.
- Para Git del laboratorio 4, usa `python herramientas/preparar_laboratorio_04.py`. El directorio visible `laboratorios/laboratorio_04/repositorio/` no es un repositorio Git independiente; sus instrucciones originales se aplican a la copia preparada.
- No reescribas historia, sustituyas evidencias ni elimines fallos didácticos para obtener una ejecución verde. No publiques ni amplíes visibilidad sin una instrucción que lo autorice.
- Una instrucción expresa del autor puede autorizar un nuevo incremento o una operación de publicación dentro de este proyecto. No solicites otra autorización por decisiones rutinarias ya incluidas en ese encargo.

## Contratos que deben conservarse

C01–C04: habilitado con existencias locales aparece; deshabilitado no; sin existencias disponibles no; existencias sólo en otro almacén no. La regla siempre utiliza el almacén solicitado.

B01–B06: búsqueda por fragmento del nombre con `strip()` y `casefold()`; búsqueda vacía conserva el catálogo disponible; el almacén se propaga correctamente. Lee la batería para sus ejemplos concretos.

N01–N10: detalle por coincidencia exacta del código dentro del catálogo disponible; devuelve un diccionario o `None`. No se normalizan códigos ni se admiten prefijos. Entradas del ejercicio: cadenas.

P01–P06: resumen de artículos disponibles por almacén y nombre; almacén, total y códigos; terminal JSON con almacén obligatorio. Lee ALCANCE.md del laboratorio 5. La propuesta omite el nombre intencionalmente; la solución conserva los 26 criterios.

W01–W06: resumen HTTP real por almacén y nombre, 400 sin almacén, transición ALFA→BETA y distinción entre vacío y error en navegador. Lee ALCANCE.md del laboratorio 6. Sus 26 contratos anteriores siguen intactos; W04 y W06 tienen subcasos.

Las existencias absolutas forman parte de I01–I08. No implementes cantidades solicitadas, reservas, aplicación completa ni capítulos posteriores sin el encargo correspondiente.

I01–I08: importación CSV de existencias absolutas, validación del archivo completo, identificadores exactos, rechazo sin cambios parciales, repetición idempotente e informe trazable. Lee `laboratorios/laboratorio_07/contexto/CONTRATO_INTEGRACION.md`. Los 17 casos nuevos se suman a los 34 casos heredados de la solución. La propuesta suma por error y conserva FALLIDO en I01/I07.

D01–D08: persistencia explícita en SQLite, procesos CLI/HTTP separados, diagnóstico de la conexión efectiva, recorrido CSV→pantalla, reinicio, rechazo de configuración inválida, atomicidad/idempotencia entre procesos e independencia de bases. Lee `laboratorios/laboratorio_08/contexto/CONTRATO_DEPURACION.md`. Son once casos además de los 51 heredados. Propuesta y solución tienen el mismo diagnóstico; sólo difieren en propagar la conexión al resumen. El diagnóstico no puede sobrescribir la base y sus alias conservan las diferencias útiles entre orígenes.

## Método CLARO

1. Contextualiza objetivo, comportamiento actual y esperado, archivos y datos relevantes.
2. Limita el cambio y explicita lo que queda fuera.
3. Acuerda criterios observables antes de implementar.
4. Resuelve en incrementos y revisa las diferencias.
5. Observa y documenta comandos, entorno, resultados y limitaciones.

## Verificación y evidencia

`python herramientas/verificar_todo.py --navegador --salida trabajo/otra_verificacion` ejecuta el recorrido completo en copias temporales y requiere una carpeta nueva. Python 3.11+, Git y dependencias de navegador instaladas según el README. Las pruebas usan HTTP local; no descargan herramientas. Sin `--navegador`, el alcance dominio/HTTP puede aprobar, pero el global queda NO EJECUTADO, aunque la salida sea 0.

Conserva el patrón exacto de fallos esperados: C04 en el inicial del laboratorio 1; B05 y B06 en el defecto del laboratorio 3; P04 y P05 en la propuesta del laboratorio 5; W05 en propuesta del laboratorio 6 al ejecutar navegador; I01/I07 en propuesta del laboratorio 7. Un fallo diferente es un problema pendiente. B01–B06 en la base del laboratorio 3 y P01–P06 en la base del laboratorio 5 permanecen NO EJECUTADO. Los ocho casos web de base 6 también quedan NO EJECUTADO porque allí no existe la web. En base 7 sí existe la web; sus 17 casos de importación permanecen NO EJECUTADO.

En el laboratorio 4, comprueba tanto las etiquetas como el árbol de trabajo cuando haya modificaciones. El verificador histórico por sí solo no acredita el código editado.

En el laboratorio 8, los fallos didácticos admitidos son exclusivamente D03, D04, D05 y D08.a en propuesta; los once D de base permanecen NO EJECUTADO. D02 debe aprobar incluso en propuesta porque su diagnóstico expone fielmente el origen equivocado. Un error de infraestructura no equivale al defecto esperado. Ejecuta también las ocho pruebas de `herramientas/pruebas/test_huellas_evidencia.py` y registra sus resultados por separado. El comprobador de huellas debe verificar todas las salidas declaradas, sin fijar el recuento histórico como constante.

Clasifica cada comprobación como APROBADO, FALLIDO, BLOQUEADO o NO EJECUTADO. Distingue ejecución local, informe aportado, ejemplo didáctico y uso real de una herramienta comercial. No inventes métricas, conversaciones, aprobaciones ni resultados. Conserva huellas originales y registra nuevas huellas cuando un saneamiento cambie bytes.

## Confidencialidad y comunicación

Revisa texto, código, datos, rutas, resultados, metadatos e historial. Omite personas, clientes, marcas laborales, direcciones identificables, secretos y combinaciones que reconozcan sistemas reales. Las tecnologías públicas necesarias para enseñar pueden nombrarse. Para afirmaciones actuales sobre productos, utiliza fuentes oficiales y registra la fecha de consulta.

Al cerrar una tarea, explica qué cambió, qué ejecutaste, qué resultó y qué queda pendiente. La evidencia nueva de Codex auditada y la carpeta histórica aún ausente son sesiones distintas; ninguna acredita Copilot. El estado editorial de esta preparación es ESTADO_DEL_LIBRO_v1.8.2.md y el operativo es ESTADO_REPOSITORIO_v1.7.2.md; las revisiones recibidas 1.8.1/1.7.1 se conservan exactas. Los estados posteriores al cierre del laboratorio 8, libro 1.7.4 y repositorio 1.6.4, y su aclaración de entorno WSL ya están incorporados como antecedentes exactos. El cierre Windows y remoto del laboratorio 7 está confirmado por los estados 1.6.2 y 1.5.2, conservados como antecedentes. La producción del capítulo 8 conserva sin cambios el auxiliar de huellas y sus ocho pruebas. Las huellas finales corresponden a bytes guardados; los históricos nunca se reparan retroactivamente.

El cierre del laboratorio 8 está confirmado en 9212ee99b88f70f0b289837b88d6bbf34da91a52. El autor ha invocado el encargo de cierre del laboratorio 9: autoriza incorporar documentación y evidencia revisadas, crear el commit, integrar en main conservando avances y publicar mediante push atómico sólo main y las etiquetas ligeras nuevas lab-09-v1.0 y repositorio-v1.5. El estado de preparación conserva la publicación pendiente; registra el resultado real y los estados posteriores fuera del commit que acreditan. Conserva las trece etiquetas históricas y cualquier referencia añadida después, sin forzar ni reaplicar el parche. No redactar todavía el capítulo 10.

## Corrección de recursos del laboratorio 8

La ejecución Windows v1.0 resultó FALLIDO por limpieza de bases abiertas y está auditada. La distribución 1.0.1 corrige los auxiliares y añade cuatro pruebas de recursos. No confundir las nuevas regresiones con criterios funcionales. Conservar captura Windows fallida, distribuciones anteriores y pruebas del recolector. La ejecución corregida Windows del autor está APROBADO y conservada en evidencia_integracion/cierre_laboratorio_08_windows/. El cierre añade documentación y evidencia, conservando el código probado. No reaplicar la corrección ni reutilizar su auxiliar sobre un árbol documental distinto.

## Incremento de confiabilidad y seguridad del laboratorio 9

Lee `laboratorios/laboratorio_09/contexto/CONTRATO_SEGURIDAD.md`, registrado antes de implementar. La base es la solución corregida del laboratorio 8: sus 62 casos heredados se ejecutan en los tres estados, incluida base. La nueva política HTTP añade S01–S08 con doce casos. Rechaza parámetros repetidos después de decodificar, claves adicionales, entradas demasiado largas y codificación inválida; conserva búsqueda y disponibilidad.

La base conserva FALLIDO exactamente en S02.a/S02.b/S02.c, S03, S04.a/S04.b, S05.a/S05.b y S06; son exigencias nuevas ausentes en la base, no regresiones históricas. La propuesta convierte pares a dict demasiado pronto y falla exclusivamente S02.a/S02.b/S02.c. La solución debe aprobar los 74 casos. Nunca aceptes un error de ejecución como un fallo didáctico.

El recolector y sus ocho pruebas permanecen sin cambios. Las nuevas pruebas focales del evaluador se contabilizan separadas de los contratos funcionales. No reutilices la cifra histórica de huellas como constante: comprueba todas las declaradas en cada ejecución. Mantén también los intentos bloqueados y su posterior resolución.
