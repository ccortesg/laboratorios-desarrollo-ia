# Estado operativo · corrección del laboratorio 8 para Windows

**Versión documental:** 1.6.1. **Fecha:** 31 de octubre de 2026, America/Hermosillo (1 de noviembre UTC).

Repositorio autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

## Base y alcance

La evidencia Windows recibida identifica HEAD y main local en `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`, árbol base `b123b5969e8077ba0cb3c4eedc9b348f94294652`; el parche del laboratorio 8 está preparado en `integracion/laboratorio-08`, árbol `2ea01dea2aa0c8907eba54ef65efcb44d547b9d7`. No hay un commit nuevo de esa integración.

Esta entrega corrige ese árbol preparado mediante un parche incremental. `BASE_CORRECCION.json` del paquete registra los árboles previo y corregido y su SHA-256. Se parte de los objetos locales conservados: no se presenta una consulta remota nueva ni una publicación. Antes del cierre posterior habrá que consultar de nuevo las referencias remotas y conservar cualquier avance.

## Diagnóstico Windows verificado

El ZIP recibido coincide con la huella aportada y sus 244 archivos. Windows: Python 3.11.9, SQLite 3.45.1, Git 2.45.1.windows.1, Node 20.20.0, Playwright 1.62.1 y Chromium 151.0.7922.34.

La ejecución original es FALLIDO, código 1. El resumen general incorpora sólo 44 baterías de laboratorios 1–7 (408 ejecuciones, 400 aprobaciones, ocho fallos didácticos); laboratorio 8 queda FALLIDO por ValueError. Al reevaluar los JSON reales se reproduce `Criterio duplicado`. Las trazas D04 acreditan `PermissionError [WinError 32]` en limpieza de la base temporal, antes de escribir ambos JSON finales. La propuesta D duplica D05 y D08.a; la solución D también registra PermissionError. Los 153 casos heredados de laboratorio 8 aprobaron.

No se interpreta el total interno de 175 como cobertura única: hay registros duplicados y resultados faltantes. Las huellas de salidas siguen coincidiendo 102/102 y 2/2; no se recalculó ni reescribió la captura.

## Cambio técnico

Dos auxiliares usan cierre explícito de SQLite: lectura snapshot y preparación D06.b. El contexto transaccional de D06.b conserva commit/rollback. La aplicación, el importador, servidor, estados y criterios C/B/N/P/W/I/D conservan sus bytes y comportamiento. No se modifica el evaluador común, su política de fallos ni el recolector de huellas y sus ocho pruebas.

Se añaden cuatro regresiones independientes R01–R04, documentación y distribución autónoma 1.0.1. `PROCEDENCIA.json` conserva la entrada antigua bajo `paquetes_anteriores` y registra la distribución nueva como fuente del árbol visible. El ZIP v1.0 sigue intacto; las huellas históricas no se sustituyen. Los laboratorios 1–7, sus distribuciones e historiales permanecen íntegros.

## Verificaciones y evidencia

- Auditoría de evidencia recibida: APROBADO como auditoría; su resultado funcional sigue FALLIDO.
- Cuatro regresiones: FALLIDO contra original (cuatro fallos previstos para detectar el defecto), APROBADO contra corregido; 4/4 huellas.
- ZIP corregido recién descomprimido: APROBADO en Linux con navegador; 175 ejecuciones, 171 aprobaciones, cuatro fallos didácticos, cero bloqueos, once NO EJECUTADO; 38/38 huellas y 151/151 archivos conservados.
- Primer intento de prueba en entorno restringido: BLOQUEADO por creación de sockets; conservado y separado del reintento con HTTP de loopback permitido.
- La prueba final del parche incremental y el conjunto completo se registra bajo `evidencia/prueba_parche/` del paquete correctivo, con resultado, comandos, versiones, huellas y conservación. El auxiliar exige todos sus resultados; no fija 102 como recuento obligatorio.

El contrato completo esperado mantiene 65 baterías y 583 ejecuciones, con 571 aprobaciones y doce fallos didácticos exactos; 48 NO EJECUTADO y diez ausentes aparte. Son referencias que se contrastan con cada resumen observado. Las ocho pruebas del recolector, cuatro de recursos y nueve del evaluador se contabilizan separadamente.

## Reanudación en Windows

Seguir únicamente la guía del paquete correctivo para esta fase. Comprobar el paquete, verificar el árbol previo, aplicar `CORREGIR_LABORATORIO_08_WINDOWS.patch` con `--check --index` y después `--index`, y ejecutar `VERIFICAR_CORRECCION.py` desde el paquete. El auxiliar crea `trabajo/correccion_lab08_windows_01`, conserva el antecedente `trabajo/integracion_08_windows_01`, ejecuta las pruebas, compara huellas dinámicas y genera un ZIP nuevo.

El cierre antiguo que exigía el árbol 2ea01... no sirve para aprobar el árbol corregido; sus registros se conservan como antecedente. La nueva identidad se comprueba contra `BASE_CORRECCION.json` y `preparado_corregido.json`.

**NO EJECUTADO:** corrección en Windows hasta recibir su nuevo ZIP; commits, integración en main, creación o movimiento de etiquetas y push. Los nombres de etiquetas previstos en la etapa anterior siguen pendientes de revisión en el cierre. Los capítulos 1–8 siguen pendientes de revisión del autor y el capítulo 9 queda fuera de alcance.
