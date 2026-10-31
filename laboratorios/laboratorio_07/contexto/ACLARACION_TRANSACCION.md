# Aclaración de revisión de la transacción

Después de la primera ejecución del laboratorio, la revisión del código identificó
que el contexto de conexión de Python no abre por sí mismo una transacción.
El contrato ya exigía que el importador controlara su aplicación. Se añade `BEGIN`
explícito para que esa obligación se conserve también con una conexión cuyo
`isolation_level` sea `None`.

I06 conserva su identificador y el caso de fila posterior inválida. Se añade una
observación dentro de ese mismo caso: un trigger temporal de la prueba provoca
un rechazo SQLite en la segunda escritura de un archivo válido. Se compara el
estado completo antes y después. El trigger no forma parte del importador ni de
los datos entregados; vive sólo en la base desechable de esa prueba.

No cambia el número de criterios ni de casos registrados: son ocho criterios I
y 17 casos. Esta comprobación no simula un corte eléctrico ni concurrencia.
El contrato previo y su SHA-256 permanecen intactos como evidencia de la secuencia.
