# Cierre confirmado del laboratorio 7

**Versión:** 1.0 · **Fecha:** 31 de octubre de 2026.  
**Resultado:** APROBADO para el cierre técnico y la publicación revisados.  
**Repositorio sintético autorizado:** https://github.com/ccortesg/laboratorios-desarrollo-ia

## 1. Conclusión y alcance

La integración del laboratorio 7 quedó publicada. La consulta independiente a GitHub, registrada el **2026-10-31 a las 23:02:25 UTC**, confirmó que `main`, `lab-07-v1.0` y `repositorio-v1.3` apuntaban al mismo commit:

```text
46f389bc4acf3e231a8eb1a1bb3972db0fe7e622
```

Su árbol es exactamente el preparado y revisado antes del cierre: `b123b5969e8077ba0cb3c4eedc9b348f94294652`. Tiene un único padre, `6382e05846e149a9a72f7fdc56da48c37a873833`, que corresponde a la base corregida del recolector. Las nueve etiquetas históricas conservan sus destinos; se añadieron las dos previstas. Fuente: [commit publicado](https://github.com/ccortesg/laboratorios-desarrollo-ia/commit/46f389bc4acf3e231a8eb1a1bb3972db0fe7e622) y `auditoria/REFERENCIAS_REMOTAS_CONFIRMADAS.json`.

Las operaciones locales y la publicación fueron realizadas por el autor. Esta revisión inspeccionó los archivos recibidos y consultó GitHub mediante solicitudes de lectura. No ejecutó de nuevo las pruebas funcionales, no accedió al equipo Windows ni modificó el remoto.

## 2. Comprobante recibido

Se recibió `EVIDENCIA_CIERRE_LABORATORIO_07_v1.0.zip`, de **3.250 bytes**, con este SHA-256:

```text
17fc950689f9e4c9853017174caac64f9171e6629c12405ad8ae9715575d2ee5
```

Contiene exactamente cuatro archivos: `commit.txt`, `codigo_push.txt`, `previo/RESULTADO_CIERRE_07.json` y `publicado/RESULTADO_CIERRE_07.json`. El ZIP supera la comprobación CRC, sin entradas duplicadas. Se conserva íntegro dentro del paquete de cierre.

Las fases registran Windows, Python 3.11.9 y Git 2.45.1.windows.1:

| Fase | Intervalo UTC del 31/10/2026 | Estado | Comandos registrados |
| --- | --- | --- | ---: |
| Previa | 23:01:09.534654–23:01:11.246856 | APROBADO; salida 0 | 21 |
| Publicada | 23:01:16.078232–23:01:17.772933 | APROBADO; salida 0 | 24 |

Todos esos comandos tienen código cero y error vacío; su secuencia es coherente con el auxiliar entregado. Las salidas registradas concuerdan con los campos de resultados. Fuente: los dos JSON del comprobante y `auditoria/AUDITORIA_DETALLADA_CIERRE.json`.

## 3. Qué acredita cada fase

En la fase previa, la rama era `integracion/laboratorio-07`; HEAD, main y origin/main seguían en la base `6382e058…`. El árbol de HEAD era `680fa6135ed0aae40e962ec3f893d72ece1389c1`, y el índice ya tenía el árbol de integración `b123b596…`. El registro no muestra cambios adicionales sin preparar, conflictos ni archivos no rastreados no ignorados.

En la fase publicada, la rama era `main`; HEAD, main y origin/main coincidían en `46f389bc…`. Los árboles de HEAD e índice coincidían con el aprobado. Los registros son coherentes con un árbol de trabajo limpio respecto de Git, lo que permite la presencia de archivos ignorados, como los resultados de trabajo.

Ambas fases declaran **172 de 172 archivos de evidencia coincidentes**, sin diferencias. Además se recalcularon directamente las 172 huellas del ZIP funcional original contra el manifiesto previamente entregado: todas coincidieron. Esta comprobación directa acredita los bytes recibidos; el estado del disco Windows queda respaldado por los registros aportados. Fuente: `auditoria/AUDITORIA_DETALLADA_CIERRE.json` y el manifiesto conservado en `auditoria/HUELLAS_ARCHIVOS_RECIBIDOS.json`.

## 4. Referencias finales e historia conservada

| Referencias | Commit confirmado |
| --- | --- |
| main, lab-07-v1.0, repositorio-v1.3 | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| lab-06-v1.0, repositorio-v1.2 | `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd` |
| lab-05-v1.0, repositorio-v1.1 | `67edef7b44524f5f621e9b060c6b9c523c1b05a8` |
| lab-01-v1.0, lab-02-v1.0, lab-03-v1.0, lab-04-v1.1, repositorio-v1.0 | `52875ff15c6648f9a042a15a94da812e37effa40` |

La fotografía remota contiene once etiquetas: nueve anteriores y dos nuevas. El commit final conserva exactamente el árbol revisado; no se incorporaron cambios adicionales durante el cierre. Las referencias describen el momento consultado y deben verificarse de nuevo antes de una futura integración.

## 5. Evidencia funcional que sigue vigente

La ejecución Windows revisada anteriormente, del **31 de octubre de 2026 de 22:37:52 a 22:38:29 UTC**, conserva estos resultados:

| Medida | Resultado |
| --- | ---: |
| Baterías | 44 |
| Ejecuciones funcionales | 408 |
| APROBADO | 400 |
| FALLIDO didácticos esperados | 8 |
| BLOQUEADO | 0 |
| NO EJECUTADO en baterías | 37 |
| Criterios ausentes registrados aparte | 10 |

Los ocho fallos previstos son C04 del inicial 1; B05/B06 del defecto 3; P04/P05 de la propuesta 5; W05 de la propuesta 6; I01/I07 de la propuesta 7. Permanecen clasificados como FALLIDO. Ningún fallo adicional fue admitido.

Por separado, las ocho pruebas del recolector registraron OK y salida cero. La revisión previa confirmó **64/64 huellas finales stdout/stderr** y **258/258 declaraciones de huellas de fuentes**. La solución del laboratorio 7 aprobó sus **51 casos**. Estas cifras proceden de la revisión funcional anterior; las auditorías y comprobaciones de cierre no se suman a las 408 ejecuciones. Fuente: `antecedentes/REVISION_LABORATORIO_07_WINDOWS_v1.0.md`.

## 6. Límites y continuidad

`codigo_push.txt` contiene cero, pero el adjunto no incluye la transcripción completa del comando de publicación ni la respuesta del servidor. Ese archivo no demuestra por sí solo el uso de `--atomic`; el resultado publicado sí quedó confirmado mediante las referencias consultadas independientemente.

**NO EJECUTADO por esta revisión:** nuevas pruebas funcionales, inspección de ejecuciones de GitHub Actions, sesiones comerciales, pruebas de producción y redacción del capítulo 8. No se afirma que Actions nunca se haya ejecutado. Se mantienen los límites funcionales anteriores, incluida la ausencia de una prueba continua que importe el CSV y observe después su resultado en la pantalla web.

No quedan bloqueos detectados para el cierre técnico del laboratorio 7. **Los capítulos 1–7 siguen pendientes de revisión editorial del autor.** El maestro editorial 1.0 y los entregables del capítulo 7 se conservan.

Los estados nuevos son `ESTADO_DEL_LIBRO_v1.6.2.md` y `ESTADO_REPOSITORIO_v1.5.2.md`. Prevalecen sobre los pendientes de cierre de las versiones anteriores y se entregan por separado: no se presupone su incorporación al repositorio publicado.

La siguiente tarea recomendada es preparar el encargo del capítulo 8, «Depuración con evidencia: investigar errores entre entornos y servicios», tomando como base este cierre y los nuevos estados. No hace falta repetir el cierre del laboratorio 7.
