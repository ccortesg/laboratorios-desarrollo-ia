# Laboratorio 05 · GitHub Copilot: de la sugerencia al trabajo delegado

Capítulo 5. **Versión recomendada: 1.0.**

Revisar un resumen y su terminal JSON; conservar tanto el almacén como el filtro por nombre.

## Preparación y descarga

Python 3.10 o posterior con SQLite y biblioteca estándar. Sin paquetes adicionales ni servicios.

[Descargar ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_05_v1.0.zip) · [guía técnica](../../laboratorios/laboratorio_05/README.md) · [mapa y SHA-256](mapa_laboratorios.json) · [avisos de esta descarga](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/main/docs/publicacion/AVISOS_DISTRIBUCIONES_v1.0.md#laboratorio-05) · [MIT](../../LICENSE) · [CC BY 4.0 completo](../../LICENSES/CC-BY-4.0.txt).

SHA-256 del ZIP: `82130be2e74782c699c5aef6e70ab9e715cc9c68676c873c67f39fd2f37a2f8c`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Comprueba el hash del archivo antes de extraerlo. La guía se mantiene bajo main; la descarga histórica conserva su commit y sus bytes. Los avisos actuales acompañan externamente ese ZIP.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_05/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
python estados/propuesta/resumen.py --almacen ALFA --nombre otra
python pruebas_resumen.py --estado propuesta
python estados/solucion/resumen.py --almacen ALFA --nombre otra
python pruebas_resumen.py --estado solucion
```



## Qué debes observar

Propuesta: P04/P05 FALLIDO y salida 1; ignora el nombre y devuelve A01 indebidamente. Solución para ALFA/otra: total 0, códigos vacíos; seis P APROBADO. La solución completa conserva los veinte casos heredados: 26 casos.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

Total cuenta artículos, no unidades. La terminal exige almacén. La propuesta es didáctica y no una respuesta histórica de Copilot.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_05/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
