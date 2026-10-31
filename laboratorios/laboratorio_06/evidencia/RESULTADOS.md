# Resultados observados del laboratorio 6

**Fecha efectiva de ejecución: 31 de octubre de 2026, UTC.** El contrato de
`ALCANCE.md` define expectativas; este documento resume los registros realmente
obtenidos. No es una sesión de Grok Build ni un resultado histórico del autor.

## Ejecución local completa

Se ejecutó `verificar.py` con `--navegador` y una carpeta de salida nueva.
Los ejecutables y la ubicación del navegador se seleccionaron mediante opciones
y variables del entorno. Los registros publican alias reproducibles y versiones,
sin rutas privadas, identidad ni variables completas.

```bash
python verificar.py --navegador --salida evidencia/ejecucion_local
```

Ese destino ya contiene la evidencia de la entrega. Para reproducirla, utiliza
otro destino, por ejemplo `trabajo/mi_verificacion_completa`. El verificador impide
sobrescribir una carpeta de salida existente.

El entorno observado fue Linux, Python 3.12.14, SQLite 3.53.1, Node 24.22.1,
Playwright 1.62.1 y Chromium 156.0.8078.80, en modo headless. El servidor escuchó
en la interfaz local y usó puertos libres durante cada batería. Los tiempos UTC,
comandos con alias, códigos de salida y huellas de stdout/stderr constan en
[`ejecucion_local/comandos.json`](ejecucion_local/comandos.json). Las versiones
Python/SQLite constan en [`ejecucion_local/entorno.json`](ejecucion_local/entorno.json)
y las del navegador en
[`ejecucion_local/solucion_navegador.json`](ejecucion_local/solucion_navegador.json).

## Conteos y clasificación

| Estado | C/B/N | P | HTTP W01–W04 | Navegador W05–W06 | Totales |
| --- | --- | --- | --- | --- | --- |
| Base | 20 APROBADO | 6 APROBADO | 5 NO EJECUTADO | 3 NO EJECUTADO | 26 AP, 8 NOE |
| Propuesta | 20 APROBADO | 6 APROBADO | 5 APROBADO | 2 APROBADO, 1 FALLIDO | 33 AP, 1 F |
| Solución | 20 APROBADO | 6 APROBADO | 5 APROBADO | 3 APROBADO | 34 AP |

Se registraron 12 baterías y 102 posiciones de caso: **94 ejecuciones, 93
aprobaciones, un fallo intencional y ocho NO EJECUTADO**. Hubo cero bloqueos y
cero errores de ejecución en la batería completa. El patrón global y el recorrido
extremo a extremo quedaron APROBADO; `verificar.py` terminó con código 0.
La fuente de los conteos es
[`ejecucion_local/resumen.json`](ejecucion_local/resumen.json).

No son 94 criterios distintos. La solución tiene 32 criterios (26 heredados y
seis W), desglosados en 34 casos porque W04 y W06 tienen dos subcasos cada uno.
Las pruebas repiten criterios sobre versiones distintas para comprobar el punto
de partida, el defecto y su corrección.

## Defecto demostrado y corrección

W05 de propuesta registró el primer resultado ALFA, total 1, A01. Después de
seleccionar BETA y consultar, observó nuevamente ALFA, total 1, A01. El caso quedó
**FALLIDO por AssertionError** frente a la expectativa BETA, total 1, A04. La misma
batería sobre solución observó ALFA/A01 y después BETA/A04 y quedó APROBADO.
Las observaciones están en
[`ejecucion_local/propuesta_navegador.json`](ejecucion_local/propuesta_navegador.json)
y [`ejecucion_local/solucion_navegador.json`](ejecucion_local/solucion_navegador.json).

El servidor de propuesta también aprobó W01–W04. El defecto está en la conexión
del formulario con la consulta: una variable captura el almacén al cargar la
página. La corrección lee `selector.value` dentro del evento submit. La función
de disponibilidad, los datos y la respuesta HTTP permanecen iguales.

