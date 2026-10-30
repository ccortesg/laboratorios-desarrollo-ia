# Revisión documental del laboratorio 4

**Versión 1.1 · 30 de octubre de 2026.** Este paquete añade un informe aportado sobre revisión y ejecución en Codex desktop. El código, las pruebas, el contrato, los datos, los archivos de Git y la evidencia histórica de la versión 1.0 se conservan byte a byte. No hay un nuevo incremento funcional.

## Qué leer y cómo ejecutar

Comienza por este documento para conocer la actualización. Después sigue `README.md`, conservado como instrucción de reproducción de la entrega original. Los comandos y los veinte criterios no cambian. Para probar el árbol actual, ejecuta `python pruebas.py` desde `repositorio/`; usa `python3` o `py -3` si ése es el intérprete disponible. Para probar las etiquetas, ejecuta `python verificar.py --salida mi_evidencia` desde la raíz del paquete y elige una salida nueva fuera del repositorio.

Los 71 archivos originales permanecen iguales. Se añaden únicamente este documento y dos archivos bajo `revision_1_1/`, fuera de la raíz Git. No se incluyen caches, nuevos commits ni registros reconstruidos. La comparación del contenido y de los metadatos de cada entrada original del ZIP quedó APROBADA durante el empaquetado; el resumen completo está en el archivo de estado del libro.

## Procedencia de la evidencia

`evidencia/` pertenece a la producción inicial. Allí se registró ejecución local de Git, Python y SQLite, y el bloqueo del CLI de Codex por falta del ejecutable. Esos registros conservan su fecha y su significado histórico.

`revision_1_1/EJECUCION_CODEX_04_saneado.md` reproduce el informe aportado para esta revisión. Se omitió una zona horaria geográfica para cumplir la anonimización; el resto de su cuerpo permanece igual. Su encabezado editorial diferencia el documento recibido de una observación independiente. El original no fue modificado.

El informe identifica Codex desktop con terminal Bash en Linux, Git 2.34.1, Python 3.10.12 y SQLite 3.37.2. Describe revisión y ejecución de la solución existente, no su implementación. La versión de la app no se consultó; no determina Windows nativo, WSL ni el sistema anfitrión. El informe registra 20/20 en el árbol actual y, por separado, 10/10 en `inicio` y 20/20 en `solucion`.

`revision_1_1/CONTRASTE_EDITORIAL.json` separa lo comprobado al revisar los materiales de lo declarado por el informe. Se cotejaron las referencias, los siete archivos del incremento, las 87 inserciones y 14 eliminaciones, los diez métodos heredados y el alcance del verificador. No se reejecutaron baterías funcionales en esta revisión exclusivamente documental.

## Las pruebas y la limpieza tienen objetos distintos

Según el informe, el árbol tenía 17 diferencias `100644 → 100755` desde la primera inspección. Sus bytes coincidían con `HEAD`; la sesión conservó los modos y no determinó su origen. La limpieza quedó FALLIDO aunque los veinte criterios aprobaron. Este resultado corresponde a aquella copia: el ZIP conserva el repositorio de referencia original y no recrea sus diferencias de permisos.

Git distingue archivos normales y ejecutables mediante esos modos. El ajuste `core.fileMode` determina si Git atiende el bit ejecutable y `git -c` aplica un valor a una invocación. Por eso la comparación reportada `git -c core.fileMode=false diff --exit-code HEAD --` no corrige permisos ni guarda una configuración nueva. Su salida 0 no demuestra por sí sola ausencia de archivos sin seguimiento ni limpieza habitual. Fuentes oficiales consultadas el 30 de octubre de 2026: [Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects), [git-config 2.51.1](https://git-scm.com/docs/git-config/2.51.1) y [git 2.51.1](https://git-scm.com/docs/git/2.51.1).

El verificador comprueba las referencias y registra el estado del árbol, pero no exige que esté limpio para aprobar. La cadena histórica `sesion_codex: "NO EJECUTADO por este verificador"` describe el alcance del script; no contradice por sí sola que una sesión de Codex lo invoque.

## Respaldo pendiente

Sólo se recibió el informe Markdown. La carpeta `evidencia_codex_04_20261030/` que cita no fue adjuntada; no está incluida en este ZIP. El cotejo independiente de sus JSON, salidas, huellas y manifiestos queda **BLOQUEADO por falta del insumo**. No se ha verificado aquí la conservación de aquella copia ni la anonimización de archivos que no se recibieron.

El siguiente paso para cerrar ese pendiente es aportar la carpeta completa saneada, incluyendo el registro de comandos, el resultado del árbol actual, el verificador de referencias y los manifiestos de conservación. La entrega debe excluir rutas personales, zonas geográficas, usuarios, correos, credenciales y otros identificadores. Deben mantenerse comandos relativos, resultados, códigos de salida, criterios y hashes de código sintético. Si se sanea un archivo con huella previa, conservar por separado la huella histórica como antecedente y registrar una nueva huella para la copia saneada; no presentar ambas como si correspondieran a los mismos bytes.

El reto por prefijos, la implementación del incremento en Codex, `/review` y las mediciones de productividad siguen **NO EJECUTADO**. La incorporación del informe no constituye aprobación editorial del autor.
