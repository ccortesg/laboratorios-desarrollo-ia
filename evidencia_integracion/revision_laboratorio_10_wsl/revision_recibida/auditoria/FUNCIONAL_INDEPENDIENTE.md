# Revisión funcional independiente · laboratorio 10 WSL

**Dictamen: APROBADO dentro del alcance auditado.** Revisión realizada el 1 de noviembre de 2026, hora de Hermosillo; las marcas originales UTC del 2 de noviembre se conservan.

## Método y resultados

No se ejecutaron scripts recibidos ni una nueva batería. Se reconstruyeron contratos e identificadores desde los originales de producción y se recontaron las 125 listas de casos recibidas. Coinciden estados individuales, tipos de error, códigos y totales: **1.043 ejecuciones, 1.018 aprobadas, 25 fallidas didácticas, cero bloqueos y cero errores de ejecución**. Hay 56 casos NO EJECUTADO en sus versiones base y diez criterios N ausentes en inicio del laboratorio 4, registrados aparte.

Los 25 fallos son exactamente los permitidos por identificador y estado; todos conservan AssertionError. No se convirtió infraestructura en fallo didáctico. Las 92 fuentes declaradas del laboratorio 10 coinciden con la producción, incluido el contrato previo.

| Estado 10 | APROBADO | FALLIDO | NO EJECUTADO |
| --- | ---: | ---: | ---: |
| Base | 74 | 0 | 8 |
| Propuesta | 81 | 1 | 0 |
| Solución | 82 | 0 | 0 |

Los 74 casos heredados aprueban en los tres estados. T02 es el único fallo de propuesta 10: el importador rechaza y conserva la base, pero el operador consulta y devuelve éxito indebido. En solución, el mismo archivo deja la consulta NO EJECUTADO y devuelve código 1; T02 aprueba esa conducta.

Un caso NO EJECUTADO puede ser registrado por un comprobador que detecta ausencia de la función o por el verificador sin iniciar proceso. Se conservan ambas convenciones históricas; un proceso que informa ausencia no se suma como ejecución funcional del caso.

## Recorrido y entorno

T08 conserva procesos, observaciones HTTP/DOM, SQLite y diagnóstico del servidor. En propuesta y solución se observa A01 antes, A01/A03 después del operador y A03 al buscar. El servidor sigue vivo, utiliza la misma base y el estado persistido coincide con las cantidades absolutas. Node/Chromium termina con código 0. El -15 del servidor es su cierre explícito por el controlador, no un fallo de prueba.

Los registros identifican WSL2/Linux, Python 3.12.16, SQLite 3.53.1, Node 22.23.1, Playwright 1.62.1 y Chromium 151.0.7922.34. El auxiliar ejecutó el conjunto con --navegador; cada batería conserva comandos y tiempos. Se observa un intento integral en este envío. Son registros de procesos nuevos y no sustituciones por la producción Linux o informes históricos Windows.

## Infraestructura separada

Las capturas unittest contienen Ran 8, Ran 9, Ran 9, Ran 4 y Ran 1, seguidos de OK y código 0: recolector, evaluadores 9/10, recursos SQLite y recursos del operador. No contienen omisiones. RO01 conserva un método con dos subcasos y OSError inyectado; no es un incidente real. No se suman estos métodos a las 1.043 ejecuciones.

## Observador y límites

Se leyó soporte_de_sesion/sitecustomize.py sin ejecutarlo. Envuelve sólo cerrar_evidencia para copiar capturas antes de llamar al original, con los mismos argumentos y retorno. No modifica decisiones, códigos ni expectativas. Añade I/O y tiempo: no acredita rendimiento equivalente. No se observó error de este observador.

La auditoría valida coherencia de registros recibidos, no reproduce WSL ni demuestra ausencia de sesiones ajenas al envío. Windows nativo no se ejecutó. Timeout no fue inducido como caso nuevo; tampoco concurrencia, fallos físicos o transacción global. Revisión editorial pendiente. Integridad de bytes y conservación Git son auditorías separadas.

## Fuentes

- verificacion_intento_01/conjunto/: 125 JSON originales de casos, enumerados y con sus hashes en FUNCIONAL_INDEPENDIENTE.json.
- verificacion_intento_01/comandos.json, capturas de infraestructura, entorno_auxiliar.json.
- verificacion_intento_01/conjunto/laboratorio_10/: T02, T08, comandos, entorno y fuentes.
- operaciones/verificacion_integral_intento_01.json, SESION.json y soporte_de_sesion/sitecustomize.py.
- Contrato, verificador común y prueba T08 originales de producción.

**Problemas materiales pendientes: ninguno.**
