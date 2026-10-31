# Contexto reutilizable: catálogo web local

## Problema y objetivo

Un usuario debe consultar qué artículos están disponibles en un almacén y, si lo
desea, buscar por parte del nombre. La regla ya existe y está verificada en la
solución del laboratorio 5. Este incremento la conecta con un formulario web,
sin crear una nueva interpretación de disponibilidad.

Un artículo aparece únicamente si está habilitado y tiene existencias disponibles
en el almacén seleccionado. El resumen devuelve `almacen`, `total` y `codigos`.
El total es el número de artículos disponibles, no la suma de sus existencias.
Los códigos conservan su escritura y orden definido por la solución heredada.

## Datos y contratos heredados

Cada estado contiene los mismos cuatro artículos sintéticos A01–A04. ALFA debe
devolver A01; BETA debe devolver A04. El artículo deshabilitado y el que no tiene
existencias quedan excluidos. No se incorporan registros ni se cambian los SQL.

`catalogo.py` conserva la búsqueda por nombre con `strip().casefold()` y
`detalle.py` la coincidencia exacta por código. `resumen.py` reutiliza el catálogo:
`resumir_catalogo(almacen, texto="")` produce el resumen y tiene una terminal
propia. Los 26 criterios heredados se ejecutan sobre los tres estados del capítulo.

## Archivos pertinentes

| Necesidad | Referencia |
| --- | --- |
| Alcance y criterios W | `ALCANCE.md` |
| Datos y esquema | `estados/base/datos/` |
| Disponibilidad | `estados/base/solucion/consulta.sql` |
| Búsqueda y resumen | `estados/base/catalogo.py`, `estados/base/resumen.py` |
| Criterios C, B y N | `estados/base/pruebas.py`, `estados/base/pruebas_detalle.py` |
| Criterios P | `pruebas_resumen.py`, invocado con `--directorio` |
| Frontera HTTP de referencia | `estados/solucion/servidor.py` |
| Interfaz de referencia | `estados/solucion/web/` |
| Comprobaciones nuevas | `pruebas_http.py`, `pruebas_navegador.cjs` |
| Evidencia y preservación | `evidencia/`, `PROCEDENCIA.json` |

## Trabajo delimitado

El formulario ofrece ALFA y BETA. Envía el almacén y un nombre opcional a
`GET /api/resumen`. El servidor llama a la función existente; no evalúa SQL
construido a partir de la URL. Las respuestas JSON y la interfaz distinguen
consulta correcta sin coincidencias de error. La aplicación no escribe datos.

El propósito es aprender a conectar componentes y validar el recorrido real.
No hay autorización, administración de artículos, servicios remotos ni funciones
de solicitudes. Esas capacidades pertenecen a una evolución no implementada.

## Cierre esperado

La solución debe conservar las 26 comprobaciones anteriores y aprobar ocho casos
web. W05 requiere interacción con un navegador: seleccionar BETA y comprobar que
se envía BETA. La disponibilidad de una herramienta comercial se registra por
separado y no condiciona el funcionamiento local del ejercicio.
