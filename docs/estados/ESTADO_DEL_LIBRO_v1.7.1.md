# Estado del libro · corrección técnica del laboratorio 8

**Versión documental:** 1.7.1. **Fecha:** 31 de octubre de 2026, America/Hermosillo (1 de noviembre UTC).

## Continuidad vigente

Se conserva DOCUMENTO_MAESTRO_EDITORIAL_v1.0.md. Los capítulos 1–8 y sus Word siguen pendientes de revisión editorial expresa del autor. No se modifica el manuscrito del capítulo 8 ni se redacta el 9. Esta actualización registra un incidente técnico observado al ejecutar el laboratorio 8 en Windows; no otorga aprobación editorial.

## Incidente acreditado

El autor aplicó el paquete sobre `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` y obtuvo el árbol preparado `2ea01dea2aa0c8907eba54ef65efcb44d547b9d7`. La evidencia recibida conserva 244 archivos y el SHA-256 `d89be25eac2cc6915bde22d3bef6bc4a9ee7052fe821542012c6698e352906b6`. Su auditoría está en `evidencia_integracion/correccion_lab08_windows_v1.0/`.

La ejecución Windows original es FALLIDO: dos auxiliares dejaron conexiones SQLite abiertas y la limpieza de temporales produjo errores. Los JSON de D04 faltan; D05 y D08.a aparecen duplicados en propuesta. El evaluador rechaza los duplicados; se reprodujo su ValueError leyendo la captura real, sin ejecutar otra vez los casos. Los 153 casos heredados del laboratorio 8 aprobaron. Los totales internos con duplicados no constituyen cobertura validada.

El recolector aprobó sus ocho pruebas y las huellas recibidas coinciden: 102/102 del conjunto y 2/2 de la captura auxiliar. Integridad y aprobación funcional son propiedades distintas.

## Corrección preparada

La distribución autónoma `LABORATORIO_08_v1.0.1.zip` cierra explícitamente las conexiones de `snapshot()` y de la preparación D06.b. Conserva datos, estados de aplicación, contratos y los cuatro fallos didácticos de propuesta. Añade cuatro regresiones R01–R04 sobre cierre, lectura sin alteraciones, commit y rollback. Las cuatro fallan contra el original y aprueban con el ajuste; se contabilizan aparte del recorrido funcional.

El ZIP corregido se descomprimió y ejecutó en Linux con navegador: 175 ejecuciones, 171 aprobaciones, cuatro fallos didácticos, cero bloqueos, once NO EJECUTADO; 38/38 huellas finales. Se conservaron sus 151 archivos. El primer intento restringido quedó BLOQUEADO por sockets; su registro se conserva junto al reintento autorizado para loopback.

La verificación final del parche y del conjunto 1–8 está en el paquete correctivo, fuera del árbol que verifica para evitar referencias circulares. La siguiente revisión debe leer su `RESULTADO_CORRECCION.json`; no debe inferir Windows desde Linux.

## Entregables y pendientes

Se entregan el paquete `CORRECCION_LABORATORIO_08_WINDOWS_v1.0.zip`, la distribución 1.0.1, la revisión del diagnóstico recibido y los estados 1.7.1 del libro y 1.6.1 del repositorio. Los paquetes anteriores, los estados 1.7/1.6 y las evidencias históricas se conservan.

**NO EJECUTADO:** nueva ejecución Windows con la corrección; cierre de la integración; etiquetas nuevas; publicación; revisión editorial de capítulos; usos comerciales nuevos. La próxima tarea es aplicar el parche incremental en la rama existente, ejecutar el auxiliar y revisar su ZIP. Ningún fallo esperado ni huella histórica se modifica para obtener aprobación.
