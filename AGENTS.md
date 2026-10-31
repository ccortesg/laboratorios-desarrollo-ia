# Instrucciones para trabajar en los laboratorios

## Propósito y alcance

Este repositorio reúne ejercicios sintéticos del libro «Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro». El principio rector es definir bien el trabajo y reconocer con evidencia cuándo está terminado.

Lee `README.md`, `CONTINUIDAD.md` y el paquete `contexto/` del laboratorio antes de modificarlo. Los capítulos 1–6 son borradores pendientes de revisión del autor. El documento maestro editorial v1.0 sigue vigente en las entregas del libro.

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

No implementes cantidades, reservas, aplicación completa ni capítulos posteriores sin el encargo correspondiente.

## Método CLARO

1. Contextualiza objetivo, comportamiento actual y esperado, archivos y datos relevantes.
2. Limita el cambio y explicita lo que queda fuera.
3. Acuerda criterios observables antes de implementar.
4. Resuelve en incrementos y revisa las diferencias.
5. Observa y documenta comandos, entorno, resultados y limitaciones.

## Verificación y evidencia

`python herramientas/verificar_todo.py --navegador --salida trabajo/otra_verificacion` ejecuta el recorrido completo en copias temporales y requiere una carpeta nueva. Python 3.10+, Git y dependencias opcionales de navegador instaladas según el README. Las pruebas usan HTTP local; no descargan herramientas. Sin `--navegador`, el alcance dominio/HTTP puede aprobar, pero el global queda NO EJECUTADO, aunque la salida sea 0.

Conserva el patrón exacto de fallos esperados: C04 en el inicial del laboratorio 1; B05 y B06 en el defecto del laboratorio 3; P04 y P05 en la propuesta del laboratorio 5; W05 en propuesta del laboratorio 6 al ejecutar navegador. Un fallo diferente es un problema pendiente. B01–B06 en la base del laboratorio 3 y P01–P06 en la base del laboratorio 5 permanecen NO EJECUTADO. Los ocho casos web de base 6 también quedan NO EJECUTADO porque allí no existe la web.

En el laboratorio 4, comprueba tanto las etiquetas como el árbol de trabajo cuando haya modificaciones. El verificador histórico por sí solo no acredita el código editado.

Clasifica cada comprobación como APROBADO, FALLIDO, BLOQUEADO o NO EJECUTADO. Distingue ejecución local, informe aportado, ejemplo didáctico y uso real de una herramienta comercial. No inventes métricas, conversaciones, aprobaciones ni resultados. Conserva huellas originales y registra nuevas huellas cuando un saneamiento cambie bytes.

## Confidencialidad y comunicación

Revisa texto, código, datos, rutas, resultados, metadatos e historial. Omite personas, clientes, marcas laborales, direcciones identificables, secretos y combinaciones que reconozcan sistemas reales. Las tecnologías públicas necesarias para enseñar pueden nombrarse. Para afirmaciones actuales sobre productos, utiliza fuentes oficiales y registra la fecha de consulta.

Al cerrar una tarea, explica qué cambió, qué ejecutaste, qué resultó y qué queda pendiente. La evidencia nueva de Codex auditada y la carpeta histórica aún ausente son sesiones distintas; ninguna acredita Copilot. El estado editorial vigente es ESTADO_DEL_LIBRO_v1.5.md, conservado en las entregas del libro.
