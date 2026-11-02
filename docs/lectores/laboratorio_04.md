# Laboratorio 04 · Codex en acción: trabajar sobre un repositorio real

Capítulo 4. **Versión recomendada: 1.1.**

Revisar referencias y el árbol de trabajo de un repositorio sintético; añadir consulta exacta por código.

## Preparación y descarga

Git y Python con sqlite3 y unittest. Para el preparador, una copia completa de este repositorio, incluido historiales/laboratorio_04.bundle.

[Descargar ZIP 1.1](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_04_v1.1.zip) · [guía técnica](../../laboratorios/laboratorio_04/README.md) · [mapa y SHA-256](mapa_laboratorios.json).

SHA-256 del ZIP: `6409c16235a406a7d22bb983327369647419c6b3c1237c443ee590dafe0511a3`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Mientras el repositorio sea privado necesitas acceso autorizado a GitHub; un QR legible no concede acceso.
Si la descarga directa requiere sesión, abre [el ZIP en GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_04_v1.1.zip) y usa su descarga autenticada. Evita guardar una página de inicio de sesión como ZIP; comprueba el hash antes de extraer.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** Raíz del repositorio completo; después trabajo/laboratorio_04 y su repositorio/.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
python herramientas/preparar_laboratorio_04.py
cd trabajo/laboratorio_04
python verificar.py --salida evidencia_referencias
cd repositorio
python pruebas.py
git diff inicio solucion --
```

Este recorrido empieza en la raíz del repositorio completo, no dentro del ZIP ni de laboratorios/laboratorio_04/repositorio/. El ZIP recomendado conserva el paquete autónomo y su Git original; la ficha utiliza el preparador documentado del repositorio general. No reutilices un destino ocupado. Para tus propias ediciones ejecuta también pruebas.py desde el repositorio preparado.

## Qué debes observar

Referencias inicio: diez APROBADO; solucion: veinte APROBADO. El árbol recién preparado debe aprobar veinte. N01–N10 no existen en inicio y quedan NO EJECUTADO. El verificador histórico no acredita tus ediciones actuales.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

Códigos exactos como cadenas: sin normalización ni prefijos. La instantánea visible en laboratorios/ no es un Git independiente. Usa el preparador; conserva cualquier copia previa.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_04/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
