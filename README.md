# Laboratorios de desarrollo de software con IA

Material práctico de **Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro**.

Siete laboratorios locales sobre un catálogo ficticio de solicitudes e inventario. Practican una regla de negocio, la preparación de contexto, encargos de generación/refactorización/depuración, la revisión de cambios en Git, la comparación entre sugerencias y encargos delegados, el recorrido de una aplicación web local y la importación transaccional de datos externos sintéticos. Todos los datos y escenarios se crearon para el libro.

**Promesa:** aprende a transformar problemas de software en instrucciones claras, cambios revisables y resultados comprobables, aprovechando la IA desde tu primera sesión.

**Estado editorial:** los capítulos 1 a 7 siguen pendientes de revisión del autor. La integración de este repositorio no equivale a aprobación editorial. El manuscrito se conserva en las entregas editoriales del libro.

## Empieza aquí

Necesitas **Python 3.10 o posterior y Git** disponibles en tu terminal. La aplicación y las comprobaciones de dominio y HTTP utilizan Python estándar y SQLite en memoria. El laboratorio 6 añade navegador local; automatizar su interacción requiere Node, Playwright y Chromium. No se necesitan cuentas comerciales. La preparación opcional descarga esas herramientas; las comprobaciones se dirigen al equipo local.

Desde la raíz del repositorio:

```bash
python herramientas/verificar_todo.py
```

Si tu equipo utiliza `python3` o `py -3`, sustituye `python` de forma consistente. El autor ejecutó los seis laboratorios y la corrección del recolector en Windows con resultado APROBADO; el cierre está en `docs/estados/ESTADO_REPOSITORIO_v1.4.1.md`. La producción del laboratorio 7 se verifica en Linux y requiere una ejecución Windows posterior. Ambas evidencias tienen procedencia distinta.

El comando trabaja en copias temporales y crea `trabajo/verificacion/`. Si esa carpeta ya existe, utiliza otra:

```bash
python herramientas/verificar_todo.py --salida trabajo/verificacion_02
```

Sin `--navegador`, el comando anterior aprueba únicamente el alcance ejecutado; el global y el extremo a extremo quedan **NO EJECUTADO**. El código 0 no acredita la interfaz. Para solicitar el recorrido completo, prepara la dependencia opcional y ejecuta desde la raíz:

```bash
cd laboratorios/laboratorio_07
npm install --ignore-scripts --package-lock=false
npx --no-install playwright install chromium
cd ../..
python herramientas/verificar_todo.py --navegador --salida trabajo/verificacion_completa
```

Un resultado global **APROBADO** exige también la interacción real del navegador. Los fallos intencionales siguen **FALLIDO** en sus pruebas individuales; un fallo adicional hace fallar la verificación. El código 0 indica patrón satisfecho en el alcance solicitado, 1 FALLIDO y 2 BLOQUEADO. Usa siempre una carpeta nueva para la evidencia.

## El recorrido

| Laboratorio | Versión importada | Aprendizaje y materiales |
| --- | --- | --- |
| [01: del código al resultado](laboratorios/laboratorio_01/README.md) | 1.0 | Regla de disponibilidad por almacén, SQL inicial defectuoso, solución y C01–C04. |
| [02: contexto y arquitectura](laboratorios/laboratorio_02/README.md) | 1.0 | Encargo CLARO, reglas, mapa de responsabilidades, decisiones y continuidad. |
| [03: generar, refactorizar y depurar](laboratorios/laboratorio_03/README.md) | 1.0 | Cinco estados relacionados, prompts didácticos, diferencias y B01–B06. |
| [04: revisión sobre un repositorio](laboratorios/laboratorio_04/LEEME_REVISION_1_1.md) | 1.1 | Consulta exacta por código, N01–N10, historia Git y atribución del informe Codex. |
| [05: de la sugerencia al trabajo delegado](laboratorios/laboratorio_05/README.md) | 1.0 | Resumen del catálogo, terminal JSON, P01–P06 y revisión de un filtro omitido. |
| [06: aplicación web local](laboratorios/laboratorio_06/README.md) | 1.0 | Formulario, HTTP real, resumen, W01–W06 y defecto de selección detectado en navegador. |
| [07: datos e integraciones](laboratorios/laboratorio_07/README.md) | 1.0 | Contrato CSV, existencias absolutas, atomicidad, idempotencia e I01–I08. |

**Antes de abrir las instrucciones históricas del laboratorio 4:** su carpeta visible en `laboratorios/` es una instantánea de lectura sin un Git anidado. Sus README originales describen el paquete autónomo. Para seguir el ejercicio de ramas y diferencias, prepara la copia independiente como se indica a continuación.

## Practicar con Git en el laboratorio 4

