# Encargo de cierre del laboratorio 9

Continúa el proyecto sintético «Desarrollo de Software en la Era de la IA» en la copia existente de `laboratorios-desarrollo-ia`.

Ejecuta este encargo completo con autonomía en las decisiones rutinarias. Este encargo, cuando el autor lo invoque, autoriza incorporar la documentación y evidencia revisadas, crear el commit de cierre, integrar en main conservando sus avances y publicar main junto con únicamente las etiquetas nuevas `lab-09-v1.0` y `repositorio-v1.5`. No publiques nada en otros repositorios ni cambies la visibilidad del proyecto.

La revisión que produjo este archivo no ejecutó esas operaciones. Comprueba el estado real antes de actuar y registra cada resultado, sin convertir una expectativa en evidencia.

## 1. Insumos y punto de partida

Localiza y lee:

- `REVISION_LABORATORIO_09_WSL_v1.0.zip`, su informe Markdown, manifiesto y verificador.
- `ESTADO_DEL_LIBRO_v1.8.1.md` y `ESTADO_REPOSITORIO_v1.7.1.md`, incluidos en esa revisión.
- `EVIDENCIA_LABORATORIO_09_WSL_v1.0.zip`, conservada dentro de la revisión.
- `BASE_INTEGRACION.json` e instrucciones del paquete original `INTEGRACION_LABORATORIO_09_v1.0`, si siguen disponibles.
- `AGENTS.md`, `CONTINUIDAD.md`, `README.md`, `VERSIONES.md`, `PROCEDENCIA.json` y los estados del repositorio.

Repositorio autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

Punto de partida auditado:

- HEAD y main: `9212ee99b88f70f0b289837b88d6bbf34da91a52`.
- Árbol de base: `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0`.
- Rama del autor: `codex/integracion-laboratorio-09`.
- Árbol del índice ya preparado: `251105483bc5bef040c57dc3a036d5bc3a7e0da0`.
- Parche ya aplicado: SHA-256 `219e9b2f2353c0b55c3418d3af3277f643ce5ce151deebafcd4f425d31cc8f42`.
- ZIP de evidencia original: SHA-256 `6aaeb6ce9e0cf781239499fae2f57bb147b5b2b07b7a20d5cfbd5d61a4ffb239`.

No reapliques el parche: las 771 rutas ya están preparadas. No ejecutes de nuevo una integración desde cero ni recuperes destructivamente la base anterior. La copia del autor conserva trece etiquetas históricas; los nombres previstos para el 9 estaban ausentes al terminar la revisión. Comprueba de nuevo todas las referencias actuales, incluidas las que puedan haberse añadido después.

Identifica si trabajas desde Windows nativo o WSL/Linux. La evidencia ya aprobada es WSL2 y utilizó Python 3.12.16, SQLite 3.53.1, Node 22.23.1, Playwright 1.62.1 y Chromium 151.0.7922.34. Existe un runtime Python aislado bajo `trabajo/`; comprueba su disponibilidad en vez de asumir que el `python3` del sistema es el intérprete funcional.

## 2. Verifica y conserva antes de añadir documentación

Verifica los bytes del paquete de revisión y su cobertura. Comprueba la huella del ZIP original y lee las auditorías, los resultados y los registros antes/preparado/después. Conserva los originales.

Registra rama, HEAD, árbol de HEAD, índice, main local, origin/main, todas las etiquetas locales/remotas y cualquier cambio sin preparar. Usa una carpeta nueva bajo `trabajo/`, sin sobrescribir intentos anteriores.

Consulta el remoto mediante `git fetch --no-tags origin` y una consulta de referencias. Comprueba la ascendencia respecto de la base auditada. Si los archivos ya preparados coinciden con el árbol auditado y la base no cambió, registra esa coincidencia. Si difieren, investiga antes de continuar: conserva cambios ajenos y separa una adaptación real de una modificación accidental.

La futura incorporación documental cambiará el árbol del índice. Conserva ambos identificadores: árbol funcional auditado y árbol documental de cierre. Después de añadir documentos no exijas que ambos sean iguales.

## 3. Incorpora la revisión sin alterar el contenido verificado

Añade los estados 1.8.1/1.7.1 exactos a `docs/estados/`. Incorpora el informe, las auditorías, los insumos de revisión y el ZIP original bajo una carpeta nueva `evidencia_integracion/revision_laboratorio_09_wsl/`. Conserva el paquete de revisión original cuando sea útil para trazabilidad; evita duplicar recursivamente paquetes que contengan su propia evidencia.

Actualiza sólo la documentación operativa necesaria, incluidas las referencias de README, continuidad, versiones, instrucciones y procedencia. Genera los siguientes estados de preparación, libro 1.8.2/repositorio 1.7.2, como **cierre preparado, publicación pendiente**. Si esas versiones ya existen, examina su procedencia y utiliza una nueva versión sin sustituir antecedentes.

No cambies código, pruebas, datos de referencia, distribuciones ni evidencias históricas para hacer coincidir una comprobación. Mantén el recolector y sus ocho pruebas. No regeneres ZIP anteriores ni recalcules sus huellas. Los manuscritos y el maestro editorial quedan fuera de este cierre.

Comprueba que los cambios posteriores al árbol auditado son los documentos autorizados. Registra rutas y hashes. Añade al índice únicamente las rutas documentales revisadas; conserva los cambios funcionales del 9 que ya estaban preparados. No utilices una inclusión indiscriminada de `trabajo/`, dependencias, bases temporales o capturas originales sin sanear.

