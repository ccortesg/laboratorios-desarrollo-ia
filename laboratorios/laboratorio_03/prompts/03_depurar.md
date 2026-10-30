# Encargo de depuración

**Ejemplos didácticos preparados para el libro.** La variante defectuosa fue creada expresamente para el ejercicio. No se atribuye a una conversación histórica ni a la salida de una herramienta comercial. El lector puede intentar el diagnóstico desde el síntoma antes de leer la explicación de la corrección en README.

## Primera versión insuficiente

> La búsqueda está fallando en otro almacén. Arréglala.

Faltan la entrada exacta, qué respuesta se obtuvo, cuál debía obtenerse, los estados comparables y un comando que reproduzca la discrepancia. Aún no hay base para escoger una causa. Una conjetura puede servir como hipótesis si se acompaña de una observación que permita contrastarla.

## Versión con CLARO

```text
Diagnostica y corrige la variante didáctica defectuosa.

C: Lee ALCANCE.md, contexto/CONTEXTO.md y
   contexto/ARQUITECTURA.md. Examina estados/defecto.py,
   laboratorio.py, los datos y pruebas.py.
   Para BETA y texto vacío se espera A04, pero la variante
   defecto devuelve A01. Con " OTRA " devuelve [] y se
   espera A04. La consulta base para BETA devuelve A04.
L: Conserva el estado defectuoso como referencia.
   Corrige en estados/corregido.py con el cambio mínimo.
   No cambies datos, SQL ni expectativas de las pruebas.
A: B05 y B06 deben recuperar A04; C01 a C04 y B01 a B04
   deben seguir aprobando. Explica la causa localizada.
R: Reproduce los síntomas con recorrido.py y ejecuta
   python pruebas.py --estado defecto.
   Formula hipótesis y busca una observación que las
   distinga. Sigue el almacén entre las llamadas.
   Aplica la corrección después de localizar el desvío.
O: Ejecuta python pruebas.py --estado corregido.
   Entrega diferencia, evidencia anterior y posterior,
   interpretación de los fallos y límites comprobados.
```

## Observación que distingue hipótesis

Los comandos concretos son:

```text
python recorrido.py --estado base --almacen BETA
python recorrido.py --estado defecto --almacen BETA --texto ""
python recorrido.py --estado defecto --almacen BETA --texto " OTRA "
```

Si la consulta base respeta BETA y la búsqueda no, revisa cómo se entrega la entrada a esa consulta antes de cambiar la regla SQL. Esta observación acota la investigación, sin demostrar por sí sola que cualquier código posterior sea correcto. La inspección de la llamada y la comprobación posterior completan el razonamiento del ejercicio.

## Cierre revisable

`python comparar.py --paso introducir-defecto` permite estudiar cómo se preparó el error. `python comparar.py --paso corregir` muestra su reparación. Las salidas esperadas del estado defectuoso son fallos pertinentes del ejercicio; la solución final debe satisfacer los diez criterios. Un error inesperado de ejecución no sustituye el fallo de aserción previsto.
