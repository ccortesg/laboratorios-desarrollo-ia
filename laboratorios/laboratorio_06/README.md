# Laboratorio 6 · Del catálogo a una aplicación web local

**Versión 1.0 · 31 de octubre de 2026.** Proyecto sintético para el capítulo
«Grok Build: de la idea a una aplicación de extremo a extremo».

La aplicación permite elegir ALFA o BETA, buscar por parte del nombre y consultar
el resumen real de artículos disponibles. Reutiliza la solución del laboratorio 5.
El código y sus verificaciones se ejecutaron localmente durante esta entrega;
**no constituyen evidencia de generación o ejecución dentro de Grok Build**.
Los prompts incluidos son ejemplos didácticos preparados para el libro.

## 1. Qué necesitas

Para ejecutar la aplicación, la terminal heredada y las comprobaciones HTTP:

- Python 3.10 o posterior con su biblioteca estándar y SQLite.
- Un navegador local para la exploración manual.

La aplicación no instala paquetes Python, no requiere una cuenta comercial ni
consulta servicios externos. Node, Playwright y Chromium solo se necesitan para
automatizar W05–W06. La ejecución acreditada utilizó Linux, Python 3.12.14,
SQLite 3.53.1, Node 24.22.1, Playwright 1.62.1 y Chromium 156.0.8078.80.
La comprobación de este laboratorio en Windows queda **NO EJECUTADO** en esta
entrega; los comandos siguientes son compatibles con Git Bash y deben verificarse
en el equipo del lector. No se confunden con la ejecución Windows histórica del
laboratorio 5.

Descomprime el paquete y entra en la carpeta que contiene este README. En Git Bash,
abre una terminal en esa carpeta o utiliza `cd` con tu ubicación de extracción.
Verifica el intérprete:

```bash
python --version
```

Si tu instalación expone `python3` o `py -3`, sustituye `python` por ese comando
en las instrucciones. No es necesario copiar datos de otro laboratorio.

## 2. Arranque y primera consulta

```bash
python estados/solucion/servidor.py --puerto 8000
```

El proceso muestra una URL local. Abre `http://127.0.0.1:8000` en tu navegador.
El servidor solo escucha en el equipo local. Mantén esta terminal abierta mientras
usas la aplicación y detenlo con **Ctrl+C**. Si el puerto ya está ocupado, usa
`--puerto 8001` y abre la URL que imprima el proceso.

Consulta ALFA sin nombre: deben aparecer el almacén ALFA, total 1 y código A01.
Cambia a BETA y consulta: deben aparecer BETA, total 1 y A04. Busca `inexistente`:
debe verse un mensaje de ausencia, total 0 y una lista vacía, sin alerta de error.
El total cuenta artículos; no suma unidades de existencias.

Puedes reproducir el defecto didáctico arrancando en otro puerto:

```bash
python estados/propuesta/servidor.py --puerto 8001
```

En esa página, seleccionar BETA y consultar sigue produciendo ALFA y A01. El
formulario conserva la selección inicial en una variable; el servidor funciona
correctamente. En la solución se lee el selector dentro de cada envío. Detén
también ese servidor al terminar.

## 3. Estados y archivos relevantes

| Ubicación | Función |
| --- | --- |
| `ALCANCE.md` | Contrato registrado antes de implementar, con criterios y límites |
| `estados/base/` | Solución heredada completa; aún sin web |
| `estados/propuesta/` | Aplicación con defecto intencional de selección |
| `estados/solucion/` | Aplicación corregida |
| `contexto/` | Reglas, arquitectura, decisiones y continuidad |
| `prompts/` | Encargos didácticos insuficiente, de planificación, implementación y revisión |
| `pruebas_resumen.py` | Batería P heredada, sin cambios |
| `pruebas_http.py` | Cinco casos W01–W04 sobre HTTP real |
| `pruebas_navegador.cjs` | Tres casos W05–W06 sobre navegador real |
| `verificar.py` | Ejecuta capas, conserva evidencias y reconoce solo el fallo deliberado |
| `comparar.py`, `diferencias/` | Diferencias reproducibles entre estados |
| `PROCEDENCIA.json` | Huellas de los archivos heredados |
| `evidencia/` | Contrato previo, resultados y registros saneados |

No modifiques las referencias ni la evidencia original al practicar. Los nueve
archivos heredados son iguales en los tres estados. `pruebas_resumen.py` también
se conserva; se invoca con `--directorio` porque la base de este capítulo ya
contiene el resumen. El antiguo selector `--estado base` de esa batería describe
la base del capítulo 5 y no debe usarse para este nuevo punto de partida.

## 4. Verificación local sin Node

Desde la raíz del laboratorio, con cualquier servidor manual detenido si ya no
lo necesitas:

```bash
python verificar.py --salida trabajo/verificacion_python
```

El verificador inicia sus servidores en puertos libres y los cierra al terminar.
No utiliza el servidor que el lector dejó abierto. La carpeta de salida debe ser
nueva: para repetir, elige otro nombre y conserva el resultado anterior.

Este modo ejecuta 78 casos heredados y diez HTTP. Si todos cumplen las
expectativas, el alcance ejecutado queda APROBADO, con 88 aprobaciones. Registra
14 NO EJECUTADO: los cinco casos HTTP de base y los nueve de navegador de los
tres estados. El estado global y el extremo a extremo permanecen **NO EJECUTADO**.
La salida 0 solo indica que pasó el alcance solicitado. No acredita la interfaz.

Las cifras anteriores describen el patrón esperado de este modo. La evidencia
publicada corresponde a la ejecución completa con navegador de la sección 6.

Para observar una capa individual:

