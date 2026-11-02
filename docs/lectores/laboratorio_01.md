# Laboratorio 01 · El nuevo oficio del desarrollador: del código al resultado

Capítulo 1. **Versión recomendada: 1.0.**

Relacionar una regla de disponibilidad por almacén con cuatro criterios observables y una corrección SQL.

## Preparación y descarga

Python con sqlite3 y unittest de la biblioteca estándar; referencia técnica Python 3.12. Editor y terminal. Sin pip, Git, Node ni cuenta comercial para este recorrido.

[Descargar ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_01_v1.0.zip) · [guía técnica](../../laboratorios/laboratorio_01/README.md) · [mapa y SHA-256](mapa_laboratorios.json).

SHA-256 del ZIP: `e47d0a8e23f63d84fe0030438e6f5e729d4a0faa955c27d2fede3120f8d57ed3`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Mientras el repositorio sea privado necesitas acceso autorizado a GitHub; un QR legible no concede acceso.
Si la descarga directa requiere sesión, abre [el ZIP en GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_01_v1.0.zip) y usa su descarga autenticada. Evita guardar una página de inicio de sesión como ZIP; comprueba el hash antes de extraer.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_01/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
python laboratorio.py --version inicial --almacen ALFA
python pruebas.py --version inicial
python laboratorio.py --version solucion --almacen ALFA
python pruebas.py --version solucion
python verificar.py --salida mi_evidencia
```



## Qué debes observar

Inicial: A01 y A04, tres criterios APROBADO y C04 FALLIDO por aserción; pruebas.py devuelve 1. Solución: A01, cuatro APROBADO y código 0. verificar.py devuelve 0 sólo al reconocer exactamente ese patrón; no convierte C04 en aprobación.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

SQLite en memoria; no evalúa cantidades solicitadas, reservas, HTTP, autorización, concurrencia ni producción.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_01/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