W06.a observó el mensaje de ausencia, total 0 y lista vacía sin alerta. W06.b
interrumpió una petición real desde Playwright y observó la alerta de error,
la lista vacía y el panel de resultado oculto. El valor anterior puede persistir
en nodos ocultos del DOM; la prueba comprueba que no se presenta como resultado
de la nueva consulta. No se simuló un DOM ni una respuesta de Grok.

## Conservación y evidencia disponible

Se cotejaron 28 archivos: nueve heredados en cada uno de los tres estados y la
batería `pruebas_resumen.py`. Todas las huellas coincidieron con la procedencia
registrada: APROBADO. Véase
[`ejecucion_local/conservacion_heredados.json`](ejecucion_local/conservacion_heredados.json).
La base conserva la funcionalidad del laboratorio 5 y no incorpora el servidor.

Cada batería ejecutada conserva su JSON, stdout y stderr. El registro de comandos
incluye los códigos de salida de los procesos. La batería de navegador de
propuesta devolvió 1, como corresponde a su aserción fallida; el verificador
reconoce exclusivamente ese fallo y mantiene su estado FALLIDO en el caso.
Los casos que no se ejecutaron se describen explícitamente y no tienen un comando
inventado. La fotografía de huellas en `sha256_fuentes.json` corresponde a los
archivos presentes cuando se ejecutó la batería; la documentación final puede
incorporar después la explicación de esos resultados sin modificar el código.

La fecha editorial del contrato inicial se corrigió del 30 al 31 de octubre.
El texto previo permanece en `ALCANCE_PREVIO.md` y coincide con la huella de
`contrato_previo.json`. `ajuste_fecha_contrato.json` registra ambas huellas y
la corrección limitada a esa fecha; los criterios y los resultados no cambiaron.

## Límites y operaciones no acreditadas

- Uso real de Grok Build para generar esta aplicación: **NO EJECUTADO**. El acceso
  necesario para atribuir una sesión quedó BLOQUEADO en la comprobación del encargo;
  el capítulo y el estado del libro conservan ese límite por separado.
- Ejecución local en Linux, HTTP real y navegador Chromium: **APROBADO** para los
  criterios entregados, con el fallo deliberado de propuesta identificado.
- Ejecución de laboratorio 6 en Windows: **NO EJECUTADO**. La experiencia Windows
  aportada por el autor corresponde al laboratorio 5 y no se traslada a este.
- Producción, carga, autenticación, seguridad integral, otros navegadores y
  accesibilidad exhaustiva: **NO EJECUTADO**.

Un diagnóstico preliminar bajo permisos restringidos impidió crear el servidor
local. Se resolvió ejecutando las comprobaciones en el entorno autorizado para
la aplicación sintética. Los resultados completos anteriores acreditan la
ejecución posterior; el diagnóstico no se presenta como un defecto del software.
La revisión visual y de teclado, si se aporta como registro separado de esta
entrega, conserva su alcance propio y no amplía los criterios funcionales.

## Revisión visual y de teclado

Se inspeccionaron las cuatro capturas sintéticas de `interfaz/` en anchos de 1280 y 390 píxeles: **APROBADO** en ese alcance. El formulario y los estados éxito, vacío y error permanecen legibles, sin solapamientos. La secuencia Tab recorrió enlace, almacén, nombre y botón; Enter ejecutó la consulta y devolvió A01. No se observó desbordamiento horizontal en 390 píxeles. `interfaz/revision.json` registra estas observaciones. No constituye una auditoría WCAG ni una prueba con lectores de pantalla o dispositivos físicos.

El diagnóstico de Grok Build está en `acceso_grok.json`; su registro inicial y el ajuste de fecha editorial se conservan por separado. Las fuentes y sus límites están en `../docs/FUENTES_GROK.md`.
