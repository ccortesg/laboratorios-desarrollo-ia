# Decisiones y supuestos

- Incremento local; SQLite en archivo para compartir estado entre procesos.
- Inicialización explícita y exclusiva; consultar/importar/servir jamás cargan semillas.
- Rutas relativas desde cwd; ruta absoluta fija al arrancar servidor para invariancia.
- Esquema didáctico validado antes de usar la base. No se ejecutan migraciones.
- La conexión por petición conserva compatibilidad con el servidor con hilos.
- Se conserva la consulta SQL y el contrato público; el defecto sólo omite un argumento.
- Diagnóstico opcional separado de la respuesta: configurado y efectivo son observaciones distintas.
- Destino de diagnóstico igual a la base (incluido mismo archivo por enlace) se rechaza.
- Alias desconocidos son opacos y distintos dentro de cada proceso; no comparables entre procesos.
- D02 acepta memoria correctamente descrita: demuestra fidelidad, no disponibilidad correcta.
- Los diez D de terminal/HTTP y D04 de navegador tienen baterías separadas para registrar cobertura.
- Las pruebas heredadas se conservan y se invocan con --directorio cuando corresponde.
- Publicación, Windows y reto no se presuponen ejecutados.
