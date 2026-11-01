# Revisión de la integración del laboratorio 9 en WSL

**Dictamen: APROBADO para continuar con el cierre.** Revisión del 1 de noviembre de 2026. La integración está preparada en una rama local y todavía no está publicada. Esta aprobación técnica no constituye aprobación editorial de los capítulos ni una ejecución del cierre.

## 1. Material recibido y alcance de la revisión

Se examinó `EVIDENCIA_LABORATORIO_09_WSL_v1.0.zip`, aportado por el autor como resultado de la ejecución de Codex. Su SHA-256 es `6aaeb6ce9e0cf781239499fae2f57bb147b5b2b07b7a20d5cfbd5d61a4ffb239`; contiene 453 archivos y ocupa 412.572 bytes. El archivo original y todos sus archivos extraídos se conservaron sin modificaciones.

La revisión realizó un recuento independiente de resultados, comprobó los bytes y manifiestos, cotejó fuentes contra el árbol preparado conocido y consultó nuevamente las referencias del repositorio autorizado. No ejecutó otra batería funcional, no accedió al disco WSL del autor y no ejecutó los scripts recibidos. Los resultados funcionales siguen atribuidos a la sesión aportada; las auditorías de esta revisión se registran por separado.

Se utilizaron el paquete de integración 1.0 y los estados libro 1.8/repositorio 1.7 de la entrega anterior. Las ocho copias de auxiliares e instrucciones incluidas en el envío coinciden byte a byte con esos insumos. No se sustituyó una versión ni fue necesaria una corrección del código.

## 2. Identidad de lo que quedó preparado

| Elemento | Resultado cotejado |
| --- | --- |
| HEAD, main local y main remoto | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |
| Árbol de la base | `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0` |
| Rama de la ejecución aportada | `codex/integracion-laboratorio-09` |
| Árbol del índice preparado | `251105483bc5bef040c57dc3a036d5bc3a7e0da0` |
| SHA-256 del parche aplicado | `219e9b2f2353c0b55c3418d3af3277f643ce5ce151deebafcd4f425d31cc8f42` |
| Rutas preparadas | 771, exactamente las declaradas en el paquete |
| Archivos anteriores protegidos | 1.502, sin divergencias respecto a los hashes recibidos y la base conocida |

Los registros inicial, preparado y final mantienen HEAD y main en la base. La única referencia local nueva declarada es la rama de integración; no hay un commit nuevo. Las trece etiquetas locales históricas se conservan en los registros y las dos etiquetas previstas siguen ausentes.

La reconsulta independiente de GitHub se realizó a las **15:37:39 de Hermosillo del 1 de noviembre de 2026**, equivalentes a **22:37:39 UTC**. Main y las trece etiquetas coinciden con los registros aportados; `lab-09-v1.0` y `repositorio-v1.5` todavía no existen. La consulta fue de sólo lectura y su alcance termina en ese momento.

La copia de preparación utilizada para esta auditoría conserva el mismo contenido, pero su rama se llama `integracion/laboratorio-09` y no tiene etiquetas locales. No se confundieron esas características con las de la copia WSL del autor, que sí conserva las trece etiquetas. La coincidencia relevante es la base y el árbol preparado.

## 3. Resultados funcionales reconstruidos

Se contaron 853 filas de casos en los JSON individuales de 92 baterías. De ellas, 805 corresponden a ejecuciones y 48 conservan NO EJECUTADO por el alcance histórico. Diez criterios ausentes se registran fuera de esas baterías: N01–N10 en `laboratorio_04/inicio`.

| Alcance | Ejecutados | APROBADO | FALLIDO didáctico | BLOQUEADO |
| --- | ---: | ---: | ---: | ---: |
| Conjunto de laboratorios 1–9 | 805 | 781 | 24 | 0 |
| Base del laboratorio 9, incluida en el conjunto | 74 | 65 | 9 | 0 |
| Propuesta del laboratorio 9, incluida en el conjunto | 74 | 71 | 3 | 0 |
| Solución del laboratorio 9, incluida en el conjunto | 74 | 74 | 0 | 0 |

