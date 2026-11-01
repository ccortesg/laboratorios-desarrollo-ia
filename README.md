# Laboratorios de desarrollo de software con IA

**Cierre del laboratorio 9 preparado, publicación pendiente:** revisión WSL incorporada; estados [libro 1.8.2](docs/estados/ESTADO_DEL_LIBRO_v1.8.2.md) y [repositorio 1.7.2](docs/estados/ESTADO_REPOSITORIO_v1.7.2.md). Consulta [la revisión](evidencia_integracion/revision_laboratorio_09_wsl/README.md) y la [continuidad vigente](CONTINUIDAD.md). El encargo del autor autoriza el commit y la publicación limitada; el comprobante posterior se entrega fuera del commit que acredita.

**Actualización técnica del laboratorio 8:** distribución [1.0.1](distribuciones/LABORATORIO_08_v1.0.1.zip), con cierre explícito de SQLite en las pruebas. La ejecución Windows original falló y se conserva; la corrección fue ejecutada por el autor y su evidencia está auditada como APROBADO. Consulta [continuidad vigente](CONTINUIDAD.md).

Material práctico de **Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro**.

Nueve laboratorios locales sobre un catálogo ficticio de solicitudes e inventario. Practican una regla de negocio, la preparación de contexto, encargos de generación/refactorización/depuración, la revisión de cambios en Git, la comparación entre sugerencias y encargos delegados, el recorrido de una aplicación web local, la importación transaccional de datos externos sintéticos la investigación del origen de datos entre procesos y una política de entrada HTTP con casos negativos y recuperación. Todos los datos y escenarios se crearon para el libro.

**Promesa:** aprende a transformar problemas de software en instrucciones claras, cambios revisables y resultados comprobables, aprovechando la IA desde tu primera sesión.

**Estado editorial:** los capítulos 1 a 9 siguen pendientes de revisión del autor. La integración de este repositorio no equivale a aprobación editorial. El manuscrito se conserva en las entregas editoriales del libro.

## Empieza aquí

Para el conjunto completo necesitas **Python 3.11 o posterior y Git** disponibles en tu terminal. La aplicación y las comprobaciones de dominio y HTTP utilizan Python estándar y SQLite. El laboratorio 8 añade un modo explícito de persistencia en archivo; los recorridos anteriores conservan su origen en memoria. La automatización de navegador requiere Node, Playwright y Chromium. No se necesitan cuentas comerciales. La preparación descarga esas herramientas; las comprobaciones se dirigen al equipo local.

Desde la raíz del repositorio:

```bash
python herramientas/verificar_todo.py
```

Si tu equipo utiliza `python3` o `py -3`, sustituye `python` de forma consistente. El autor ejecutó los laboratorios 1–7 en Windows con resultado APROBADO y publicó el cierre del 7. Lo acredita `docs/estados/ESTADO_REPOSITORIO_v1.5.2.md`; ese pendiente está cerrado. La producción del laboratorio 8 se verificó en Linux y su corrección se ejecutó después en Windows por el autor. La revisión aprobada está en [evidencia del cierre](evidencia_integracion/cierre_laboratorio_08_windows/README.md); las dos ejecuciones se conservan por separado.

El comando trabaja en copias temporales y crea `trabajo/verificacion/`. Si esa carpeta ya existe, utiliza otra:

```bash
python herramientas/verificar_todo.py --salida trabajo/verificacion_02
```

Sin `--navegador`, el comando anterior aprueba únicamente el alcance ejecutado; el global y el extremo a extremo quedan **NO EJECUTADO**. El código 0 no acredita la interfaz. Para solicitar el recorrido completo, prepara la dependencia opcional y ejecuta desde la raíz:

