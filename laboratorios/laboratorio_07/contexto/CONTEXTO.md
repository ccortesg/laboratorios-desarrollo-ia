# Contexto suficiente para otra sesión

Problema: una exportación de existencias de un sistema sintético debe alimentar
el catálogo local. “Importar” es insuficiente: hay que definir identificadores,
cantidades absolutas, rechazo completo y el origen que consultará el catálogo.

Consulta primero `CONTRATO_INTEGRACION.md`, luego `ARQUITECTURA.md` y `TRAZABILIDAD.md`.
Lee `estados/solucion/importacion.py`, `laboratorio.py`, `catalogo.py` y `resumen.py`.
Los SQL en `datos/` de cada estado son los datos originales de referencia.
`datos/actualizacion_valida.csv` en la raíz es una entrada adicional del ejercicio.

Los identificadores A01–A04 y ALFA/BETA son sintéticos. El nombre puede buscarse
con strip/casefold según B, pero códigos y almacenes del CSV se comparan exactamente.
La regla de disponibilidad sigue en `solucion/consulta.sql` y no se duplica en el
importador. El resumen cuenta artículos disponibles, no unidades.

Cada prueba comienza con su base aislada. Dos repeticiones de una importación
deben compartir conexión para comprobar idempotencia. La demostración imprime
existencias y resumen de la conexión modificada; la web conserva el funcionamiento
anterior y no es una interfaz de importación.
