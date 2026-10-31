# Decisiones y supuestos

1. CSV estricto con encabezado conocido y cantidades absolutas, no movimientos.
   El formato completo y los casos ambiguos se fijan en el contrato previo.
2. Identificadores exactos. No aplicar la normalización de nombres a códigos.
3. Cantidades entre 0 y 2147483647. Es un límite didáctico del intercambio, no
   una afirmación sobre la capacidad máxima de SQLite.
4. Validación completa antes de escritura y transacción de aplicación. Los
   cambios pendientes del llamador se rechazan para no confirmarlos por accidente.
5. La conexión opcional en las funciones preserva las llamadas antiguas.
   No se modifica el comportamiento HTTP heredado para aceptar una importación.
6. Cero y pares omitidos tienen significados distintos: cero actualiza; omisión
   conserva. Una relación inexistente puede crearse con maestros conocidos.
7. Se conserva el SHA-256 de los bytes de entrada. BOM y finales de línea pueden
   cambiar esa huella aunque el contenido interpretado sea equivalente.
8. `filas_aplicadas` cuenta pares cuyo estado cambió; repetir un archivo válido
   puede dar cero aplicadas y estado `APLICADO`.
9. El único defecto de la propuesta es sumar. Las validaciones son iguales a la
   solución; I01 e I07 lo detectan con resultados públicos, no inspeccionando SQL.
10. La evidencia no acredita cortes de energía, carga, concurrencia ni servicio
    comercial. Los límites se conservan aunque todos los casos definidos pasen.