```bash
python herramientas/preparar_laboratorio_04.py
cd trabajo/laboratorio_04
python verificar.py --salida evidencia_referencias
cd repositorio
python pruebas.py
git diff inicio solucion --
```

El preparador utiliza [el bundle local](historiales/README.md), crea un repositorio independiente en `trabajo/laboratorio_04/repositorio/` y conserva los commits originales. No requiere GitHub. Comprueba que sus 17 archivos coincidan con la solución visible, que las etiquetas sean las correctas y que el árbol esté limpio. No sobrescribe destinos existentes ni ejecuta pruebas funcionales por sí solo.

Para comenzar el ejercicio desde la base, dentro de esa copia nueva:

```bash
git switch -c practica inicio
python pruebas.py
```

En `inicio` se esperan diez aprobaciones; en `solucion`, veinte. Las pruebas del verificador histórico examinan copias de las etiquetas. Para verificar tus modificaciones actuales, ejecuta también `python pruebas.py` desde `repositorio/`. El separador `--` evita confundir la etiqueta `solucion` con la carpeta del mismo nombre.

## Resultados que debes reconocer

| Batería | Aprobados | Fallidos intencionales | No ejecutados en la batería |
| --- | ---: | --- | ---: |
| 01 / inicial | 3 | C04 | 0 |
| 01 / solución | 4 | Ninguno | 0 |
| 02 / solución | 4 | Ninguno | 0 |
| 03 / base | 4 | Ninguno | 6: B01–B06 |
| 03 / generado | 10 | Ninguno | 0 |
| 03 / refactorizado | 10 | Ninguno | 0 |
| 03 / defecto | 8 | B05 y B06 | 0 |
| 03 / corregido | 10 | Ninguno | 0 |
| 04 / inicio | 10 | Ninguno | 0 |
| 04 / solución | 20 | Ninguno | 0 |
| 04 / árbol actual recién reconstruido | 20 | Ninguno | 0 |
| 05 / base / heredados | 20 | Ninguno | 0 |
| 05 / base / resumen | 0 | Ninguno | 6: P01–P06 |
| 05 / propuesta / heredados | 20 | Ninguno | 0 |
| 05 / propuesta / resumen | 4 | P04 y P05 | 0 |
| 05 / solución / heredados | 20 | Ninguno | 0 |
| 05 / solución / resumen | 6 | Ninguno | 0 |

N01–N10 todavía no existen en `inicio` del laboratorio 4. El resumen los identifica por separado como **NO EJECUTADO**; no son diez pruebas omitidas por `unittest` ni diez aprobaciones.

El criterio central permanece igual: un artículo aparece sólo si está habilitado y tiene existencias positivas en el almacén seleccionado. La búsqueda por nombre y el detalle reutilizan esa regla. El laboratorio 6 añade una interfaz y un adaptador HTTP locales; no hay reservas, cantidades solicitadas ni servicios productivos.

## Practicar el laboratorio 5

El paquete autónomo está en `distribuciones/LABORATORIO_05_v1.0.zip`. Para practicar,
extráelo en una carpeta nueva dentro de `trabajo/`, conservando los archivos importados:

```bash
python -m zipfile -e distribuciones/LABORATORIO_05_v1.0.zip trabajo/practica_05
cd trabajo/practica_05/laboratorio_05
python verificar.py --salida mi_evidencia
```

Utiliza otro nombre si ya existe `trabajo/practica_05`. La solución aprueba 26 criterios.
La propuesta incorrecta conserva FALLIDO en P04/P05; la base omite seis criterios nuevos.
La verificación conjunta de los laboratorios 1–5 registró 17 baterías, 178 ejecuciones, 173 aprobaciones,
cinco fallos didácticos y 12 NO EJECUTADO en baterías. Los diez N ausentes en el inicio
del laboratorio 4 se registran aparte. Consulta la [comprobación de integración](evidencia_integracion/laboratorio_05_v1.0/COMPROBACION.json).

## Practicar el laboratorio 6

Extrae `distribuciones/LABORATORIO_06_v1.0.zip` en una carpeta nueva de `trabajo/` y sigue su README. Desde su raíz:

```bash
python estados/solucion/servidor.py --puerto 8000
```

Abre la URL local que muestra la terminal y detén el servidor con Ctrl+C. El catálogo consulta datos reales del ejercicio: ALFA devuelve A01; BETA, A04. La propuesta conserva ALFA de forma deliberada y falla W05; la solución lee el selector en cada envío. `total` cuenta artículos.

