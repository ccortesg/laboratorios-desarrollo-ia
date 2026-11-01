# Revisión de la evidencia Windows del laboratorio 7

**Versión:** 1.0 · **Fecha:** 31 de octubre de 2026.  
**Dictamen funcional:** APROBADO para el alcance documentado.  
**Situación de integración:** verificación del índice local y cierre Git pendientes.

## 1. Qué se recibió y qué se comprobó

El autor aportó `EVIDENCIA_LABORATORIO_07_WINDOWS_v1.0.zip` después de ejecutar directamente el procedimiento en su equipo. El archivo tiene 127.021 bytes y 172 archivos interiores. La comprobación de integridad ZIP/CRC no encontró errores. Su SHA-256 es:

```text
d68836097e31a980850451c0e8836173056986d77b1534385f1f455ffcc1b777
```

La revisión extrajo los archivos en una carpeta nueva, rechazando rutas externas y enlaces. Comparó sus bytes antes y después de la auditoría: los 172 archivos permanecieron idénticos. El original se conserva dentro de este paquete, sin reescritura. `auditoria/HUELLAS_ARCHIVOS_RECIBIDOS.json` registra las huellas de los archivos recibidos para cotejos posteriores; no sustituye los registros originales.

Se contrastaron los 44 JSON de detalle con el resumen conjunto, los resúmenes de cada laboratorio, los códigos de salida registrados y las salidas de texto disponibles. Se ejecutó nuevamente el comprobador de huellas, en modo de lectura, sobre los archivos recibidos. También se compararon 258 declaraciones de huellas de fuentes con las de la aplicación del parche ya probada.

**Atribución:** la ejecución funcional Windows pertenece al autor. Esta revisión realizó auditorías de archivos en Linux y consultas de lectura a GitHub. No volvió a ejecutar las 408 comprobaciones funcionales ni las ocho pruebas del recolector; tampoco ejecutó el código en el Windows del autor.

## 2. Resultados funcionales

| Laboratorio | Baterías | Ejecutados | APROBADO | FALLIDO didácticos | NO EJECUTADO en baterías |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 2 | 8 | 7 | 1 | 0 |
| 2 | 1 | 4 | 4 | 0 | 0 |
| 3 | 5 | 44 | 42 | 2 | 6 |
| 4 | 3 | 50 | 50 | 0 | 0 |
| 5 | 6 | 72 | 70 | 2 | 6 |
| 6 | 12 | 94 | 93 | 1 | 8 |
| 7 | 15 | 136 | 134 | 2 | 17 |
| **Total** | **44** | **408** | **400** | **8** | **37** |

Los detalles contienen 445 registros: 408 ejecutados y 37 NO EJECUTADO. No hay BLOQUEADO ni errores de ejecución distintos de las aserciones didácticas previstas. N01–N10 del inicio del laboratorio 4 son diez criterios ausentes registrados aparte; no se incluyen en los 37 ni en las 408 ejecuciones.

Los ocho FALLIDO corresponden exactamente a C04 en inicial del laboratorio 1; B05 y B06 en defecto del 3; P04 y P05 en propuesta del 5; W05 en propuesta del 6; I01 e I07 en propuesta del 7. Las cinco baterías afectadas registran salida 1, como corresponde al defecto deliberado. Los verificadores superiores aprueban el patrón esperado sin convertir esos fallos individuales en aprobaciones.

Las ocho pruebas específicas del recolector muestran ocho resultados `ok`, cierre `OK` y código 0. Son una batería separada de las 408 ejecuciones funcionales.

Fuentes internas del ZIP: `trabajo/verificacion_integracion_07_windows_01/resumen.json`, los JSON de detalle referenciados allí y `trabajo/pruebas_recolector_07_windows_01/{salida.txt,codigo_salida.txt}`. El contraste por batería se conserva en `auditoria/auditoria_coherencia_windows.json`.

## 3. Integridad y conservación

| Comprobación de esta revisión | Resultado |
| --- | --- |
| Integridad del contenedor ZIP | APROBADO; 172 archivos legibles |
| Recuento independiente de detalles y resúmenes | APROBADO; sin discrepancias |
| Huellas stdout/stderr contra los bytes recibidos | APROBADO; 64/64, salida 0 |
| Declaraciones de huellas de fuentes frente al paquete probado | APROBADO; 258/258 |
| Conservación de los archivos recibidos durante la auditoría | APROBADO; 172/172 idénticos |
| Revisión acotada de datos identificables | APROBADO; sin hallazgos en los patrones examinados |

El comprobador recalculó SHA-256 sobre los bytes finales guardados; no normalizó saltos de línea ni reparó huellas. Los campos de captura y los de salida final permanecen separados. Las 258 coincidencias describen declaraciones de fuentes en los registros: no son 258 pruebas funcionales ni una lectura directa del disco del autor. Los 32 valores del laboratorio 4 corresponden a las referencias reconstruidas y los dos auxiliares figuran en su propio registro.

La revisión de confidencialidad examinó rutas de usuario, correos y formatos habituales de tokens, además del contenido operativo de los registros. No encontró datos identificables en ese alcance. El resultado no equivale a una certificación exhaustiva de seguridad.

