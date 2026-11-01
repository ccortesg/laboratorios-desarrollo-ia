# Revisión de la ejecución corregida del laboratorio 8 en Windows

**Versión:** 1.0. **Fecha:** 31 de octubre de 2026, America/Hermosillo.

## Dictamen

**APROBADO para preparar el cierre de la integración.** La evidencia aportada por el autor acredita el recorrido completo en Windows sobre el árbol corregido `9ea6109fe8e89a2785bdce255252ffaabea1d122`. Se verificaron sus archivos, salidas, resultados individuales, fuentes declaradas y conservación del antecedente. No se detectaron fallos funcionales distintos de los doce fallos didácticos previstos.

Esta revisión analiza una ejecución realizada por el autor. No representa una nueva ejecución Windows del revisor. El commit del laboratorio 8, la integración en main, las etiquetas nuevas y la publicación siguen **NO EJECUTADO**. Los capítulos 1–8 permanecen pendientes de revisión editorial.

## Evidencia recibida

- Archivo: `EVIDENCIA_CORRECCION_LAB08_WINDOWS_02.zip`.
- SHA-256: `2e8503f199f85184ef55de2c8808cda7b358e4dd75554a03371be51b4d7b1445`.
- Contenido: **254 archivos**, sin entradas duplicadas ni rutas inseguras.
- Manifiesto interno: **253/253 archivos coincidentes**, con cobertura completa. El archivo restante es el propio `SHA256_ARCHIVOS.json`, excluido de su mapa para evitar autorreferencia.
- Cierre de la ejecución: `2026-11-01T05:48:21.061312Z`, equivalente al **31 de octubre de 2026, 22:48:21 en Hermosillo**.

El ZIP recibido se conserva sin modificación dentro de `recibido/` del paquete de revisión. No se recalculan sus huellas declaradas para hacerlas coincidir.

## Resultados funcionales observados y cotejados

Se contrastaron los 65 registros de baterías del resumen con sus JSON individuales, identificadores, tipos de error y códigos de salida. La reevaluación de los registros con el evaluador común conservado coincide con el resumen recibido.

| Medida | Resultado observado |
|---|---:|
| Laboratorios | 8 |
| Baterías | 65 |
| Ejecuciones funcionales | 583 |
| APROBADO | 571 |
| FALLIDO didácticos previstos | 12 |
| BLOQUEADO | 0 |
| Errores de ejecución | 0 |
| NO EJECUTADO dentro de baterías | 48 |
| Criterios ausentes registrados aparte | 10 |

Hay 631 registros de casos dentro de las baterías: 583 ejecutados más 48 NO EJECUTADO. Los diez criterios ausentes quedan fuera de ese total. Estas cifras cuentan ejecuciones de distintos estados del material; no representan 583 requisitos únicos.

Los doce fallos conservan `FALLIDO` y corresponden exclusivamente a:

| Laboratorio y estado | Criterios |
|---|---|
| 1, inicial | C04 |
| 3, defecto | B05 y B06 |
| 5, propuesta | P04 y P05 |
| 6, propuesta en navegador | W05 |
| 7, propuesta | I01 e I07 |
| 8, propuesta de depuración | D03, D05 y D08.a |
| 8, propuesta de depuración en navegador | D04 |

Todos esos fallos son de aserción. No hay identificadores duplicados ni errores `PermissionError`, `WinError 32` o `Criterio duplicado` en la nueva evidencia del laboratorio 8. La terminación explícita de los servidores por el controlador se distingue de los códigos de salida de las baterías.

## Pruebas auxiliares e integridad

Las capturas de `unittest` confirman **8 pruebas del recolector, 4 pruebas de recursos y 9 pruebas del evaluador**, todas con `OK` y código de salida 0, sin omisiones. Se contabilizan separadamente del conjunto funcional.

Se recalcularon las huellas sobre los bytes recibidos: **102/102 salidas del conjunto** y **10/10 salidas auxiliares** coinciden. Los 112 campos de captura se conservan; en esta ejecución coinciden también con los hashes finales. La auditoría no transforma los archivos.

