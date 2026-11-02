# Revisión independiente del laboratorio 10

**Fecha:** 2 de noviembre de 2026, UTC. **Resultado:** APROBADO dentro del alcance revisado. No se detectaron problemas funcionales materiales pendientes en los contratos T01–T08 ni una aceptación indebida de su defecto didáctico.

## Alcance y método

Se revisaron el contrato previo, los dos operadores, las comprobaciones T01–T08 y RO01, el verificador autónomo, los registros de `ejecuciones/autonomo_01` y `ejecuciones/conjunto_01`, los archivos heredados y la documentación final del laboratorio. Se hizo una revisión complementaria de la vigencia de README, AGENTS, CONTINUIDAD, VERSIONES y PROCEDENCIA del repositorio.

La revisión del operador fue realizada por un agente distinto de su implementador. Es una revisión interna del proyecto sintético, no una certificación externa. Se leyeron código y archivos existentes, se contaron casos y se calcularon SHA-256 en memoria. No se ejecutó otra batería funcional, no se inició un servicio y no se modificó el laboratorio, su evidencia ni sus referencias Git. El manuscrito y el Word del capítulo 10 quedaron fuera de esta auditoría.

Los datos reproducibles de la revisión se conservan en `DATOS_REVISION_INDEPENDIENTE_LAB10.json`, `RECUENTO_INDEPENDIENTE_LAB10.json` y el resumen `REVISION_INDEPENDIENTE_LAB10.json`.

## Contrato, conservación y diferencia didáctica

La copia previa `CONTRATO_LABORATORIO_10_PREVIO.md` coincide byte a byte con `contexto/CONTRATO_AUTOMATIZACION.md` y con el SHA-256 declarado en PROCEDENCIA: `18eb14f8251d1179a009f008793023b61268db63faa44c4a713357fe25cc86fe`. No se sustituyó el contrato para acomodar los resultados.

Los 17 archivos de la solución 9 coinciden en cada uno de los tres estados del laboratorio 10. Base no añade archivos; propuesta y solución añaden exclusivamente `operar.py`. Los 71 archivos declarados heredados en PROCEDENCIA también coinciden con sus huellas. Para cada ejecución inspeccionada, los 75 archivos ejecutables, de datos y de web que aparecen en su registro de fuentes coinciden con los archivos actuales revisados.

La diferencia entre ambos operadores se concentra en la condición de continuación. La propuesta permite continuar cuando el importador devuelve código 1 y JSON `RECHAZADO`; la solución exige la importación confirmada. Los errores de precondición, las capturas, los tiempos límite y la protección de destinos son compartidos. No se transfieren al laboratorio 10 los fallos de seguridad admitidos únicamente en estados históricos del laboratorio 9.

## Revisión del comportamiento y las comprobaciones

| Caso | Observación que sustenta el criterio | Resultado de revisión |
|---|---|---|
| T01 | Ejecuta el operador como proceso; consulta después un snapshot real de SQLite y contrasta resumen, A03/ALFA=3 y habilitación de A02. | APROBADO |
| T02 | Compara el estado completo antes/después; exige salida 1, importación no confirmada, consulta NO EJECUTADO, ausencia de captura de consulta y resumen nulo. La propuesta devuelve 0 y activa la aserción. | APROBADO |
| T03 | Repite sobre la misma base con carpetas distintas, contrasta pares omitidos y bytes del primer recibo. | APROBADO |
| T04 | Comprueba rechazo por base ausente y ausencia de base y recibo creados. No se utiliza un catálogo alternativo. | APROBADO |
| T05 | Prueba destino existente y destino protegido; contrasta bytes de base, CSV y recibo previo, además de ausencia del destino protegido. | APROBADO |
| T06 | Compara la instantánea, su tamaño y SHA-256, la huella informada por el importador, códigos de ambos pasos, resumen consultado y hashes finales de capturas. Cambiar el CSV original después no modifica el recibo. | APROBADO |
| T07 | Ejecuta desde otro directorio y con espacios en las rutas; coloca un `persistencia.py` ajeno que terminaría con 97 si se seleccionara. Contrasta el resultado y la SQLite elegida. | APROBADO |
| T08 | Mantiene un servidor real sobre una base explícita; Chromium consulta antes y después de `execFileSync` del operador. Compara respuestas HTTP y DOM, y el resumen del operador con la segunda respuesta HTTP. | APROBADO |

Estas comprobaciones observan cambios y consecuencias del programa, en lugar de limitarse a verificar la presencia de una instrucción en su código. La constatación de un caso feliz no sustituye T02: propuesta también aprueba T08 con CSV válido, pero continúa equivocadamente cuando la importación se rechaza.

En la evidencia T02 de propuesta, el importador conserva código 1 y estado FALLIDO; la consulta devuelve 0, el resultado global es APROBADO y el catálogo sigue mostrando sólo A01. La batería conserva T02 FALLIDO por `AssertionError`. En solución, el recibo conserva importación FALLIDO, consulta NO EJECUTADO, código global 1 y resumen nulo; por eso la comprobación T02 aprueba. No se renombró el fallo ni se aceptó una excepción de infraestructura como sustituto del defecto.

## Recibos, capturas y tratamiento de límites

