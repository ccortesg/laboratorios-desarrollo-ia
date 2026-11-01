# Estado del libro · capítulo 9 preparado para revisión

**Versión:** 1.8. **Fecha:** 1 de noviembre de 2026. **Antecedente vigente conservado:** `ESTADO_DEL_LIBRO_v1.7.4.md` y `CIERRE_LABORATORIO_08_CONFIRMADO_v1.0.md`.

## Entrega editorial

Completados `CAPITULO_09_v1.0.md` y `CAPITULO_09_v1.0.docx`, «Confiabilidad y seguridad del software generado por IA». El borrador contiene 4.236 palabras por separación de espacios, diez secciones y una Crónica de Adopción Real de 523 palabras, rotulada como reconstrucción narrativa sintética. El Word contiene el capítulo completo en once páginas, renderizadas e inspeccionadas; texto, código y seis referencias coinciden con el Markdown. Sus metadatos de autor están vacíos.

La promesa, el principio rector, el público, el índice y CLARO permanecen vigentes. `DOCUMENTO_MAESTRO_EDITORIAL_v1.0.md` no cambia: el incremento técnico no exige una modificación editorial. Los capítulos 1–8 siguen pendientes de revisión del autor; el capítulo 9 se incorpora como otro borrador pendiente. No se infieren aprobaciones editoriales de los resultados técnicos ni del cierre de GitHub.

La entrega incluye además `LABORATORIO_09_v1.0.zip`, `ESTADO_REPOSITORIO_v1.7.md` e `INTEGRACION_LABORATORIO_09_v1.0.zip`. El manuscrito y el Word permanecen en el flujo editorial, fuera del repositorio técnico.

## Decisión didáctica y técnica

El laboratorio parte de la solución corregida del 8 y conserva el recorrido CSV → importador CLI → SQLite persistente → HTTP → navegador. El incremento define una política pequeña para GET `/api/resumen`: parámetros admitidos, rechazo de repeticiones después de decodificar, sintaxis estricta de percent-encoding y UTF-8, y límites de query y nombre. Los límites de 2.048 bytes y 80 puntos de código Unicode son decisiones didácticas, no requisitos universales.

La base mantiene el código anterior. La propuesta transforma pares a diccionario demasiado pronto y pierde las repeticiones que debe detectar. La solución conserva la lista hasta validarla. El capítulo explica la diferencia entre una entrada ambigua, un resultado vacío, un rechazo y un fallo interno, y relaciona cada caso con su evidencia.

Se conservan 62 casos heredados. Ocho criterios nuevos S01–S08 añaden doce casos: la solución contiene 56 criterios distintos y 74 casos. La ejecución de los mismos casos en tres estados genera 222 ejecuciones; no son 222 criterios diferentes. El reto de comprobar cabeceras comunes en respuestas 200/400/414/500 está descrito y evaluable, pero no implementado.

## Resultados nuevos observados

Las ejecuciones de esta producción corresponden a Linux, Python 3.12.14, SQLite 3.53.1, Node 24.22.1, Playwright 1.62.1 y Chrome for Testing 151.0.7922.34.

| Comprobación | Resultado observado |
| --- | --- |
| Autónomo completo | APROBADO; 27 baterías; 222 ejecuciones; 210 APROBADO y 12 FALLIDO didácticos exactos; cero bloqueos y errores. |
| Solución del laboratorio 9 | 74/74 casos APROBADO, incluidos los 62 heredados. |
| Conjunto de laboratorios 1–9 | APROBADO, código 0; 92 baterías; 805 ejecuciones; 781 APROBADO y 24 FALLIDO didácticos; cero bloqueos. |
| Casos históricos omitidos por alcance | 48 NO EJECUTADO en baterías del conjunto y diez criterios ausentes aparte. |
| Huellas finales | 54/54 del autónomo; 156/156 del conjunto funcional. |
| Infraestructura, separada | Ocho pruebas del recolector, nueve del evaluador y cuatro regresiones de recursos SQLite APROBADO. |
| ZIP descomprimido | APROBADO; los 292 archivos conservaron sus bytes; reprodujo 222/210/12 y 54/54 huellas funcionales. |

Cada fila identifica un alcance. Las repeticiones desde el ZIP y desde la copia con el parche no se suman para aparentar mayor cobertura. Los informes del ensayo del parche acompañan el paquete de integración, fuera del árbol que acreditan.

El primer autónomo resultó FALLIDO por dos TimeoutExpired adicionales en S06. Los diagnósticos con dos versiones de navegador localizaron la espera en la lectura `response.json()` después de HTTP 400, sin determinar su causa interna completa. Se corrigió únicamente la observación redundante de la prueba: S06 mantiene HTTP, DOM, controles y recuperación; S04.a comprueba el cuerpo JSON exacto. Se conservaron las capturas, el instrumento anterior y su diferencia. No se cambiaron la aplicación, el contrato, las expectativas heredadas ni los plazos para ocultar el fallo.

## Continuidad, fuentes y límites

La base remota se reconsultó el 1 de noviembre de 2026 a las 21:50:33 UTC. Main, `lab-08-v1.0` y `repositorio-v1.4` conservaban `9212ee99b88f70f0b289837b88d6bbf34da91a52`, árbol `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0`; las trece etiquetas permanecían intactas. Se incorporan como adiciones exactas los estados 1.7.4/1.6.4, el cierre confirmado y su revisión recibida por separado.

Las 583 ejecuciones Windows del laboratorio 8 y el cierre WSL posterior conservan su atribución histórica. El conjunto nuevo volvió a ejecutar ese subconjunto en Linux; la coincidencia de sus cifras no transforma los antecedentes en resultados nuevos. Esta entrega no acredita una nueva sesión comercial de Codex, Copilot o Grok Build ni una ejecución Windows/WSL del laboratorio 9.

Las seis fuentes primarias del capítulo se consultaron el 1 de noviembre de 2026. Prompts didácticos, reconstrucción narrativa y resultados observados se identifican expresamente. La revisión de contenido, datos, nombres y metadatos mantiene el material sintético; las referencias del repositorio se reservan a documentación operativa.

**NO EJECUTADO:** integración del 9 en main, publicación, etiquetas nuevas, ejecución del reto y evaluación productiva de seguridad. El ejercicio no implementa autenticación, autorización, exposición pública ni pruebas generales de carga. No queda un fallo inesperado aceptado como didáctico en la solución final.

## Siguiente tarea

Revisar voz, profundidad técnica y utilidad del recorrido, y preparar la integración local con Codex siguiendo el prompt incluido en el paquete. Ese paso termina con evidencia nueva para revisión, sin commit, main, etiquetas ni push. El cierre remoto requerirá un encargo posterior. No se redactó el capítulo 10.
