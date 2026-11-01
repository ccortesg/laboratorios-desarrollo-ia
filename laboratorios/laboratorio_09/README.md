# Laboratorio 9 · Confiabilidad y seguridad del catálogo

Versión 1.0. Material autónomo, sintético y local. Descomprime el paquete y trabaja desde esta carpeta. La aplicación usa Python estándar y SQLite; Node y Playwright sólo intervienen en las comprobaciones de navegador. No requiere cuentas, claves ni servicios externos.

## Qué cambia

La solución corregida del laboratorio 8 es la base de este ejercicio. Ya conserva el recorrido CSV → importador CLI → SQLite persistente → HTTP → navegador. El incremento define una frontera de entrada explícita para `GET /api/resumen`: claves admitidas, repetición, sintaxis, UTF-8 y límites pequeños de tamaño. El catálogo, las existencias, la importación y la pantalla conservan sus reglas.

Lee primero `contexto/CONTRATO_SEGURIDAD.md`. Se escribió antes de implementar. `contexto/CONTEXTO.md` indica qué archivos leer; `contexto/TRAZABILIDAD.md` relaciona criterios y comprobaciones. Los contratos anteriores de importación y depuración se conservan como antecedentes: cuando describen una «base», se refieren al estado de su laboratorio de origen. En el laboratorio 9 los tres estados incorporan la persistencia corregida.

| Estado | Comportamiento |
| --- | --- |
| `estados/base` | Copia exacta de la solución corregida del laboratorio 8. Acepta la política anterior y conserva 62 casos heredados. |
| `estados/propuesta` | Añade los límites, pero convierte los pares a diccionario demasiado pronto. Pierde las claves repetidas y elige silenciosamente el último valor. |
| `estados/solucion` | Valida las repeticiones en la lista de pares y sólo después construye el diccionario. |

El defecto de la propuesta se preparó para el libro. No procede de una sesión comercial ni se atribuye a una herramienta. Las diferencias revisables están en `diferencias/`.

## Preparación

Necesitas Python 3.11 o posterior. Para los recorridos de navegador, Node 20 o posterior y Playwright 1.62.1, fijado en `package.json`. Desde Git Bash de Windows, abre la carpeta descomprimida y ejecuta:

```bash
export PYTHONIOENCODING=utf-8
python --version
node --version
npm install --ignore-scripts --package-lock=false
npx --no-install playwright install chromium
```

La instalación descarga herramientas públicas de comprobación. La aplicación y las pruebas usan exclusivamente el servidor sintético en `127.0.0.1`. Si el entorno impide iniciar procesos o sockets locales, la comprobación debe quedar BLOQUEADO; instalar dependencias no equivale a ejecutar las pruebas.

## Recorrido manual completo

Crea una carpeta de práctica nueva; el inicializador rechaza un archivo SQLite existente para evitar sobrescribirlo. Estos comandos parten de la raíz del laboratorio:

```bash
mkdir -p trabajo/demo_09_01
python estados/solucion/persistencia.py iniciar --base trabajo/demo_09_01/catalogo.sqlite
python estados/solucion/persistencia.py importar --base trabajo/demo_09_01/catalogo.sqlite --archivo datos/actualizacion_valida.csv
python estados/solucion/persistencia.py consultar --base trabajo/demo_09_01/catalogo.sqlite --almacen ALFA
```

**Expectativa:** la importación devuelve `APLICADO`. La consulta identifica el origen persistente y devuelve `A01` y `A03`, total 2. El CSV establece cantidades absolutas: A01 queda en 5, A03 en 3; A02 sigue deshabilitado aunque tenga 8 unidades. No vuelve a crear los datos iniciales al consultar.

Inicia el servidor sobre ese mismo archivo:

```bash
python estados/solucion/servidor.py --base trabajo/demo_09_01/catalogo.sqlite --puerto 8000
```

Mantén esta terminal abierta y visita `http://127.0.0.1:8000`. Selecciona ALFA y consulta sin nombre: deben aparecer A01/A03. Busca ` AGOTADO `: debe aparecer A03. El formulario heredado conserva su presentación del ejercicio web original; la procedencia del laboratorio se identifica en este README y en el paquete de contexto.

Para observar el rechazo desde una segunda terminal, abre en el navegador:

```text
http://127.0.0.1:8000/api/resumen?almacen=ALFA&almacen=BETA
```

**Expectativa:** HTTP 400 y el código `PARAMETRO_REPETIDO`. El JSON de error no es un catálogo vacío. Vuelve al formulario, introduce un nombre de 81 puntos de código y consulta. Debe mostrarse el error, ocultarse el resultado previo y habilitarse de nuevo el formulario. Una búsqueda posterior válida debe funcionar. Detén el servidor con Ctrl+C al terminar.

Los verificadores automatizados eligen puertos libres y generan sus propias bases aisladas. No utilizan ni modifican `trabajo/demo_09_01/catalogo.sqlite`.

## Reproducir el defecto y su corrección

Las mismas once comprobaciones HTTP se ejecutan sobre cada estado:

