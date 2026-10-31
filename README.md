# Laboratorios de desarrollo de software con IA

Material práctico de **Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro**.

Cinco laboratorios locales sobre un catálogo ficticio de solicitudes e inventario. Practican una regla de negocio, la preparación de contexto, encargos de generación/refactorización/depuración, la revisión de cambios en Git y la comparación entre sugerencias y encargos delegados. Todos los datos y escenarios se crearon para el libro.

**Promesa:** aprende a transformar problemas de software en instrucciones claras, cambios revisables y resultados comprobables, aprovechando la IA desde tu primera sesión.

**Estado editorial:** los capítulos 1 a 5 siguen pendientes de revisión del autor. La integración de este repositorio no equivale a aprobación editorial. El manuscrito se conserva en las entregas editoriales del libro.

## Empieza aquí

Necesitas **Python 3.10 o posterior y Git** disponibles en tu terminal. Los ejercicios utilizan la biblioteca estándar de Python y SQLite en memoria; no requieren instalar paquetes, configurar cuentas comerciales ni acceder a servicios externos.

Desde la raíz del repositorio:

```bash
python herramientas/verificar_todo.py
```

Si tu equipo utiliza `python3` o `py -3`, sustituye `python` de forma consistente. La ejecución observada de esta integración fue en Linux; la compatibilidad con Windows nativo todavía no se ejecutó.

El comando trabaja en copias temporales y crea `trabajo/verificacion/`. Si esa carpeta ya existe, utiliza otra:

```bash
python herramientas/verificar_todo.py --salida trabajo/verificacion_02
```

Un resultado global **APROBADO** significa que cada estado reproduce exactamente el patrón previsto. Los fallos intencionales se conservan como **FALLIDO** en sus pruebas individuales; cualquier fallo adicional hace fallar la verificación. Los códigos del comando común son 0 para APROBADO, 1 para FALLIDO y 2 para BLOQUEADO.

## El recorrido

| Laboratorio | Versión importada | Aprendizaje y materiales |
| --- | --- | --- |
| [01: del código al resultado](laboratorios/laboratorio_01/README.md) | 1.0 | Regla de disponibilidad por almacén, SQL inicial defectuoso, solución y C01–C04. |
| [02: contexto y arquitectura](laboratorios/laboratorio_02/README.md) | 1.0 | Encargo CLARO, reglas, mapa de responsabilidades, decisiones y continuidad. |
| [03: generar, refactorizar y depurar](laboratorios/laboratorio_03/README.md) | 1.0 | Cinco estados relacionados, prompts didácticos, diferencias y B01–B06. |
| [04: revisión sobre un repositorio](laboratorios/laboratorio_04/LEEME_REVISION_1_1.md) | 1.1 | Consulta exacta por código, N01–N10, historia Git y atribución del informe Codex. |
| [05: de la sugerencia al trabajo delegado](laboratorios/laboratorio_05/README.md) | 1.0 | Resumen del catálogo, terminal JSON, P01–P06 y revisión de un filtro omitido. |

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

El criterio central permanece igual: un artículo aparece sólo si está habilitado y tiene existencias positivas en el almacén seleccionado. La búsqueda por nombre y el detalle reutilizan esa regla. No hay reservas, cantidades solicitadas, frontend ni servicios productivos.

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
La verificación conjunta ampliada espera 17 baterías, 178 ejecuciones, 173 aprobaciones,
cinco fallos didácticos y 12 NO EJECUTADO en baterías. Los diez N ausentes en el inicio
del laboratorio 4 se registran aparte. Consulta la [comprobación de integración](evidencia_integracion/laboratorio_05_v1.0/COMPROBACION.json).

## Dónde está cada cosa

| Ruta | Función |
| --- | --- |
| `laboratorios/` | Código, datos sintéticos, contexto, prompts y evidencia histórica importados sin modificar sus bytes. |
| `distribuciones/` | Los cinco ZIP autónomos originales y sus SHA-256. |
| `historiales/` | Bundle con la historia original del ejercicio Git del laboratorio 4. |
| `herramientas/` | Preparación y verificación común, sin dependencias externas. |
| `evidencia_integracion/2026-10-30/` | Registros saneados de la nueva ejecución local de integración. |
| `trabajo/` | Copias de práctica y resultados personales; Git la ignora. |
| [PROCEDENCIA.json](PROCEDENCIA.json) | Huellas de los 198 archivos importados y de los paquetes originales. |
| [VERSIONES.md](VERSIONES.md) | Correspondencia entre versiones y etiquetas del repositorio. |
| [CONTINUIDAD.md](CONTINUIDAD.md) | Decisiones, evidencia, pendientes y siguiente tarea. |

Los registros nuevos no sustituyen los históricos. El informe histórico saneado sobre Codex desktop conserva su procedencia. La evidencia nueva auditada en ESTADO_REPOSITORIO_v1.2.md corresponde a otra sesión y se conserva en las entregas del libro; no reemplaza la carpeta histórica aún ausente. Copilot permanece NO EJECUTADO en la producción del laboratorio 5.

## Trabajar con un asistente

Lee [AGENTS.md](AGENTS.md) y el paquete de contexto del laboratorio correspondiente. Aplica **CLARO**: Contextualiza, Limita, Acuerda aceptación, Resuelve en incrementos y Observa/documenta. Solicita un cambio pequeño con criterios explícitos, revisa diferencias y registra los comandos realmente ejecutados.

Los prompts incluidos son ejemplos didácticos. Ejecutar los scripts localmente no acredita uso de Codex, GitHub Copilot ni Grok Build.

## Distribución y revisión

La preparación corresponde a un repositorio privado de trabajo. No se ha elegido una licencia para distribución pública. El código del laboratorio es didáctico y no acredita preparación productiva. Para conocer qué quedó efectivamente verificado, consulta [CONTINUIDAD.md](CONTINUIDAD.md) y los registros de integración.
