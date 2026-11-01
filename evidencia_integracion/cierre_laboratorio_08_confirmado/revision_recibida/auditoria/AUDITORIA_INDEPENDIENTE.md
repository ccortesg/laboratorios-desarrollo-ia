# Auditoría independiente del cierre del laboratorio 8 desde WSL

**Estado: APROBADO.** Revisión de sólo lectura de `EVIDENCIA_CIERRE_LAB08_WSL_01.zip`, sin ejecutar código contenido en el archivo ni consultar el repositorio remoto.

## Identidad observada

- SHA-256 del ZIP: `0cc40f48d9ce456c9f88cc333fb5ec1a6614cc332b7ee43a10804a751198d37f`.
- Commit de cierre registrado: `9212ee99b88f70f0b289837b88d6bbf34da91a52`.
- Árbol de cierre registrado: `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0`.
- Base histórica: `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`.
- Árbol Windows corregido de origen: `9ea6109fe8e89a2785bdce255252ffaabea1d122`.

## Comprobaciones realizadas

Se comprobaron 36 puntos, con 36 aprobados y 0 fallidos. El ZIP conserva 116 archivos; su manifiesto cubre exactamente los otros 115 y todos los SHA-256 coinciden. La copia del paquete original contiene 27 archivos, incluidos su manifiesto y los 26 elementos que éste declara. No se alteró el archivo recibido.

Las 23 capturas conservan 22 operaciones exitosas y un fallo de infraestructura resuelto. Se comprobaron los 46 archivos stdout/stderr contra el manifiesto y las 32 huellas finales explícitas de las capturas 08–23. Las primeras siete capturas no incluyen huellas separadas de captura y saneamiento; sus 14 flujos sí están cubiertos por el manifiesto final. Esta diferencia está reconocida en las notas y no se suplió inventando hashes.

Los seis enlaces SHA-256 entre configuración, manifiesto original, antes, preparado, prepublicación y resultado final coinciden. La secuencia conserva el árbol Windows corregido, incorpora exactamente 25 rutas documentales y registra un índice final de 549 rutas cambiadas respecto a la base. El mapa protegido contiene 1.486 rutas disjuntas del incremento documental. Su cotejo sobre todos los blobs debe validarse en la revisión Git externa: esta auditoría no dispone de esos 1.486 contenidos dentro del ZIP.

## Publicación y preservación

Los argumentos y resultados conservados acreditan un commit, incorporación de ambos main ya contenidos, avance rápido final, dos etiquetas nuevas y un push con `--atomic --no-follow-tags` limitado a main, lab-08-v1.0 y repositorio-v1.4. Todas las operaciones enumeradas concluyeron con código cero. Las respuestas remotas anteriores y posteriores muestran las once etiquetas históricas sin cambios y únicamente las dos nuevas. Las identidades locales y remotas registradas coinciden con el commit y árbol indicados.

La comprobación del estado remoto actual queda en la revisión del agente principal. No se atribuye a esta auditoría una nueva publicación ni una consulta de red.

## Pruebas y entorno

La captura de las ocho pruebas del recolector contiene ocho casos distintos con resultado `ok`, resumen `Ran 8 tests`, `OK` y código cero. Se ejecutaron en WSL2/Linux con Git 2.34.1 y Python 3.10.12 para los auxiliares. La modificación `core.filemode=false` se registra mediante `git config --local`, por tanto limitada a la configuración del repositorio. Las capturas muestran el ajuste sin cambios de contenido o modo de índice en las verificaciones documentales.

La captura 06 conserva un error por `index.lock` y código 128; la captura 07 registra el mismo refresco exitoso. El diagnóstico del proceso concurrente figura como explicación del ejecutor: las capturas prueban el bloqueo y su resolución, pero no identifican por sí solas el proceso propietario del lock.

Las **583 ejecuciones funcionales** y sus resultados corresponden a la ejecución histórica Windows del autor. No se suman a las ocho nuevas pruebas WSL ni se presentan como una nueva verificación funcional del cierre.

## Observación editorial menor

Los estados 1.7.4 y 1.6.4 y el campo `metodo_subida` del resultado conservan una referencia fija a la «salida de Git Bash» procedente del auxiliar. `NOTAS_ENTORNO_Y_ALCANCE.md` aclara expresamente que esta publicación se ejecutó con Git Linux desde WSL, y las capturas lo corroboran. Conviene expresar el entorno correcto en la nueva continuidad, manteniendo sin cambios la evidencia original. La discrepancia no invalida la conservación de referencias ni el resultado de cierre.

Los capítulos 1–8 continúan pendientes de revisión editorial del autor. El capítulo 9 no se redactó. Los comprobantes posteriores al push se conservan fuera del commit; no se requiere otro commit ni mover etiquetas para acreditar este cierre.

## Confidencialidad y límites

Se inspeccionaron los registros y documentos nuevos para localizar rutas personales, correos, credenciales en URL y tokens comunes, sin coincidencias. Las rutas y URL del repositorio sintético autorizado se conservan donde cumplen una función operativa. Esta comprobación de patrones no demuestra por sí sola la ausencia de cualquier secreto imaginable.

Un manifiesto SHA-256 permite comprobar integridad frente a los valores declarados; no aporta una firma de autoría. La conclusión se basa en la correspondencia de hashes, identidades, comandos, salidas y tiempos conservados. No se ejecutó ningún script recibido, prueba funcional, navegador ni comando Git mutador.
