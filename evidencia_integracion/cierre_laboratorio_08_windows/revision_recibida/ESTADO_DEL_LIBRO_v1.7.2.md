# Estado del libro · ejecución Windows corregida del laboratorio 8

**Versión documental:** 1.7.2. **Fecha:** 31 de octubre de 2026, America/Hermosillo.
**Antecedente conservado:** `ESTADO_DEL_LIBRO_v1.7.1.md`.

## Continuidad editorial

Se conserva `DOCUMENTO_MAESTRO_EDITORIAL_v1.0.md`, la promesa, el principio rector, CLARO, el índice y las reglas de anonimización. Los capítulos 1–8 y sus Word continúan pendientes de revisión expresa del autor. No se incorpora una observación editorial que no haya sido aportada. Esta entrega no modifica los manuscritos ni redacta el capítulo 9.

## Incidente y corrección acreditados

El primer pase Windows del laboratorio 8 permanece **FALLIDO** como antecedente. Sus auxiliares dejaban conexiones SQLite abiertas, lo que produjo errores de limpieza, duplicados y resultados ausentes. Las huellas de aquel pase se conservan, sin corregirlas retrospectivamente.

La revisión técnica 1.0.1 cierra explícitamente las conexiones de la instantánea y de la preparación D06.b, conserva la transacción y añade cuatro regresiones de recursos. Los estados de aplicación y los criterios funcionales permanecen intactos.

El autor ejecutó el paquete corregido en Windows. Se recibió `EVIDENCIA_CORRECCION_LAB08_WINDOWS_02.zip`, SHA-256 `2e8503f199f85184ef55de2c8808cda7b358e4dd75554a03371be51b4d7b1445`, con 254 archivos. La auditoría confirma **APROBADO**, salida 0: 65 baterías, 583 ejecuciones, 571 aprobaciones, doce fallos didácticos exactos, cero bloqueos y cero errores de ejecución; 48 NO EJECUTADO en baterías y diez ausentes aparte.

Las ocho pruebas del recolector, cuatro de recursos y nueve del evaluador aprueban y se cuentan por separado. Coinciden 253/253 archivos del manifiesto, 102/102 huellas del conjunto y 10/10 auxiliares. El antecedente se conserva 244/244. D04 acredita el recorrido CSV→CLI→SQLite persistente→HTTP→navegador con el mismo servidor activo antes y después de importar.

## Identidad y entregables de continuidad

La ejecución corresponde a la rama `integracion/laboratorio-08`, HEAD/main local `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` y árbol preparado corregido `9ea6109fe8e89a2785bdce255252ffaabea1d122`.

Se entregan `REVISION_LABORATORIO_08_WINDOWS_v1.0.md`, su paquete ZIP con auditorías y evidencia recibida, este estado, `ESTADO_REPOSITORIO_v1.6.2.md` y el prompt de cierre. Se conservan los paquetes originales y correctivos anteriores. Los nuevos documentos se entregan fuera del árbol probado; su incorporación futura deberá registrarse como un incremento documental.

## Pendientes y siguiente tarea

- **APROBADO:** corrección técnica, ejecución Windows aportada por el autor y auditoría de esa evidencia.
- **APROBADO:** consulta remota de referencias; no equivale a publicar el laboratorio 8.
- **NO EJECUTADO:** commit del laboratorio 8, integración en main, etiquetas nuevas y push.
- **Pendiente editorial:** revisión del autor de los capítulos 1–8.

Siguiente tarea: cerrar la integración del laboratorio 8, añadiendo esta evidencia y documentación sin borrar antecedentes, comprobar otra vez las referencias, revisar el commit y publicar únicamente el incremento y las etiquetas nuevas autorizadas. El capítulo 9 corresponde a una entrega posterior.
