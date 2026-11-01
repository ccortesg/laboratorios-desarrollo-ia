# Estado operativo del repositorio · laboratorio 8 preparado

**Versión documental:** 1.6 · **Fecha:** 1 de noviembre de 2026, UTC.

Repositorio sintético autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

La versión técnica publicada sigue siendo repositorio-v1.3, con laboratorio 7. Esta entrega prepara la integración técnica 1.4 y laboratorio 8 v1.0 para revisión. `ESTADO_REPOSITORIO_v1.5.2.md`, `ESTADO_DEL_LIBRO_v1.6.2.md` y el cierre confirmado del 7 se recuperan y conservan como antecedentes; sus pendientes ya cerrados no se reabren.

## 1. Base comprobada

Consulta remota efectiva mediante lectura de GitHub: **2026-10-31 23:47:03 UTC**.

| Objeto | Identificador |
| --- | --- |
| main, lab-07-v1.0 y repositorio-v1.3 | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| Árbol de la base | `b123b5969e8077ba0cb3c4eedc9b348f94294652` |
| Único padre, con recolector corregido | `6382e05846e149a9a72f7fdc56da48c37a873833` |
| lab-06-v1.0 y repositorio-v1.2 | `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd` |

Las once etiquetas consultadas mantienen sus destinos. La lista completa está en `evidencia_integracion/laboratorio_08_v1.0/auditoria/BASE_REMOTA.json` y en el paquete. No se encontró un avance posterior a la base en esa consulta. Debe consultarse de nuevo antes de aplicar en otro momento.

Git por HTTPS no dispuso de autenticación en este entorno. La copia local se recuperó de objetos conservados y metadatos del commit existente obtenidos mediante lectura autorizada; se verificaron exactamente el SHA del commit y su árbol. Esto no creó un commit nuevo ni acredita una clonación HTTPS satisfactoria. La rama de trabajo es `produccion/capitulo-08`, con HEAD en la base confirmada.

## 2. Cambios preparados

Se añade `laboratorios/laboratorio_08/` con 142 archivos y su distribución autónoma. Incluye contexto, contrato, estados, datos, diagnóstico, comprobaciones, diff y evidencia local. El laboratorio introduce persistencia explícita sin modificar los archivos de los laboratorios 1–7.

Se amplía `herramientas/verificar_todo.py` para evaluar 21 baterías adicionales. Valida el patrón exacto, incluidos conteos y casos parcialmente BLOQUEADO si falta acceso local; no acepta excepciones internas como defectos didácticos. El auxiliar `huellas_evidencia.py` y sus ocho pruebas conservan sus bytes y semántica.

Se actualizan README, AGENTS, CONTINUIDAD, VERSIONES, procedencia y manifiesto de distribuciones. Los atributos sólo añaden excepciones acotadas para conservar diffs y Markdown históricos; no se corrigen sus bytes retroactivamente. La carpeta de trabajo del laboratorio 8 queda ignorada. El cierre del 7 recibido por separado se incorpora bajo `evidencia_integracion/cierre_laboratorio_07_confirmado/` y sus estados se añaden a `docs/estados/`.

La auditoría conserva 954/954 archivos históricos de la base en laboratorios, distribuciones, historiales y evidencia. El manifiesto de distribuciones se amplía conservando las siete entradas previas. Las entradas antiguas de PROCEDENCIA se mantienen; el inventario visible actualizado contiene 592 archivos de ocho laboratorios. Esta cuenta describe archivos, no cobertura funcional.

## 3. Resultados nuevos

Comando de conjunto ejecutado en Linux:

```bash
python herramientas/verificar_todo.py --navegador --salida SALIDA/conjunto_01
```

Inicio 2026-11-01 00:01:38 UTC; fin 00:02:43 UTC; código 0. Se registró APROBADO global y en los recorridos de extremo a extremo. El paquete conserva otra ejecución desde la copia limpia con el parche aplicado.

| Medida funcional | Resultado del conjunto 1–8 |
| --- | ---: |
| Baterías | 65 |
| Ejecuciones | 583 |
| APROBADO | 571 |
| FALLIDO didácticos exactos | 12 |
| BLOQUEADO | 0 |
| NO EJECUTADO en baterías | 48 |
| Criterios ausentes aparte | 10 |

Fallos admitidos exclusivamente: C04 en inicial 1; B05/B06 en defecto 3; P04/P05 en propuesta 5; W05 en propuesta 6; I01/I07 en propuesta 7; D03/D04/D05/D08.a en propuesta 8. Permanecen FALLIDO por aserciones; no hay fallos inesperados aceptados.

