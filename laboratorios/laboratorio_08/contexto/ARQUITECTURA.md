# Componentes implementados

| Componente | Responsabilidad |
| --- | --- |
| persistencia.py | Inicializar sin sobrescribir, abrir un archivo existente, validar esquema y exponer CLI de importar/consultar. |
| importacion.py | Reutilizar el contrato CSV absoluto, validación completa y aplicación transaccional del capítulo 7. |
| servidor.py | Adaptar HTTP; conservar modo predeterminado y abrir/cerrar una conexión persistente por petición. |
| laboratorio.py | Elegir la conexión efectiva, ejecutar SQL y emitir observación opcional. |
| origen.py | Diagnóstico mediante contexto por petición; alias sintéticos, rechazo de colisión con la base. |
| catalogo.py y resumen.py | Disponibilidad, filtro por nombre y resumen; sin duplicar negocio. |
| soporte_procesos.py | Lanzar procesos reales, leer disponibilidad, consultar loopback y cerrar recursos. |
| pruebas_depuracion.py | Diez casos D de CLI/HTTP con estado independiente observado por SQL. |
| pruebas_recorrido.py y .cjs | D04 continuo con servidor vivo, Chromium real y otro proceso importador. |
| verificar.py | Contrastar estados contra el patrón exacto y cerrar huellas de evidencia nueva. |

La inicialización exclusiva usa el esquema y datos de referencia una sola vez.
Las aperturas posteriores usan URI SQLite mode=ro para consultar o mode=rw para importar;
ninguna crea una base. La compatibilidad exige columnas, tipos, nulabilidad, claves primarias
y las dos relaciones de existencias del esquema didáctico.

El diagnóstico se instala por contexto y se observa después de resolver la conexión.
No comparte una conexión SQLite entre hilos ni desactiva su comprobación de hilo.
No se agregan endpoints ni campos a /api/resumen.

Propuesto para evolución, no implementado: autenticación, importación mediante formulario,
varios productores concurrentes, migraciones y despliegue. El reto es un comparador de
informes de sólo lectura, tampoco implementado.
