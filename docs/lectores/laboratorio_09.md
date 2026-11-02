# Laboratorio 09 · Confiabilidad y seguridad del software generado por IA

Capítulo 9. **Versión recomendada: 1.0.**

Rechazar entradas HTTP ambiguas o inválidas y comprobar la recuperación sin perder los contratos heredados.

## Preparación y descarga

Python 3.11 o posterior con SQLite y un navegador manual. Para automatizar: Node 20+, Playwright y Chromium.

[Descargar ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_09_v1.0.zip) · [guía técnica](../../laboratorios/laboratorio_09/README.md) · [mapa y SHA-256](mapa_laboratorios.json) · [avisos de esta descarga](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/main/docs/publicacion/AVISOS_DISTRIBUCIONES_v1.0.md#laboratorio-09) · [MIT](../../LICENSE) · [CC BY 4.0 completo](../../LICENSES/CC-BY-4.0.txt).

SHA-256 del ZIP: `6010765d31beab92b35447439864e5af0b321c99962b7bc692a0dacf66ecc17a`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Comprueba el hash del archivo antes de extraerlo. La guía se mantiene bajo main; la descarga histórica conserva su commit y sus bytes. Los avisos actuales acompañan externamente ese ZIP.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_09/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
mkdir -p trabajo/demo_09_01
python estados/solucion/persistencia.py iniciar --base trabajo/demo_09_01/catalogo.sqlite
python estados/solucion/persistencia.py importar --base trabajo/demo_09_01/catalogo.sqlite --archivo datos/actualizacion_valida.csv
python estados/solucion/persistencia.py consultar --base trabajo/demo_09_01/catalogo.sqlite --almacen ALFA
python estados/solucion/servidor.py --base trabajo/demo_09_01/catalogo.sqlite --puerto 8000
```

Con el servidor abierto visita http://127.0.0.1:8000 y después http://127.0.0.1:8000/api/resumen?almacen=ALFA&almacen=BETA para observar el rechazo.

## Qué debes observar

La importación queda APLICADO y ALFA devuelve A01/A03, total 2. En el navegador la query repetida devuelve HTTP 400 y PARAMETRO_REPETIDO, distinto de un catálogo vacío. Detén el servidor con Ctrl+C. Solución: 74 casos; base falla sólo S02.a/S02.b/S02.c, S03, S04.a/S04.b, S05.a/S05.b y S06; propuesta sólo S02.a/S02.b/S02.c. Los 62 heredados aprueban en los tres estados.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

Política HTTP acotada; no prueba autenticación, autorización, TLS, resistencia global a denegación de servicio ni ausencia universal de inyección.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_09/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
