# Informe de cierre del laboratorio 9 · WSL · v1.0

**Resultado técnico:** APROBADO. Confirmado mediante consultas remotas después del push atómico, el 2026-11-01T23:19:41.305555+00:00.

| Referencia o contenido | SHA confirmado |
| --- | --- |
| main remoto | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| lab-09-v1.0 | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| repositorio-v1.5 | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| Árbol del commit de cierre | `790e875fc95495c39ea2b5ebe7621a4ae1afa30f` |
| Árbol funcional auditado anterior | `251105483bc5bef040c57dc3a036d5bc3a7e0da0` |
| Commit de base conservado | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |

Se incorporaron la revisión WSL exacta y los estados recibidos libro 1.8.1/repositorio 1.7.1. Los estados de preparación 1.8.2/1.7.2 permanecen en el commit como fotografía anterior a la publicación. El incremento posterior al árbol funcional consta de 29 rutas documentales; 2.268 archivos anteriores conservan identidad y los 1.502 archivos protegidos mantienen sus hashes. No se reaplicó el parche ni se modificaron código, pruebas, datos, distribuciones o evidencias anteriores.

El commit se creó en `codex/integracion-laboratorio-09`, se integró en main por avance rápido y se publicaron exclusivamente las tres referencias autorizadas, sin forzar. Las trece etiquetas históricas conservan su identidad local y remota; las dos nuevas son ligeras. Main no presentó avances ajenos durante este cierre. El árbol de trabajo terminó limpio, en main. Las consultas acreditan el estado puntual registrado, sin impedir futuros avances legítimos.

Las 805 ejecuciones de 92 baterías son evidencia WSL anterior auditada: 781 APROBADO, 24 FALLIDO didácticos exactos, cero bloqueos y cero errores de ejecución; 48 NO EJECUTADO y diez criterios ausentes aparte. Solución 9: 74/74. La infraestructura histórica 8/9/4 sigue separada. Este cierre no repitió esas 805 ejecuciones. Ejecutó ocho pruebas nuevas del recolector, APROBADO con salida 0, y comprobó todas las huellas declaradas de la evidencia usada: 210/210, derivadas de los registros. Se cotejaron también CRC, cobertura de manifiestos, archivos y referencias Git.

Entorno nuevo observado: Linux/WSL2, Python funcional 3.12.16, SQLite 3.53.1; Python de preparación 3.10.12. Las pruebas funcionales anteriores conservan su atribución WSL; Windows nativo, CI remota, producción y nuevas interacciones Copilot/Grok Build están NO EJECUTADO en este cierre. Los intentos anteriores FALLIDO o BLOQUEADO y sus resoluciones se conservan con sus bytes y estados. Las dos capturas originales ausentes del envío previo no se reconstruyeron; sus bytes finales sí se verificaron.

El maestro editorial 1.0 y los manuscritos no se modificaron. Los capítulos 1–9 continúan pendientes de revisión editorial del autor. No se redactó el capítulo 10.

Este documento se genera después de publicar y permanece fuera del commit que acredita. Su evidencia está en el ZIP de cierre, con manifiesto completo y hashes de bytes finales. El SHA-256 del ZIP se entrega aparte para evitar autorreferencia.


## Qué cambió y qué se ejecutó

Se mantuvo el índice funcional recibido con sus 771 rutas preparadas. Se verificaron el ZIP de revisión (SHA-256 `3309df01455ce38f8c0e29ced072ea63fa33c788ef1d240f24336714bce64eaf`, 16 archivos extraídos) y el ZIP funcional original (SHA-256 `6aaeb6ce9e0cf781239499fae2f57bb147b5b2b07b7a20d5cfbd5d61a4ffb239`, 453 archivos y 452 entradas del manifiesto). Ambas extracciones coinciden byte a byte con sus contenedores. Los estados 1.8.1/1.7.1 son copias exactas.

El contenido autorizado añadido se identifica por rutas, SHA-256 y tamaños en [VALIDACION_PRECOMMIT.json](../VALIDACION_PRECOMMIT.json). README, continuidad, versiones, AGENTS y procedencia se actualizaron como documentación de preparación. Se conservó íntegro el índice histórico de evidencia al resultar suficiente la referencia de raíz; [ajuste de la adición propia](../AJUSTE_DOCUMENTAL.json). Los originales del paquete y las evidencias anteriores no se alteraron.

Antes de añadir documentos se comprobaron los 2.273 archivos del árbol auditado; después, sólo difieren los cinco documentos operativos de raíz autorizados, y se añaden 24 rutas documentales. El recolector y sus ocho pruebas coinciden incluso con la base del laboratorio 8. La comprobación del índice acredita bytes y modos para todo archivo previo que debía conservarse.

Las referencias iniciales, anteriores a commit, anteriores a etiquetas y posteriores al push están en `operaciones/`. Se utilizó `git fetch --no-tags origin`, se comprobó ascendencia, se integró con `git merge --ff-only codex/integracion-laboratorio-09` y se crearon sólo las dos etiquetas ligeras nuevas. La publicación exacta fue:

```bash
git push --atomic --no-follow-tags origin refs/heads/main:refs/heads/main refs/tags/lab-09-v1.0:refs/tags/lab-09-v1.0 refs/tags/repositorio-v1.5:refs/tags/repositorio-v1.5
```