Fuentes: `auditoria/comprobador_huellas.stdout.txt`, `auditoria/COTEJO_FUENTES_DECLARADAS.json`, `auditoria/ESCANEO_CONFIDENCIALIDAD.json` y el manifiesto de archivos recibidos.

## 4. Entorno y alcance del navegador

Los registros aportados identifican Windows, CPython 3.11.9, SQLite 3.45.1 y Git 2.45.1.windows.1. Los cinco procesos de navegador consignan Node v20.20.0, Playwright 1.62.1 y Chromium 151.0.7922.34. Se conservan estas versiones efectivas; no se sustituyen por las de la ejecución Linux anterior.

La ejecución conjunta abarca del 31 de octubre de 2026 a las 22:37:52 UTC al cierre registrado a las 22:38:29 UTC. En la zona del autor son las 15:37:52 y 15:38:29 del mismo día. Estos horarios describen registros técnicos, no una medición de productividad.

El navegador acredita W05, W06.a y W06.b en los estados que implementan la web: quince ejecuciones, catorce aprobadas y un fallo didáctico previsto. La base del laboratorio 6 no implementa la web y conserva sus casos como NO EJECUTADO. La base del laboratorio 7 sí conserva la web; la ausencia prevista allí corresponde a la importación.

El conjunto no documenta una prueba continua de importar CSV y observar después ese cambio en una pantalla del navegador. Las pruebas de importación acreditan el contrato y la consulta del catálogo con los datos importados; las de navegador comprueban el recorrido web heredado. Tampoco se atribuye una ejecución adicional del CLI por cada caso I: los registros identifican la invocación de la batería. No se certifican producción, carga, concurrencia, accesibilidad ni recuperación ante cortes físicos. No se acredita una sesión comercial nueva de Codex, Copilot o Grok Build.

## 5. Estado Git: lo conocido y lo pendiente

Una consulta nueva de lectura a GitHub, registrada el 31 de octubre de 2026 a las 22:41:34 UTC, confirmó:

| Referencia | Resultado |
| --- | --- |
| `main` | `6382e05846e149a9a72f7fdc56da48c37a873833` |
| Árbol de `main` | `680fa6135ed0aae40e962ec3f893d72ece1389c1` |
| `lab-06-v1.0` y `repositorio-v1.2` | `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd` |
| Nueve etiquetas históricas | Conservan las referencias registradas |
| `lab-07-v1.0` y `repositorio-v1.3` | Ausentes en la consulta |

La fuente operativa está en `auditoria/REFERENCIAS_REMOTAS.json`, con los endpoints consultados. Esta fotografía no garantiza que las referencias permanezcan iguales después de la consulta; el cierre vuelve a comprobarlas.

**El ZIP no incluye la fotografía del repositorio principal del autor:** rama, HEAD, índice, diferencias y árbol preparado. Los registros Git del laboratorio 4 describen una copia didáctica reconstruida; no acreditan esos datos del repositorio principal. Por ello la revisión funcional queda APROBADA, mientras que el índice y la preparación final del commit siguen pendientes de comprobación local.

El árbol esperado, si se aplicó únicamente el parche entregado sobre la base confirmada, es:

```text
b123b5969e8077ba0cb3c4eedc9b348f94294652
```

`COMPROBAR_CIERRE_07.py` comprueba esa condición, el estado del trabajo, las referencias, el destino remoto y la identidad de la evidencia local. Cualquier diferencia impide el cierre directo y conserva el estado para revisar la adaptación. No se necesita repetir las pruebas funcionales si se confirma exactamente el árbol probado y no hay modificaciones adicionales; una adaptación de código requiere verificar el resultado adaptado.

## 6. Siguiente tarea y continuidad

La siguiente tarea es cerrar la integración Git: comprobar el índice, crear el commit en la rama de integración, avanzar `main` mediante fast-forward y publicar exclusivamente `main`, `lab-07-v1.0` y `repositorio-v1.3`. El procedimiento está en `INSTRUCCIONES_CIERRE_GIT_BASH.md`. Los auxiliares entregados no se han ejecutado en el equipo del autor; sus pruebas propias de preparación se documentan aparte y no se suman a las 408.

Durante esta revisión no se creó un commit del autor, no se modificó `main`, no se publicaron etiquetas y no se hizo push. La documentación de estado nueva registra la ejecución Windows y mantiene la publicación pendiente. Los manuscritos 1–7 siguen pendientes de revisión editorial; el maestro 1.0 se conserva y el capítulo 8 no se redactó.

## Referencias técnicas

Consulta efectiva: 31 de octubre de 2026.

- [Git: git-write-tree](https://git-scm.com/docs/git-write-tree): el identificador se construye a partir del índice; se contrasta además el directorio de trabajo.
- [Git: git-merge](https://git-scm.com/docs/git-merge): `--ff-only` rechaza una integración que no puede resolverse mediante fast-forward.
- [Git: git-push](https://git-scm.com/docs/git-push): `--atomic` exige actualizar todas las referencias solicitadas o ninguna; `--no-follow-tags` evita incluir etiquetas anotadas adicionales por configuración.
