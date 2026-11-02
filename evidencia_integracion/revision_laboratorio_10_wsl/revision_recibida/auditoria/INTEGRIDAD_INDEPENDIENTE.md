# Revisión independiente de integridad · laboratorio 10 WSL

**Resultado: APROBADO para los bytes recibidos y sus declaraciones de integridad.**

Fecha de revisión: 1 de noviembre de 2026, America/Hermosillo. Los registros originales conservan sus tiempos UTC. La auditoría fue de lectura: no ejecutó los scripts enviados ni importó su `sitecustomize.py`, no repitió las pruebas funcionales y no reescribió ninguna evidencia recibida.

## Manifiesto y cobertura

El manifiesto enumera **665 archivos**. Se contrastaron los tamaños y SHA-256 de todos ellos, la ausencia de duplicados y referencias inseguras y la cobertura completa de los archivos presentes. El ZIP contiene **666 archivos contando el propio manifiesto**. No hay archivos faltantes ni adicionales respecto al inventario.

La comprobación final del manifiesto volvió a confirmar que la revisión dejó intactos los bytes recibidos.

## Huellas de salidas

| Alcance | Declaraciones contrastadas con los bytes finales | Capturadas iguales a finales | Capturadas distintas de finales |
| --- | ---: | ---: | ---: |
| Sesión completa | 340/340 | 337 | 3 |
| Auxiliar de verificación | 284/284 | 284 | 0 |
| Conjunto funcional | 272/272 | 272 | 0 |

Estos conjuntos se incluyen unos dentro de otros; **no son 896 comprobaciones distintas**. El recuento independiente de los JSON coincide con tres invocaciones de sólo lectura del recolector original de confianza, ejecutadas con `python -I -B`, sin fijar un total histórico y sin llamar a `cerrar_evidencia`.

Las tres diferencias entre captura y salida final pertenecen a operaciones externas cuyo saneamiento fue documentado. Sus huellas finales corresponden exactamente con los bytes incluidos. Todos los registros de salida mantienen campos de huella capturada válidos; no se sustituyó una huella inicial para hacer coincidir una captura divergente dentro de esta auditoría.

## Capturas anteriores al saneamiento

Las **284 referencias** del inventario `CAPTURAS_ORIGINALES_COTEJADAS.json` corresponden exactamente a las del auxiliar: registro, identificador, flujo y SHA-256 capturado. Sus huellas capturadas coinciden también con las finales presentes en este envío.

El inventario declara un almacén externo con 95 blobs comprobados durante la sesión WSL. El script recibido cuenta en ese almacén todos los blobs, incluidos documentos de comandos y cierres intermedios; las 284 declaraciones finales sólo emplean 36 SHA-256 distintos. Esos recuentos describen universos diferentes.

**Límite:** los archivos originales de ese almacén permanecen fuera del ZIP. No se leyó ni verificó físicamente ese directorio desde esta revisión. La comprobación independiente acredita los bytes finales disponibles y la coherencia del inventario aportado; el cotejo del almacén original conserva la atribución a la sesión WSL.

## Observador de capturas

Se revisó como texto `soporte_de_sesion/sitecustomize.py`. Se activa mediante `LAB10_ARCHIVO_CAPTURAS`, intercepta la carga del módulo de huellas y copia los archivos declarados antes de llamar al cierre original. El envoltorio conserva los argumentos `salida` y `transformar` y devuelve el resultado de la función original. El código revisado no altera las salidas declaradas, los resultados de pruebas ni las fuentes versionadas.

El observador constituye instrumentación adicional de la ejecución; esta revisión estática no equivale a demostrar dinámicamente su transparencia. Los errores de creación del almacén situados fuera del bloque de captura podrían interrumpir un proceso; la ejecución aportada no registra ese problema. No se identificó una sustitución de las validaciones del recolector ni una omisión deliberada de resultados fallidos.

## Anonimización

Se inspeccionaron las **666 entradas UTF-8** mediante patrones acotados para rutas de perfiles Windows/Linux, rutas privadas del entorno de ejecución, tokens de GitHub, claves privadas y correos. No aparecieron coincidencias. Se conservan la URL autorizada del proyecto sintético y las rutas relativas necesarias para entender la evidencia.

Esta revisión no inspeccionó los originales excluidos del ZIP ni constituye una auditoría de sistemas externos.

## Conclusión y límites

No se encontraron discrepancias materiales de integridad en la evidencia compartida. Los originales y evidencias históricas no fueron modificados. El estado funcional y la identidad del repositorio deben leerse junto a sus revisiones específicas; esta auditoría no crea commits, no publica cambios y no aprueba editorialmente los manuscritos.

SHA-256 permite contrastar los bytes recibidos con su declaración; no autentica por sí solo el origen externo del paquete. El detalle reproducible de esta revisión, las salidas del recolector, las huellas y las tres sustituciones saneadas se conserva en `INTEGRIDAD_INDEPENDIENTE.json`.
