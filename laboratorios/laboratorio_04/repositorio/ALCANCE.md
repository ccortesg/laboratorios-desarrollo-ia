# Contrato previo del laboratorio 4

**Fecha:** 30 de octubre de 2026. Este documento se fija antes de implementar el incremento. Describe expectativas, no resultados observados. El historial Git conservará este contrato en la etiqueta `inicio` y la implementación en `solucion`.

## Necesidad e incremento

Añadir `obtener_articulo(almacen, codigo)` en `detalle.py`. Recibe dos cadenas y devuelve el diccionario con `codigo` y `nombre` del artículo disponible cuyo código coincide exactamente, o `None` si no pertenece al catálogo disponible del almacén. Reutiliza `consultar_catalogo("solucion", almacen)`; no modifica SQL, datos, disponibilidad ni búsqueda por nombre.

El identificador se compara sin retirar espacios, cambiar mayúsculas ni interpretar prefijos. La búsqueda por nombre conserva su normalización anterior. No se implementan cantidades solicitadas, reservas, autorizaciones, nuevas interfaces, persistencia, servicios, red ni despliegues. Los tipos que no sean cadenas quedan fuera del contrato. La tecnología del laboratorio no decide la arquitectura productiva futura.

## Criterios conservados

C01 a C04 mantienen habilitación, cantidad positiva y almacén seleccionado. B01 a B06 mantienen la búsqueda por subcadena del nombre, normalización de espacios exteriores y mayúsculas, término vacío, exclusión remota y transmisión de BETA. Los diez métodos y sus expectativas se conservarán literalmente; sólo se adapta el montaje de la batería para importar `catalogo.py`, copia del estado corregido del laboratorio 3.

## Criterios nuevos

| ID | Almacén | Código solicitado | Expectativa |
| --- | --- | --- | --- |
| N01 | ALFA | `A01` | Diccionario completo de A01 |
| N02 | BETA | `A04` | Diccionario completo de A04 |
| N03 | ALFA | `A02` | `None`, artículo deshabilitado |
| N04 | ALFA | `A03` | `None`, cantidad cero |
| N05 | ALFA | `A04` | `None`, existencias sólo en BETA |
| N06 | BETA | `A01` | `None`, existencias sólo en ALFA |
| N07 | ALFA | `A99` | `None`, código inexistente |
| N08 | ALFA | `a01` | `None`, coincidencia sensible a mayúsculas |
| N09 | ALFA | ` A01 ` | `None`, no se retiran espacios |
| N10 | ALFA | `A0` | `None`, un prefijo no es el código exacto |

Los esperados proceden del contrato y los datos sintéticos; no se calculan llamando a la implementación. Cada criterio nuevo tiene una prueba con una entrada concreta. Los negativos comprueban la nueva entrada pública, además de conservar las diez comprobaciones heredadas.

## Archivos y secuencia autorizada del ejercicio

El punto `inicio` contiene el catálogo corregido, las diez pruebas anteriores, este contrato, las instrucciones persistentes y su contexto. Primero se comprobará esa base. El incremento añadirá `detalle.py` y `pruebas_detalle.py`, conectará la batería nueva en `pruebas.py` y actualizará `contexto/CONTEXTO.md`, `ARQUITECTURA.md`, `DECISIONES.md` y `CONTINUIDAD.md`. Estos son los únicos archivos del cambio entre las etiquetas.

No se modificarán `catalogo.py`, `laboratorio.py`, `datos/`, `solucion/consulta.sql`, este contrato ni los diez métodos de prueba heredados. Se revisarán diferencias y se ejecutará la batería completa antes de cerrar. La etiqueta `solucion` identificará el resultado de referencia; una reproducción propia debe conservar sus propias diferencias y evidencia.

## Evidencia y límites

El verificador externo al repositorio extraerá los dos commits en carpetas temporales, ejecutará sus baterías, registrará resultados y comprobará sus identidades y conteos: diez aprobaciones en inicio, veinte en solución. El inicio no implementa detalle; N01–N10 se describirán como NO EJECUTADO allí, sin presentarlos como aprobados. No se necesita un fallo intencional nuevo en esta etapa.

La disponibilidad de Codex se comprobará separadamente. Documentación de funciones, ejecución local y sesión comercial son evidencias distintas. No se atribuirá a Codex la autoría ni la ejecución del incremento sin una sesión real documentada. APROBADO, FALLIDO, BLOQUEADO y NO EJECUTADO se acompañarán siempre del objeto y motivo. Los resultados finitos no acreditan rendimiento, seguridad integral ni preparación para producción.
