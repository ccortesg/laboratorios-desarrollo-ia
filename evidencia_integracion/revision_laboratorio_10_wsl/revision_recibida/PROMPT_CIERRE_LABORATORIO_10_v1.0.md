# Encargo de cierre del laboratorio 10

Este encargo se propone para una ejecución posterior solicitada por el autor. No fue ejecutado como parte de la revisión de evidencia. Al recibir la instrucción expresa de ejecutar este archivo, realiza la incorporación documental, el commit, la integración en main y la publicación descritos a continuación, con autonomía en decisiones rutinarias.

## Objetivo y alcance

Cerrar el laboratorio 10 del proyecto sintético “Desarrollo de Software en la Era de la IA”, conservando los laboratorios 1–10, sus distribuciones, evidencias y etiquetas históricas. No modificar manuscritos ni redactar contenido adicional. Los capítulos 1–10 siguen pendientes de revisión editorial.

Trabaja sobre la copia existente de `laboratorios-desarrollo-ia` en el proyecto de Codex. Identifica primero el acceso real y el entorno; distingue Windows nativo de WSL/Linux. Usa exclusivamente el repositorio autorizado https://github.com/ccortesg/laboratorios-desarrollo-ia y materiales del libro. No accedas a otros proyectos ni sistemas productivos.

## 1. Recuperar y verificar la continuidad

Localiza REVISION_LABORATORIO_10_WSL_v1.0.zip y verifica su manifiesto mediante el verificador incluido. Lee la revisión, ESTADO_DEL_LIBRO_v1.9.1.md, ESTADO_REPOSITORIO_v1.8.1.md y sus antecedentes. Lee AGENTS.md y la continuidad del repositorio. El maestro editorial 1.0 permanece vigente.

Base auditada: commit `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3`, árbol `790e875fc95495c39ea2b5ebe7621a4ae1afa30f`. Rama observada: `codex/integracion-laboratorio-10`. Árbol del índice aprobado: `78b136a253cb3cb79143a0c81ee09f7892efa40f`. El incremento tiene 1.372 rutas, incluidas nueve modificaciones de archivos existentes. El ZIP original de evidencia WSL tiene SHA-256 `3a2dd4825f83056ce77cb9d2ef4a0cf5b2da205b68d2298438fd2811c4637818`.

Comprueba la situación actual antes de escribir. El último envío dejó los cambios preparados sin commit, main en la base, sin cambios sin preparar y sin etiquetas lab-10-v1.0 o repositorio-v1.6. No supongas que sigue así. Consulta remoto y conserva las quince etiquetas históricas y todas las referencias existentes. Si el cierre ya se publicó, verifica y registra ese hecho; no dupliques commits ni etiquetas.

No reapliques el parche del laboratorio si el índice ya corresponde al árbol auditado. Si encuentras diferencias, identifica las rutas, conserva los cambios y explica si afectan a la evidencia aprobada. No uses reset destructivo, clean, limpieza de trabajo, fuerza sobre ramas o etiquetas ni sobrescritura de evidencias.

## 2. Incorporar sólo documentación y evidencia nueva

Antes de modificar, registra HEAD, rama, main local/remoto, árbol del índice, diferencias y etiquetas. Guarda todo en una carpeta nueva de `trabajo/`, con capturas saneadas y huellas.

Incorpora los estados 1.9.1/1.8.1 a docs/estados y la revisión y el ZIP original recibido a una carpeta nueva de evidencia_integracion, manteniendo su identidad byte a byte. Conserva todos los estados anteriores.

Prepara estados nuevos ESTADO_DEL_LIBRO_v1.9.2.md y ESTADO_REPOSITORIO_v1.8.2.md que describan el cierre preparado, todavía sin atribuir una publicación futura. Actualiza únicamente la continuidad operativa necesaria, como README, CONTINUIDAD, VERSIONES, AGENTS o PROCEDENCIA cuando corresponda. Declara una lista exacta de las rutas documentales permitidas antes de editar.

No modifiques código, datos, pruebas, manuscritos, distribuciones ni evidencias históricas para incorporar la revisión. El árbol total cambiará al añadir documentación; verifica que las diferencias respecto al árbol auditado se limitan a las rutas documentales declaradas. Conserva aparte cualquier avance posterior autorizado de main.

## 3. Validar antes del commit

Comprueba el manifiesto de esta revisión, las huellas recibidas, la conservación de archivos protegidos y las diferencias del índice. Ejecuta las ocho pruebas del recolector y registra su resultado como infraestructura nueva.

