# Laboratorio 4

## Qué practicarás

Preparar un encargo sobre un repositorio Git local, identificar la base, revisar archivos y diferencias, comprobar un incremento y cerrar con evidencia. El paquete contiene un repositorio real en `repositorio/`, incluido su directorio `.git`, con dos commits sintéticos y dos etiquetas. No requiere descargar capítulos anteriores ni conectarse a un servicio.

El incremento es `obtener_articulo(almacen, codigo)`: devuelve el registro disponible cuyo código coincide exactamente, o `None`. `repositorio/ALCANCE.md` conserva el contrato fijado antes de implementar. La búsqueda por nombre y la disponibilidad del capítulo 3 se mantienen.

## Preparación y dos directorios de trabajo

Descomprime el ZIP y conserva el directorio `.git`, aunque tu explorador lo oculte. Necesitas Git y Python con `sqlite3` y `unittest`. Sólo se usa la biblioteca estándar. El entorno ejecutado figura en `evidencia/entorno.json`; no se acredita compatibilidad con otros entornos sin comprobarlos. Los comandos usan `python`; si tu instalación utiliza `python3` o `py -3`, mantén esa variante.

La **raíz del paquete**, `laboratorio_04`, contiene este README, el verificador, `repositorio/` y la evidencia. La **raíz del repositorio**, `laboratorio_04/repositorio`, contiene código, contexto y `.git`. Cada bloque indica desde dónde ejecutarlo.

Desde la raíz del paquete:

```text
python --version
python -c "import sqlite3, unittest; print(sqlite3.sqlite_version)"
git --version
python verificar.py --salida mi_evidencia
```

`mi_evidencia` debe ser una carpeta nueva, fuera de `repositorio/`. El verificador devuelve BLOQUEADO y código 2 si la salida ya existe, falta Git o falta `.git`. No sobrescribe la evidencia distribuida.

El verificador extrae las etiquetas `inicio` y `solucion` a carpetas temporales y ejecuta sus baterías. **No ejecuta las pruebas sobre tus ediciones actuales del árbol de trabajo.** Para eso usa `python pruebas.py` dentro de `repositorio/`. La distinción permite estudiar referencias estables sin ocultar qué código se comprobó.

## Punto de partida y cambio de referencia

Desde la raíz del repositorio:

```text
git status --short
git log --oneline --decorate
git rev-parse refs/tags/inicio
git rev-parse refs/tags/solucion
git diff --stat inicio solucion --
git diff inicio solucion -- detalle.py pruebas_detalle.py pruebas.py
python pruebas.py
```

`inicio` contiene el catálogo corregido del capítulo 3, sus diez criterios, contexto, AGENTS.md y contrato previo. `solucion` añade la función, diez criterios nuevos, su conexión a la batería y cuatro actualizaciones de contexto. El paquete se entrega con `main` en `solucion`; la batería actual debe aprobar veinte criterios. El separador `--` evita confundir la etiqueta `solucion` con la carpeta SQL del mismo nombre.

| Referencia | Implementado | Expectativa de la batería |
| --- | --- | --- |
| inicio | Disponibilidad y búsqueda por nombre | C01–C04 y B01–B06: diez aprobaciones |
| solucion | Lo anterior más consulta exacta | Los diez anteriores y N01–N10: veinte aprobaciones |

N01–N10 no se ejecutan en `inicio`, donde detalle y su batería no existen. Esa ausencia no es un fallo intencional ni una aprobación. En esta etapa no se incorpora una variante defectuosa nueva.

## Preparar un encargo

Lee `repositorio/AGENTS.md`, `ALCANCE.md` y los cuatro documentos de `contexto/`. El archivo de instrucciones contiene límites y referencias duraderas; el contrato fija el incremento; el contexto describe lo que existe y lo que sigue propuesto. El prompt de `prompts/ENCARGO.md` es un ejemplo didáctico preparado para el libro.

Para practicar desde la base, haz primero una copia del paquete completo y trabaja allí. Desde el repositorio de esa copia, confirma que `git status --short` no muestre cambios y ejecuta:

```text
git switch -c practica inicio
python pruebas.py
```

La expectativa es diez aprobaciones. Encarga o implementa sólo el contrato de `ALCANCE.md`. Conserva intacta la otra copia para revisar la solución de referencia. Si el árbol tiene cambios, no los borres ni fuerces el cambio de rama. Ejecuta siempre `python pruebas.py` sobre el árbol que realmente quieres evaluar.