El cotejo de fuentes comprueba 335 declaraciones de los manifiestos de fuentes, herramientas y referencias Git. Otras 240 declaraciones repetidas corresponden a conservación y preparación: 222 y 18 respectivamente. Las **575 declaraciones coinciden**, pero no se presentan como 575 archivos únicos ni se suman como pruebas funcionales. Los objetos históricos del laboratorio 4 se leyeron desde su bundle local en una copia temporal.

El auxiliar ejecutado y `BASE_CORRECCION.json` coinciden con los archivos del paquete correctivo entregado. El mapa del antecedente coincide **244/244** con los bytes del ZIP Windows fallido recibido anteriormente. Ese resultado histórico sigue siendo FALLIDO y se conserva.

## Recorrido CSV → CLI → SQLite → HTTP → navegador

El resultado `solucion_depuracion_navegador.json` demuestra que D04 aprueba con el mismo servidor activo antes y después de importar. En ALFA, la pantalla pasa de A01 a A01+A03; BETA queda vacío y la búsqueda devuelve A03. El importador informa cuatro filas leídas, cuatro validadas y cuatro aplicadas. La instantánea final de SQLite concuerda con esos valores y el diagnóstico identifica la misma base persistente.

Esta evidencia acredita que la consulta web utiliza los datos importados. La solución registra los once casos D aprobados: diez en la batería de terminal y uno en navegador. Sus 51 casos heredados también aprueban.

Entorno registrado: Windows; Python 3.11.9; SQLite 3.45.1; Git 2.45.1.windows.1; Node 20.20.0; Playwright 1.62.1; Chromium 151.0.7922.34.

## Identidad Git y consulta remota

La identidad inicial y final de la ejecución Windows es idéntica:

- Rama: `integracion/laboratorio-08`.
- HEAD y main local: `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`.
- Árbol preparado: `9ea6109fe8e89a2785bdce255252ffaabea1d122`.
- Sin diferencias sin preparar.
- Once etiquetas locales conservadas respecto del antecedente.

Se consultaron las referencias del repositorio autorizado mediante la API oficial de GitHub. Main remoto permanece en `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`; sus once etiquetas coinciden con el antecedente. `lab-08-v1.0` y `repositorio-v1.4` no existen en esa consulta. La fecha efectiva y las respuestas normalizadas se conservan en `auditoria/REFERENCIAS_REMOTAS_CONFIRMADAS.json`.

La consulta Git por terminal y la apertura directa por el servicio web no estuvieron disponibles en el entorno de revisión; la consulta mediante la conexión de GitHub sí se completó. El intento inicial se conserva por separado y no se interpreta como un bloqueo del laboratorio.

## Alcance del cierre y siguiente tarea

La corrección técnica y la ejecución Windows quedan acreditadas. La próxima tarea es incorporar esta revisión y los nuevos estados como documentación adicional, revisar las diferencias, crear el commit e integrar y publicar el incremento con las etiquetas nuevas previstas, reconsultando antes las referencias remotas. Los nombres previstos no equivalen a etiquetas ya creadas.

Los documentos de esta revisión se entregan aparte: todavía no forman parte del árbol `9ea6109fe8e89a2785bdce255252ffaabea1d122`. Si se incorporan al repositorio, habrá un árbol nuevo que deberá registrarse, conservando la identificación del código verificado.

No se acredita despliegue productivo, rendimiento, seguridad integral, GitHub Actions ni uso comercial de Codex, Copilot o Grok Build. La aprobación técnica no aprueba los manuscritos. No se redacta el capítulo 9.

## Fuentes de esta revisión

Las fuentes principales son `RESULTADO_CORRECCION.json`, `preparado_corregido.json`, `SHA256_ARCHIVOS.json`, `conjunto/resumen.json`, las baterías individuales y las capturas del ZIP recibido. Los informes de auditoría incorporan los cotejos nuevos y distinguen el recuento de cada comprobación. Las consultas remotas utilizan únicamente el repositorio sintético autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia.
