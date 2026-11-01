# Revisión del diagnóstico Windows · Laboratorio 8

**Versión:** 1.0. **Estado de la auditoría:** APROBADO. **Estado funcional recibido:** FALLIDO.

Esta revisión analiza la captura aportada por el autor. No constituye una ejecución nueva de Windows ni una aprobación de los manuscritos. Los archivos recibidos se conservan sin cambios.

## Identidad e integridad

El ZIP `DIAGNOSTICO_LABORATORIO_08_WINDOWS_v1.0.zip` contiene 244 archivos. Su SHA-256 coincide exactamente con la huella comunicada:

```
d89be25eac2cc6915bde22d3bef6bc4a9ee7052fe821542012c6698e352906b6
```

Las 244 copias extraídas coinciden con sus entradas originales. El registro preparado identifica HEAD `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622`, árbol base `b123b5969e8077ba0cb3c4eedc9b348f94294652` y árbol de índice `2ea01dea2aa0c8907eba54ef65efcb44d547b9d7`, en `integracion/laboratorio-08`. Registra main conservada y ningún cambio adicional sin preparar. Estos datos corresponden al momento registrado; no sustituyen una inspección posterior del equipo.

El comprobador original de huellas, ejecutado en modo de sólo lectura durante esta auditoría, aprobó **102/102** salidas del conjunto y **2/2** de la captura del recolector, ambos con salida 0. Los hashes corresponden a los bytes finales guardados. Esta integridad permite analizar el fallo; no acredita éxito funcional.

## Entorno y verificaciones anteriores al fallo

La captura del conjunto comenzó el **1 de noviembre de 2026 a las 01:32:13 UTC** (31 de octubre, 18:32:13 con desfase UTC−07:00). Registra Windows, Python 3.11.9, SQLite 3.45.1 y Git 2.45.1.windows.1. Las pruebas de navegador heredadas del laboratorio 8 registran Node v20.20.0, Playwright 1.62.1 y Chromium 151.0.7922.34.

La salida capturada del recolector acredita **ocho pruebas, OK y código 0**. Sus pruebas y sus dos huellas se contabilizan aparte de los casos funcionales.

Las 75 huellas de fuentes declaradas por el laboratorio 8 coinciden con los bytes de la copia original preparada. También coinciden directamente otras 224 fuentes de los laboratorios 1–3 y 5–7 y las dos herramientas declaradas del laboratorio 4. Las 32 declaraciones de referencias Git del laboratorio 4 coinciden con la captura Linux original; no se reconstruyó ese repositorio durante esta auditoría. La evidencia no declara hashes específicos del verificador común o de su módulo de huellas: no se atribuye a ese cotejo una cobertura que no tiene.

## Qué falló realmente

El conjunto termina FALLIDO, código 1, con **44 baterías y 408 ejecuciones agregadas**: 400 aprobadas y ocho fallos didácticos de los laboratorios 1–7; cero bloqueos, 37 NO EJECUTADO dentro de esas baterías y diez criterios ausentes aparte. El registro del laboratorio 8 señala `ValueError` durante su evaluación. Sus baterías no llegaron a incorporarse al resumen global.

El laboratorio 8 sí produjo registros. Sus quince baterías heredadas, que corresponden a 51 casos por cada uno de los tres estados, contienen **153 aprobaciones**. Los errores se concentran en el soporte nuevo de depuración.

| Evidencia | Observación |
| --- | --- |
| `propuesta_depuracion.json` | Doce registros para diez identificadores. D05 y D08.a figuran dos veces: aserción didáctica y PermissionError. Hay ocho PermissionError, tres aserciones fallidas y una aprobación. |
| `solucion_depuracion.json` | Diez registros: ocho PermissionError y dos aprobaciones (D03 y D06.a). |
| `propuesta_depuracion_navegador.stderr.txt` | Traza PermissionError, WinError 32, al limpiar el archivo sintético principal.sqlite mediante TemporaryDirectory. |
| `solucion_depuracion_navegador.stderr.txt` | El mismo tipo de error de limpieza. |
| Ambos JSON de depuración con navegador | Ausentes: la limpieza interrumpe el controlador antes de escribirlos. |

El resumen interno declara 175 ejecuciones, 156 aprobaciones, 19 fallos y 18 errores de ejecución, pero **sus totales no se validan**: dos registros duplicados y dos resultados faltantes pueden compensarse numéricamente. No se suman estas cifras como cobertura válida ni como una segunda ejecución del conjunto.

## Causa y grado de certeza

Las dos trazas de navegador acreditan el fallo de limpieza sobre `principal.sqlite`: Windows impide eliminar el archivo que sigue abierto. En `soporte_procesos.py`, `snapshot()` utiliza `with sqlite3.connect(...)` sin un cierre explícito. La preparación de D06.b en `pruebas_depuracion.py` presenta el mismo patrón.

El contexto de una conexión SQLite administra la transacción y no cierra la conexión; la documentación oficial lo explica en [Connection context manager](https://docs.python.org/3.11/library/sqlite3.html#how-to-use-the-connection-context-manager). Python también documenta el posible PermissionError al eliminar archivos abiertos en Windows en [TemporaryDirectory](https://docs.python.org/3.11/library/tempfile.html#tempfile.TemporaryDirectory).

Los dieciséis errores terminales conservan el tipo PermissionError y observaciones funcionales completas, coherentes con un error al limpiar la prueba. Esos registros no incluyen una traza completa por cada caso; la confirmación directa de la fase cleanup procede de las dos trazas D04.

El evaluador común rechaza identificadores duplicados con ValueError. Se reejecutó únicamente ese evaluador sobre los JSON Windows recibidos, en modo de lectura, y reprodujo exactamente `ValueError: Criterio duplicado`. No se ejecutaron otra vez los casos funcionales. El resultado confirma por qué ninguna batería del laboratorio 8 llegó al acumulador.

## Corrección y siguientes pasos

La corrección debe cerrar explícitamente las conexiones de soporte y de la preparación de D06.b. Se conservarán los contratos y los fallos didácticos D03, D04, D05 y D08.a de propuesta. No corresponde ignorar errores de limpieza, aceptar identificadores duplicados ni modificar los resultados recibidos.

La ejecución fallida queda como antecedente. Tras aplicar una corrección revisada se debe generar evidencia nueva, ejecutar las comprobaciones completas y verificar sus huellas. Una comprobación posterior en Linux no sustituye la nueva ejecución Windows. La integración en main, las etiquetas y la publicación permanecen pendientes; la revisión editorial del autor también.

## Fuentes de evidencia

La fuente primaria es el ZIP recibido, identificado por su SHA-256. Los registros relevantes son `antes.json`, `preparado.json`, `conjunto/resumen.json`, `conjunto/laboratorio_08/resumen.json`, los JSON de depuración, las dos trazas stderr de D04 y `recolector/comandos.json`. Sus rutas aquí son relativas y sintéticas. El JSON de auditoría conserva los cotejos y las huellas de los archivos relevantes; no se incorpora el ZIP crudo al material publicable.
