# Continuidad del laboratorio 3

**Versión:** 1.0. **Fecha:** 30 de octubre de 2026.

## Estado y referencias

El incremento elegido es búsqueda por subcadena del nombre sobre el catálogo disponible. `ALCANCE.md` conserva el contrato fijado antes de implementar los estados. `laboratorio.py`, los datos y la consulta proceden sin cambios del laboratorio 2. Los nuevos módulos conservan los estados generado, refactorizado, defecto y corregido.

Las expectativas y la trazabilidad están en CONTEXTO. ARQUITECTURA explica las responsabilidades implementadas y las propuestas. DECISIONES conserva D01 a D03 y registra las elecciones de esta entrega. Los tres encargos reutilizables están en `prompts/`; todos son ejemplos preparados para el libro.

## Cómo comprobarlo

Desde la raíz del laboratorio, ejecuta `python verificar.py --salida mi_evidencia` con una carpeta que no exista. Compara tu `resumen.json` con `evidencia/resumen.json`, sin sustituir tu observación por el registro distribuido. Los resultados de cada criterio están en `pruebas_<estado>.json`.

El estado base sólo ejecuta C01 a C04. Los B figuran NO EJECUTADOS porque aún no tiene búsqueda. Los estados generado, refactorizado y corregido deben aprobar diez criterios. En defecto deben fallar exclusivamente B05 y B06 por el almacén omitido. Su batería devuelve código 1; la verificación global devuelve 0 sólo si observa el patrón previsto completo.

`observacion_diagnostica.json` conserva la comparación entre consulta base y búsqueda para BETA. Los archivos `diferencias/` y el comando `comparar.py` permiten revisar la generación, la extracción, la introducción del defecto y su corrección. `sha256_fuentes.json` vincula la ejecución con las fuentes y documentos concretos.

## Límites y pendientes

Los capítulos anteriores y este capítulo siguen siendo borradores pendientes de revisión del autor. No se han inventado observaciones editoriales nuevas ni aprobaciones.

El paquete acredita ejecución local, no uso real dentro de Codex, GitHub Copilot o Grok Build. No se ha realizado una comparación experimental de prompts ni una prueba con lectores humanos. Tampoco se implementó el reto de cantidades del capítulo 1, la pantalla propuesta del capítulo 2 ni una aplicación productiva.

El siguiente trabajo puede preparar un repositorio sintético para el capítulo 4 y definir un encargo revisable sobre él. Antes de afirmar uso de una herramienta comercial será necesario ejecutar esa sesión y registrar su evidencia. Los requisitos y permisos de esa siguiente etapa aún deben concretarse; esta nota no inicia un despliegue ni amplía los accesos.