## Revisar diferencias con la pregunta adecuada

`git status --short` identifica cambios y archivos sin seguimiento. `git diff --` muestra diferencias sin preparar en archivos seguidos; `git diff --cached --` muestra lo preparado para el siguiente commit. Un archivo nuevo sin seguimiento debe abrirse y revisarse expresamente: no aparece en esos diffs hasta que se incorpora al seguimiento. No añadas indiscriminadamente archivos ajenos al encargo.

En el paquete final limpio, `git diff --` devuelve una salida vacía porque el incremento ya está comprometido. `git diff inicio solucion --` muestra el cambio completo entre las dos referencias. La salida vacía del primer comando no demuestra que las referencias sean iguales. La observación registrada está en `evidencia/revision_git.json` y la diferencia completa en `evidencia/cambio.diff`.

`git diff --check inicio solucion --` comprueba problemas de espacios o marcas de conflicto que detecte Git. Su éxito no demuestra disponibilidad correcta ni sustituye las pruebas. Revisa que los siete archivos cambiados correspondan al contrato; el código de datos, SQL y catálogo conserva su contenido. Las referencias primarias de estos comandos son [git status](https://git-scm.com/docs/git-status) y [git diff](https://git-scm.com/docs/git-diff), consultadas el 30 de octubre de 2026.

## Codex y evidencia real

La comprobación de acceso realizada para esta entrega figura en `evidencia/codex_disponibilidad.json`. Se comprobó el ejecutable en PATH; no se encontró Codex CLI. La comprobación de disponibilidad está APROBADA como observación; el inicio del CLI está BLOQUEADO por ese impedimento y la sesión de trabajo con Codex está NO EJECUTADA. No se infiere ausencia de acceso del lector en otro entorno.

Este paquete acredita ejecución local de Git, Python y SQLite. Los prompts preparados no son transcripciones de una ejecución comercial. Si dispones de una modalidad autorizada de Codex, abre una copia de práctica, verifica su estado y permisos y utiliza el encargo acotado. Conserva por separado lo que esa sesión realmente hizo y ejecutó. No se requiere comprar servicios para reproducir el laboratorio local.

Referencias oficiales consultadas el 30 de octubre de 2026: [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) y [permisos y seguridad](https://learn.chatgpt.com/docs/agent-approvals-security). Describen funciones documentadas; no acreditan su ejecución en este laboratorio.

## Qué contiene la evidencia

`resumen.json` reúne dictamen, referencias y conteos. `pruebas_inicio.json` y `pruebas_solucion.json` conservan cada criterio ejecutado, entradas cuando corresponden, esperado, observado y estado. Los archivos `.txt` conservan la salida de las baterías. `entorno.json` registra versiones sin rutas del equipo.

`revision_git.json` y `cambio.diff` conservan la revisión de referencias y árbol actual. `sha256_referencias.json` vincula cada commit con sus archivos; `sha256_herramientas.json` registra este README y el verificador. `procedencia.json` documenta la comparación con el laboratorio 3; `contrato_previo.json` conserva la huella fijada antes de implementar. Los registros de acceso a Codex y procedencia pertenecen a la preparación editorial; el verificador no vuelve a realizar esas actividades.

**APROBADO** significa que una comprobación realizada satisfizo su expectativa. **FALLIDO** significa discrepancia observada. **BLOQUEADO** identifica una precondición que impidió continuar. **NO EJECUTADO** indica una actividad que no se realizó. Lee siempre el objeto de cada estado. No hay fallos intencionales nuevos; un fallo de la solución debe investigarse.

## Límites

Los veinte escenarios no demuestran corrección para toda entrada posible, orden entre varios disponibles, Unicode exhaustivo, rendimiento, autorización, seguridad integral o concurrencia. Cada consulta reconstruye SQLite en memoria. No se implementan cantidades, reservas, frontend, API ni persistencia. La inspección del código complementa los casos; ninguna ejecución local demuestra productividad de una herramienta comercial.

El historial Git sólo contiene datos y nombres sintéticos. La identidad `Laboratorio <sintetico>` fue creada para el ejercicio y no es una dirección de correo. No hay remotos, hooks distribuidos ni credenciales. La aprobación editorial del autor permanece pendiente.
