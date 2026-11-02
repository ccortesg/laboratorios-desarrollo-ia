# Laboratorio 07 · Datos e integraciones: cuando los sistemas deben ponerse de acuerdo

Capítulo 7. **Versión recomendada: 1.0.**

Importar existencias absolutas desde CSV con validación completa, atomicidad e idempotencia.

## Preparación y descarga

Python 3.11 o posterior con SQLite. Sólo la automatización de la web heredada requiere Node 20+, Playwright y Chromium.

[Descargar ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_07_v1.0.zip) · [guía técnica](../../laboratorios/laboratorio_07/README.md) · [mapa y SHA-256](mapa_laboratorios.json).

SHA-256 del ZIP: `2f579f87eb3a907e67ab195acb285543ee5997a805ff1add2e422dc7bc9b0b85`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Mientras el repositorio sea privado necesitas acceso autorizado a GitHub; un QR legible no concede acceso.
Si la descarga directa requiere sesión, abre [el ZIP en GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_07_v1.0.zip) y usa su descarga autenticada. Evita guardar una página de inicio de sesión como ZIP; comprueba el hash antes de extraer.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_07/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
python demostrar.py --estado propuesta --archivo datos/actualizacion_valida.csv --almacen ALFA --repeticiones 2
python demostrar.py --estado solucion --archivo datos/actualizacion_valida.csv --almacen ALFA --repeticiones 2
python pruebas_integracion.py --estado solucion
```



## Qué debes observar

Propuesta suma: A01 pasa 7→12→17; I01/I07 son FALLIDO en su batería. Solución reemplaza: A01 pasa a 5 y permanece en 5; ALFA muestra A01/A03. Los 17 casos I aprueban en solución, que conserva 34 anteriores (51 en total); en base los 17 I quedan NO EJECUTADO.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

Cada demostración usa una base nueva en memoria y repite dentro de la misma conexión. Dos procesos nuevos no demuestran idempotencia. No hay pantalla de importación ni persistencia entre procesos en este incremento.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_07/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