El operador lee una vez el CSV, reserva una carpeta nueva y guarda `entrada.csv` como bytes. El importador recibe esa instantánea. Ambos hijos se invocan mediante una lista de argumentos, con `shell=False`, el intérprete actual y un script resuelto desde el estado del operador. La validación de la base abre y cierra explícitamente la conexión heredada antes de importar.

Cada salida de proceso se escribe como bytes antes del saneamiento. El recolector conserva las huellas de captura y contrasta las finales. Los pasos sin ejecución no adquieren archivos ni hashes ficticios. Se recalcularon de forma independiente, sin reescribir archivos, las 116 huellas declaradas en el autónomo y las 272 del conjunto: todas coinciden con los bytes finales. Las 116 y 272 son cantidades observadas en esas ejecuciones, no constantes del contrato.

RO01 conserva una prueba de infraestructura, con dos estados como subcasos e inyección controlada de `OSError`. Su captura registra `Ran 1 test`, `OK` y código 0. Sus dos huellas coinciden. La prueba exige operación BLOQUEADA, consulta NO EJECUTADO, base sin cambios y ninguna captura inventada cuando el hijo no llegó a iniciarse. No es una incidencia real del equipo ni un noveno criterio T.

El tiempo límite de 20 segundos está implementado y un `TimeoutExpired` detiene el flujo conservando capturas parciales y BLOQUEADO. **No se provocó un timeout nuevo en las ejecuciones revisadas.** La comprobación de ese camino es estática en esta auditoría y no se presenta como una prueba dinámica adicional.

La importación y la consulta no comparten una transacción global. Una importación confirmada permanece aplicada si la consulta posterior falla. No observar confirmación tras una interrupción tampoco prueba que SQLite no cambió. El código y la documentación explican ambos límites; no se añaden reintentos, reversión global ni reinicialización.

## Resultados observados, sin duplicar cobertura

El recuento independiente de los archivos de casos del laboratorio 10 coincide en el autónomo y en su subconjunto de la ejecución conjunta:

| Estado de laboratorio 10 | APROBADO | FALLIDO | NO EJECUTADO |
|---|---:|---:|---:|
| Base | 74 | 0 | 8 |
| Propuesta | 81 | 1, T02 | 0 |
| Solución | 82 | 0 | 0 |

Son 33 baterías, 238 ejecuciones, 237 aprobaciones, un fallo didáctico y ocho casos NO EJECUTADO. Se contrastaron las identidades y los códigos de las 33 entradas de comandos; no sólo los totales declarados. La solución comprende 82 casos distintos correspondientes a 64 criterios.

El resumen conjunto observado registra diez laboratorios, 125 baterías, 1.043 ejecuciones, 1.018 aprobaciones, 25 fallos didácticos y cero bloqueos, con 56 NO EJECUTADO en baterías y diez criterios ausentes contabilizados aparte. Su resultado y el extremo a extremo del laboratorio 10 son APROBADO. Estos totales no se suman al autónomo ni a RO01 para aparentar más criterios distintos.

El entorno registrado es Linux, Python 3.12.14 y SQLite 3.53.1. T08 registra Node 24.22.1, Playwright 1.62.1 y Chromium 151.0.7922.34. La auditoría acredita consistencia de esos registros; no atribuye estas ejecuciones a Windows, WSL del autor ni a una herramienta comercial.

## Documentación y anonimización

README, contexto, trazabilidad, prompts y diferencias del laboratorio distinguen contrato, expectativas y resultados observados. El reto de revisión previa está rotulado como no implementado. Los prompts se identifican como didácticos y no se presentan como conversaciones históricas. La revisión editorial de los capítulos 1–10 permanece pendiente.

La inspección acotada de los archivos textuales de las dos ejecuciones no encontró las rutas de workspace, usuarios Linux/Windows, temporales del ejercicio sin alias o rutas WSL buscadas. La lectura manual del código y de los recibos seleccionados encontró únicamente nombres sintéticos y alias. Esta revisión acotada no demuestra ausencia universal de datos identificables ni sustituye la política de trabajar sólo con entradas sintéticas.

**Observación documental DOC-01, resuelta:** el README raíz mantenía una sección de situación remota antigua que podía confundirse con la vigencia y una fila que aún describía el incremento 9. Se avisó al coordinador sin editar el repositorio. El coordinador cambió la fila a laboratorio 10 y rotuló la sección como antecedente del cierre 9, con la base actual explícita. La corrección fue revalidada por lectura. CONTINUIDAD y VERSIONES ya separaban correctamente la vigencia de sus antecedentes.

## Límites y cierre de la revisión

No quedan hallazgos funcionales materiales ni observaciones documentales pendientes dentro del alcance inspeccionado. No se acredita prueba de timeout inducido, interrupción física, almacenamiento lleno, escritores concurrentes, autenticación, permisos multiusuario o servicio productivo. Tampoco se realizó análisis exhaustivo de mutaciones, fuzzing o una auditoría de sistemas externos.

El ensayo del ZIP, la aplicación del parche, las consultas remotas, las pruebas finales de los auxiliares de integración y la presentación del Word se registran en sus auditorías específicas. Esta revisión no los sustituye. La integración en `main`, commit, etiquetas y publicación continúan fuera de esta entrega. El manuscrito todavía requiere su propia revisión editorial.
