# Decisiones y continuidad del laboratorio 4

**Fecha:** 30 de octubre de 2026. VIGENTE EN EL LABORATORIO describe una decisión aplicada al ejercicio, no una aprobación editorial del autor. PROPUESTA identifica trabajo futuro sin implementar. Se conservan los motivos relevantes del capítulo 2 y se registra la ampliación de alcance.

## D01 Ejecución local con base en memoria

**Estado:** VIGENTE EN EL LABORATORIO, conservada del capítulo 2.

**Contexto:** la práctica debe ser pequeña, autónoma y reproducible. **Decisión:** conservar Python, SQLite en memoria y los datos sintéticos originales. **Consecuencia:** cada consulta reconstruye los datos; no hay servicios ni persistencia. La elección no fija el stack futuro ni acredita uso productivo.

## D02 Conservación de la regla y las comprobaciones

**Estado:** CONSERVADA EN SU REGLA; alcance documental del capítulo 2 ampliado por D04.

**Decisión original:** conservar la regla, los tres SQL y las cuatro funciones de prueba para preparar contexto sin ampliar funciones. **Continuidad:** los SQL y el ejecutor permanecen byte a byte; C01 a C04 conservan su texto y ahora también atraviesan la búsqueda. El límite de no añadir funciones correspondía a la etapa anterior; el encargo actual autoriza el incremento de D04. No se reinterpreta la etapa anterior como si ya lo hubiera implementado.

## D03 Evaluar una evolución antes de elegir tecnología

**Estado:** PROPUESTA, conservada y NO IMPLEMENTADA.

**Contexto:** la aplicación conductora podría necesitar interfaz y frontera de servicio. **Propuesta:** evaluar esa separación después de definir usuarios, entradas, errores, persistencia y aceptación. **Consecuencia prevista:** la arquitectura futura deberá revisarse con esos requisitos. La búsqueda local no resuelve esa elección.

## D04 Añadir búsqueda sobre el resultado disponible

**Estado:** VIGENTE EN EL LABORATORIO; amplía el alcance de D02 para la etapa 3.

**Contexto:** se necesita una función pequeña para comparar encargos de generación, refactorización y depuración. **Decisión:** filtrar por subcadena del nombre después de consultar disponibilidad, sin cambiar SQL ni datos. El contrato de la etapa 3 se conserva en su entrega original; las reglas vigentes de búsqueda figuran en CONTEXTO. **Consecuencia:** el comportamiento es fácil de seguir y conserva la regla en un único lugar; no se estudian volumen ni rendimiento de una búsqueda productiva.

## D05 Separar responsabilidades mediante una refactorización acotada

**Estado:** VIGENTE EN EL LABORATORIO.

**Contexto:** la función generada mezcla la consulta y la transformación de resultados. **Decisión:** extraer `filtrar_por_nombre` y mantener intacta la interfaz pública. **Consecuencia:** el lector puede revisar qué operación depende de datos y cuál recibe una lista. Esta decisión didáctica no supone que todo bloque corto deba extraerse ni que el cambio mejore el rendimiento.

## D06 Preservar estados y comprobar el fallo exacto

**Estado:** HISTÓRICA DEL LABORATORIO 3. Sus archivos y evidencia permanecen en aquella entrega; este repositorio parte únicamente de su estado corregido.

**Contexto:** la depuración necesita un defecto reproducible y una corrección comparables. **Decisión:** conservar módulos separados, introducir expresamente la omisión del almacén y exigir que B05 y B06 fallen por aserción antes de aceptar el recorrido. **Consecuencia:** `defecto` sigue siendo incorrecto aunque el verificador global apruebe la demostración. `corregido` debe satisfacer toda la batería. Las diferencias muestran también la introducción intencional del defecto.

## D07 Conservar evidencia nueva sin sobrescribir la anterior

**Estado:** VIGENTE EN EL LABORATORIO, continuidad de la práctica del capítulo 2.

El verificador exige una carpeta nueva. Se registran ejecución local, expectativas, estados y huellas por separado. Las pruebas no evalúan semánticamente prompts ni documentación. Una sesión comercial o una lectura con usuarios necesitaría su propia evidencia.

## D08 Crear un repositorio local con un punto de partida identificable

**Estado:** VIGENTE EN EL LABORATORIO 4. Se conserva el catálogo corregido como `catalogo.py`, se adapta el montaje de la batería y se mantienen los diez métodos de prueba. La etiqueta `inicio` incluye el contrato previo. El historial usa exclusivamente identidad sintética y no tiene remotos. Las referencias distribuidas y el árbol actual deben revisarse por separado.

## D09 Añadir consulta por código exacto

**Estado:** IMPLEMENTADO EN SOLUCION; el contrato permanece en inicio. `ALCANCE.md` define N01–N10. La función consulta disponibilidad y devuelve el registro exacto o `None`; no hereda la normalización de la búsqueda por nombre. Esta elección usa el reto anterior como incremento nuevo, sin afirmar que ya estuviera ejecutado en el capítulo 3.

## D10 Distinguir evidencia local y uso de Codex

**Estado:** VIGENTE EN EL LABORATORIO 4. La modalidad y el acceso se comprueban antes de atribuir una sesión. Los prompts son didácticos; los registros de pruebas locales no acreditan uso comercial. El verificador del paquete prueba commits etiquetados; las ediciones del lector se comprueban con `python pruebas.py` dentro del repositorio.
