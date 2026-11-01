# Requisitos, datos, componentes y comprobaciones

| Contrato | Datos / operación | Componente | Comprobación |
| --- | --- | --- | --- |
| C01–C04, B01–B06, N01–N10 | Datos de referencia intactos | Catálogo y detalle | `estados/*/pruebas.py`, 20 casos |
| P01–P06 | Resumen por almacén/nombre | `resumen.py` | `pruebas_resumen.py`, 6 casos |
| W01–W06 | HTTP y estados de la pantalla | Servidor y web | `pruebas_http.py`, 5; `pruebas_navegador.cjs`, 3 |
| I01–I08 | CSV y bases aisladas | Importación | `pruebas_integracion.py`, 17 casos |
| D01–D08 | CLI, archivo, HTTP, navegador e independencia de bases | Persistencia y diagnóstico | `pruebas_depuracion.py`, 10; `pruebas_recorrido.*`, 1 |
| S01 | CSV válido, A03 visible, búsqueda normalizada y nombre de 80 puntos de código | Política, resumen y base persistente | `pruebas_seguridad.py`, 1 caso |
| S02 | Dos almacenes, dos nombres iguales, clave codificada equivalente | Lista de pares antes del diccionario | `pruebas_seguridad.py`, 3 casos |
| S03 | Clave adicional `debug` | Lista de claves admitidas | `pruebas_seguridad.py`, 1 caso |
| S04 | Nombre de 81 puntos de código; query de 2.048/2.049 bytes | Límites de entrada | `pruebas_seguridad.py`, 2 casos |
| S05 | Percent inválido y UTF-8 inválido | Sintaxis y decodificación | `pruebas_seguridad.py`, 2 casos |
| S06 | Consulta válida → rechazo real → consulta válida | HTTP y pantalla del mismo servidor persistente | `pruebas_seguridad_navegador.*`, 1 caso |
| S07 | Texto de búsqueda parecido a SQL | Valores parametrizados y búsqueda literal del dominio | `pruebas_seguridad.py`, 1 caso |
| S08 | Renombrar/restaurar una base aislada con servidor vivo | Apertura real y error público | `pruebas_seguridad.py`, 1 caso |

Los 62 casos heredados más los doce nuevos forman 74 por estado. El grupo S tiene ocho criterios, no doce criterios. Cada caso puede incluir varias observaciones; por ejemplo, S04.b comprueba el borde, el rechazo y una consulta posterior dentro de una ejecución registrada. No se suman esas observaciones como pruebas independientes.

Los cuatro casos de recursos y las ocho pruebas comunes del recolector son infraestructura. La conservación de archivos y las verificaciones SHA-256 son auditorías. Sus recuentos no se agregan a las 222 ejecuciones funcionales de los tres estados.
