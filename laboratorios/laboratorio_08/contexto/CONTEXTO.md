# Contexto suficiente para continuar

Síntoma didáctico: importación confirmada y consulta directa correcta, pero catálogo web
sin actualizar. El laboratorio 7 era correcto en memoria; este incremento añade persistencia
entre procesos y estudia su propagación hasta el consumidor.

Lee CONTRATO_DEPURACION.md, CONTRATO_INTEGRACION.md, ARQUITECTURA.md y TRAZABILIDAD.md.
En estados/solucion consulta persistencia.py, servidor.py, laboratorio.py y origen.py.
La regla SQL, catalogo.py, resumen.py e importacion.py se reutilizan.

Los SQL de referencia no cambian. Las importaciones de prueba usan archivos SQLite aislados.
Nunca inicialices de nuevo al consultar o iniciar el servidor. La salida HTTP mantiene su
contrato; el diagnóstico opcional vive en otro archivo y observa la conexión efectiva.

Resultados observados: ../evidencia/RESULTADOS.md e INVESTIGACION.md. No reconstruyas
conversaciones ni atribuyas esta práctica a una herramienta comercial.
