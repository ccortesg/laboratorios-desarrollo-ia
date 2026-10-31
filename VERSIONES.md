# Versiones y procedencia

**Integración del repositorio:** 1.1 · **Fecha:** 30 de octubre de 2026.

Las versiones de laboratorio conservan el significado de sus entregas editoriales. La versión 1.0 identifica su primera integración conjunta; la 1.1 incorpora el laboratorio 5 sin modificar los cuatro paquetes anteriores.

| Laboratorio | Paquete de referencia | Etiqueta de integración |
| --- | --- | --- |
| 01 | `distribuciones/LABORATORIO_01_v1.0.zip` | `lab-01-v1.0` |
| 02 | `distribuciones/LABORATORIO_02_v1.0.zip` | `lab-02-v1.0` |
| 03 | `distribuciones/LABORATORIO_03_v1.0.zip` | `lab-03-v1.0` |
| 04 | `distribuciones/LABORATORIO_04_v1.1.zip` | `lab-04-v1.1` |
| 05 | `distribuciones/LABORATORIO_05_v1.0.zip` | `lab-05-v1.0` |

Las cuatro etiquetas de laboratorios 1–4 identifican el mismo commit de importación conjunta. No representan commits retrospectivos de las fechas de producción de cada capítulo. `repositorio-v1.0` identifica también esa integración. La creación de una etiqueta local no acredita una publicación de Release en GitHub.

`lab-05-v1.0` y `repositorio-v1.1` corresponden al commit que integre esta actualización. Deben crearse después de comprobar el cambio; este documento no acredita por sí solo su creación o subida. Las cinco etiquetas anteriores se conservan en su commit original.

## Conservación

La primera integración importó 120 archivos visibles, sin cambios de bytes: 17 del laboratorio 1, 21 del 2, 46 del 3 y 36 del 4. Los 38 archivos internos del Git original del laboratorio 4 no se incluyen como un `.git` anidado en el árbol principal. El ZIP original los conserva y `historiales/laboratorio_04.bundle` transporta sus objetos y referencias.

El laboratorio 5 añade 78 archivos visibles idénticos a su ZIP; el total actual es 198. No incluye un Git anidado.

Las huellas de los paquetes están en `distribuciones/SHA256SUMS`; las de cada archivo visible, en `PROCEDENCIA.json`. La copia preparada permite recuperar las etiquetas originales:

| Referencia del ejercicio 4 | Commit original |
| --- | --- |
| `inicio` | `25f9b7a6d09341b6419d3d27237f1f1b68a6b64d` |
| `solucion` | `d7782e31acff5bd599f70ce6bb288f0a4219f775` |

## Evolución

Una corrección documental tendrá una versión identificable. Un cambio de comportamiento requerirá contrato, pruebas y evidencia nueva. Los archivos históricos y los ZIP de referencia conservarán sus huellas. Las nuevas ejecuciones se guardan por separado.

El maestro editorial v1.0 y el estado del libro v1.4 son las referencias editoriales vigentes. Los capítulos 1–5 permanecen pendientes de revisión del autor. El manuscrito y su Word siguen en el flujo editorial; aquí se incorpora el laboratorio 5.
