# Estado operativo del repositorio — cierre del laboratorio 7 confirmado

**Versión documental:** 1.5.2 · **Fecha:** 31 de octubre de 2026.  
**Antecedente conservado:** ESTADO_REPOSITORIO_v1.5.1.md.  
**Repositorio autorizado:** https://github.com/ccortesg/laboratorios-desarrollo-ia  
**Versión técnica publicada:** repositorio-v1.3.  
**Laboratorio publicado:** lab-07-v1.0.

## 1. Cambio de estado

El cierre técnico deja de estar pendiente. El autor aportó `EVIDENCIA_CIERRE_LABORATORIO_07_v1.0.zip`; se auditó su coherencia y se contrastaron independientemente las referencias con GitHub mediante GET. No se realizaron escrituras remotas durante esta revisión.

La versión documental 1.5.2 identifica este estado de continuidad; la etiqueta técnica repositorio-v1.3 identifica la publicación del código. Son numeraciones distintas.

## 2. Referencias y árbol confirmados

Consulta efectiva: **2026-10-31 23:02:25 UTC**.

| Referencia u objeto | Identificador |
| --- | --- |
| main | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| lab-07-v1.0 | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| repositorio-v1.3 | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| Árbol del commit final | `b123b5969e8077ba0cb3c4eedc9b348f94294652` |
| Único padre y base utilizada | `6382e05846e149a9a72f7fdc56da48c37a873833` |
| Árbol de la base | `680fa6135ed0aae40e962ec3f893d72ece1389c1` |
| lab-06-v1.0 y repositorio-v1.2 | `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd` |

Mensaje del commit: «Integra laboratorio 7 y repositorio 1.3». El árbol final coincide exactamente con el probado; la transición desde la base comprende un único commit nuevo. La corrección del recolector sigue presente por continuidad con la base.

Las nueve etiquetas anteriores mantienen sus valores exactos. Las cinco lab-01-v1.0, lab-02-v1.0, lab-03-v1.0, lab-04-v1.1 y repositorio-v1.0 siguen en `52875ff15c6648f9a042a15a94da812e37effa40`. Lab-05-v1.0 y repositorio-v1.1 siguen en `67edef7b44524f5f621e9b060c6b9c523c1b05a8`. Lab-06-v1.0 y repositorio-v1.2 conservan el destino mostrado arriba.

La consulta contiene once etiquetas y sólo añade las dos nuevas previstas. Fuentes: [commit de GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/commit/46f389bc4acf3e231a8eb1a1bb3972db0fe7e622) y `auditoria/REFERENCIAS_REMOTAS_CONFIRMADAS.json` del paquete de cierre.

## 3. Cierre Windows aportado y contrastado

SHA-256 del ZIP recibido:

```text
17fc950689f9e4c9853017174caac64f9171e6629c12405ad8ae9715575d2ee5
```

Contiene cuatro archivos, con CRC válido. `commit.txt` identifica el commit publicado y `codigo_push.txt` contiene cero. Los JSON previo y publicado declaran APROBADO y salida 0. La fase previa registra el índice preparado en la rama de integración; la posterior registra main, HEAD y origin/main en el commit final, con índice igual a HEAD y sin cambios adicionales respecto de Git.

Las fases ocurrieron el 31/10/2026 entre 23:01:09 y 23:01:18 UTC. Registran Windows, Python 3.11.9 y Git 2.45.1.windows.1. Los 21 y 24 comandos registrados, respectivamente, devuelven cero y sus resultados son coherentes con el auxiliar entregado.

Cada fase registra 172/172 archivos de evidencia coincidentes. Además, la auditoría directa confirmó las 172 huellas del ZIP funcional original contra el manifiesto de la revisión previa. No se modificaron los comprobantes ni la evidencia histórica.

El adjunto no conserva la transcripción completa del push. El resultado publicado está confirmado; el archivo de código de salida por sí solo no prueba sus opciones exactas.

## 4. Resultados funcionales vigentes

Corresponden a la ejecución Windows del autor de **22:37:52–22:38:29 UTC del 31/10/2026**, ya revisada. No son una ejecución nueva de este cierre.

| Medida | Resultado |
| --- | ---: |
| Laboratorios | 7 |
| Baterías | 44 |
| Ejecuciones funcionales | 408 |
| APROBADO | 400 |
| FALLIDO didácticos esperados | 8 |
| BLOQUEADO | 0 |
| NO EJECUTADO en baterías | 37 |
| Criterios ausentes registrados aparte | 10 |

Fallos previstos exclusivamente: C04 en inicial 1; B05/B06 en defecto 3; P04/P05 en propuesta 5; W05 en propuesta 6; I01/I07 en propuesta 7. La solución 7 conserva 51 casos aprobados.

Por separado: ocho pruebas del recolector aprobadas, 64/64 huellas finales stdout/stderr coincidentes y 258/258 declaraciones de huellas de fuentes cotejadas. El cierre conserva 172 archivos de evidencia; estos recuentos tienen objetos distintos y no se suman como cobertura funcional.

Entorno funcional declarado: Windows, CPython 3.11.9, SQLite 3.45.1, Git 2.45.1.windows.1, Node v20.20.0, Playwright 1.62.1 y Chromium 151.0.7922.34. Se ejecutó el navegador en los estados con recorrido web. Fuente: revisión Windows previa, conservada en `antecedentes/` del paquete de cierre.

## 5. Alcance y pendientes

**APROBADO:** cierre documentado, referencias remotas, árbol exacto, padre único, preservación de etiquetas y coherencia de evidencia.

**BLOQUEADO:** ninguno detectado para esta integración.

**NO EJECUTADO por esta revisión:** acceso directo a Windows, nueva ejecución funcional, consulta de ejecuciones de GitHub Actions, nuevas sesiones comerciales y pruebas de producción. No se infiere el estado de Actions a partir del push.

Se conserva el límite funcional: la importación CSV y el recorrido web heredado no acreditan una única prueba continua de importación seguida de observación en la interfaz. Los casos I no prueban por sí solos cada variante de los comandos CLI.

Los manuscritos 1–7 siguen pendientes de revisión editorial. El maestro 1.0 no cambia; el capítulo 8 permanece sin redactar.

## 6. Continuidad y siguiente tarea

Se entregan `ESTADO_DEL_LIBRO_v1.6.2.md`, este estado y `CIERRE_LABORATORIO_07_CONFIRMADO_v1.0.md` por separado. No se afirma que estén dentro del commit publicado. Incorporarlos a una entrega futura requerirá un cambio documental nuevo; no corresponde mover las etiquetas existentes.

La siguiente tarea es preparar el encargo del capítulo 8 tomando como base el commit confirmado y los estados nuevos. Consultar de nuevo main al empezar; si avanzó, conservar y revisar sus cambios. No restaurar la base ni forzar etiquetas.

No se necesita crear otro commit ni repetir el push para cerrar el laboratorio 7. Las comprobaciones y pendientes de las versiones 1.5 y 1.5.1 quedan resueltos en el alcance acreditado por este estado; se conservan como antecedentes.
