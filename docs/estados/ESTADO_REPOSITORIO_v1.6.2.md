# Estado operativo · laboratorio 8 verificado en Windows

**Versión documental:** 1.6.2. **Fecha:** 31 de octubre de 2026, America/Hermosillo.
**Antecedente conservado:** `ESTADO_REPOSITORIO_v1.6.1.md`.

Repositorio autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

## Punto de partida vigente

La evidencia corregida aportada por el autor identifica:

| Elemento | Valor |
|---|---|
| Rama local | `integracion/laboratorio-08` |
| HEAD | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| Main local | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| Árbol preparado anterior | `2ea01dea2aa0c8907eba54ef65efcb44d547b9d7` |
| Árbol preparado corregido y verificado | `9ea6109fe8e89a2785bdce255252ffaabea1d122` |
| Diferencias sin preparar | Ninguna |
| Etiquetas locales | Once; conservadas |

La corrección ya está aplicada. No reaplicar el parche original ni el correctivo. El árbol 9ea6109... incluye la distribución `LABORATORIO_08_v1.0.1.zip` y conserva la distribución original 1.0.

## Ejecución Windows y auditoría

Archivo recibido: `EVIDENCIA_CORRECCION_LAB08_WINDOWS_02.zip`.

SHA-256: `2e8503f199f85184ef55de2c8808cda7b358e4dd75554a03371be51b4d7b1445`.

**APROBADO**, código 0. 65 baterías; 583 ejecuciones; 571 aprobaciones; doce fallos didácticos previstos; cero bloqueos; cero errores de ejecución; 48 NO EJECUTADO en baterías y diez ausentes aparte. Pruebas auxiliares separadas: ocho recolector, cuatro recursos y nueve evaluador, todas aprobadas.

Integridad revisada: 254 archivos del ZIP; 253/253 en su manifiesto; 102/102 huellas del conjunto; 10/10 auxiliares; 244/244 archivos del antecedente conservados. Los auxiliares y configuración utilizados coinciden con el paquete correctivo entregado. Los doce fallos son exactamente los documentados en el contrato común. Los JSON y las trazas nuevas no presentan los errores de limpieza del primer pase.

La distribución y el código continúan siendo sintéticos. La revisión actual reevalúa los registros recibidos; no ejecuta otra vez las pruebas en Windows ni atribuye la ejecución a una herramienta comercial.

## Referencias remotas consultadas

La API oficial de GitHub devuelve main en `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` y once etiquetas coincidentes con el antecedente. `lab-07-v1.0` y `repositorio-v1.3` siguen en ese commit. `lab-06-v1.0` y `repositorio-v1.2` siguen en `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd`.

`lab-08-v1.0` y `repositorio-v1.4` están ausentes en la consulta. Se conservan como nombres previstos, no creados. La distribución técnica 1.0.1 debe quedar identificada expresamente al preparar el cierre para distinguirla del ZIP inicial 1.0.

Las referencias, fecha efectiva y método están en `auditoria/REFERENCIAS_REMOTAS_CONFIRMADAS.json` del paquete de revisión. La consulta es una observación puntual: repetirla inmediatamente antes de integrar/publicar y conservar cualquier avance de main.

## Documentación nueva y límites

La revisión y estos estados se entregan por separado, fuera del árbol preparado. Todavía no se añadieron a la copia Windows ni al repositorio remoto. Su incorporación producirá un árbol nuevo: registrar esa identidad y cotejar los archivos ejecutables con el árbol verificado. Si sólo se añade documentación y evidencia, no atribuirle una nueva ejecución funcional. Si cambia código o se integra un avance que lo afecte, ejecutar las comprobaciones pertinentes.

Se mantienen el recolector corregido, sus ocho pruebas, los laboratorios 1–7, distribuciones, evidencias, historial y etiquetas. No se reescribe el primer pase Windows fallido. Los estados anteriores permanecen como antecedentes; este documento prevalece sobre el pendiente de ejecutar la corrección en Windows.

## Próxima tarea

Preparar el cierre documental y la incorporación de la evidencia nueva; verificar referencias y diferencias; crear el commit y, en la etapa autorizada de cierre, integrar main, crear únicamente las etiquetas nuevas previstas y efectuar una subida sin forzar referencias. Confirmar después las referencias remotas y conservar el comprobante final.

**NO EJECUTADO todavía:** commit del incremento, integración main, etiquetas nuevas y push. **Pendiente:** revisión editorial de los capítulos 1–8. No redactar el capítulo 9 en este cierre.
