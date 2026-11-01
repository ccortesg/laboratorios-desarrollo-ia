# Estado del libro · capítulo 8 preparado para revisión

**Versión:** 1.7 · **Fecha de cierre:** 1 de noviembre de 2026, UTC.

Antecedentes vigentes recuperados: `ESTADO_DEL_LIBRO_v1.6.2.md`, `ESTADO_REPOSITORIO_v1.5.2.md` y `CIERRE_LABORATORIO_07_CONFIRMADO_v1.0.md`. Esta entrega ejecuta `PROMPT_CAPITULO_08_v1.0.md`. Los antecedentes se conservan; el cierre Windows y remoto del laboratorio 7 permanece confirmado.

## Decisiones editoriales

Se conserva `DOCUMENTO_MAESTRO_EDITORIAL_v1.0.md` sin modificación. Continúan el índice aprobado, el proyecto sintético de solicitudes e inventario y CLARO: Contextualiza el problema, Limita el alcance, Acuerda criterios de aceptación, Resuelve en incrementos y Observa/documenta.

Promesa: «Aprende a transformar problemas de software en instrucciones claras, cambios revisables y resultados comprobables, aprovechando la IA desde tu primera sesión».

Principio: «La habilidad decisiva consiste en definir bien el trabajo y reconocer, con evidencia, cuándo está terminado».

Se mantienen el público con conocimientos básicos de programación, la anonimización absoluta y las crónicas como reconstrucciones narrativas sintéticas con desarrolladores experimentados. No se recibieron observaciones editoriales nuevas ni aprobaciones expresas. **Los capítulos 1–8 siguen pendientes de revisión editorial del autor.** Una aprobación funcional o publicación de código no aprueba los manuscritos.

## Entregables de esta etapa

- `CAPITULO_08_v1.0.md`: capítulo completo, 4.394 palabras por separación de espacios; diez secciones y crónica sintética de 524 palabras.
- `CAPITULO_08_v1.0.docx`: contenido completo equivalente al Markdown, once páginas renderizadas e inspeccionadas; encabezados, código, enlaces y metadatos revisados. Presentación basada en el Word del capítulo 7.
- `LABORATORIO_08_v1.0.zip`: laboratorio autónomo con 142 archivos, estados base/propuesta/solución, contrato, contexto, datos, comprobaciones, investigación y evidencia.
- Este estado y `ESTADO_REPOSITORIO_v1.6.md`.
- `INTEGRACION_LABORATORIO_08_v1.0.zip`: parche, base y árbol preparado, manifiesto, verificador, instrucciones Windows y evidencia de integración local.

El laboratorio se construyó y ejecutó antes de redactar sus resultados. La narración distingue ejemplos preparados, hipótesis, resultados observados y límites. El reto de comparar dos informes guardados es de sólo lectura, tiene criterios de evaluación y permanece **NO EJECUTADO**.

## Aprendizaje e incremento implementado

El capítulo investiga el síntoma «la importación y la consulta directa son correctas, pero la pantalla conserva el catálogo anterior». El laboratorio 7 era correcto dentro de su alcance en memoria; no se le atribuye este defecto. El incremento nuevo añade SQLite en archivo, inicialización explícita, importador y consulta CLI, servidor con base seleccionada y diagnóstico del origen efectivo dentro de la consulta.

El defecto didáctico de propuesta omite propagar la conexión al resumen HTTP. La solución transmite esa conexión; el diff conserva una línea funcional. No se alteran CSV, filtros, interfaz ni expectativas para conseguir que aprueben. Las pruebas observan entrada, cantidades persistidas, origen efectivo, JSON HTTP y pantalla, con procesos separados y el mismo servidor vivo durante la importación.

Se conservan 51 casos C/B/N/P/W/I con datos de referencia intactos. D01–D08 añaden once casos; la solución reúne 48 criterios distintos y 62 casos. La base deja los once D como NO EJECUTADO porque todavía no tiene persistencia.

## Resultados observados de esta producción

