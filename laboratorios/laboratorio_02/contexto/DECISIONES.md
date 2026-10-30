# Decisiones del laboratorio

Estos registros breves conservan motivos y consecuencias. **VIGENTE EN EL LABORATORIO** describe una decisión técnica aplicada en este ejercicio; no significa aprobación editorial del autor. **PROPUESTA** indica una alternativa pendiente de evaluación e implementación.

## D01 Ejecución local con base en memoria

**Estado:** VIGENTE EN EL LABORATORIO. **Fecha:** 30 de octubre de 2026.

**Contexto:** necesitamos un ejercicio pequeño, reproducible y autónomo que permita seguir una regla completa.

**Decisión:** conservar Python, SQLite en memoria y los datos sintéticos del piloto.

**Consecuencias:** cada consulta parte del mismo estado, sin servicios ni persistencia. La reproducción necesita Python con sus módulos requeridos. Esta elección no fija el stack de toda la aplicación futura ni acredita operación productiva.

## D02 Conservar la regla y sus comprobaciones

**Estado:** VIGENTE EN EL LABORATORIO. **Fecha:** 30 de octubre de 2026.

**Contexto:** el objetivo del capítulo 2 es preparar contexto y arquitectura sobre un comportamiento ya corregido.

**Decisión:** mantener los tres SQL y las cuatro funciones de prueba del piloto. El ejecutor admite únicamente la versión `solucion`; se conserva la opción explícita `--version solucion` para mantener continuidad con los comandos anteriores.

**Consecuencias:** el lector puede relacionar requisito, consulta y prueba sin una modificación funcional adicional. Los resultados esperados permanecen iguales. La consulta defectuosa del capítulo 1 no forma parte de este paquete.

## D03 Documentar la evolución antes de elegir tecnología

**Estado:** PROPUESTA para una entrega futura. **Fecha:** 30 de octubre de 2026.

**Contexto:** la aplicación conductora podría requerir una interfaz y una frontera de servicio cuando se definan nuevas funciones.

**Decisión propuesta:** evaluar esa separación después de precisar usuarios, entradas, errores, persistencia y criterios de aceptación. No elegir ahora un framework ni introducir una dependencia.

**Consecuencias previstas:** la arquitectura futura deberá revisarse con sus requisitos. El laboratorio actual sigue siendo local. Esta propuesta no está implementada ni comprobada.

## Cómo actualizar estos registros

Si una decisión cambia, conserva su motivo original y marca qué registro la sustituye. Diferencia una observación del código, una elección de implementación y una propuesta. No reescribas una alternativa pendiente como si siempre hubiera sido parte del sistema.
