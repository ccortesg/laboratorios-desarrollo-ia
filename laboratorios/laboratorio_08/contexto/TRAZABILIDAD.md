# Requisitos, datos, componentes y observaciones

| Grupo | Datos y componente | Comprobación |
| --- | --- | --- |
| C/B/N | SQL original, laboratorio/catalogo/detalle | estados/*/pruebas.py, veinte casos |
| P | resumen.py y terminal original | pruebas_resumen.py, seis casos |
| W | servidor sin --base y UI original | pruebas_http.py y pruebas_navegador.cjs, ocho casos |
| I | CSV sintéticos y importacion.py | pruebas_integracion.py, diecisiete casos |
| D01 | CSV válido, persistencia CLI, reapertura | cantidades exactas y resumen desde procesos separados |
| D02 | diagnóstico CLI/HTTP y colisión de destino | origen efectivo fiel, mismo estado y bytes tras rechazo |
| D03 | base importada y HTTP | ALFA, BETA, búsqueda y deshabilitado |
| D04 | misma página/servidor y CSV | antes → importación CLI → después, cambio de almacén y búsqueda |
| D05 | base absoluta, dos directorios con espacios | resultados antes/después del reinicio y ausencia de resembrado |
| D06.a/b | ruta ausente/esquema ajeno | rechazo por CLI y servidor, ausencia de creación o modificación |
| D07.a/b | error_tardio.csv y actualización parcial A01 | snapshot de tres tablas e idempotencia con omitidos |
| D08.a/b | dos archivos y reinicialización | separación de resultados y conservación de datos/bytes |

Las D agrupan ocho criterios en once casos; una observación interna adicional dentro de
D02 no se cuenta como un criterio independiente. Base no implementa los once D.