```bash
python -B pruebas_seguridad.py --estado base --json trabajo/seguridad_base_01.json
python -B pruebas_seguridad.py --estado propuesta --json trabajo/seguridad_propuesta_01.json
python -B pruebas_seguridad.py --estado solucion --json trabajo/seguridad_solucion_01.json
```

**Expectativas:** base devuelve código 1 con ocho fallos de la política nueva; propuesta devuelve 1 con S02.a/S02.b/S02.c FALLIDO; solución devuelve 0 con once aprobaciones. S06 se ejecuta por separado en Chromium real:

```bash
python -B pruebas_seguridad_navegador.py --estado base --json trabajo/navegador_base_01.json
python -B pruebas_seguridad_navegador.py --estado propuesta --json trabajo/navegador_propuesta_01.json
python -B pruebas_seguridad_navegador.py --estado solucion --json trabajo/navegador_solucion_01.json
```

La base debe fallar S06; propuesta y solución deben aprobar. Esta prueba prepara la base mediante el importador CLI y observa tres respuestas HTTP y tres estados visibles sobre el mismo servidor: consulta válida, rechazo real y recuperación. No intercepta ni simula respuestas.

## Verificación autónoma completa

Utiliza siempre un destino nuevo. El verificador se niega a sobrescribir una ejecución anterior:

```bash
python -B verificar.py --navegador --salida trabajo/verificacion_09_01
codigo_laboratorio_09=$?
printf 'Codigo del laboratorio: %s\n' "$codigo_laboratorio_09"
python -B soporte/huellas_evidencia.py trabajo/verificacion_09_01
```

El código de salida 0 del verificador completo exige el patrón exacto y todos los recorridos de navegador. Las pruebas individuales defectuosas siguen registradas como FALLIDO; el resumen aprueba la reproducción del patrón, no convierte esos casos en correctos.

| Estado | Casos ejecutados esperados | APROBADO | FALLIDO esperado |
| --- | ---: | ---: | ---: |
| Base | 74 | 65 | 9 |
| Propuesta | 74 | 71 | 3 |
| Solución | 74 | 74 | 0 |
| Total de esta ejecución autónoma | 222 | 210 | 12 |

Son 56 criterios distintos y 74 casos en la solución. Ejecutar los mismos casos sobre tres estados produce 222 ejecuciones; no crea 222 criterios nuevos. Las 27 baterías agrupadas contienen esos casos. Los 62 heredados deben aprobar en los tres estados. Sólo se admite `AssertionError` en las identidades fallidas expresamente acordadas. Un error inesperado, un caso ausente o un fallo adicional impide aprobar el conjunto.

Sin `--navegador`, se ejecutan dominio, CLI y HTTP, pero el estado global queda **NO EJECUTADO**. Puede haber código 0 para ese alcance parcial; no acredita los cinco casos de navegador por estado. Una dependencia o servidor inaccesible se registra **BLOQUEADO**, no como defecto didáctico.

Las regresiones de recursos heredadas son infraestructura y se ejecutan por separado:

```bash
python -B pruebas_recursos.py
```

Las ocho pruebas comunes del recolector se ejecutan durante la verificación de la integración en el repositorio. No se suman a los resultados funcionales de este laboratorio.

## Evidencia y límites

`evidencia/` conserva resultados de la preparación, con entorno y comandos saneados. Consulta su índice antes de atribuir un resultado a una plataforma. Una ejecución local Linux no acredita Windows, WSL ni una sesión de Codex, Copilot o Grok Build. Las expectativas de este README son el contrato; los JSON guardados son la evidencia efectivamente observada.

`verificar.py` compara los archivos heredados declarados en `PROCEDENCIA.json`, captura bytes de stdout/stderr, realiza el saneamiento y verifica sus huellas finales. Se conservan las huellas de captura cuando corresponden. El comprobador de huellas sólo lee; no repara divergencias ni normaliza saltos de línea para hacer coincidir un hash.

La política es deliberadamente pequeña. El límite de 2.048 bytes es de la query y se comprueba después de que el servidor haya recibido la petición; no demuestra resistencia global a denegación de servicio. Los 80 puntos de código no equivalen necesariamente a 80 símbolos visibles. S07 comprueba una cadena sintética parecida a SQL, no la ausencia universal de inyección. S08 interrumpe un archivo local aislado y comprueba un error genérico; no modifica sistemas ajenos.

Autenticación, autorización, TLS, exposición pública, concurrencia, pruebas de carga, auditoría completa de dependencias y despliegue productivo quedan fuera. El servidor estándar se utiliza como instrumento de enseñanza local. No se implementa una nueva pantalla, API externa ni plataforma.

## Reto del lector

Diseña una comprobación adicional que verifique las cabeceras comunes en respuestas 200, 400, 414 y 500. Debe observar HTTP real, identificar qué garantiza cada cabecera y conservar la base. El código ya centraliza la respuesta; el reto consiste en comprobar una propiedad de forma consistente. Evalúa que la prueba detecte una omisión deliberada en una copia propia y vuelva a aprobar al restaurarla. Este reto no se implementó ni se suma a los resultados de la entrega.
