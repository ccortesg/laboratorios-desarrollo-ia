# Laboratorio 10 · Automatización y operación del catálogo

Versión 1.0. Ejercicio autónomo, local y sintético. La aplicación y el operador usan Python estándar y SQLite. Node y Playwright sólo se necesitan para las comprobaciones de navegador.

## El incremento

La solución del laboratorio 9 ya importa CSV, conserva los datos en SQLite y atiende consultas HTTP con su política de entrada. Este ejercicio añade una operación repetible: importar mediante una CLI real, consultar mediante otra CLI sobre la misma base y producir un recibo. El programa debe detenerse si el primer paso falla.

Lee `contexto/CONTRATO_AUTOMATIZACION.md`, registrado antes de implementar. Las reglas anteriores de disponibilidad, búsqueda, detalle, resumen, web, importación, persistencia y seguridad se conservan. Los contratos originales incluidos como antecedentes describen los estados de sus propios laboratorios; la base de este ejercicio es la solución 9 completa.

| Estado | Comportamiento |
| --- | --- |
| `estados/base` | Copia exacta de la solución 9, todavía sin `operar.py`. Los 74 casos heredados deben aprobar. |
| `estados/propuesta` | Añade el operador, pero continúa tras una importación rechazada y devuelve como éxito una consulta del catálogo anterior. |
| `estados/solucion` | Exige importación confirmada antes de consultar; conserva el rechazo y registra la consulta NO EJECUTADO. |

El defecto se preparó para el libro. La secuencia es determinista: no elige objetivos, no recibe comandos de un modelo y no acredita un agente comercial.

## Preparación

Necesitas Python 3.11 o posterior. Para las pruebas de navegador necesitas Node 20 o posterior y Playwright 1.62.1, fijado en `package.json`. Desde la carpeta descomprimida, en Git Bash de Windows:

```bash
export PYTHONIOENCODING=utf-8
python --version
node --version
npm install --ignore-scripts --package-lock=false
npx --no-install playwright install chromium
```

La preparación descarga herramientas públicas. La aplicación y las pruebas usan archivos sintéticos y HTTP en `127.0.0.1`. El operador no necesita Node, navegador, cuentas ni claves.

## Primera operación

Crea una carpeta de práctica nueva y una base explícita:

```bash
mkdir -p trabajo/demo_10_01
python -B estados/solucion/persistencia.py iniciar --base trabajo/demo_10_01/catalogo.sqlite
```

La inicialización rechaza un archivo existente. Después ejecuta:

```bash
python -B estados/solucion/operar.py --base trabajo/demo_10_01/catalogo.sqlite --archivo datos/actualizacion_valida.csv --almacen ALFA --salida trabajo/demo_10_01/recibo_01
```

**Expectativa:** código 0 y resultado APROBADO. La importación aplica cantidades absolutas: A01/ALFA=5, A03/ALFA=3, A02 sigue deshabilitado y A04/BETA=0. La consulta devuelve A01/A03 en ALFA, total 2. La salida contiene `entrada.csv`, `resultado.json`, `comandos.json`, capturas de ambos pasos y `huellas.json`.

`entrada.csv` es una copia exacta de los bytes leídos para esta operación; el importador usa esa copia. Su SHA-256 no se calcula mediante una segunda lectura del archivo original. `resultado.json` muestra si se observó una importación confirmada y cuál fue el resumen posterior. Las rutas del equipo se sustituyen por alias en el recibo.

Comprueba las huellas del recibo:

```bash
python -B soporte/huellas_evidencia.py trabajo/demo_10_01/recibo_01
```

Para repetir la operación, conserva la misma base y el mismo CSV, pero utiliza `recibo_02`. La repetición no acumula existencias y el recibo anterior conserva sus bytes. Si reutilizas `recibo_01`, el operador rechaza el destino antes de importar.

## Ver el resultado en HTTP y navegador

Inicia el servidor sobre el mismo archivo:

```bash
python -B estados/solucion/servidor.py --base trabajo/demo_10_01/catalogo.sqlite --puerto 8000
```

Visita `http://127.0.0.1:8000`, selecciona ALFA y consulta sin nombre: deben aparecer A01/A03. Busca ` AGOTADO `: debe aparecer A03. El formulario es el heredado del ejercicio web original; su presentación no se rediseña en este capítulo. Detén el servidor con Ctrl+C al terminar.

La prueba T08 automatiza una secuencia más exigente: mantiene un mismo servidor vivo, observa el catálogo inicial, ejecuta el operador desde otro proceso y vuelve a consultar HTTP y pantalla. Las respuestas no se interceptan ni se simulan.

## Reproducir el defecto

Las mismas siete comprobaciones de terminal se ejecutan contra propuesta y solución:

