# Resultados observados del laboratorio 7

Fecha técnica de inicio UTC: 2026-10-31T17:55:26.494189+00:00.
Entorno: Linux, Python 3.12.14, SQLite 3.53.1,
Node v24.22.1, Playwright 1.62.1 y Chromium 156.0.8078.80.
El navegador instalado del entorno se seleccionó explícitamente; las instrucciones
para el lector usan la instalación estándar. No se distribuye ese ejecutable.

Comando lógico observado desde la raíz del laboratorio:

```bash
python verificar.py --navegador --salida <CARPETA_NUEVA>
```

Estado global: **APROBADO**, salida 0. Quince baterías,
136 ejecuciones: 134 APROBADO,
2 FALLIDO didácticos, cero bloqueados y cero errores
inesperados. Los 17 casos I de base son NO EJECUTADO y se cuentan aparte de las
136 ejecuciones. Los únicos fallos son I01 e I07 en propuesta; permanecen FALLIDO.
La solución satisface 51/51 casos, correspondientes a 40 criterios.

Las 36 comprobaciones de procedencia son APROBADO. Las 30/30 huellas de salidas
del verificador coinciden con los bytes finales; captura y finales están separados
en comandos.json. El SHA-256 del contrato previo coincide con su archivo.

## Lo que se observó

La demostración con el archivo válido registra A01/ALFA de 7 a 12 y después a 17
en propuesta. La solución pasa de 7 a 5 y permanece en 5. En solución la primera
aplicación registra cuatro filas aplicadas; la segunda, cero y cuatro sin cambio.
ALFA muestra A01/A03, A02 sigue deshabilitado y BETA queda vacío tras recibir cero.
El rechazo tardío conserva todas las existencias originales y termina con código1.

I06 incluye el rechazo de una entrada con error posterior y una escritura SQLite
rechazada mediante un trigger temporal de prueba. En ambos escenarios las tres
tablas conservan su estado. La escritura controlada usa isolation_level=None y
verifica que el BEGIN explícito protege el lote. No se simulan cortes físicos.

Las cuatro demostraciones tienen sus comandos y ocho huellas verificadas en
`demostracion/`. Son observaciones complementarias; no se suman a los casos de las
15 baterías ni se presentan como una cobertura funcional mayor.

## Evidencia y límites

`ejecucion_local/` contiene resumen, entorno, comandos, expectativas, observaciones,
conservación heredada y huellas de fuentes. Los registros copiados conservan sus
bytes. La salida de la primera prueba de desarrollo queda fuera de esta evidencia
final; el contrato previo y la aclaración transaccional documentan la secuencia.

APROBADO se refiere al contrato sintético y al navegador registrado. No acredita
Windows, otros navegadores, pruebas de carga, concurrencia, auditoría integral de
seguridad, persistencia entre procesos ni uso comercial de herramientas de IA.
Los retos del capítulo son NO EJECUTADO. La evidencia editorial y el paquete de
integración se verifican por separado.
