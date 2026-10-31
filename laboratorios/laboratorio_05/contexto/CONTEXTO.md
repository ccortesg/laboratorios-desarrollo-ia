# Contexto suficiente para continuar

## Lo que existe

Cada estado contiene una copia funcional local de la solución del laboratorio 4.
`laboratorio.py` crea SQLite en memoria con los cuatro artículos sintéticos y
ejecuta una consulta parametrizada. Un artículo está disponible cuando está
habilitado y tiene cantidad positiva en el almacén seleccionado. No hay reservas.

`catalogo.py` expone `buscar_catalogo(almacen, texto)`. Filtra por subcadena del
nombre dentro del catálogo disponible; aplica `strip().casefold()` al término y
`casefold()` al nombre. Un término vacío conserva todos los disponibles. No elimina
acentos ni promete búsqueda aproximada.

`detalle.py` expone `obtener_articulo(almacen, codigo)`. Devuelve el registro disponible
con código exacto o `None`. No normaliza el código, retira espacios ni admite prefijos.
Las entradas de ambas funciones son cadenas. La habilitación de un artículo no
equivale a autorización de un usuario.

## Lo nuevo

`resumir_catalogo(almacen, texto="")` produce `almacen`, `total` y `codigos`.
`total` cuenta artículos y no unidades. Reutiliza `buscar_catalogo`; no reescribe SQL
ni toma atajos que omitan el nombre. La terminal exige almacén y ofrece nombre
opcional. El contrato completo y P01–P06 están en `../ALCANCE.md`.

## Trazabilidad

| Reglas | Datos o entrada | Componente | Comprobación |
| --- | --- | --- | --- |
| C01–C04: disponibilidad | A01 local, A02 deshabilitado, A03 agotado, A04 remoto | `solucion/consulta.sql` y `catalogo.py` | `pruebas.py` de cada estado |
| B01–B06: nombre | ALFA/BETA, término vacío, espacios, caja y ausencia | `catalogo.py` | `pruebas.py` de cada estado |
| N01–N10: código exacto | Códigos válidos, remotos, inexistente, caja, espacios, prefijo | `detalle.py` | `pruebas_detalle.py`, ejecutado por `pruebas.py` |
| P01–P04: resumen funcional | ALFA/BETA y filtros explícitos | Nuevo `resumen.py` | `pruebas_resumen.py` |
| P05–P06: terminal | BETA/inexistente y almacén omitido | `main()` de `resumen.py` | `pruebas_resumen.py`, mediante subproceso |

Las expectativas literales están en las pruebas; no se calculan llamando a la
función bajo examen. Los ocho archivos heredados y sus hashes constan en
`../PROCEDENCIA.json`. La consulta SQL conserva orden por código, pero el dataset
no permite comprobar el orden de varios resultados dentro de un mismo almacén.

## Qué no debe inferirse

El laboratorio local no acredita una sesión comercial, una aplicación desplegada,
seguridad integral ni mejoras de tiempo. La propuesta incorrecta fue preparada
expresamente para practicar revisión. Los borradores editoriales continúan
pendientes de revisión del autor.
