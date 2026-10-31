# Evidencia de producción del laboratorio 5

**Fecha efectiva:** 31 de octubre de 2026 UTC. **Procedencia:** ejecución local con
herramientas de ChatGPT. Los estados distribuidos no se generaron con GitHub Copilot.

## Contrato anterior a la implementación

`contrato_previo.json` identifica `ALCANCE.md` con una huella tomada antes de crear
el módulo nuevo. Esa huella sigue coincidiendo:
`43ad8ff461b989a249404af11af886d9df059f832699d135d6d8698171270858`.

Las expectativas previas eran conservar los veinte criterios heredados, omitir
P01–P06 en base, observar exactamente P04/P05 fallidos por aserción en propuesta
y aprobar los veintiséis en solución. La tabla siguiente contiene lo observado.

## Ejecución observada

Desde la raíz del laboratorio se ejecutó:

```bash
python3 -B verificar.py --salida evidencia/ejecucion_local
```

El comando terminó con **código 0** y dictamen **APROBADO**. El intérprete y SQLite
se identifican en `ejecucion_local/entorno.json`. El verificador ejecutó los seis
subprocesos indicados en `ejecucion_local/comandos.json` y guardó sus salidas sin
transformarlas. Las rutas absolutas del intérprete y del destino se representan
con alias documentados; no se publican datos del equipo ni variables de entorno.

| Estado | Heredados APROBADO | Nuevos APROBADO | Nuevos FALLIDO | Nuevos NO EJECUTADO |
| --- | ---: | ---: | --- | ---: |
| base | 20 | 0 | Ninguno | 6 |
| propuesta | 20 | 4 | P04 y P05 | 0 |
| solucion | 20 | 6 | Ninguno | 0 |

Son **72 ejecuciones funcionales: 70 APROBADO y 2 FALLIDO**, más seis criterios
NO EJECUTADO que no se suman a esas ejecuciones. No hubo errores de ejecución.
La batería de nuevos criterios de propuesta terminó con salida 1; las otras cinco
baterías terminaron con 0. Ambos fallos son `AssertionError` intencionales. Los
registros conservan entradas, expectativas y valores observados.

El dictamen global reconoce exactamente ese patrón didáctico y la conservación
de los archivos heredados. **La propuesta sigue siendo incorrecta.** La solución
aprobó 26/26; no tiene fallos funcionales pendientes dentro de estos criterios.
La comparación de las 24 copias —ocho archivos por estado— con las huellas de
procedencia quedó APROBADO.

## Qué descubren los fallos

P04 pide ALFA y nombre `otra`. Se esperaba total 0 y códigos vacíos; la propuesta
devolvió total 1 y A01. P05 invoca la terminal con BETA y `inexistente`; se esperaba
un objeto JSON con total 0 y códigos vacíos, pero devolvió total 1 y A04.

Los veinte criterios heredados pasaron incluso en la propuesta. Comprueban el
comportamiento anterior y no ejercitan el módulo nuevo. La corrección sustituye
la consulta directa por `buscar_catalogo(almacen, texto)` y conserva el filtro de
nombre, además de la disponibilidad. Las expectativas de P01–P06 son iguales en
propuesta y solución.

Se ejecutaron también tres demostraciones de terminal; sus comandos, salidas,
códigos y huellas están en `demostraciones/comandos.json`. Corroboran ALFA/otra
antes y después, y BETA/` OTRA ` en la solución. No se suman a las 72 pruebas.

## Acceso real a Copilot

**APROBADO:** comprobación de las capacidades accesibles. No se encontró ejecutable
`copilot` ni herramienta de Copilot invocable. El comando `code` es un envoltorio:
`--version` y `--list-extensions --show-versions` terminaron con salida 127 y mensaje
`code or code-insiders is not installed`. Eso no acredita un editor operativo.

**BLOQUEADO:** iniciar una sesión de Copilot con una interfaz invocable en este
entorno. **NO EJECUTADO:** sugerencias, delegación y revisión comercial con Copilot.
`acceso_copilot.json` conserva las observaciones y sus límites. No se verificó la
suscripción del autor. No se solicitaron secretos ni se cambiaron permisos.

Las funciones de producto explicadas en el capítulo proceden de documentación
oficial, no de estas pruebas. Los prompts y la propuesta con defecto son materiales
didácticos preparados para el libro. La evidencia previa de Codex no se usa para
atribuir una sesión a Copilot.

## Alcance de los registros

La captura funcional acredita los archivos y escenarios enumerados. No comprueba
múltiples coincidencias, orden entre varios artículos, entradas ajenas al contrato,
Unicode exhaustivo, volumen, concurrencia, autorización ni seguridad integral.
El reto de omitir el nombre sólo en la terminal permanece NO EJECUTADO en la
referencia de producción.

`sha256_fuentes.json` es una instantánea de los archivos existentes al ejecutar
la batería. Los informes de evidencia, las diferencias generadas después y el
ajuste editorial posterior del reto no se presentan como entradas de aquella
ejecución. El código funcional no se modificó después de esa captura. La reproducción
del ZIP final corresponde a una verificación separada, que debe guardar sus propios
registros sin sobrescribir este directorio.
