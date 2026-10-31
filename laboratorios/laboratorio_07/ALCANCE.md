# Alcance del incremento

El laboratorio demuestra un adaptador CSV de existencias y una consulta del
catálogo sobre la misma conexión SQLite en memoria. Conserva las funciones
anteriores cuando no se proporciona una conexión.

Contrato completo: `contexto/CONTRATO_INTEGRACION.md`. La decisión y su SHA-256
se registraron en `evidencia/contrato_previo.json` antes de implementar código.

Se añaden ocho criterios I01–I08 con 17 casos. Cada estado conserva los 34 casos
C/B/N/P/W anteriores. La base contiene la web corregida del laboratorio 6; no
hereda el defecto de selección de su antigua propuesta. El único defecto nuevo
es la suma de cantidades absolutas en la propuesta de este laboratorio.

La importación no añade maestros, no modifica habilitación ni nombre y no borra
pares omitidos. Crea un par antes ausente sólo si sus dos identificadores existen.
La función entrega un informe de negocio; el verificador decide si se cumple el
contrato observando estado, resultados, errores y los casos negativos.

Quedan fuera: servicio externo, persistencia entre procesos, pantalla de subida,
concurrencia, reservas, cantidades solicitadas, autenticación y producción.
