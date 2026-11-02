# Estado de preparación para publicación · v1.0

**Fecha: 2 de noviembre de 2026. Ajustes para lectores preparados; apertura pública NO EJECUTADO.** Este informe se escribe antes del commit. El comprobante posterior a la subida se entrega fuera del commit cuya identidad acredita; no se anticipa aquí su SHA ni se interpreta la autorización como un push ejecutado.

## Base y alcance

Base local y remota consultada: `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; árbol `69d691ec538807193e6e2437946197da86fd8837`. Main, lab-10-v1.0 y repositorio-v1.6 coinciden. Las 17 etiquetas están presentes. GitHub devuelve visibilidad privada y permiso de escritura; Issues está habilitado y la licencia del proyecto es null. Rama de preparación: `codex/preparacion-repositorio-publico-v1.0`. Árbol inicial limpio, sin cambios ajenos observados.

Entorno observado: WSL2/Linux x86_64, CPython 3.10.12 y Git 2.34.1. Esta ejecución no acredita Windows nativo ni CI remota. La versión de referencia del primer ejercicio es Python 3.12; se registra por separado el intérprete realmente usado. No se ensayan con Python 3.10 los laboratorios que requieren 3.11+.

Se leyeron AGENTS, README, CONTINUIDAD, VERSIONES, PROCEDENCIA, los diez README técnicos y distribuciones/SHA256SUMS. La revisión WSL del laboratorio 10 y sus estados 1.9.2/1.8.2 documentan ejecuciones históricas. El estado 1.9.3 posterior se encontró en la entrega local del cierre, fuera de Git; su publicación se volvió a comprobar por referencias. **ESTADO_DEL_LIBRO_v1.9.6.md no está disponible en el proyecto ni en los 97 archivos de la carpeta editorial proporcionada.** No se inspeccionan otros proyectos para buscarlo ni se inventa su contenido. Durante la preparación el autor facilitó esa carpeta de Drive: se consultaron de lectura el maestro editorial 1.0 y los capítulos 2, 3, 4 v1.1 y 5. Sus encabezados y el índice confirmaron los diez títulos; ese cotejo está APROBADO. Los manuscritos no se modifican ni se incorporan a Git.

## Cambios de acceso

README principal orientado al primer ZIP; [índice y diez fichas](../lectores/README.md); [mapa único](../lectores/mapa_laboratorios.json); diez PNG y diez SVG; hoja de revisión A4; [diez recuadros editoriales](INTEGRACION_QR_EN_LIBRO_v1.0.md); herramientas reproducibles de generación y verificación con dependencias separadas; [propuesta de licencia](PROPUESTA_LICENCIA_v1.0.md). El README anterior se conserva íntegro como antecedente.

Las guías usan rutas mantenibles bajo main con compromiso de conservarlas. Los ZIP usan URLs raw fijadas al commit existente de la base, que ya contiene las diez distribuciones recomendadas. No se crean Releases, Pages ni etiquetas. Se recomienda 8 v1.0.1 y se mantiene su 1.0 histórica. No se modifica el contenido técnico protegido ni manuscritos.

## Verificación de esta ejecución

| Comprobación nueva | Estado y resultado |
| --- | --- |
| Diez fichas y versiones, ZIP, QR y enlaces locales | APROBADO: 94 controles locales. Once ZIP declarados, incluidos los diez recomendados y el antecedente 8 v1.0, con CRC y SHA-256 correctos. Los diez recomendados existen byte por byte en el commit fijado. |
| Lectura autenticada de las diez descargas | APROBADO: API GitHub, JSON base64 decodificado; diez SHA-256 recibidos coinciden. No acredita acceso anónimo al enlace raw. |
| QR PNG y SVG | APROBADO: diez destinos exactos; fondo blanco opaco, margen de cuatro módulos y sólo negro/blanco. Cada SVG renderizado coincide píxel a píxel con su PNG. La simulación de 42 mm a 300 dpi también decodifica los diez. |
| Presentación editorial | APROBADO para inspección digital de hoja A4 y geometría de 42 mm; prueba física de escaneo NO EJECUTADO. [Detalle reproducible](REPRODUCIR_QR_v1.0.md). |
| Primer recorrido, desde ZIP extraído en carpeta nueva | APROBADO como patrón didáctico: inicial A01/A04, tres APROBADO y C04 FALLIDO por aserción, salida 1; solución A01, cuatro APROBADO y salida 0; verificar.py devuelve 0. El fallo C04 conserva su estado FALLIDO. |
| Recolector de huellas | APROBADO: ocho pruebas unittest, código 0, infraestructura separada de los contratos funcionales. No se modifica su código. |
| Conservación técnica | APROBADO: 3.684 archivos existentes distintos del README principal conservan SHA-256; el README anterior se conserva íntegro en el antecedente nuevo. Se repite el cotejo antes y después de integrar. |
| Revisión para divulgación | APROBADO dentro del alcance declarado: historial alcanzable, contenedores y candidatos inspeccionados; sin credenciales reales identificadas. Las limitaciones no equivalen a garantía de ausencia absoluta. [Método y límites](REVISION_DIVULGACION_v1.0.md). |
| Main autenticada después del push | NO EJECUTADO en esta instantánea previa: diez guías y referencias se comprueban después y se registran fuera del commit. |
| Acceso anónimo, apertura pública, Windows nuevo, CI y nueva batería funcional 2–10 | NO EJECUTADO. Se preserva la evidencia histórica, sin atribuirla a esta preparación. |

El primer control local de enlaces fue FALLIDO porque el informe de estado todavía no existía; se conservó ese resultado y el pase posterior aprobó. El primer método de captura binaria de la API terminó con error del transporte CLI; no demuestra ZIP corruptos. La respuesta JSON base64 resolvió la lectura y reprodujo las diez huellas. El instrumento de revisión también corrigió una recursión de cabecera de bundle; no se cambió material técnico. Los intentos y sus resoluciones permanecen en la evidencia externa.

Los comandos, tiempos UTC, stdout/stderr saneados y códigos se entregan en `trabajo/ENTREGA_REPOSITORIO_PUBLICO_v1.0.zip` (o un nombre nuevo si ese destino ya existe). El archivo incorpora comprobante posterior al push, informes, mapa, QR, recuadros y manifiesto/verificador de lectura. El mapa versionado conserva su condición de instantánea anterior al commit; los estados remotos posteriores no se insertan mediante una cadena de commits.

Comandos principales nuevos: generación con `python docs/publicacion/generar_recursos_lectores.py`; verificación con `python docs/publicacion/verificar_recursos_lectores.py --salida trabajo/una_salida_nueva.json`; primer recorrido con los seis comandos del README desde la raíz del ZIP 1 extraído; infraestructura con `python3 -B -m unittest herramientas/pruebas/test_huellas_evidencia.py`. Las dependencias del QR están fijadas en archivos requirements propios, sin mezclarse con los laboratorios. No se repitió la batería funcional completa.

## Pendientes separados

Elegir y aplicar una licencia con titularidad confirmada; resolver decisiones de atribución o anonimización que resulten de la revisión para divulgación; autorizar la apertura pública y verificar después las diez guías y descargas sin autenticación; hacer prueba física de escaneo; insertar los recuadros en la siguiente revisión editorial y comprobar el Word/impreso resultantes. Ninguna de estas decisiones impide subir los ajustes de acceso al repositorio privado.

El maestro editorial 1.0 sigue vigente y los capítulos 1–10 pendientes de revisión. Los recursos QR todavía no están insertados en el manuscrito. Las pruebas locales nuevas, las evidencias históricas Windows/WSL y las interacciones comerciales acreditadas permanecen separadas; no se atribuyen las ejecuciones Python a un producto comercial.
