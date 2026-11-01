# Investigación reproducible del síntoma

Reconstrucción didáctica sobre un defecto deliberado conocido antes de implementar.
Las observaciones siguientes proceden de la ejecución real conservada en
`ejecucion_local/`; no son respuestas simuladas de una herramienta comercial.

## Entrada y síntoma

CSV válido con huella
`d4c2daa0016e34ea251cb2d3eed024c7e3150347a360e1b7781e798011344506`.
La importación de la propuesta registra APLICADO y cuatro pares cambiados.
La consulta directa ve A01/A03 en ALFA, mientras HTTP responde 200 con A01.
La pantalla conserva el catálogo anterior. D03 y D04 registran estas diferencias.

## Hipótesis y experimentos

| Hipótesis | Observación que la distinguiría | Experimento y resultado observado | Conclusión limitada |
| --- | --- | --- | --- |
| La importación no quedó confirmada | Otro proceso seguiría leyendo cantidades iniciales | D01 importa, termina y abre por otra CLI; SQL independiente y CLI ven 5/8/3/0 | Descartada para esta entrada y archivo |
| La pantalla aplica mal el filtro, pero HTTP es correcto | HTTP devolvería A01/A03 y la UI sólo A01 | D03 consulta HTTP sin navegador: ya devuelve A01; D04 muestra lo mismo | La divergencia ya existe antes de la representación |
| El servidor consulta otro origen | Origen efectivo distinto al configurado y datos de referencia | D02: CLI archivo:principal; HTTP memoria; D08.a muestra pérdida de distinción entre archivos | Respaldada por observaciones de origen y contenido |
| Basta registrar la configuración para demostrar el origen | Origen configurado y efectivo serían siempre equivalentes | D02 registra archivo:principal como configurado y memoria como efectivo en la misma petición | Esa inferencia no es válida en este escenario |

Estas conclusiones no descartan que otros defectos puedan producir síntomas similares.
No se construyeron fallos adicionales para simular que todas las hipótesis fueran ciertas.

## Intervención y comparación

La diferencia `diferencias/propuesta_a_solucion.diff` transmite la conexión al
resumen HTTP. La consulta SQL, el CSV, los filtros, la interfaz y las expectativas
permanecen iguales. La misma batería D cambia de tres fallos terminal/HTTP y un
fallo de navegador a once aprobaciones. Los 51 casos heredados aprueban en ambos.

D05 usa la misma ruta absoluta desde dos directorios con espacios y reinicia el
servidor: la solución conserva los datos, sin resembrado. D08.a compara dos bases:
la importada y el control no importado siguen independientes en solución.

## Diagnóstico que no altera la base

D02 también intenta destinar el diagnóstico a la propia base.
CLI y servidor rechazan DIAGNOSTICO_INVALIDO con salida 2; la huella del archivo
y el estado se conservan. No se afirma una auditoría de todos los errores de E/S.
Los alias de otros orígenes son distintos dentro del proceso y no revelan rutas;
no sirven para comparar identidad entre procesos diferentes.

## Referencias a resultados

- `ejecucion_local/propuesta_depuracion.json`: D01, D02, D03, D05, D06, D07 y D08.
- `ejecucion_local/solucion_depuracion.json`: mismas comprobaciones tras la corrección.
- `ejecucion_local/propuesta_depuracion_navegador.json`: D04 con importación correcta y UI anterior.
- `ejecucion_local/solucion_depuracion_navegador.json`: D04 con servidor vivo y UI actualizada.
- `ejecucion_local/comandos.json`: comandos de baterías, tiempos, códigos y huellas.
- `ejecucion_local/resumen.json`: patrón exacto y límites del conjunto.

Observaciones adicionales e hipótesis del lector deben registrarse como nuevas,
con sus propias entradas y salidas. No modifiques estos resultados históricos.
