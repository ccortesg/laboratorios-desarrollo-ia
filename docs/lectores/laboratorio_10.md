# Laboratorio 10 · Automatización, agentes y operación: prepararse para lo que sigue

Capítulo 10. **Versión recomendada: 1.0.**

Ejecutar importación y consulta con comandos fijos sobre la misma base, detenerse ante rechazo y conservar recibos.

## Preparación y descarga

Python 3.11 o posterior con SQLite. El operador no requiere navegador; la automatización web requiere Node 20+, Playwright y Chromium.

[Descargar ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_10_v1.0.zip) · [guía técnica](../../laboratorios/laboratorio_10/README.md) · [mapa y SHA-256](mapa_laboratorios.json).

SHA-256 del ZIP: `5e39d5fb92e2408684003809d65f753b16929c7ad649e70f1c8eec0e26eb54f3`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Mientras el repositorio sea privado necesitas acceso autorizado a GitHub; un QR legible no concede acceso.
Si la descarga directa requiere sesión, abre [el ZIP en GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_10_v1.0.zip) y usa su descarga autenticada. Evita guardar una página de inicio de sesión como ZIP; comprueba el hash antes de extraer.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_10/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
mkdir -p trabajo/demo_10_01
python -B estados/solucion/persistencia.py iniciar --base trabajo/demo_10_01/catalogo.sqlite
python -B estados/solucion/operar.py --base trabajo/demo_10_01/catalogo.sqlite --archivo datos/actualizacion_valida.csv --almacen ALFA --salida trabajo/demo_10_01/recibo_01
python -B soporte/huellas_evidencia.py trabajo/demo_10_01/recibo_01
```



## Qué debes observar

Operación válida: código 0, APROBADO, A01/A03 y total 2. El recibo conserva entrada.csv, resultado.json, comandos.json, capturas y huellas.json. Los 74 heredados deben aprobar en cada estado. Base: ocho T NO EJECUTADO; propuesta: sólo T02 FALLIDO por aserción y salida 1; solución completa: 82 casos APROBADO.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

No hay transacción global, reintento automático ni agente comercial. Una importación confirmada persiste aunque falle después la consulta. La falta de confirmación no demuestra que la base esté intacta.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_10/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