El subconjunto 1–7 conserva 44 baterías, 408 ejecuciones, 400 aprobaciones, ocho fallos, cero bloqueos y 37 NO EJECUTADO. Es una ejecución Linux nueva; la ejecución Windows histórica conserva sus propios registros.

Por separado, aprobaron ocho pruebas del recolector y nueve pruebas focales del evaluador. Se comprobaron dinámicamente 102/102 huellas finales stdout/stderr del conjunto, sin fijar un recuento histórico. Coincidieron también 333/333 declaraciones de fuentes principales, incluidos los blobs históricos del laboratorio 4 leídos desde su bundle. Los campos repetidos de preparación y conservación se desglosan en su auditoría; no se suman a las ejecuciones funcionales ni se presentan como archivos únicos.

El laboratorio autónomo produjo 21 baterías, 175 ejecuciones, 171 aprobaciones, cuatro fallos previstos, cero bloqueos y once NO EJECUTADO en base. La solución satisface 62/62 casos, correspondientes a 48 criterios. El pase desde el ZIP descomprimido reprodujo ese patrón, con 38/38 huellas finales y 142/142 archivos intactos después de ejecutar.

Entorno: Linux, Python 3.12.14, SQLite 3.53.1, Git 2.51.1, Node 24.22.1, Playwright 1.62.1 y Chrome for Testing 156.0.8078.80. Las pruebas usan ese ejecutable compatible mediante la opción documentada; la descarga habitual de Playwright no produjo un ZIP válido. El origen oficial y la huella del navegador están registrados, sin incluir binarios en la entrega.

## 4. Integración y trazabilidad

`INTEGRACION_LABORATORIO_08_v1.0.zip` contiene `INTEGRAR_LABORATORIO_08.patch`, `BASE_INTEGRACION.json`, un manifiesto SHA-256, `VERIFICAR_PAQUETE.py`, instrucciones Git Bash y evidencia saneada.

El parche se comprueba y aplica con `--index` sobre una copia limpia del commit registrado; se verifica el árbol resultante y se ejecutan el recolector, el conjunto con navegador y el comprobador dinámico de huellas. **El identificador exacto del árbol preparado está en `BASE_INTEGRACION.json`, campo `arbol_preparado`**, junto con la huella del parche. Se registra fuera del árbol para evitar una referencia circular. Los resultados finales de esa prueba están en `evidencia/prueba_parche/` del paquete.

Los registros incluidos en el repositorio describen el primer pase de producción y la comprobación del ZIP. La prueba final del parche se guarda fuera del parche, en su paquete, para no cambiar el árbol ya verificado. No se reescribe evidencia histórica para hacer coincidir huellas.

## 5. Estado y límites

**APROBADO:** ejecución local del laboratorio y del conjunto; ocho pruebas del recolector; pruebas focales del evaluador; huellas finales; conservación histórica; ejecución del ZIP; revisión del capítulo y presentación renderizada del Word. La aplicación final del parche y su evidencia están identificadas en el paquete.

**BLOQUEADO:** ninguno pendiente en el alcance local completado.

**NO EJECUTADO:** Windows del laboratorio 8, nuevas sesiones comerciales, GitHub Actions, producción, concurrencia de escritores, carga, recuperación física, seguridad integral y reto opcional. El escenario D04 sí demuestra la cadena CSV→CLI→SQLite persistente→HTTP→pantalla en Linux, con el mismo servidor vivo durante la importación. Ese alcance no se extiende a otros entornos por inferencia.

No se creó un commit nuevo, no se integró main, no se crearon o movieron etiquetas y no se hizo push. `lab-08-v1.0` y `repositorio-v1.4` son nombres previstos, pendientes de creación. Las once etiquetas existentes mantienen su identidad. Los capítulos 1–8 permanecen pendientes de revisión editorial; el maestro 1.0 no cambia.

## 6. Siguiente operación

Seguir `INSTRUCCIONES_WINDOWS.md` del paquete: comprobar integridad, registrar estado y referencias, crear una rama local, conservar cualquier avance de main, aplicar, revisar diferencias y ejecutar las comprobaciones. El procedimiento termina con el cambio y una evidencia Windows nuevos preparados para revisión, sin cierre automático.

Si la base avanzó, no regresar a una etiqueta antigua ni forzar la aplicación. Conservar el avance, revisar los archivos comunes y adaptar el parche en la rama nueva; el árbol exacto cambiará y deberá registrarse y verificarse de nuevo. La revisión posterior decidirá el cierre técnico. El capítulo 9 no se redacta en esta etapa.
