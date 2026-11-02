# Revisión del cierre del laboratorio 9 · v1.0

**Resultado:** APROBADO en el alcance de integridad, conservación y publicación revisado. **Fecha:** 1 de noviembre de 2026. **Consulta remota nueva:** 23:35:34 UTC, equivalente a las 16:35:34 en Hermosillo.

El cierre del laboratorio 9 está publicado y confirmado. Esta revisión examinó el ZIP aportado, lo cotejó con los insumos de la revisión anterior y consultó de nuevo el repositorio autorizado. No se detectaron errores materiales pendientes en esos controles. Los capítulos 1–9 siguen pendientes de revisión editorial del autor.

## 1. Material recibido y alcance

Se recibió `EVIDENCIA_CIERRE_LABORATORIO_09_WSL_v1.0.zip`, de **1.131.278 bytes**, con SHA-256:

```text
d43d7559dc53df91fbc44524d40508c77813f29637bc5ce1aac33a214bd70757
```

El ZIP contiene 675 archivos. Su manifiesto declara 674; la única exclusión es el propio manifiesto, para evitar autorreferencia. Se comprobaron CRC, rutas, cobertura, tamaños y hashes de todos los archivos declarados. La extracción conserva exactamente los 675 archivos del ZIP. No hay duplicados de ruta, enlaces simbólicos ni rutas que salgan del paquete.

Se contrastó también la revisión WSL incluida con el ZIP previamente entregado: ambos archivos son idénticos. Los 453 archivos de evidencia funcional anterior incluidos en el cierre coinciden con el envío original de esa ejecución. Esta revisión no ejecutó scripts recibidos, pruebas funcionales ni operaciones Git de escritura; realizó comprobaciones de archivos y consultas remotas de lectura.

Fuentes locales: [recepción](auditoria/RECEPCION.json) e [integridad independiente](auditoria/INTEGRIDAD_INDEPENDIENTE.json). El ZIP recibido completo se conserva en [recibido/](recibido/EVIDENCIA_CIERRE_LABORATORIO_09_WSL_v1.0.zip).

## 2. Publicación comprobada de nuevo

| Elemento | Identidad confirmada |
| --- | --- |
| `main` remoto | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| `lab-09-v1.0` | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| `repositorio-v1.5` | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| Árbol publicado | `790e875fc95495c39ea2b5ebe7621a4ae1afa30f` |
| Padre del commit publicado | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |
| Árbol funcional auditado antes del cierre | `251105483bc5bef040c57dc3a036d5bc3a7e0da0` |

Las trece etiquetas históricas conservan sus identidades. Las dos nuevas apuntan directamente al commit de cierre; el total actual es de quince etiquetas. Las referencias consultadas coinciden con los comprobantes posteriores del paquete recibido. La consulta es una constatación puntual y no impide que `main` avance legítimamente después.

Las capturas recibidas acreditan la creación del commit en `codex/integracion-laboratorio-09`, la integración por avance rápido y el push atómico limitado a `main`, `lab-09-v1.0` y `repositorio-v1.5`, sin forzar referencias. También registran un árbol de trabajo limpio al terminar en `main`. Ese último dato corresponde a la ejecución recibida: esta revisión no accedió al disco WSL del autor.