```bash
python -B pruebas_automatizacion.py --estado propuesta --json trabajo/t_propuesta_01.json
python -B pruebas_automatizacion.py --estado solucion --json trabajo/t_solucion_01.json
```

**Expectativas:** propuesta devuelve código 1 con T02 FALLIDO; solución devuelve 0 con siete aprobaciones. T02 prepara una primera fila válida seguida de una cantidad negativa. El importador rechaza todo y conserva la base. La propuesta continúa consultando y declara éxito con datos antiguos; la solución detiene el flujo, declara FALLIDO y deja la consulta NO EJECUTADO. El fallo esperado es una aserción sobre ese comportamiento, no un error de infraestructura.

El recorrido nuevo de navegador se ejecuta por separado:

```bash
python -B pruebas_automatizacion_navegador.py --estado propuesta --json trabajo/t08_propuesta_01.json
python -B pruebas_automatizacion_navegador.py --estado solucion --json trabajo/t08_solucion_01.json
```

Ambos deben aprobar T08, porque este caso utiliza una entrada válida. La existencia de un caso feliz no demuestra la parada ante un rechazo; T02 aporta esa observación complementaria.

Los controladores conservan copias exactas de los recibos producidos junto a sus JSON. Usa destinos nuevos para no mezclar ejecuciones ni sobrescribirlos.

## Verificación autónoma completa

```bash
python -B verificar.py --navegador --salida trabajo/verificacion_10_01
codigo_laboratorio_10=$?
printf 'Codigo del laboratorio: %s\n' "$codigo_laboratorio_10"
python -B soporte/huellas_evidencia.py trabajo/verificacion_10_01
```

El verificador comprueba la conservación de las fuentes heredadas, ejecuta las baterías sobre bases aisladas y exige exactamente el patrón del contrato. Sin `--navegador`, el global queda NO EJECUTADO, aunque el alcance realizado termine con código 0. Una dependencia o permiso que impida iniciar procesos debe quedar BLOQUEADO.

**Expectativas del contrato, no resultados históricos reutilizados:**

| Estado | Ejecuciones | APROBADO | FALLIDO esperado | NO EJECUTADO |
| --- | ---: | ---: | ---: | ---: |
| Base | 74 | 74 | 0 | 8 |
| Propuesta | 82 | 81 | 1, T02 | 0 |
| Solución | 82 | 82 | 0 | 0 |
| Total autónomo | 238 | 237 | 1 | 8 |

La solución contiene 64 criterios y 82 casos. El total de ejecuciones cuenta la repetición de casos en diferentes estados; no significa 238 criterios distintos. Las 33 baterías incluyen las dos del incremento que permanecen NO EJECUTADO en base.

La ejecución nueva de esta entrega observó ese patrón: 33 baterías, 238 ejecuciones, 237 aprobaciones, un fallo didáctico y ocho NO EJECUTADO, con 116/116 huellas aprobadas. El registro completo y sus límites están en `evidencia/ejecucion_local`; `evidencia/README.md` distingue esta ejecución de las focales previas.

Las regresiones de infraestructura se mantienen aparte:

```bash
python -B pruebas_recursos.py
python -B pruebas_operador_recursos.py
```

La primera conserva las cuatro regresiones heredadas de SQLite. La segunda contiene RO01, un método con dos estados que inyecta la imposibilidad de iniciar un hijo: debe mantener BLOQUEADO y no inventar capturas. No son criterios funcionales T. Las ocho pruebas comunes del recolector se ejecutan además durante la integración del repositorio.

## Qué demuestra el recibo y qué queda fuera

El recibo permite identificar los bytes de entrada, conocer qué pasos se ejecutaron, comprobar sus salidas y localizar el punto de parada. Una huella no prueba por sí misma la corrección del dato ni quién ejecutó el programa. La evidencia incluida identifica el entorno realmente usado; ejecutar aquí no acredita Windows ni el uso de un producto comercial.

La operación no es una única transacción. Si se confirmó la importación y después falla la consulta, los datos importados permanecen. Si vence un tiempo límite sin observar confirmación, tampoco se puede concluir que la base quedó intacta: hay que consultar e investigar. El programa no reinicializa, revierte ni reintenta automáticamente.

La práctica supone operación local secuencial. Concurrencia, fallos físicos, programación periódica, servicios permanentes, colas, credenciales, agentes que elijan acciones y despliegue público quedan fuera. Las instrucciones y los datos no se convierten en código de shell.

## Reto del lector

Diseña un modo de revisión previa que describa los pasos y los archivos elegidos sin importar, consultar ni reservar un recibo. Debe tener un resultado distinguible de una ejecución efectiva, preservar todos los bytes de entrada y rechazar opciones inválidas. Comprueba que no genera una marca de operación APROBADA y que el modo normal conserva T01–T08. Este modo no se implementó ni se suma a las comprobaciones de la entrega.