```bash
cd laboratorios/laboratorio_09
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
| [08: depuración con evidencia](laboratorios/laboratorio_08/README.md) | 1.0.1 | Persistencia explícita, procesos separados, origen efectivo, hipótesis discriminantes y D01–D08. |
| [09: confiabilidad y seguridad](laboratorios/laboratorio_09/README.md) | 1.0 | Política de query HTTP, límites de confianza, casos negativos, recuperación y S01–S08. |

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

## Practicar el laboratorio 8

Extrae `distribuciones/LABORATORIO_08_v1.0.1.zip` en una carpeta nueva y sigue su README. La distribución 1.0 se conserva como antecedente. Desde la raíz del laboratorio autónomo, después de preparar el navegador:

```bash
python verificar.py --navegador --salida trabajo/verificacion_01
```

La base conserva la solución del 7. Propuesta y solución añaden los comandos `iniciar`, `importar` y `consultar`, junto con el parámetro `--base` del servidor. La inicialización es explícita y rechaza destinos ocupados. Importación, consulta y HTTP abren el archivo existente; nunca lo vuelven a sembrar. El diagnóstico opcional diferencia el origen configurado de la conexión efectivamente utilizada.

El escenario D04 mantiene un servidor en funcionamiento, observa la pantalla inicial, ejecuta el importador CLI como otro proceso y vuelve a consultar desde el navegador. Después del CSV, ALFA muestra A01 y A03; BETA queda vacío. Las cantidades exactas se comprueban en SQLite: el resumen continúa contando artículos. La propuesta omite propagar la conexión y conserva exactamente FALLIDO en D03, D04, D05 y D08.a. La solución conserva los 51 casos anteriores y satisface los once D. Los once D de base están NO EJECUTADO por alcance.

La evidencia original del laboratorio está dentro de su distribución y en `evidencia_integracion/laboratorio_08_v1.0/`. La ejecución Windows corregida del 8, sus auditorías y el ZIP recibido están en `evidencia_integracion/cierre_laboratorio_08_windows/`. La evidencia Windows del 7 sigue separada en `evidencia_integracion/cierre_laboratorio_07_confirmado/`. Cada ejecución conserva su atribución; ninguna acredita por sí misma uso de una herramienta comercial.

## Practicar el laboratorio 9

Extrae `distribuciones/LABORATORIO_09_v1.0.zip` en una carpeta nueva. Prepara su dependencia de navegador y ejecuta `python -B verificar.py --navegador --salida trabajo/una_ejecucion_nueva` desde la raíz extraída.

La base conserva los 62 casos de la solución corregida del 8. La política nueva valida la query antes de consultar el catálogo: rechaza repeticiones, claves adicionales, codificación inválida y tamaños fuera del contrato. La propuesta pierde duplicados al construir un diccionario prematuramente; la solución los detecta cuando todavía existen los pares originales.

El autónomo registró APROBADO: 27 baterías, 222 ejecuciones, 210 APROBADO y doce FALLIDO previstos; 54/54 huellas finales. Los nueve fallos de base pertenecen a la política nueva, y los tres de propuesta son exclusivamente S02.a/S02.b/S02.c. La solución aprobó 74/74. El ZIP descomprimido reprodujo esos resultados. La evidencia conserva un intento con dos errores inesperados del instrumento S06 y su corrección, sin convertirlos en fallos didácticos.

El conjunto nuevo de nueve laboratorios obtuvo APROBADO: 92 baterías, 805 ejecuciones, 781 APROBADO y 24 FALLIDO didácticos, cero bloqueos, 48 NO EJECUTADO en baterías y diez ausentes aparte; 156/156 huellas funcionales. Las ocho pruebas del recolector, nueve del evaluador y cuatro de recursos SQLite se registran separadamente. La ejecución de esta entrega es Linux; no acredita Windows ni uso de herramientas comerciales.

Consulta `contexto/CONTRATO_SEGURIDAD.md` dentro del laboratorio y `evidencia_integracion/laboratorio_09_v1.0/` para los comandos y resultados. La política y los ensayos son acotados a este proyecto local; no constituyen una evaluación integral de seguridad productiva.

## Dónde está cada cosa

| Ruta | Función |
| --- | --- |
| `laboratorios/` | Código, datos sintéticos, contexto, prompts y evidencia histórica importados sin modificar sus bytes. |
| `distribuciones/` | Los paquetes autónomos actuales, versiones históricas y sus SHA-256. |
| `historiales/` | Bundle con la historia original del ejercicio Git del laboratorio 4. |
| `herramientas/` | Preparación y verificación común; navegador automatizado opcional con dependencias de prueba. |
| `evidencia_integracion/2026-10-30/` | Registros históricos saneados de la primera integración. |
| `trabajo/` | Copias de práctica y resultados personales; Git la ignora. |
| [PROCEDENCIA.json](PROCEDENCIA.json) | Huellas por archivo y paquete; las entradas anteriores se conservan y se añade la del laboratorio 9. |
| [VERSIONES.md](VERSIONES.md) | Correspondencia entre versiones y etiquetas del repositorio. |
| [CONTINUIDAD.md](CONTINUIDAD.md) | Decisiones, evidencia, pendientes y siguiente tarea. |

Los registros nuevos no sustituyen los históricos. El informe histórico saneado sobre Codex desktop conserva su procedencia. La evidencia nueva auditada en ESTADO_REPOSITORIO_v1.2.md corresponde a otra sesión y se conserva en las entregas del libro; no reemplaza la carpeta histórica aún ausente. Copilot permanece NO EJECUTADO en la producción del laboratorio 5.

## Trabajar con un asistente

Lee [AGENTS.md](AGENTS.md) y el paquete de contexto del laboratorio correspondiente. Aplica **CLARO**: Contextualiza, Limita, Acuerda aceptación, Resuelve en incrementos y Observa/documenta. Solicita un cambio pequeño con criterios explícitos, revisa diferencias y registra los comandos realmente ejecutados.

Los prompts incluidos son ejemplos didácticos. Ejecutar los scripts localmente no acredita uso de Codex, GitHub Copilot ni Grok Build.

## Situación remota y continuidad

Base registrada: `9212ee99b88f70f0b289837b88d6bbf34da91a52`, árbol `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0`. La consulta del 1 de noviembre de 2026 a las 21:50:33 UTC confirmó main, lab-08-v1.0 y repositorio-v1.4 en ese commit y las trece etiquetas intactas. El cierre del laboratorio 8 está publicado; se incorporan sus estados posteriores 1.7.4/1.6.4 y su revisión, conservando la precisión de entorno WSL y el antecedente funcional Windows.

La integración técnica 1.5 está auditada en WSL sobre `251105483bc5bef040c57dc3a036d5bc3a7e0da0`. El cierre documental incorpora los estados 1.8.1/1.7.1 exactos y prepara 1.8.2/1.7.2. La publicación autorizada de main y únicamente `lab-09-v1.0`/`repositorio-v1.5` se comprobará después, conservando todas las referencias históricas; sus comprobantes quedarán fuera del commit que acreditan. Las 805 ejecuciones son evidencia anterior: el cierre documental ejecuta las ocho pruebas del recolector y comprueba identidad y huellas. Las versiones documentales y técnicas son independientes; capítulos 1–9 pendientes de revisión editorial.

## Distribución y revisión

La preparación corresponde a un repositorio privado de trabajo. No se ha elegido una licencia para distribución pública. El código del laboratorio es didáctico y no acredita preparación productiva. Para conocer qué quedó efectivamente verificado, consulta [CONTINUIDAD.md](CONTINUIDAD.md) y los registros de integración.