La solución 9 aprueba los 62 casos heredados y los doce casos del incremento. El recorrido con navegador está ejecutado y aprobado. No hay errores de ejecución ni bloqueos disfrazados de fallos didácticos.

Los 24 FALLIDO tienen el tipo de error de aserción esperado y estas identidades exactas:

| Batería | Fallos previstos y observados |
| --- | --- |
| Inicial del laboratorio 1 | C04 |
| Defecto del laboratorio 3 | B05, B06 |
| Propuesta de resumen del laboratorio 5 | P04, P05 |
| Propuesta de navegador del laboratorio 6 | W05 |
| Propuesta de integración del laboratorio 7 | I01, I07 |
| Propuesta de depuración del laboratorio 8 | D03, D05, D08.a |
| Propuesta de depuración en navegador del laboratorio 8 | D04 |
| Base de seguridad del laboratorio 9 | S02.a, S02.b, S02.c, S03, S04.a, S04.b, S05.a, S05.b |
| Base de seguridad en navegador del laboratorio 9 | S06 |
| Propuesta de seguridad del laboratorio 9 | S02.a, S02.b, S02.c |

La base 9 falla exigencias nuevas que aún no implementa; conserva aprobado el contrato heredado. La propuesta falla por perder los parámetros repetidos al convertir prematuramente sus pares a un diccionario. La aprobación del recorrido exige ese patrón exacto y una solución sin fallos; no cambia los FALLIDO individuales a APROBADO.

Las 805 ejecuciones pertenecen a esta sesión WSL. No se suman a las ejecuciones Linux de producción para aparentar más casos, y no reutilizan como resultados nuevos las 583 ejecuciones históricas de Windows del laboratorio 8.

## 4. Infraestructura, fuentes y huellas

Las capturas contienen los nombres individuales, `ok`, los conteos y el cierre `OK` de las ocho pruebas del recolector, nueve del evaluador y cuatro de recursos SQLite. Todos terminaron con código 0. Los 21 nombres se cotejaron con las fuentes mediante lectura y análisis sintáctico; estas pruebas no se añaden a las 805 ejecuciones funcionales.

Se cotejaron 387 referencias de ocho manifiestos `sha256_fuentes.json` contra los archivos conocidos y los blobs del árbol preparado: todas coinciden. El laboratorio 4 utiliza otros manifiestos; se verificaron sus dos herramientas, 17 archivos visibles de solución, el bundle distribuido y las referencias correspondientes. No se reconstruyó ni ejecutó otra vez su repositorio durante esta auditoría.

| Capa de integridad | Resultado independiente |
| --- | --- |
| Contenedor ZIP y extracción | 453/453 archivos idénticos; CRC correcto; sin rutas inseguras, duplicados ni enlaces |
| Manifiesto del envío | 452/452 archivos con tamaño y SHA-256 coincidentes; excluye sólo el propio manifiesto |
| Huellas funcionales | 156/156 coincidentes |
| Huellas de la verificación con auxiliares | 164/164: incluyen las 156 anteriores y ocho capturas externas |
| Huellas de operaciones de preparación | 46/46, correspondientes a 23 operaciones |
| Total de huellas finales declaradas en el envío | 210/210: 156 + 8 + 46 |

Los recuentos se obtuvieron de las referencias existentes; no se fijó 210 para forzar una aprobación. Tres registros NO EJECUTADO conservan su ausencia de salidas y huellas. Las diez distribuciones se comprobaron en la sesión recibida y su captura termina correctamente.