Fuentes: [consulta remota nueva](auditoria/REFERENCIAS_REMOTAS_RECONSULTADAS.json), [auditoría del cierre](auditoria/CIERRE_INDEPENDIENTE.json) y [commit publicado](https://github.com/ccortesg/laboratorios-desarrollo-ia/commit/6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3).

## 3. Conservación del trabajo validado

Se comparó el árbol funcional auditado con el árbol publicado. De los 2.273 archivos existentes antes del cierre, **2.268 mantienen objeto Git, tipo y modo**. Cambiaron cinco documentos de raíz: `AGENTS.md`, `CONTINUIDAD.md`, `PROCEDENCIA.json`, `README.md` y `VERSIONES.md`. Se añadieron 24 rutas documentales y de evidencia; no se retiró ninguna. El resultado publicado contiene 2.297 archivos.

Las **29 rutas** describen exclusivamente el cambio documental posterior al árbol funcional auditado. No son el total del incremento del laboratorio 9 respecto de la base anterior. Los 1.502 archivos protegidos conservan su identidad, al igual que el código del recolector y sus ocho pruebas. Se cotejaron también los 29 documentos del cierre con sus contenidos o fuentes conocidas y los objetos declarados por GitHub.

El árbol final es distinto del árbol funcional porque incluye esos documentos. Esta diferencia queda explicada y comprobada; no representa una alteración posterior del código, los datos, las pruebas o las distribuciones ya verificadas.

Fuentes: [comparación del árbol publicado](auditoria/COTEJO_ARBOL_PUBLICADO.json), [documentación cotejada](auditoria/DOCUMENTACION_PUBLICADA.json) y [auditoría del cierre](auditoria/CIERRE_INDEPENDIENTE.json).

## 4. Resultados de ejecución y de integridad

| Evidencia | Resultado | Procedencia |
| --- | --- | --- |
| Conjunto funcional: 92 baterías, 805 ejecuciones | 781 APROBADO y 24 FALLIDO didácticos exactos; cero bloqueos y cero errores de ejecución | Ejecución WSL anterior, conservada y auditada |
| Solución del laboratorio 9 | 74/74 casos aprobados | Misma ejecución funcional anterior |
| Casos no ejecutados de estados didácticos | 48 NO EJECUTADO en baterías; diez criterios ausentes registrados aparte | Evidencia histórica; no se suman a las 805 ejecuciones |
| Ocho pruebas existentes del recolector | Nueva ejecución: APROBADO, código 0 | Cierre recibido |
| Operaciones registradas del cierre | 64 registros, todos con código 0 | Capturas recibidas y cotejadas |
| Capturas nuevas de stdout/stderr | 128/128 huellas correctas | 64 operaciones × dos flujos |
| Capturas históricas incorporadas | 210/210 huellas finales correctas | Ejecución anterior conservada |
| Total de huellas finales de salida examinadas | 338/338 correctas | Verificación independiente actual |
| Manifiesto del cierre | 674/674 archivos correctos | Verificación independiente actual |

Las 64 operaciones incluyen preparación, consultas Git, validaciones, publicación y registro. No equivalen a 64 pruebas funcionales ni se suman a las 805. Las cifras históricas de infraestructura —ocho pruebas del recolector, nueve de infraestructura y cuatro de recursos— permanecen separadas.

El cierre no repitió la batería funcional completa. La nueva ejecución del recolector volvió a correr **las ocho pruebas ya existentes**; no añadió ocho pruebas al código. La expresión «ocho pruebas nuevas» de los documentos recibidos se interpreta en ese sentido de ejecución nueva.

El índice previo enumera 62 operaciones. El registro definitivo añade la generación documental y la validación posterior: son 64, todas cubiertas por el manifiesto final. Esta secuencia está documentada y no deja capturas sin justificar.

Los 24 fallos funcionales históricos permanecen FALLIDO en los estados didácticos definidos. No se convirtieron en aprobaciones ni se admitieron errores adicionales para cerrar el laboratorio. Los antecedentes de intentos fallidos o bloqueados conservan su registro; la publicación confirmada no los borra.

Fuentes: [integridad independiente](auditoria/INTEGRIDAD_INDEPENDIENTE.json), [auditoría del cierre](auditoria/CIERRE_INDEPENDIENTE.json) y [resultado agregado de esta revisión](auditoria/RESULTADO_AUDITORIA.json).

## 5. Continuidad documental vigente

Se conservan sin modificar los documentos posteriores entregados por la ejecución de cierre:

- [ESTADO_DEL_LIBRO_v1.8.3.md](documentos_recibidos/entrega/ESTADO_DEL_LIBRO_v1.8.3.md).
- [ESTADO_REPOSITORIO_v1.7.3.md](documentos_recibidos/entrega/ESTADO_REPOSITORIO_v1.7.3.md).
- [CIERRE_LABORATORIO_09_CONFIRMADO_v1.0.md](documentos_recibidos/entrega/CIERRE_LABORATORIO_09_CONFIRMADO_v1.0.md).

Los estados 1.8.2 del libro y 1.7.2 del repositorio permanecen dentro del commit como registro de la preparación anterior al push. Los estados 1.8.3 y 1.7.3 y el cierre confirmado se generaron después y están fuera del commit que acreditan. Su ubicación está expresamente documentada. Para la próxima entrega deben aportarse junto con este paquete; no deben sustituirse por los estados previos ni suponerse ya incorporados en GitHub.

No hace falta producir otra versión de los estados para cambiar una etiqueta de «pendiente» histórica: el estado posterior ya explica y cierra esa etapa. El maestro editorial sigue en 1.0. Los manuscritos se conservan y los capítulos 1–9 permanecen pendientes de la revisión del autor.

## 6. Límites y conclusión operativa

Dos capturas históricas tienen un hash original distinto del final porque se sanearon. Sus bytes finales están disponibles, coinciden con el envío anterior y fueron comprobados. Los bytes originales anteriores al saneamiento están fuera del ZIP y no pudieron recalcularse en esta revisión. Las 128 capturas nuevas sí coinciden tanto con su hash final como con el hash original declarado. La integridad de un archivo no acredita por sí sola quién ejecutó su contenido; por eso se mantuvo separada de la comprobación remota independiente.

La revisión de anonimización examinó patrones concretos en 1.142 instancias de texto, incluidas las copias anidadas. No detectó hallazgos materiales en esos patrones. La URL del repositorio sintético autorizado se conserva en la documentación operativa. Este control no es una auditoría universal de secretos ni una certificación de seguridad para producción.

**BLOQUEADO:** ninguno pendiente para el cierre auditado. **NO EJECUTADO en esta revisión:** batería funcional nueva, Windows nativo, CI remota, despliegues y pruebas de herramientas comerciales. El alcance aprobado es la integridad, coherencia documental, conservación y publicación del cierre recibido.

El siguiente trabajo recomendado es producir el capítulo y laboratorio 10, «Automatización, agentes y operación: prepararse para lo que sigue», desde la continuidad confirmada. Se incluye [PROMPT_CAPITULO_10_v1.0.md](PROMPT_CAPITULO_10_v1.0.md) como encargo preparado para una etapa posterior. No se ha ejecutado ni redactado el capítulo 10 durante esta revisión.
