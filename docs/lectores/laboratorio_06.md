# Laboratorio 06 · Grok Build: de la idea a una aplicación de extremo a extremo

Capítulo 6. **Versión recomendada: 1.0.**

Recorrer formulario, HTTP y dominio; observar el cambio ALFA→BETA y distinguir vacío de error.

## Preparación y descarga

Python 3.10 o posterior con SQLite y un navegador para uso manual. Sólo la automatización requiere Node 20+, Playwright y Chromium.

[Descargar ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_06_v1.0.zip) · [guía técnica](../../laboratorios/laboratorio_06/README.md) · [mapa y SHA-256](mapa_laboratorios.json).

SHA-256 del ZIP: `79728447611c6ddbb1ab1615ca573a1e7199390c4890ec8796e699003b0880ef`.
El enlace está fijado al commit `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`; no sigue los cambios de main.
Mientras el repositorio sea privado necesitas acceso autorizado a GitHub; un QR legible no concede acceso.
Si la descarga directa requiere sesión, abre [el ZIP en GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_06_v1.0.zip) y usa su descarga autenticada. Evita guardar una página de inicio de sesión como ZIP; comprueba el hash antes de extraer.

Extrae el ZIP en una carpeta nueva de práctica, preferiblemente en trabajo/ si usas el repositorio completo. Conserva juntas sus subcarpetas. **Carpeta de ejecución:** laboratorio_06/ dentro del ZIP extraído.
`python` representa tu intérprete; sustituye de forma consistente por `python3` o `py -3` cuando corresponda.
Los bloques con `mkdir -p` usan Bash o Git Bash, como el README técnico.

## Recorrido mínimo

```bash
python estados/solucion/servidor.py --puerto 8000
```



## Qué debes observar

Abre http://127.0.0.1:8000: ALFA sin nombre devuelve A01, total 1; cambiar a BETA devuelve A04, total 1. Buscar inexistente devuelve total 0 y ausencia, sin alerta. Detén el servidor con Ctrl+C. El defecto de propuesta es W05; sólo se observa al enviar BETA en navegador. La solución completa satisface 34 casos; los ocho W de base son NO EJECUTADO.

Estas son expectativas del material. La preparación de acceso ejecutó de nuevo sólo el recorrido del laboratorio 1; las demás fichas reutilizan instrucciones técnicas existentes. Consulta la evidencia de tu propia ejecución para afirmar un resultado nuevo.

APROBADO indica un criterio satisfecho; FALLIDO, una discrepancia; BLOQUEADO, una precondición que impide comenzar; NO EJECUTADO, una actividad no realizada. Un fallo distinto del patrón didáctico, una excepción inesperada o una dependencia ausente requieren investigación.

## Límites y continuación

HTTP local en loopback. No es despliegue, ni uso acreditado de Grok Build, ni auditoría integral de seguridad.

Para ampliar o automatizar el recorrido, sigue el [README técnico](../../laboratorios/laboratorio_06/README.md) y lee su contexto antes de editar tu copia. En los laboratorios web, un verificador sin --navegador puede devolver 0 mientras el global permanece NO EJECUTADO. La instalación opcional de Node/Playwright/Chromium se describe en cada README técnico.

[Correcciones y soporte](README.md#correcciones-y-soporte) · [los diez laboratorios](README.md). El enlace de esta guía bajo main es mantenible y puede actualizarse: el compromiso editorial es conservar esta ruta; una nueva distribución tendrá una URL y huella propias. Los capítulos siguen pendientes de revisión editorial. La ejecución local no acredita uso de una herramienta comercial.
