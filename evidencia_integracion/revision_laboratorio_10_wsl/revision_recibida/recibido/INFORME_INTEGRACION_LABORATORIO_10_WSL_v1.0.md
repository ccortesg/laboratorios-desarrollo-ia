# Integración del laboratorio 10 · revisión WSL v1.0

**Resultado técnico: APROBADO. Integración preparada para revisión.**

Evidencia nueva de esta sesión, cerrada a 2026-11-02T01:37:08.109715+00:00 (UTC).
Los capítulos 1–10 siguen pendientes de la revisión editorial del autor.

## Cambio e identidad

Se incorporó una sola vez el parche del paquete recibido: laboratorio 10, distribución,
contrato y contexto, operador con propuesta y solución, pruebas, evidencia aportada y
continuidad documental. El operador importa una instantánea CSV y consulta la misma
SQLite mediante dos CLI; la solución exige confirmación de importación antes de consultar.
El manuscrito y Word recibidos permanecen en el paquete editorial sin cambios.

| Identidad | Valor observado |
| --- | --- |
| Rama local | `codex/integracion-laboratorio-10` |
| Base utilizada y HEAD conservado | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| Árbol de la base | `790e875fc95495c39ea2b5ebe7621a4ae1afa30f` |
| Árbol preparado | `78b136a253cb3cb79143a0c81ee09f7892efa40f` |
| Rutas preparadas | 1372 |
| Índice y bytes de trabajo cotejados | 3660 archivos coincidentes |
| SHA-256 del parche | `60a0f636ebb254fb5e1a98724127780069209ee9d0f690966566dd8f80e2a808` |

La base local y remota coincidía exactamente con la del paquete. `git fetch --no-tags origin`
y las consultas actuales de referencias funcionaron en esta sesión. No hubo avances que
adaptar ni divergencias que resolver. Se eligió el prefijo local `codex/`; las rutas y los bytes
del incremento no se adaptaron. El manifiesto aprobó sus 624 archivos al inicio y al cierre.
El árbol coincide con el declarado por el paquete; su manifiesto y archivo de base no se modificaron.

`git apply --check --index` y la aplicación real terminaron con código 0. La aplicación emitió
34 avisos de espacios; se conservaron sus capturas y los bytes recibidos. La revisión posterior
`git diff --cached --check` aprobó, sin reescribir espacios ni terminadores de evidencia.

## Entorno y ejecución

| Componente | Observado |
| --- | --- |
| Sistema efectivo | Linux/WSL2, `6.18.54.1-microsoft-standard-WSL2` |
| Python utilizado | 3.12.16 (CPython) |
| SQLite | 3.53.1 |
| Git | 2.34.1 |
| Node / npm | 22.23.1 / 10.9.8 |
| Playwright | 1.62.1 |
| Chromium iniciado y utilizado | 151.0.7922.34 |

El `python3` predeterminado era 3.10.12. Se utilizó el intérprete aislado 3.12.16 ya existente
en `trabajo/runtime_lab09_wsl/python/cpython-3.12.16-linux-x86_64-gnu/bin/python3.12` para
los auxiliares y todas las pruebas funcionales y de infraestructura. No se modificó el Python del sistema.
`LAB06_CHROMIUM`, `NODE_PATH` y las variables Playwright inspeccionadas estaban ausentes.
Se ejecutaron `npm install --ignore-scripts --package-lock=false` y la instalación declarada
de Chromium desde el laboratorio 10. No se creó un package-lock versionado.

Se ejecutó `EJECUTAR_VERIFICACION.py` con repositorio, registro preparado y salida explícitos:
`verificacion_intento_01/`. El auxiliar contrastó HEAD, índice, rama, main, etiquetas y parche
antes de probar. Su resultado fue **APROBADO, código 0**. Hubo un solo intento integral;
no se ajustaron expectativas ni se repitieron pruebas para obtener ese resultado.

Los comandos, argumentos saneados, versiones, tiempos UTC, códigos de salida y SHA-256
capturados/finales están en `operaciones/` y en los `comandos.json` del auxiliar y del conjunto.
El comando interno del conjunto incluye `--navegador`; no se volvió a ejecutar sobre su salida.

## Resultados funcionales observados

**APROBADO:** 10 laboratorios, 125 baterías y 1043
ejecuciones: **1018 APROBADO y 25 FALLIDO didácticos**.
Bloqueos: 0. Errores de ejecución: 0.
Los 56 NO EJECUTADO en baterías y los
10 criterios ausentes de inicio 4 se registran aparte.
Un recuento independiente de los estados observados coincide con todos los totales y el patrón.

| Laboratorio 10 / estado | APROBADO | FALLIDO | NO EJECUTADO |
| --- | ---: | ---: | ---: |
| base | 74 | 0 | 8 |
| propuesta | 81 | 1 | 0 |
| solucion | 82 | 0 | 0 |

Los 74 heredados aprobaron en los tres estados. En base faltan únicamente los ocho T por
alcance. Propuesta falló exclusivamente T02 por AssertionError; T08 aprobó. Solución aprobó
82/82, incluido el recorrido real CSV → operador → CLI → SQLite → HTTP → Chromium.
También se comprobaron las referencias y el árbol actual reconstruido del laboratorio 4.

Los siguientes identificadores conservaron **FALLIDO**, por aserción, en sus estados didácticos:

