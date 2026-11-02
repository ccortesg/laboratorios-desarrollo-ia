# Laboratorio 02 · Contexto y arquitectura

Capítulo 2. **Versión recomendada: 1.0.**

**Título del capítulo:** se usa la denominación técnica disponible; su título editorial completo requiere cotejo con el índice entregado por separado.

Preparar un encargo CLARO, un mapa de responsabilidades y una continuidad verificable sin alterar el catálogo.

## Preparación y descarga

Python con sqlite3 y unittest; referencia técnica Python 3.12. Editor y terminal. Sin paquetes adicionales.

[Descargar ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_02_v1.0.zip) · [guía técnica](../../laboratorios/laboratorio_02/README.md) · [mapa y SHA-256](mapa_laboratorios.json).

SHA-256 del ZIP: `442e63d079fa229e500199ca3e5292369238c658e72db83cadc1ac243d31d4e1`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Mientras el repositorio sea privado necesitas acceso autorizado a GitHub; un QR legible no concede acceso.
Si la descarga directa requiere sesión, abre [el ZIP en GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_02_v1.0.zip) y usa su descarga autenticada. Evita guardar una página de inicio de sesión como ZIP; comprueba el hash antes de extraer.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_02/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
python laboratorio.py --version solucion --almacen ALFA
python pruebas.py --version solucion
python verificar.py --salida mi_evidencia
```

Antes de ejecutar, lee contexto/ENCARGO_INSUFICIENTE.md, CONTEXTO.md, ARQUITECTURA.md y DECISIONES.md; después contrasta ENCARGO_CLARO.md y CONTINUIDAD.md.

## Qué debes observar

ALFA devuelve A01 y los cuatro criterios C aprueban. La revisión K01–K06 del contexto es documental y se registra por separado; el verificador no evalúa su calidad.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

Contexto y arquitectura sobre comportamiento existente. No hay web, persistencia, reservas ni medición de productividad.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_02/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