```bash
python estados/solucion/pruebas.py --json trabajo/heredados_solucion.json
python pruebas_resumen.py --directorio estados/solucion --json trabajo/resumen_solucion.json
python pruebas_http.py --estado solucion --json trabajo/http_solucion.json
```

Los primeros comandos comprueban 20 casos C/B/N y seis casos P. El último realiza
cinco peticiones a un servidor local real: ALFA, BETA con nombre normalizado,
consulta válida vacía y dos formas de omitir el almacén requerido.

## 5. Preparación opcional del navegador automatizado

Necesitas Node 20 o posterior y npm para instalar la dependencia de comprobación
en esta carpeta. `package.json` fija Playwright 1.62.1; no se entrega un lockfile,
por lo que la instalación recomendada es `npm install`, no `npm ci`.

```bash
node --version
npm --version
npm install --ignore-scripts
npx --no-install playwright install chromium
```

Estos comandos de preparación descargan dependencias públicas y el navegador;
requieren conectividad. La aplicación no los necesita para funcionar y las pruebas
solo se dirigen al servidor local. `node_modules/` queda fuera del material
versionado. No se instala nada globalmente. En un equipo sin acceso a esas
dependencias, registra BLOQUEADO para la automatización y conserva el trabajo
de dominio y HTTP que sí puedas ejecutar.

En un entorno que ya tenga un Chromium compatible se puede indicar su ejecutable
mediante `LAB06_CHROMIUM`. Si la variable no existe, el script usa la resolución
normal de Playwright; `PLAYWRIGHT_BROWSERS_PATH` puede indicar su caché estándar.
No hace falta usar estas variables con la instalación ordinaria del apartado.
`--node` permite elegir otro ejecutable Node para `verificar.py`.

## 6. Recorrido completo y evidencia

```bash
python verificar.py --navegador --salida trabajo/verificacion_completa
```

El resultado completo observado de esta entrega está en
`evidencia/ejecucion_local/resumen.json` y se explica en `evidencia/RESULTADOS.md`:

| Estado | Casos ejecutados | APROBADO | FALLIDO | NO EJECUTADO |
| --- | ---: | ---: | ---: | ---: |
| Base | 26 | 26 | 0 | 8 |
| Propuesta | 34 | 33 | 1 | 0 |
| Solución | 34 | 34 | 0 | 0 |
| Total | 94 | 93 | 1 | 8 |

El único FALLIDO es W05 de propuesta, una aserción que demuestra el defecto
intencional. La solución no tiene fallos pendientes dentro del alcance comprobado.
Los ocho casos W de base no se ejecutan porque allí aún no existe la aplicación
web. El patrón completo queda APROBADO porque coincide exactamente con estos
estados, no porque se hayan ocultado los fallos.

`verificar.py` devuelve 0 cuando el patrón solicitado se cumple, 1 por fallo
inesperado y 2 por bloqueo. Si falta el navegador después de solicitarlo, el global
queda BLOQUEADO. Una dependencia ausente no se cuenta como comprobación aprobada.
Cada batería individual devuelve 1 si falla: es lo esperado al ejecutar la prueba
de navegador contra propuesta sin el verificador que reconoce su finalidad.

W06.b provoca un fallo de transporte solo en el contexto de prueba mediante
`route.abort('failed')`. La aplicación no contiene una ruta para inducir errores.
La prueba comprueba que la alerta es visible y que los resultados anteriores están
ocultos; no certifica todos los modos posibles de fallo de red.

## 7. Crear y comprobar tu propia implementación

En Git Bash, con una carpeta de práctica que todavía no exista:

```bash
cp -R estados/base mi_practica
```

Lee el contexto y usa los prompts para implementar allí el servidor y la interfaz.
La base ya tiene todas las funciones de dominio. Cuando termines:

```bash
python mi_practica/pruebas.py --json trabajo/practica_heredados.json
python pruebas_resumen.py --directorio mi_practica --json trabajo/practica_resumen.json
python pruebas_http.py --directorio mi_practica --json trabajo/practica_http.json
python mi_practica/servidor.py --puerto 8000
```

El último comando deja el servidor activo. En una segunda terminal, situada en
la raíz del laboratorio, ejecuta la prueba contra **esa copia**:

```bash
node pruebas_navegador.cjs --url http://127.0.0.1:8000 --estado copia_del_lector --json trabajo/practica_navegador.json
```

Después detén el servidor con Ctrl+C. El nombre pasado a `--estado` en este script
es una etiqueta de evidencia; la URL decide qué aplicación se prueba. Si elegiste
otro puerto, cambia también la URL. No presentes una ejecución de las referencias
de `verificar.py` como prueba de tu propia implementación.

## 8. Revisar diferencias y continuar

Las diferencias incluidas se generan con:

```bash
python comparar.py --salida trabajo/diferencias_nuevas
```

Compara `propuesta_a_solucion.diff`: la corrección elimina la captura inicial y
lee la selección en cada submit. Base a solución añade cuatro archivos por estado
web y no modifica el dominio. Las diferencias son material de revisión; no son un
parche para aplicar sobre entregas anteriores.

El reto del capítulo consiste en agregar una mejora acotada en una copia, declarar
su contrato y comprobarla conservando los criterios existentes. No implementes
por inercia reservas, cantidades ni una aplicación completa. Cierra cada sesión
con la plantilla de `contexto/CONTINUIDAD.md` y conserva evidencia nueva.

## 9. Límites

Este paquete demuestra el recorrido local formulario → HTTP → dominio → respuesta.
No acredita uso real de Grok Build, despliegue, autorización, carga, seguridad
integral, compatibilidad con todos los navegadores ni accesibilidad exhaustiva.
Los cuatro artículos son suficientes para el contrato acotado; no representan
datos de una organización. Los capítulos anteriores continúan pendientes de
revisión editorial del autor. No se publica ni se sube nada desde el laboratorio.