| Alcance | Resultado |
| --- | --- |
| Laboratorio 8 con navegador | APROBADO: 21 baterías, 175 ejecuciones, 171 aprobaciones, cuatro fallos didácticos exactos, cero bloqueos y once NO EJECUTADO. Solución 62/62; huellas finales 38/38. |
| Laboratorio 8 extraído de su ZIP | APROBADO: mismo patrón funcional, 38/38 huellas y 142/142 archivos conservados después de ejecutar. |
| Conjunto 1–8 con navegador | APROBADO: 65 baterías, 583 ejecuciones, 571 aprobaciones, doce fallos didácticos, cero bloqueos, 48 NO EJECUTADO en baterías y diez criterios ausentes aparte. Huellas finales 102/102. |
| Recolector común | APROBADO: ocho pruebas específicas; auxiliar y pruebas conservados sin cambios. Se cuentan por separado. |
| Evaluador del conjunto ampliado | APROBADO: nueve pruebas focales con registros sintéticos para rechazar desviaciones. No se suman a las pruebas funcionales. |

La ejecución de referencia del laboratorio ocurrió el 31 de octubre de 2026 entre 23:57:31 y 23:58:04 UTC. La extracción y el conjunto nuevos se ejecutaron el 1 de noviembre UTC. Las fechas y códigos exactos constan en sus registros. La prueba final del parche tiene evidencia separada dentro del paquete de integración.

Los cuatro fallos nuevos son exclusivamente D03, D04, D05 y D08.a en propuesta 8. Se añaden a los ocho didácticos históricos, que permanecen FALLIDO. Un fallo diferente no está admitido. El subconjunto 1–7 de esta ejecución conserva el patrón 44/408/400/8/0/37; su ejecución Linux es nueva y no sustituye la evidencia Windows del autor.

Se observó ALFA con A01 antes de importar y A01/A03 después; BETA quedó vacío y la búsqueda ` AGOTADO ` devolvió A03. SQLite conservó 5, 8, 3 y 0 en los pares del CSV, con A02 deshabilitado. El resumen cuenta artículos, no unidades. En propuesta, HTTP consultó memoria y la pantalla conservó la referencia pese a la importación correcta.

Entorno observado: Linux, Python 3.12.14, SQLite 3.53.1, Git 2.51.1, Node 24.22.1, Playwright 1.62.1 y Chrome for Testing 156.0.8078.80. La descarga habitual de Chromium no produjo un ZIP válido; se utilizó un navegador compatible obtenido de la distribución oficial, identificado en la evidencia. No se empaqueta el navegador.

## Continuidad técnica y límites

Base remota consultada el 31 de octubre de 2026 a las 23:47:03 UTC: commit `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`, árbol `b123b5969e8077ba0cb3c4eedc9b348f94294652`. Main y las etiquetas lab-07-v1.0/repositorio-v1.3 coincidían. Las once etiquetas existentes se conservaron. La base incluye la corrección del recolector.

El trabajo nuevo se prepara en la rama local `produccion/capitulo-08`. El identificador del árbol preparado y la huella del parche están en `BASE_INTEGRACION.json` del paquete. **No se crea commit, no se integra main, no se crean o mueven etiquetas y no se hace push.** Los nombres lab-08-v1.0 y repositorio-v1.4 son sólo previsiones.

**BLOQUEADO:** ninguno pendiente para el alcance local ejecutado. **NO EJECUTADO:** Windows del laboratorio 8, uso acreditado de herramientas comerciales, GitHub Actions, producción, escritores concurrentes, carga, recuperación física, seguridad integral, reto opcional y capítulo 9. Cambiar de directorio no acredita otro sistema operativo. La revisión del Word corresponde al render disponible, no a una inspección en Microsoft Word del equipo del autor.

Las seis fuentes técnicas primarias se consultaron el 31 de octubre de 2026 y se citan junto a sus afirmaciones. Las afirmaciones sobre el ejercicio se apoyan en los registros incluidos. No se atribuye esta ejecución local a Codex, Copilot o Grok Build.

## Próxima tarea recomendada

Aplicar y verificar el paquete 8 en una rama local de Windows, conservando cualquier avance de main. Seguir `INSTRUCCIONES_WINDOWS.md`; conservar la nueva evidencia y el árbol del índice. Revisar ese resultado antes de autorizar commit, integración y publicación.

La revisión editorial debe centrarse en tres aspectos: la claridad de la voz al separar hechos e hipótesis; la profundidad suficiente para comprender procesos y conexiones; y la utilidad del recorrido para investigar un problema propio. La redacción del capítulo 9 queda fuera de esta entrega.
