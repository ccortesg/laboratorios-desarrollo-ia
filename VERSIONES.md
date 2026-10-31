# Versiones vigentes · Integración 1.3 preparada

**Fecha:** 31 de octubre de 2026. La versión técnica preparada es 1.3; el estado operativo es [1.5](docs/estados/ESTADO_REPOSITORIO_v1.5.md) y el estado del libro es [1.6](docs/estados/ESTADO_DEL_LIBRO_v1.6.md). El maestro editorial permanece en 1.0.

| Entrega o corrección | Situación confirmada |
| --- | --- |
| Integración 1.2 y laboratorio 6 | Publicados por el autor; lab-06-v1.0 y repositorio-v1.2 permanecen en 31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd. |
| Corrección del recolector posterior a 1.2 | main confirmado en 6382e05846e149a9a72f7fdc56da48c37a873833; H01 cerrado para nuevas ejecuciones. No creó una etiqueta nueva. |
| Laboratorio 7 v1.0 e integración 1.3 | Preparados y verificados localmente. lab-07-v1.0 y repositorio-v1.3 son etiquetas previstas, no creadas. |

Las nueve etiquetas existentes conservan sus referencias. Los laboratorios 1–6, sus distribuciones, historiales y evidencias permanecen como antecedentes; el incremento y su evidencia se añaden por separado. La prueba local no acredita una subida ni una ejecución Windows del laboratorio 7.

El contrato nuevo incorpora I01–I08 sin cambiar C/B/N/P/W. La verificación conjunta de siete laboratorios registró 44 baterías, 408 ejecuciones, 400 aprobaciones y ocho fallos didácticos, con 64/64 huellas coincidentes. El detalle y el cierre del empaquetado están en el estado operativo.

Los capítulos 1–7 continúan pendientes de revisión editorial del autor. Manuscritos y Word permanecen en la entrega editorial.

## Historial conservado

Los textos siguientes se conservan como referencias históricas. Sus expresiones de preparación o publicación pendiente corresponden a la fecha de cada entrega, no al estado vigente que encabeza este archivo.

# Versiones y procedencia

**Integración preparada: 1.2 · Fecha: 31 de octubre de 2026 (UTC).**

El estado operativo es `ESTADO_REPOSITORIO_v1.3.md`; el estado editorial es `ESTADO_DEL_LIBRO_v1.5.md`. Sus números no sustituyen la versión de integración del repositorio.

| Laboratorio | Paquete de referencia | Etiqueta de integración |
| --- | --- | --- |
| 01 | `distribuciones/LABORATORIO_01_v1.0.zip` | `lab-01-v1.0` |
| 02 | `distribuciones/LABORATORIO_02_v1.0.zip` | `lab-02-v1.0` |
| 03 | `distribuciones/LABORATORIO_03_v1.0.zip` | `lab-03-v1.0` |
| 04 | `distribuciones/LABORATORIO_04_v1.1.zip` | `lab-04-v1.1` |
| 05 | `distribuciones/LABORATORIO_05_v1.0.zip` | `lab-05-v1.0` |
| 06 | `distribuciones/LABORATORIO_06_v1.0.zip` | `lab-06-v1.0`, prevista, no creada |

## Referencias observadas

La integración inicial 1.0 conserva las cinco etiquetas de laboratorios 1–4 y `repositorio-v1.0` en `52875ff15c6648f9a042a15a94da812e37effa40`. Son etiquetas de importación conjunta, no commits retrospectivos de las fechas de escritura.

La integración 1.1 está confirmada en `67edef7b44524f5f621e9b060c6b9c523c1b05a8`, árbol `a1d70872f969886c5f33f88692b61e90579a18ed`. `main`, `lab-05-v1.0` y `repositorio-v1.1` coincidieron al consultar GitHub. Se conserva esa referencia como base del parche nuevo.

La integración 1.2 está preparada localmente. Después de aplicar, revisar, comprobar y crear el commit correspondiente, podrán crearse únicamente `lab-06-v1.0` y `repositorio-v1.2`. No se movieron ni se sustituyeron etiquetas anteriores. Ningún documento local acredita por sí solo una subida o una Release.

## Conservación

Los 198 archivos visibles y los cinco ZIP anteriores conservan sus bytes: 17 archivos del laboratorio 1, 21 del 2, 46 del 3, 36 del 4 y 78 del 5. El laboratorio 6 añade 112 archivos idénticos a su ZIP; el total es 310. No incorpora Git anidado ni dependencias descargadas.

Los 38 archivos internos del Git original del laboratorio 4 permanecen en su ZIP. `historiales/laboratorio_04.bundle` conserva sus objetos y referencias: `inicio` apunta a `25f9b7a6d09341b6419d3d27237f1f1b68a6b64d` y `solucion` a `d7782e31acff5bd599f70ce6bb288f0a4219f775`.

Las huellas de los seis paquetes están en `distribuciones/SHA256SUMS`; cada archivo visible está inventariado en `PROCEDENCIA.json`. La evidencia nueva se añade por separado en `evidencia_integracion/laboratorio_06_v1.0/`.

El documento maestro editorial v1.0 sigue vigente. Los capítulos 1–6 permanecen pendientes de revisión del autor. Manuscritos y Word se conservan fuera del repositorio técnico.