La operación y la reconsulta terminaron con salida 0. El resultado real está en [PUBLICACION_CONFIRMADA.json](../PUBLICACION_CONFIRMADA.json). Los registros de comandos contienen argumentos exactos, directorio mediante alias, inicio/fin UTC, código de salida, stdout/stderr y hashes originales/finales separados. Las capturas originales nuevas se preservan localmente en `trabajo/cierre_lab09_wsl_20261101T231144Z_capturas_originales/`, fuera del ZIP saneado.

## Clasificación

| Alcance | Estado y atribución |
| --- | --- |
| Identidad del árbol auditado, paquetes, manifiestos y 210 huellas anteriores | APROBADO; nueva comprobación de integridad, sin nueva batería funcional. |
| Ocho pruebas del recolector | APROBADO; nueva ejecución del cierre, salida 0. |
| 805 ejecuciones funcionales y pruebas 8/9/4 | APROBADO como evidencia anterior auditada; 24 FALLIDO didácticos conservados. |
| Commit, avance rápido, push atómico y referencias finales | APROBADO; operaciones nuevas efectivamente ejecutadas. |
| Fallos inesperados o bloqueos nuevos pendientes | Ninguno. |
| Repetición funcional, Windows nativo, CI remota, producción y reto opcional | NO EJECUTADO en este cierre. |
| Revisión editorial de capítulos 1–9 | Pendiente del autor; la validación técnica no la acredita. |

## Operaciones y códigos

| Registro | Salida | Estado |
| --- | ---: | --- |
| ajustar_indice_documental | 0 | APROBADO |
| arbol_documental_preparado | 0 | APROBADO |
| arbol_documental_validado | 0 | APROBADO |
| ascendencia_base_remota | 0 | APROBADO |
| ascendencia_main_precommit | 0 | APROBADO |
| ascendencia_origin_precommit | 0 | APROBADO |
| avance_remoto_prepublicacion | 0 | APROBADO |
| cambiar_a_main | 0 | APROBADO |
| cierre_ancestro_remoto_final | 0 | APROBADO |
| commit_cierre | 0 | APROBADO |
| crear_lab-09-v1_0 | 0 | APROBADO |
| crear_repositorio-v1_5 | 0 | APROBADO |
| diff_documentacion | 0 | APROBADO |
| entorno_runtime | 0 | APROBADO |
| estado_antes_integracion | 0 | APROBADO |
| estado_local_final | 0 | APROBADO |
| fetch_antes_integracion | 0 | APROBADO |
| fetch_despues_publicacion | 0 | APROBADO |
| fetch_inicial | 0 | APROBADO |
| fetch_precommit | 0 | APROBADO |
| fetch_prepublicacion | 0 | APROBADO |
| formato_indice | 0 | APROBADO |
| huellas_evidencia_aportada | 0 | APROBADO |
| identidad_commit_cierre | 0 | APROBADO |
| identidad_inicial | 0 | APROBADO |
| identidad_local_final | 0 | APROBADO |
| identidad_main_integrado | 0 | APROBADO |
| indice_inicial | 0 | APROBADO |
| indice_inmediato_precommit | 0 | APROBADO |
| integrar_main_avance_rapido | 0 | APROBADO |
| inventario_arbol_funcional | 0 | APROBADO |
| inventario_documental_precommit | 0 | APROBADO |
| locales_despues_publicacion | 0 | APROBADO |
| locales_prepublicacion | 0 | APROBADO |
| main_ancestro_cierre | 0 | APROBADO |
| main_inmediato_pre_push | 0 | APROBADO |
| nuevos_inicial | 0 | APROBADO |
| nuevos_precommit | 0 | APROBADO |
| origin_ancestro_cierre | 0 | APROBADO |
| preparar_documentacion | 0 | APROBADO |
| preparar_solo_documentacion | 0 | APROBADO |
| publicar_cierre | 0 | APROBADO |
| push_atomico_autorizado | 0 | APROBADO |
| rama_inicial | 0 | APROBADO |
| ramas_finales | 0 | APROBADO |
| recolector | 0 | APROBADO |
| refs_iniciales | 0 | APROBADO |
| remotas_antes_integracion | 0 | APROBADO |
| remotas_despues_publicacion | 0 | APROBADO |
| remotas_iniciales | 0 | APROBADO |
| remotas_precommit | 0 | APROBADO |
| remotas_prepublicacion | 0 | APROBADO |
| remoto_configurado | 0 | APROBADO |
| rutas_documentales_precommit | 0 | APROBADO |
| rutas_indice_inicial | 0 | APROBADO |
| sin_preparar_inicial | 0 | APROBADO |
| sin_preparar_precommit | 0 | APROBADO |
| tipo_lab-09-v1_0 | 0 | APROBADO |
| tipo_repositorio-v1_5 | 0 | APROBADO |
| validacion_precommit | 0 | APROBADO |
| verificar_insumos | 0 | APROBADO |
| verificar_revision | 0 | APROBADO |

El índice definitivo se deriva de todos los JSON realmente capturados al finalizar: [operaciones/comandos.json](../operaciones/comandos.json). Los resultados generados después de esta tabla también se incluyen allí. El manifiesto final se calcula después del saneamiento, con cobertura completa excepto el propio manifiesto. La verificación posterior del ZIP y su SHA-256 se conservan fuera del archivo. Ningún comprobante posterior se añadió al commit publicado.