## 4. Verificaciones previas al commit

La evidencia WSL auditada conserva 92 baterías y 805 ejecuciones: 781 APROBADO, 24 FALLIDO didácticos exactos, cero bloqueos y cero errores de ejecución. Las 48 omisiones históricas y diez criterios ausentes se registran aparte. Solución 9: 74/74. Infraestructura separada: 8/9/4. Huellas finales del envío: 210/210, distribuidas en 156 funcionales, ocho de auxiliares y 46 de operaciones.

Esos números son resultados anteriores acreditados, no una nueva ejecución de este cierre. No repitas las 805 pruebas si sólo añadiste documentación y comprobaste que las fuentes funcionales, datos, pruebas y dependencias relevantes conservan su identidad. Ejecuta las ocho pruebas del recolector con el intérprete adecuado y comprueba todas las huellas declaradas de la evidencia utilizada; registra ambos alcances por separado.

Si una adaptación a avances de main modifica contenido funcional o pruebas, verifica el resultado compuesto con navegador y evidencia nueva antes de publicarlo. No ajustes los fallos esperados. Conserva cualquier intento FALLIDO o BLOQUEADO y resuelve su causa sin sobrescribirlo.

Revisa `git diff --cached --check`, diferencias preparadas, ausencia de cambios inesperados y conservación de los archivos protegidos. Mantén las referencias históricas. El manifiesto debe comprobar los bytes finales después del saneamiento; las capturas originales y finales siguen siendo campos distintos.

## 5. Crea el commit e integra conservando avances

Cuando las verificaciones pertinentes aprueben, crea el commit autorizado con un mensaje descriptivo, por ejemplo `Integra laboratorio 9 y evidencia WSL auditada`. Registra su SHA completo y su árbol; no inventes esos valores anticipadamente.

Vuelve a consultar origin/main y conserva tanto main local como remoto. Si han avanzado, incorpora sus cambios en la rama de integración sin reset destructivo, reescritura ni publicación forzada. Resuelve conflictos con revisión de contenido y repite únicamente las comprobaciones que exijan los cambios reales. No descartes trabajo posterior para recuperar el árbol antiguo.

Integra en main mediante avance rápido cuando la relación lo permita. Si no lo permite, prepara primero una rama que conserve ambas historias y comprueba el resultado. No uses `--force`, `reset --hard`, `clean` ni sustituciones masivas de archivos para resolver la integración.

## 6. Etiquetas y publicación limitada

Antes de crear etiquetas, consulta de nuevo main y las etiquetas remotas. Comprueba que todas las referencias históricas conservan su identidad. No borres ni fuerces ninguna.

Crea únicamente `lab-09-v1.0` y `repositorio-v1.5` sobre el commit final revisado de este cierre. Usa etiquetas ligeras, coherentes con las publicaciones anteriores. Si alguna ya existe en el mismo commit porque se está reanudando este cierre, consérvala y verifica su procedencia; no la recrees. Si apunta a otro objeto o existe una situación incompatible, conserva el estado y explica el conflicto antes de publicar.

Publica exclusivamente las tres referencias autorizadas mediante push atómico:

```bash
git push --atomic --no-follow-tags origin refs/heads/main:refs/heads/main refs/tags/lab-09-v1.0:refs/tags/lab-09-v1.0 refs/tags/repositorio-v1.5:refs/tags/repositorio-v1.5
```

No uses `--tags`, `--all` ni variantes forzadas. Si el push se rechaza por un avance remoto o cualquier otra causa, conserva la evidencia, vuelve a consultar las referencias y adapta sólo lo que esté autorizado sin mover etiquetas. No declares publicada una operación fallida ni supongas que no hubo cambios ante una respuesta indeterminada: consulta el remoto.

## 7. Comprueba el cierre real y entrega evidencia

Después de la publicación, verifica los SHA de main y ambas etiquetas mediante consultas remotas; comprueba también las etiquetas históricas, el árbol del commit, las ramas y el estado local. Si main avanza por una intervención posterior, registra su nueva identidad y relación de ascendencia sin retrocederlo. Las etiquetas del cierre deben conservar el commit publicado.

Genera fuera del commit que acreditan, bajo una carpeta nueva de `trabajo/`:

- Un informe de cierre con base, commit y árbol reales, comandos, entorno, códigos de salida y referencias antes/después.
- `CIERRE_LABORATORIO_09_CONFIRMADO_v1.0.md`, únicamente si la publicación quedó efectivamente confirmada.
- Estados posteriores libro 1.8.3/repositorio 1.7.3, o las siguientes versiones libres, que describan el resultado real. Si no se publicó, deben conservar el bloqueo o pendiente en vez de afirmar un cierre.
- Un ZIP de evidencia con manifiesto SHA-256, comprobación de cobertura y hashes finales, por ejemplo `EVIDENCIA_CIERRE_LABORATORIO_09_WSL_v1.0.zip` si el entorno fue WSL.

Mantén los comprobantes posteriores fuera del commit que verifican para evitar una referencia circular. Distingue la ejecución funcional WSL ya auditada de las pruebas y operaciones nuevas del cierre. No atribuyas a esta tarea las 805 ejecuciones salvo que realmente las repitas y registres por separado.

Entrega el ZIP, su SHA-256, los documentos finales y una explicación del estado alcanzado. Conserva pendiente la revisión editorial de los capítulos 1–9. No redactes el capítulo 10.