| Batería | Identificadores FALLIDO observados |
| --- | --- |
| `laboratorio_01/inicial` | C04 |
| `laboratorio_03/defecto` | B05, B06 |
| `laboratorio_05/propuesta_resumen` | P04, P05 |
| `laboratorio_06/propuesta_navegador` | W05 |
| `laboratorio_07/propuesta_integracion` | I01, I07 |
| `laboratorio_08/propuesta_depuracion` | D03, D05, D08.a |
| `laboratorio_08/propuesta_depuracion_navegador` | D04 |
| `laboratorio_09/base_seguridad` | S02.a, S02.b, S02.c, S03, S04.a, S04.b, S05.a, S05.b |
| `laboratorio_09/base_seguridad_navegador` | S06 |
| `laboratorio_09/propuesta_seguridad` | S02.a, S02.b, S02.c |
| `laboratorio_10/propuesta_automatizacion` | T02 |

No hubo fallos adicionales. Los resultados de los laboratorios anteriores fueron ejecutados
de nuevo por este conjunto; no son sustituciones por los informes históricos suministrados.

## Infraestructura e integridad, separadas de los casos funcionales

| Grupo | Métodos observados | Resultado |
| --- | ---: | --- |
| recolector | 8 | APROBADO |
| evaluador_09 | 9 | APROBADO |
| evaluador_10 | 9 | APROBADO |
| recursos_sqlite | 4 | APROBADO |
| operador_recursos | 1 | APROBADO |

RO01 es un método con dos estados como subcasos. Inyecta OSError y comprueba un bloqueo
simulado al iniciar un hijo; no describe una incidencia real ni se suma a T01–T08.

| Comprobación de huellas | Resultado |
| --- | --- |
| Conjunto funcional, todas las declaradas | APROBADO: 272/272 |
| Revisión del auxiliar, todas las declaradas | APROBADO: 284/284 |
| Sesión completa, incluidos los comandos propios agregados | APROBADO: 340/340 |
| Bytes originales de las capturas de la revisión | APROBADO: 284 declaraciones cotejadas |

Se invocó el recolector vigente sobre la revisión y el conjunto sin fijar `--esperadas`.
Las cantidades anteriores son observadas, no constantes históricas. Las ocho pruebas del
recolector y su código se conservaron exactos. También se cotejó la distribución autónoma:
CRC correcto y sus 450 archivos idénticos a la copia integrada.
Ese cotejo de bytes no representa una segunda ejecución funcional autónoma.

Para conservar los bytes antes del saneamiento se utilizó un observador documentado en
`soporte_de_sesion/sitecustomize.py`: copia las salidas declaradas antes de llamar al cierre
original, con los mismos argumentos y resultado. No se modificó ninguna fuente versionada.
El alcance y el cotejo de cada captura están documentados; los fixtures de infraestructura
no se contabilizan como criterios funcionales adicionales.

Los originales con rutas locales permanecen fuera del envío compartible, en
`trabajo/integracion_10_wsl_20261102T005853Z_capturas_originales/`. El ZIP conserva las salidas saneadas, sus huellas
capturadas y finales y el inventario que demuestra la correspondencia de los bytes originales.
No se normalizaron LF/CRLF para hacer coincidir huellas ni se repararon evidencias históricas.

## Conservación y consultas finales

`main` y HEAD permanecen en `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3`. Las quince etiquetas históricas y todas las
referencias locales preexistentes conservan sus identidades. No existen las etiquetas previstas
`lab-10-v1.0` y `repositorio-v1.6`. No se crearon commits, no se integró en main, no se crearon
ni movieron etiquetas y no se hizo push.

La reconsulta remota final terminó a 2026-11-02T01:32:58.251228+00:00: main sigue en
`6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3`; no hubo avances y las etiquetas remotas se conservan.
El índice final conserva el árbol preparado y no hay cambios sin preparar ni archivos ajenos
sin seguimiento. Se cotejaron 2288 archivos versionados originales
protegidos y 3156 archivos de evidencia anterior en trabajo:
todos conservan sus bytes. Los modos de los originales versionados también se conservaron.
Los nueve archivos existentes modificados por el parche se distinguen explícitamente de los
protegidos. El inventario de contenido comenzó antes de aplicar; sus metadatos Git se leyeron
al terminar. `antes.json` acredita el estado inicial limpio y el cotejo con HEAD confirma los
bytes anteriores de esos nueve archivos. No se sustituye esa precisión temporal por una
afirmación de captura atómica.

## Límites y entrega

Windows nativo: **NO EJECUTADO**. Esta ejecución es WSL2 y no se atribuye a Windows.
CI remota, producción, nuevas sesiones Copilot/Grok Build y publicación: **NO EJECUTADO**.
No hay bloqueos técnicos pendientes dentro del alcance comprobado. No se acredita una
revisión editorial ni se redactó contenido adicional del libro.

Los escenarios son locales, sintéticos y secuenciales. No amplían el contrato a concurrencia,
fallos físicos o recuperación destructiva. RO01 no sustituye una prueba de agotamiento del
timeout. Una consulta fallida no revierte una importación ya confirmada.

La evidencia nueva se entrega aparte de los estados y evidencias históricos del parche.
El ZIP se crea con EMPAQUETAR_EVIDENCIA.py; su SHA-256 y la comprobación independiente del
CRC y manifiesto se entregan fuera del ZIP para evitar autorreferencias. El punto de cierre
es la rama local preparada para revisión. Los capítulos 1–10 permanecen pendientes del autor.
