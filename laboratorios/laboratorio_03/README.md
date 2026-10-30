# Laboratorio 3

## Qué practicarás

Preparar encargos distintos para generar una búsqueda pequeña, refactorizarla conservando su comportamiento y diagnosticar un defecto intencional. El catálogo contiene únicamente datos sintéticos. El paquete es autónomo: no requiere descargar los laboratorios anteriores ni conectarse a servicios.

El alcance se fijó en [ALCANCE.md](ALCANCE.md) antes de implementar los módulos nuevos. La búsqueda recibe almacén y texto, consulta los artículos disponibles y filtra una subcadena del nombre. El contexto del capítulo 2 se mantiene y se actualiza en [CONTEXTO](contexto/CONTEXTO.md), [ARQUITECTURA](contexto/ARQUITECTURA.md), [DECISIONES](contexto/DECISIONES.md) y [CONTINUIDAD](contexto/CONTINUIDAD.md).

## Preparación

Descomprime el ZIP y abre una terminal dentro de `laboratorio_03`, junto a este README. Necesitas Python 3 con `sqlite3` y `unittest`; el entorno de referencia utiliza Python 3.12. Sólo se usa la biblioteca estándar. Si tu intérprete se invoca con `python3` o `py -3`, sustituye `python` de forma consistente.

```text
python --version
python -c "import sqlite3, unittest; print(sqlite3.sqlite_version)"
```

La versión efectivamente ejecutada está en `evidencia/entorno.json`. No se acredita compatibilidad comprobada con todas las instalaciones de Python. La ausencia de un módulo requerido impide iniciar la práctica y debe registrarse como BLOQUEADO.

## Estados conservados

| Estado | Qué existe | Ubicación |
| --- | --- | --- |
| base | Catálogo corregido del capítulo 2, todavía sin búsqueda | `laboratorio.py`, `datos/`, `solucion/consulta.sql` |
| generado | Primera función de búsqueda con el filtro integrado | `estados/generado.py` |
| refactorizado | Búsqueda que delega el filtro en una función pura | `estados/refactorizado.py` |
| defecto | Copia didáctica que omite transmitir el almacén | `estados/defecto.py` |
| corregido | Restaura la transmisión del almacén | `estados/corregido.py` |

Los estados son archivos independientes, no cambios que el lector deba aplicar sobre una instalación anterior. `solucion/consulta.sql` es la consulta base conservada; `corregido` es el estado final de la nueva búsqueda. La regla SQL no cambia en ninguno de los recorridos.

## Recorrido 1 Generar

Lee [el encargo de generación](prompts/01_generar.md), identifica qué falta en su primera versión y contrástala con la versión CLARO. Examina la base y la implementación nueva.

```text
python pruebas.py --estado base
python comparar.py --paso generar
python recorrido.py --estado generado --almacen ALFA --texto "  LoCaL  "
python pruebas.py --estado generado
```

La expectativa de la base es cuatro criterios aprobados y seis NO EJECUTADOS porque la búsqueda no existe. En `generado` la expectativa es diez aprobados. La demostración debe devolver el registro de A01.

## Recorrido 2 Refactorizar

Lee [el encargo de refactorización](prompts/02_refactorizar.md). Su contrato público conserva entradas, salidas, normalización y disponibilidad. La extracción permite reconocer por separado el acceso al catálogo y el filtro de una lista ya recibida.

```text
python comparar.py --paso refactorizar
python pruebas.py --estado refactorizado
```

La expectativa vuelve a ser diez criterios aprobados. No se modifican las pruebas para adaptarlas a la nueva estructura. Los casos finitos no demuestran equivalencia para toda entrada posible; la revisión de la diferencia complementa la evidencia.

## Recorrido 3 Depurar

Lee [el encargo de depuración](prompts/03_depurar.md). El defecto se introdujo expresamente para la enseñanza; no se presenta como una respuesta histórica de un asistente.

```text
python comparar.py --paso introducir-defecto
python recorrido.py --estado base --almacen BETA
python recorrido.py --estado defecto --almacen BETA --texto ""
python recorrido.py --estado defecto --almacen BETA --texto " OTRA "
python pruebas.py --estado defecto
```

La consulta base debe devolver A04. En el defecto se esperan A01 con texto vacío y lista vacía con `" OTRA "`, ambos contrarios al requisito de BETA. B05 y B06 deben resultar FALLIDOS. El código de salida 1 de esta batería es intencional. C01 a C04 y los cuatro B de ALFA pueden aprobar aunque la ubicación no se transmita correctamente.

```text
python comparar.py --paso corregir
python recorrido.py --estado corregido --almacen BETA --texto " OTRA "
python pruebas.py --estado corregido
```

La corrección debe devolver A04 y aprobar los diez criterios. El cambio de comportamiento consiste en transmitir `almacen` a la consulta, evitando activar su valor por defecto ALFA.

## Ejecutar y conservar todo el recorrido

```text
python verificar.py --salida mi_evidencia
```

`mi_evidencia` debe ser una carpeta que **no exista**. Para repetir, elige otro nombre. La carpeta `evidencia` ya contiene la ejecución distribuida y debe conservarse como referencia. Si la salida existe, el verificador devuelve BLOQUEADO y código 2 antes de iniciar las comprobaciones.

El verificador ejecuta las cinco baterías con el mismo intérprete, registra cinco observaciones diagnósticas y genera huellas de los archivos fuente. Sólo devuelve APROBADO y código 0 si se cumplen las expectativas exactas del recorrido. En el estado defectuoso exige fallos de aserción exclusivamente en B05 y B06; un error diferente no cuenta como demostración correcta. La valoración global no convierte esos dos fallos de comportamiento en aprobaciones.

Consulta `resumen.json`, los cinco `pruebas_<estado>.json`, `observacion_diagnostica.json`, `entorno.json` y `sha256_fuentes.json` dentro de la carpeta generada. Los archivos de texto conservan las salidas sin rutas del equipo. `evidencia/procedencia.json` documenta además la comparación efectuada al preparar el paquete con el laboratorio 2; reproducirlo no necesita ese laboratorio.

## Cómo interpretar los resultados

**APROBADO:** la comprobación realizada satisface su criterio. **FALLIDO:** se observó una discrepancia. **BLOQUEADO:** una precondición impidió continuar. **NO EJECUTADO:** la actividad no se realizó. Lee siempre el objeto y el motivo junto al estado.

Los prompts son ejemplos didácticos preparados para el libro. Los módulos son implementaciones de referencia y no transcripciones de una sesión comercial. Ejecutarlos localmente no acredita haberlos utilizado dentro de Codex, GitHub Copilot o Grok Build ni mide la eficacia de un prompt. El reto del capítulo, la lectura con usuarios y las evaluaciones productivas no forman parte de esta batería.

Los datos tienen un artículo disponible por almacén. Las pruebas comprueban los diez escenarios descritos, no el orden de varios resultados, todos los caracteres Unicode, tipos fuera del contrato, rendimiento, seguridad integral o concurrencia. La evolución de la aplicación completa permanece propuesta, no implementada.
