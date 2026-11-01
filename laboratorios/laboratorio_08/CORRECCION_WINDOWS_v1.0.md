# Corrección de recursos SQLite · versión 1.0.1

## Problema observado y alcance

La ejecución Windows aportada por el autor del laboratorio 8 v1.0 terminó FALLIDO. El ZIP recibido identifica 244 archivos y tiene SHA-256 `d89be25eac2cc6915bde22d3bef6bc4a9ee7052fe821542012c6698e352906b6`. Las huellas de sus salidas coinciden; su resultado fallido se conserva.

Los auxiliares `snapshot()` y la preparación de D06.b abrían conexiones SQLite sin cierre explícito. Al limpiar las carpetas temporales, Windows registró errores de acceso a archivos abiertos. Las trazas de D04 muestran `PermissionError [WinError 32]`; faltan los dos JSON finales de ese recorrido. En la propuesta de terminal, D05 y D08.a tienen registros duplicados por la aserción didáctica y un error posterior. El evaluador rechaza esa duplicación y el resumen general no incorpora las 21 baterías del laboratorio 8.

La corrección libera las conexiones incluso cuando una consulta falla. Conserva la transacción de la preparación de D06.b, sus datos, las consultas del catálogo y los criterios C/B/N/P/W/I/D. No admite errores adicionales ni convierte fallos de infraestructura en fallos didácticos.

## Comprobar la corrección

Desde la raíz de este laboratorio:

```bash
python -m unittest discover -s . -p pruebas_recursos.py -v
python verificar.py --navegador --salida trabajo/verificacion_corregida_01
```

La primera batería comprueba liberación de conexiones y conservación del comportamiento; se contabiliza aparte de los 62 casos funcionales de la solución. La segunda exige una carpeta nueva y el navegador ya preparado según README. La propuesta debe seguir fallando únicamente D03, D04, D05 y D08.a. Base conserva sus once casos D NO EJECUTADO.

La distribución v1.0.1 conserva la evidencia histórica v1.0 sin alterarla. Su contenido describe las fuentes ejecutadas en aquel momento; no afirma que los archivos modificados actuales tengan las mismas huellas. La nueva evidencia de corrección se entrega separadamente y se identifica por su versión y ejecución. La verificación Windows posterior a este ajuste sigue NO EJECUTADO hasta recibir sus resultados.

## Referencias primarias

Consulta efectiva: 2026-11-01 UTC (31 de octubre en America/Hermosillo).

- [Python 3.11: contexto de conexiones SQLite](https://docs.python.org/3.11/library/sqlite3.html#how-to-use-the-connection-context-manager): el contexto resuelve transacciones y no cierra automáticamente la conexión.
- [Python 3.11: contextlib.closing](https://docs.python.org/3.11/library/contextlib.html#contextlib.closing): cierre del recurso al salir, también cuando ocurre una excepción.
- [Python 3.11: TemporaryDirectory](https://docs.python.org/3.11/library/tempfile.html#tempfile.TemporaryDirectory): limpieza y errores por archivos abiertos en Windows.

Esta corrección no acredita una nueva sesión de una herramienta comercial ni aprobación editorial de los capítulos.
