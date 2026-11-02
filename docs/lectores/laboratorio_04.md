# Laboratorio 04 · Codex en acción: trabajar sobre un repositorio real

Capítulo 4. **Versión recomendada: 1.1.**

Revisar referencias y el árbol de trabajo de un repositorio sintético; añadir consulta exacta por código.

## Preparación y descarga

Git y Python con sqlite3 y unittest; sólo biblioteca estándar. El ZIP incluye repositorio/.git; no necesita el repositorio completo ni servicios comerciales.

[Descargar ZIP 1.1](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_04_v1.1.zip) · [guía técnica](../../laboratorios/laboratorio_04/README.md) · [mapa y SHA-256](mapa_laboratorios.json) · [avisos de esta descarga](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/main/docs/publicacion/AVISOS_DISTRIBUCIONES_v1.0.md#laboratorio-04) · [MIT](../../LICENSE) · [CC BY 4.0 completo](../../LICENSES/CC-BY-4.0.txt).

SHA-256 del ZIP: `6409c16235a406a7d22bb983327369647419c6b3c1237c443ee590dafe0511a3`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Comprueba el hash del archivo antes de extraerlo. La guía se mantiene bajo main; la descarga histórica conserva su commit y sus bytes. Los avisos actuales acompañan externamente ese ZIP.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_04/ del ZIP extraído; después laboratorio_04/repositorio/.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo desde el ZIP autónomo

Conserva `repositorio/.git`, aunque el explorador lo oculte. Abre la terminal en **laboratorio_04/** de una extracción nueva, junto a verificar.py:

```bash
python --version
python -c "import sqlite3, unittest; print(sqlite3.sqlite_version)"
git --version
python verificar.py --salida mi_evidencia
```

`mi_evidencia` debe ser nueva y queda fuera de repositorio/. Este verificador comprueba las etiquetas, sin evaluar tus ediciones actuales. Después, desde esa misma raíz:

```bash
cd repositorio
git status --short
git log --oneline --decorate
git rev-parse refs/tags/inicio
git rev-parse refs/tags/solucion
git diff --stat inicio solucion --
git diff inicio solucion -- detalle.py pruebas_detalle.py pruebas.py
python pruebas.py
```

La última batería comprueba el árbol actual. No necesitas descargar el repositorio de acompañamiento completo. Lee el README incluido en el ZIP para continuar la práctica desde inicio en otra copia.

### Alternativa con el repositorio completo

Desde la **raíz del repositorio de acompañamiento**, con historiales/laboratorio_04.bundle disponible y el destino trabajo/laboratorio_04 libre:

```bash
python herramientas/preparar_laboratorio_04.py
cd trabajo/laboratorio_04
python verificar.py --salida mi_evidencia
cd repositorio
python pruebas.py
```

Esta alternativa prepara la copia Git a partir del bundle. La carpeta visible laboratorios/laboratorio_04/repositorio/ del repositorio general no contiene un Git independiente. Conserva cualquier copia previa.

## Qué debes observar

Referencias inicio: diez APROBADO; solucion: veinte APROBADO. El árbol recién preparado debe aprobar veinte. N01–N10 no existen en inicio y quedan NO EJECUTADO. El verificador histórico no acredita tus ediciones actuales.

El recorrido autónomo se comprueba de nuevo durante el encargo de licencias y apertura; sus comandos, códigos y resultados se conservan en el comprobante externo posterior. El ensayo del laboratorio 1 pertenece a la preparación anterior. Ninguno acredita ejecución de una herramienta comercial.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

Códigos exactos como cadenas, sin normalización ni prefijos. Conservar .git del ZIP. El verificador compara etiquetas; pruebas.py comprueba el árbol actual. El preparador sólo es la alternativa del repositorio completo.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_04/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
