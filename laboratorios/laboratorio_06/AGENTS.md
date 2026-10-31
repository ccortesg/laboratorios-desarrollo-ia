# Instrucciones para trabajar en este laboratorio

Todo el proyecto es sintético. Lee `ALCANCE.md`, `contexto/CONTEXTO.md`,
`contexto/ARQUITECTURA.md`, `contexto/DECISIONES.md` y `contexto/CONTINUIDAD.md`
antes de proponer modificaciones. Describe el plan, sus archivos y sus criterios.

Conserva las referencias de `estados/` y la evidencia histórica. Trabaja en una
copia propia, por ejemplo `mi_practica/`, y registra resultados nuevos en una
carpeta distinta de `trabajo/`. No reescribas expectativas para hacer pasar una
implementación. El verificador de referencia comprueba los estados incluidos;
una modificación en `mi_practica/` requiere comprobar expresamente esa copia.

El incremento vigente es una consulta web local. Reutiliza `resumir_catalogo` y
mantén C01–C04, B01–B06, N01–N10 y P01–P06. No dupliques la regla de disponibilidad
en JavaScript. No añadas servicios externos, usuarios, datos reales, pagos,
reservas, cantidades solicitadas ni despliegues. Sirve únicamente los recursos
permitidos y escucha en la interfaz local.

Los únicos fallos esperados del laboratorio 6 son W05 en `estados/propuesta`.
La base no incorpora web: sus ocho casos W son NO EJECUTADO. La solución debe
aprobar todos sus casos. Sin navegador real no se declara verificado el recorrido
completo. Una dependencia ausente es BLOQUEADO si se intentó usarla; una tarea
no intentada es NO EJECUTADO.

No atribuyas el código o una prueba local a Grok Build. Los prompts son ejemplos
didácticos. Cualquier interacción comercial necesita evidencia propia. No
accedas a sistemas privados ni publiques fuera de este entorno. Al terminar,
entrega diferencias, comandos, resultados observados y límites de verificación.
