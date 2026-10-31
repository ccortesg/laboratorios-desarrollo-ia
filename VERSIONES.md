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
