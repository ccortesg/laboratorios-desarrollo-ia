# Resultados observados del laboratorio 8

**Estado global: APROBADO.** Ejecución local del 31 de octubre de 2026, desde
23:57:31.249361 hasta 23:58:04.512080 UTC. Comando principal:

```text
python verificar.py --navegador --salida trabajo/ejecucion_final_01
```

La salida nueva se conserva sin cambiar sus bytes en `ejecucion_local/`.
El entorno proporcionó Node/Playwright y un ejecutable Chrome for Testing mediante
la configuración opcional documentada. Se usó permiso de ejecución para servidores
y navegador locales, pues el sandbox inicial impedía abrir sockets. No se atribuye
esta ejecución al Windows del autor ni a una herramienta comercial.

| Entorno observado | Versión |
| --- | --- |
| Sistema | Linux |
| Python | 3.12.14 |
| SQLite | 3.53.1 |
| Node | v24.22.1 |
| Playwright | 1.62.1 |
| Chrome for Testing, motor Chromium | 156.0.8078.80 |

Los registros principales son entorno.json, comandos.json y resumen.json.
Cada batería conserva su JSON, stdout y stderr. Las operaciones CLI/HTTP internas
de los casos D se registran dentro de su observación, con rutas y URL sustituidas
por alias. El cierre controlado de procesos de servidor puede registrar -15 en
Linux: es la terminación solicitada por el controlador, no el resultado de una prueba.

## Conteos y significado

| Estado | Heredados | D aprobados | D fallidos | D no ejecutados |
| --- | ---: | ---: | --- | ---: |
| base | 51 APROBADO | 0 | Ninguno | 11 |
| propuesta | 51 APROBADO | 7 | D03, D04, D05, D08.a | 0 |
| solucion | 51 APROBADO | 11 | Ninguno | 0 |

Se observaron **21 baterías, 175 ejecuciones funcionales, 171 aprobaciones, cuatro
fallos didácticos, cero bloqueos, once NO EJECUTADO y cero errores de ejecución**.
La solución aprobó 62/62 casos, correspondientes a 48 criterios distintos.
Los casos no ejecutados de base pertenecen al incremento persistente ausente;
no son aprobaciones. Los fallos previstos siguen FALLIDO por AssertionError.

La conservación de los 23 archivos heredados exactos resultó APROBADA.
Coincidieron **38/38 huellas finales stdout/stderr**. Las huellas capturadas y finales
mantienen su distinción; el saneamiento no se aplicó después para ocultar diferencias.
Estas auditorías no se suman a las 175 ejecuciones. Las ocho pruebas del recolector
común se ejecutan y documentan en la integración del repositorio, por separado.

## Recorrido continuo observado

D04 inició una base nueva y un servidor como proceso, abrió Chromium y consultó ALFA:
un artículo, A01. Sin reiniciar servidor ni página, otro proceso importó cuatro filas.
El informe `APLICADO` no sustituye la observación: registra cuatro filas leídas,
validadas y aplicadas. Huella del CSV:

```text
d4c2daa0016e34ea251cb2d3eed024c7e3150347a360e1b7781e798011344506
```

En solución, la siguiente consulta mostró A01/A03 en ALFA, BETA vacío y A03 al buscar
` AGOTADO `. En propuesta, siguieron A01 en ALFA, A04 en BETA y búsqueda vacía.
La importación y el estado SQLite sí habían cambiado en ambos. Los datos completos
están en solucion_depuracion_navegador.json y propuesta_depuracion_navegador.json.

D02 observó el origen configurado `archivo:principal` en ambas consultas.
En propuesta, CLI utilizó `archivo:principal` y HTTP utilizó `memoria`.
En solución, ambas consultas utilizaron el archivo seleccionado.
Su comprobación aprueba la fidelidad del diagnóstico; la corrección funcional
se evalúa por separado en D03/D04/D05/D08.a.

## Límites

D04 sí acredita CSV→archivo→HTTP→pantalla en este entorno y escenario.
No acredita varios sistemas operativos, producción, múltiples escritores, carga,
recuperación física ni seguridad integral. W06.b mantiene una interrupción controlada
del transporte como caso heredado independiente. No hay pantalla de importación.

El reto comparador de informes, la ejecución Windows, nuevas sesiones comerciales
y la publicación están NO EJECUTADO en esta producción local. Los manuscritos siguen
pendientes de revisión del autor. Esta evidencia no sustituye las ejecuciones históricas.
