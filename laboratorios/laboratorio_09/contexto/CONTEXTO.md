# Contexto reutilizable · laboratorio 9

## Problema y objetivo

El formulario genera normalmente una URL simple, pero cualquier consumidor del servidor puede enviar claves repetidas, desconocidas, mal codificadas o excesivas. El objetivo es fijar una política explícita de entrada para el resumen del catálogo antes de consultar los datos. El resultado correcto incluye rechazo previsible, un error público genérico y recuperación de la pantalla.

## Archivos pertinentes

1. `CONTRATO_SEGURIDAD.md`: decisiones anteriores a la implementación y S01–S08.
2. `estados/base/servidor.py`: adaptación HTTP anterior, con selección del primer valor repetido.
3. `estados/propuesta/politica_consulta.py`: defecto didáctico preparado.
4. `estados/solucion/politica_consulta.py` y `servidor.py`: validación y adaptación corregidas.
5. `estados/solucion/persistencia.py`, `resumen.py` y `laboratorio.py`: base real y consulta ya verificadas; no se modifican.
6. `pruebas_seguridad.py` y `pruebas_seguridad_navegador.*`: once casos HTTP y el recorrido visible.
7. `verificar.py`: patrón exacto, contratos heredados, evidencia y huellas.
8. `PROCEDENCIA.json` y `diferencias/`: conservación y cambio revisable.

## Datos y alcance

Los únicos almacenes de referencia son ALFA/BETA. Los artículos A01–A04 son sintéticos. El CSV `datos/actualizacion_valida.csv` hace visible A03, mantiene A02 deshabilitado y deja A04 sin unidades en BETA. Las pruebas crean una base aislada por escenario; no editan los datos de referencia ni reutilizan la base del recorrido manual.

Las consultas CLI y las interfaces de dominio conservan sus entradas previas. El nuevo límite se aplica al adaptador HTTP de `/api/resumen`; no redefine importación, reservas, autenticación ni autorizaciones.

## Qué cuenta como terminado

Debe coincidir la lista exacta de fallos esperados, aprobar los 62 heredados en los tres estados, aprobar los doce S en solución, ejecutar el navegador real y comprobar las huellas finales. Los conteos por sí solos no bastan: se cotejan también identidades, tipos de error, estados y códigos de salida. La revisión editorial del capítulo es una decisión posterior del autor.