El laboratorio 6 registra 12 baterías y 94 ejecuciones: 93 APROBADO y W05 FALLIDO intencional en propuesta; ocho casos web NO EJECUTADO en base. La solución satisface 34 casos, correspondientes a 32 criterios: 26 heredados y seis W con subcasos. La verificación conjunta con navegador observó 29 baterías, 272 ejecuciones, 266 aprobaciones y seis fallos didácticos, más 20 NO EJECUTADO en baterías y diez N ausentes registrados aparte. La nueva evidencia está en `evidencia_integracion/laboratorio_06_v1.0/`.

## Practicar el laboratorio 7

El paquete autónomo está en `distribuciones/LABORATORIO_07_v1.0.zip`. Extráelo en una carpeta nueva de `trabajo/`. Desde su raíz:

```bash
python demostrar.py --estado solucion --archivo datos/actualizacion_valida.csv --repeticiones 2
python verificar.py --navegador --salida trabajo/verificacion_01
```

Prepara Playwright y Chromium como indica su README antes del segundo comando. Para una comprobación sin navegador, omite `--navegador`; el alcance de dominio y HTTP puede aprobar, pero el estado global queda NO EJECUTADO.

El CSV reemplaza cantidades por par artículo–almacén. La demostración mantiene una misma conexión en memoria para importar y consultar. A01/ALFA pasa de 7 a 5 y permanece en 5 al repetir; A02 sigue deshabilitado. La propuesta suma por error y debe fallar I01/I07. Los 17 casos I corresponden a ocho criterios y se ejecutan separados de los 34 casos heredados. La web anterior mantiene su origen predeterminado; no hay pantalla de importación ni persistencia entre ejecuciones.

Los resultados nuevos y sus límites están en `evidencia_integracion/laboratorio_07_v1.0/COMPROBACION.json`. El recolector verifica todas las huellas declaradas para cada ejecución. Sus ocho pruebas específicas se registran aparte de los totales funcionales.

## Dónde está cada cosa

| Ruta | Función |
| --- | --- |
| `laboratorios/` | Código, datos sintéticos, contexto, prompts y evidencia histórica importados sin modificar sus bytes. |
| `distribuciones/` | Los siete ZIP autónomos y sus SHA-256. |
| `historiales/` | Bundle con la historia original del ejercicio Git del laboratorio 4. |
| `herramientas/` | Preparación y verificación común; navegador automatizado opcional con dependencias de prueba. |
| `evidencia_integracion/2026-10-30/` | Registros históricos saneados de la primera integración. |
| `trabajo/` | Copias de práctica y resultados personales; Git la ignora. |
| [PROCEDENCIA.json](PROCEDENCIA.json) | Huellas por archivo y paquete; conserva los 310 archivos de los laboratorios 1–6 y añade la procedencia del laboratorio 7. |
| [VERSIONES.md](VERSIONES.md) | Correspondencia entre versiones y etiquetas del repositorio. |
| [CONTINUIDAD.md](CONTINUIDAD.md) | Decisiones, evidencia, pendientes y siguiente tarea. |

Los registros nuevos no sustituyen los históricos. El informe histórico saneado sobre Codex desktop conserva su procedencia. La evidencia nueva auditada en ESTADO_REPOSITORIO_v1.2.md corresponde a otra sesión y se conserva en las entregas del libro; no reemplaza la carpeta histórica aún ausente. Copilot permanece NO EJECUTADO en la producción del laboratorio 5.

## Trabajar con un asistente

Lee [AGENTS.md](AGENTS.md) y el paquete de contexto del laboratorio correspondiente. Aplica **CLARO**: Contextualiza, Limita, Acuerda aceptación, Resuelve en incrementos y Observa/documenta. Solicita un cambio pequeño con criterios explícitos, revisa diferencias y registra los comandos realmente ejecutados.

Los prompts incluidos son ejemplos didácticos. Ejecutar los scripts localmente no acredita uso de Codex, GitHub Copilot ni Grok Build.

## Situación remota y continuidad

La base remota confirmada para esta preparación es `6382e05846e149a9a72f7fdc56da48c37a873833`, con la corrección del recolector. `lab-06-v1.0` y `repositorio-v1.2` permanecen en `31aaf0615ed1be1d0b6718d57b3d6ddb974a0cbd`. La integración técnica 1.3 añade el laboratorio 7 en una copia local preparada; su subida y las etiquetas previstas `lab-07-v1.0` y `repositorio-v1.3` siguen pendientes. Consulta `docs/estados/ESTADO_REPOSITORIO_v1.5.md`; la versión del estado es independiente de la versión de integración.

## Distribución y revisión

La preparación corresponde a un repositorio privado de trabajo. No se ha elegido una licencia para distribución pública. El código del laboratorio es didáctico y no acredita preparación productiva. Para conocer qué quedó efectivamente verificado, consulta [CONTINUIDAD.md](CONTINUIDAD.md) y los registros de integración.
