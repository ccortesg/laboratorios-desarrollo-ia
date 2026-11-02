# Laboratorio 08 · Depuración con evidencia: investigar errores entre entornos y servicios

Capítulo 8. **Versión recomendada: 1.0.1.**

Seguir CSV→CLI→SQLite persistente→HTTP→pantalla e identificar la conexión efectivamente utilizada.

## Preparación y descarga

Python 3.11 o posterior con SQLite y un navegador manual. Para automatizar: Node 20+, Playwright y Chromium.

[Descargar ZIP 1.0.1](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_08_v1.0.1.zip) · [guía técnica](../../laboratorios/laboratorio_08/README.md) · [mapa y SHA-256](mapa_laboratorios.json) · [avisos de esta descarga](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/main/docs/publicacion/AVISOS_DISTRIBUCIONES_v1.0.md#laboratorio-08) · [MIT](../../LICENSE) · [CC BY 4.0 completo](../../LICENSES/CC-BY-4.0.txt).

SHA-256 del ZIP: `8e445b1ecb195e96999f9ab7123e4bbeb93ce43a056a0fefbb91e3379f617cea`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Comprueba el hash del archivo antes de extraerlo. La guía se mantiene bajo main; la descarga histórica conserva su commit y sus bytes. Los avisos actuales acompañan externamente ese ZIP.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_08/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
mkdir trabajo
python estados/solucion/persistencia.py iniciar --base trabajo/catalogo.sqlite
python estados/solucion/servidor.py --base trabajo/catalogo.sqlite --puerto 8000 --diagnostico trabajo/servidor.jsonl
```

Mantén el servidor abierto. Desde una segunda terminal situada en la misma raíz, ejecuta:

```bash
python estados/solucion/persistencia.py importar --base trabajo/catalogo.sqlite --archivo datos/actualizacion_valida.csv
python estados/solucion/persistencia.py consultar --base trabajo/catalogo.sqlite --almacen ALFA --diagnostico trabajo/consulta.jsonl
```

Consulta de nuevo en el navegador y detén con Ctrl+C. Reinicia el mismo comando de servidor para observar persistencia.

## Qué debes observar

Antes de importar ALFA muestra A01. Tras importar en otra terminal, ALFA muestra A01/A03 y BETA queda vacío; reiniciar contra la misma base conserva el resultado. D02 aprueba también en propuesta al revelar el origen equivocado. Propuesta falla sólo D03, D04, D05 y D08.a; los once D de base quedan NO EJECUTADO. Solución: 51 heredados más once D, 62 casos.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

La distribución 1.0 sigue como antecedente del fallo Windows por recursos abiertos; usa 1.0.1. Diagnóstico y base deben tener destinos distintos. No hay múltiples escritores, recuperación física ni auditoría productiva.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_08/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.

La [distribución 1.0 histórica](../../distribuciones/LABORATORIO_08_v1.0.zip) y su evidencia se conservan. La corrección recomendada está explicada en [CORRECCION_WINDOWS_v1.0.md](../../laboratorios/laboratorio_08/CORRECCION_WINDOWS_v1.0.md).
