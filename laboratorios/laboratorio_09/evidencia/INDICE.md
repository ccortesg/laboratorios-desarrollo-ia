# Evidencia de preparación del laboratorio 9

Fecha efectiva: 1 de noviembre de 2026. Todas estas ejecuciones nuevas se realizaron localmente en Linux sobre material sintético. No acreditan una ejecución Windows o WSL del autor ni una sesión comercial. Los históricos de los laboratorios anteriores permanecen separados e intactos.

## Resultado final

`autonomo_02_aprobado/resumen.json` registra **APROBADO**, código de proceso 0: 27 baterías, 222 ejecuciones, 210 APROBADO, doce FALLIDO expresamente esperados, cero BLOQUEADO, cero NO EJECUTADO y cero errores de ejecución. La solución aprueba sus 74 casos; base conserva nueve fallos frente a la nueva política y propuesta tres de duplicación. Los 62 heredados aprueban en cada estado.

El verificador comprobó 54/54 huellas de stdout/stderr correspondientes a sus 27 procesos. La captura externa del proceso completo añade dos archivos de salida, registrados por separado en `captura_proceso/`; no son casos funcionales adicionales. `entorno.json`, los registros de navegador y `NAVEGADOR_151_FUENTE.json` documentan el entorno: Playwright 1.62.1 y Chrome for Testing 151.0.7922.34, ejecutable oficial indicado mediante LAB06_CHROMIUM. No se distribuye el navegador dentro del laboratorio.

## Intentos anteriores conservados

- `http_preparatorio/http_solucion_01.json`: los once casos quedaron BLOQUEADO al impedir el entorno restringido iniciar el servidor local. No se reinterpretaron como fallos de la política.
- `http_preparatorio/http_solucion_02.json`: repetición autorizada en loopback; once casos HTTP APROBADO. Es una comprobación acotada, distinta del recorrido completo.
- `autonomo_01_fallido/`: 222 ejecuciones, 208 APROBADO y catorce FALLIDO. Doce eran esperados; S06 de propuesta y solución fallaron con `TimeoutExpired`, por lo que el global quedó FALLIDO. Se comprobaron 54/54 huellas. El navegador de este intento fue Chrome for Testing 156.0.8078.80; las fuentes de descarga se conservan.
- `diagnostico_s06_chrome156/` y `diagnostico_s06_chrome151/`: reproducciones aisladas con el código original y DEBUG=pw:api. Ambas alcanzaron `response.json()` después de recibir HTTP 400, pero esa lectura no terminó antes del plazo de 70 segundos. La comparación mantuvo código, entradas y plazo; cambió el ejecutable de navegador. No hay base para atribuir la causa interna a una versión concreta.
- `instrumentacion_s06/`: decisión, código anterior y diferencia de la corrección del instrumento. S06 dejó de pedir con Playwright un cuerpo que el formulario rechaza sin consumir. Conserva la observación del estado HTTP, el error visible, la ocultación de resultados anteriores, los controles y la consulta posterior correcta. S04.a mantiene la comprobación HTTP del JSON y del código de error exactos. No se cambió la aplicación, el contrato S06 ni el tiempo de espera.

El resultado final aprueba después de esa corrección de instrumentación. Los intentos fallidos no se borraron ni se volvieron a etiquetar. Su existencia no incrementa el número de criterios distintos y sus ejecuciones no se suman a las 222 del resultado final.

## Infraestructura y auditorías

`recursos_01/` registra cuatro regresiones heredadas del cierre de conexiones SQLite, todas aprobadas, código 0. Son infraestructura: se contabilizan aparte del catálogo y de S01–S08. Las ocho pruebas del recolector común y el conjunto de laboratorios 1–9 se registran en la evidencia de integración del repositorio, no se atribuyen a esta ejecución autónoma.

`MANIFIESTO_EVIDENCIA.json` identifica los bytes de cada archivo de esta carpeta salvo el propio manifiesto. Las huellas de captura y las finales se distinguen en los registros que requirieron saneamiento. `REVISION_HUELLAS_EVIDENCIA.json` registra una comprobación de sólo lectura sobre todas las referencias stdout/stderr de los archivos `comandos.json` aquí conservados. Esa auditoría no constituye una nueva prueba funcional ni modifica hashes anteriores.

## Límites

No se ha determinado la causa interna completa del bloqueo de lectura de cuerpo observado en Playwright; se aisló la operación y se corrigió una observación redundante del instrumento manteniendo el contrato. El navegador final sí completó el recorrido requerido. No se ejecutaron aquí Windows, permisos multiusuario, carga, concurrencia, exposición pública ni la actividad de una herramienta comercial. El reto de cabeceras sigue sin implementar.
