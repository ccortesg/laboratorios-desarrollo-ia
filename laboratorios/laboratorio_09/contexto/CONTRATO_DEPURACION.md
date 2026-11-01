# Contrato del laboratorio 8

Decisiones registradas antes de implementar el incremento. Sólo datos sintéticos.

## Alcance y compatibilidad

La base copia la solución del laboratorio 7: importación y consulta en memoria,
con web de referencia. Es correcta dentro de ese alcance. Propuesta y solución
añaden SQLite en archivo y CLI/HTTP/navegador sobre la misma base explícita.
Sin selección persistente se conservan todas las interfaces anteriores.
Los 51 casos C/B/N/P/W/I utilizan sus referencias intactas y bases aisladas.

Inicializar es una operación explícita que rechaza destinos existentes. Abrir
una base para importar, consultar o servir nunca la crea ni carga las semillas.
Se exige el esquema de referencia; una ruta inexistente o esquema incompatible
produce rechazo y no cambia ni crea bases. Las rutas relativas se resuelven
respecto del directorio de invocación y se fijan al arrancar. Para conservar
el mismo origen entre directorios, los comandos utilizan su ruta absoluta.
Los errores públicos no incluyen rutas, identidad, SQL interno ni variables.

El CSV conserva íntegro CONTRATO_INTEGRACION.md. El importador recibe la conexión,
valida el archivo completo y reemplaza cantidades absolutas. El servidor abre y
cierra una conexión por petición. El resumen conserva almacén, total y códigos;
total cuenta artículos, no unidades. El diagnóstico opcional registra origen
configurado y origen efectivo observados dentro de la consulta real, con alias
sintéticos distintos. No añade campos ni rutas HTTP al contrato público.

## Estados y defecto predefinido

`base` no tiene persistencia ni diagnóstico nuevo: sus once casos D constan
NO EJECUTADO. `propuesta` inicializa, importa, valida y abre correctamente el
archivo, pero el manejador HTTP omite la conexión al llamar al resumen. Éste
consulta una base de referencia en memoria. `solucion` transmite esa conexión.
La instrumentación es la misma en ambas. No se modifican filtros, datos ni UI
para reparar el defecto; el diff conserva una única omisión funcional.

## Criterios y casos

| Criterio | Casos | Observación |
| --- | --- | --- |
| D01 | D01 | Un proceso importa y otro consulta cantidades persistidas. |
| D02 | D02 | El diagnóstico del origen efectivo concuerda con el estado realmente consultado, incluso cuando es incorrecto. |
| D03 | D03 | HTTP devuelve los datos importados por almacén y nombre. |
| D04 | D04 | Navegador real observa antes, importación CLI y después sobre el mismo servidor vivo. |
| D05 | D05 | Otro directorio y reinicio conservan el mismo archivo y resultado HTTP. |
| D06 | D06.a, D06.b | Ruta inexistente y esquema incompatible se rechazan sin creación o modificación. |
| D07 | D07.a, D07.b | Error tardío conserva todo el estado; repetición entre procesos es idempotente y conserva omitidos. |
| D08 | D08.a, D08.b | Dos bases producen estados independientes; reinicializar una existente no la sobrescribe. |

Son ocho criterios, once casos: diez de terminal/HTTP y uno de navegador.
La propuesta debe FALLAR exactamente D03, D05, D08.a y D04, por aserciones de
negocio. D02 aprueba si describe fielmente el origen efectivo, aunque evidencie
el defecto. La solución debe aprobar los once. No se toleran errores de proceso
como fallos intencionales. Base conserva 51 heredados; solución tendrá 62 casos.

CSV válido: A01/ALFA=5, A02/ALFA=8, A03/ALFA=3 y A04/BETA=0. ALFA devuelve
A01 y A03; BETA vacío; buscar ` AGOTADO ` devuelve A03. A02 sigue deshabilitado.
La propuesta HTTP conserva A01 en ALFA y A04 en BETA pese al archivo importado.

## Investigación y límites

Comparar importación confirmada, consulta persistente, HTTP y UI con la misma
entrada y base. Contrastar hipótesis mediante observaciones y registrar comandos.
La secuencia usa un defecto didáctico conocido, no un incidente histórico.
Cambiar el directorio no acredita otro sistema operativo. No se incorporan
pantalla de importación, autenticación, API externa, escritores concurrentes,
caché, carga, seguridad integral ni recuperación ante fallos físicos.