Hay dos huellas de captura diferentes de las finales: el stderr de la aplicación del parche y el stdout de arranque del navegador. Sus archivos finales sí coinciden con sus SHA. La diferencia es coherente con el saneamiento declarado, pero los bytes originales están fuera del ZIP y no pueden reconstruirse a partir de un hash. La revisión independiente acredita los bytes finales compartidos; la conservación de esas dos capturas originales continúa atribuida al productor. No se recalcularon huellas para ocultar una discrepancia.

## 5. Entorno y observaciones resueltas

La sesión aportada se ejecutó en **Linux/WSL2**, con Git 2.34.1, Node 22.23.1, npm 10.9.8, Playwright 1.62.1 y Chromium 151.0.7922.34. Se registró un arranque real del navegador.

El Python inicial era 3.10.12. Se preparó un intérprete aislado bajo `trabajo/` y las pruebas se ejecutaron con **Python 3.12.16 y SQLite 3.53.1**. Los registros distinguen preparación y ejecución; no se acredita Windows nativo.

La aplicación del parche emitió advertencias de espacios finales en 30 líneas de materiales importados. Terminó con código 0, `git diff --cached --check` aprobó y el índice coincide exactamente con el árbol distribuido. No hubo una corrección de bytes históricos para eliminar las advertencias. Las 23 operaciones documentadas terminaron con código 0 y la conservación final no encontró cambios sin preparar ni archivos nuevos no ignorados.

Se revisaron nombres, texto y metadatos del envío sin encontrar rutas personales, correos, nombres típicos de equipos ni credenciales en los patrones examinados. Se conservan tres URL del repositorio autorizado y su API dentro de la copia exacta de `BASE_INTEGRACION.json`; corresponden a la documentación operativa permitida. El paquete no debe confundirse con un extracto de manuscrito listo para publicación anónima. Una búsqueda por patrones no constituye un detector universal de información identificable.

## 6. Estado alcanzado y siguiente tarea

**APROBADO:** evidencia de integración preparada, patrón funcional, infraestructura separada, huellas finales, correspondencia de fuentes y conservación de la base. **FALLIDO inesperado pendiente:** ninguno identificado. **BLOQUEADO:** ninguno dentro del alcance revisado.

**NO EJECUTADO por esta revisión:** nueva batería funcional, acceso directo al WSL del autor, reconstrucción de las dos capturas originales no incluidas, commit, integración en main, etiquetas y push. Los resultados funcionales son los aportados por la sesión Codex del autor. El campo «herramientas comerciales: NO EJECUTADO por este verificador» describe lo que hace el programa de pruebas; no niega la orquestación de Codex comunicada por el autor.

La siguiente tarea recomendada es incorporar esta revisión y los estados libro 1.8.1/repositorio 1.7.1, preparar el cierre documental y, mediante un encargo que lo autorice expresamente, crear el commit, integrar main y publicar únicamente las dos etiquetas previstas. El prompt adjunto describe ese encargo futuro; no se ha ejecutado como parte de esta revisión.

No hace falta reaplicar el parche ni repetir la batería completa mientras el código, las pruebas, los datos y el árbol funcional verificado permanezcan iguales. Una adaptación a avances posteriores que afecte ese contenido necesita su propia comprobación antes de cerrar.

El maestro editorial 1.0 y los manuscritos no se modificaron. Los capítulos 1–9 continúan pendientes de revisión editorial del autor. No se redactó el capítulo 10.

## Documentación de respaldo

- [Auditoría independiente de integridad](auditoria/INTEGRIDAD_INDEPENDIENTE.json).
- [Auditoría independiente funcional y de fuentes](auditoria/FUNCIONAL_INDEPENDIENTE.json).
- [Cotejo Git y conservación](auditoria/GIT_Y_CONSERVACION.json).
- [Consulta remota de esta revisión](auditoria/REFERENCIAS_REMOTAS_RECONSULTADAS.json).
- [Evidencia original recibida, conservada sin cambios](recibido/EVIDENCIA_LABORATORIO_09_WSL_v1.0.zip).