Las 1.043 ejecuciones funcionales aprobadas pertenecen a la sesión WSL auditada. No las presentes como reejecutadas por el cierre. Si el cambio es exclusivamente documental y la identidad técnica se conserva, no es necesario repetir la batería completa. Si se modifica contenido funcional, se resuelven conflictos técnicos o un avance de main altera el alcance verificado, ejecuta las comprobaciones pertinentes y el conjunto con navegador antes de declarar aprobado el nuevo estado. Usa salidas nuevas y conserva los intentos.

Mantén APROBADO, FALLIDO, BLOQUEADO y NO EJECUTADO. No conviertas fallos inesperados en didácticos ni interpretes huellas válidas como aprobación funcional. Si un impedimento real permanece, completa el trabajo independiente y detalla qué falta antes de publicar.

## 4. Commit e integración conservando avances

Con la validación aprobada, crea el commit autorizado en la rama de integración. Revisa antes el contenido preparado; no uses git add indiscriminado sobre archivos ajenos o trabajo/. Conserva el esquema de metadatos sintéticos del repositorio sin cambiar la configuración global de Git ni divulgar identidad personal en los materiales del libro.

Vuelve a ejecutar fetch sin traer etiquetas y conserva el estado actual de main local y remoto. Integra en la rama de trabajo los avances que correspondan sin retroceder ninguna referencia. Resuelve conflictos rutinarios manteniendo ambos trabajos y verifica el resultado. Si una resolución requiere una decisión de alcance nueva, conserva la propuesta y documenta la decisión pendiente.

Integra la rama final en main por avance rápido cuando la relación lo permita. Si main avanzó durante el proceso, vuelve a conservar ese avance antes de continuar. Registra commit y árbol realmente obtenidos; no reutilices el árbol auditado como identidad del nuevo commit documental.

## 5. Etiquetas y publicación exacta

Comprueba otra vez que lab-10-v1.0 y repositorio-v1.6 están ausentes local y remotamente. Si alguna ya existe, inspecciona su identidad; nunca la fuerces, muevas o recrees silenciosamente. Si corresponde al mismo cierre ya realizado, registra el estado sin repetirlo.

Crea únicamente las dos etiquetas nuevas previstas, conservando la convención de etiquetas ligeras del repositorio y apuntándolas al commit final de main. Publica exclusivamente esas referencias y main:

```bash
git push --atomic --no-follow-tags origin main refs/tags/lab-10-v1.0 refs/tags/repositorio-v1.6
```

No uses --tags, --force, --mirror ni push de ramas adicionales. Si el push es rechazado por avance remoto, conserva el trabajo local, consulta el avance y adapta el cierre; no fuerces las referencias ni muevas etiquetas ya creadas. Expón cualquier decisión pendiente si no es posible conservarlas y completar la publicación.

## 6. Confirmación posterior y entrega

Consulta después main, ambas etiquetas nuevas y todas las históricas. Comprueba que main y las dos nuevas coinciden en el commit final y que las quince anteriores conservan sus identidades. Verifica el árbol local, el índice y la ausencia de cambios ajenos. No declares publicado el cierre sólo porque se creó el commit local.

Genera, fuera del commit que describen, CIERRE_LABORATORIO_10_CONFIRMADO_v1.0.md, ESTADO_DEL_LIBRO_v1.9.3.md y ESTADO_REPOSITORIO_v1.8.3.md con las referencias reales, entorno, fechas, verificaciones nuevas, evidencia histórica utilizada y pendientes. Estos documentos se llaman confirmado únicamente si la consulta remota demuestra la publicación. Si no se completó, entrega un estado pendiente con el motivo preciso, sin inventar confirmación.

Entrega EVIDENCIA_CIERRE_LABORATORIO_10_WSL_v1.0.zip si el entorno fue WSL, o un nombre que identifique correctamente el entorno utilizado. Incluye comandos, códigos, consultas antes/después, diferencias, identidades, conservación, informes y un manifiesto de los bytes finales. Conserva las huellas capturadas y finales por separado, sin normalizaciones posteriores. Verifica el ZIP creado y entrega su SHA-256 fuera del archivo para evitar autorreferencias.

El cierre técnico no aprueba los capítulos. Mantén explícitamente pendiente la revisión editorial integral de los diez borradores. No publiques el libro ni otros materiales y no redactes capítulos adicionales.
