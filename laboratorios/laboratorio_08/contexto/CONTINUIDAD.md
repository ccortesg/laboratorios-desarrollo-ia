# Continuidad vigente · corrección 1.0.1

La ejecución Windows v1.0 aportada por el autor detectó un problema de liberación de recursos en los auxiliares de prueba. `CORRECCION_WINDOWS_v1.0.md` explica el alcance. Las conexiones se cierran explícitamente; no cambia ningún contrato funcional ni el defecto intencional de propuesta. `pruebas_recursos.py` es una batería de regresión adicional, separada de los casos del catálogo.

El estado de la corrección en Windows es NO EJECUTADO hasta una nueva ejecución. La evidencia original FALLIDO se conserva. Los resultados Linux de v1.0 siguen identificando su código y su entorno; no constituyen una aprobación retrospectiva de Windows ni una prueba de v1.0.1.

## Antecedente v1.0 conservado

# Continuidad

Este incremento parte de la solución del laboratorio 7 y conserva C/B/N/P/W/I.
La base mantiene su alcance correcto en memoria. Propuesta/solución incorporan persistencia.
El contrato y el patrón esperado se escribieron antes de implementar.

Consulta evidencia/RESULTADOS.md para las ejecuciones efectivas y evidencia/INVESTIGACION.md
para las observaciones que discriminan hipótesis. No conviertas el patrón esperado en
evidencia ni un código cero parcial en prueba completa.

No se acredita Windows desde una ejecución Linux. No se implementó el reto del capítulo.
Los manuscritos siguen pendientes de revisión editorial. Usa una carpeta de evidencia nueva
en cada intento y conserva las huellas y originales.
