# Laboratorio 7 · Datos e integraciones

Importa un CSV sintético de existencias, valida su contrato y consulta el catálogo
en la misma base desechable. Aprende a distinguir un proceso que termina de un
resultado que satisface las reglas acordadas.

## Preparación

Python 3.11 o posterior. La importación utiliza únicamente la biblioteca estándar
y SQLite; no necesita servicios, credenciales ni conexión de red. Los archivos
SQL de referencia conservan los cuatro artículos y los almacenes ALFA y BETA.
El directorio `estados/base` reproduce la solución del laboratorio 6.

Los comandos siguientes se ejecutan desde la carpeta `laboratorio_07` después
de descomprimir el paquete. En sistemas que lo requieran sustituye `python` por
`python3` o `py -3` de forma consistente.

## Primer recorrido

Lee `contexto/CONTRATO_INTEGRACION.md` antes de ejecutar el importador. El CSV
representa cantidades absolutas: A01/ALFA=5 debe reemplazar 7 por 5.

```bash
python demostrar.py --estado propuesta --archivo datos/actualizacion_valida.csv --almacen ALFA --repeticiones 2
python demostrar.py --estado solucion --archivo datos/actualizacion_valida.csv --almacen ALFA --repeticiones 2
```

Cada invocación crea una base nueva en memoria, y sus dos repeticiones usan esa
misma conexión. No pruebes idempotencia lanzando dos procesos con una repetición:
cada uno volvería a empezar con los datos originales.

La propuesta contiene un defecto deliberado: suma. A01 pasa de 7 a 12 y después a
17. La solución sustituye y permanece en 5. La consulta ALFA muestra A01 y A03 en
ambos estados: esa lista por sí sola no permite identificar el error de cantidad.
Inspecciona también las existencias y el almacén BETA:

```bash
python demostrar.py --estado solucion --archivo datos/actualizacion_valida.csv --almacen BETA --repeticiones 2
python demostrar.py --estado solucion --archivo datos/error_tardio.csv --almacen ALFA
```

El archivo válido deja BETA vacío. El archivo inválido termina con código 1,
informe `RECHAZADO` y las tablas intactas. El informe `APLICADO` describe una
operación del importador, no el resultado de las comprobaciones. La propuesta
también puede informar `APLICADO` aunque viole el contrato.

## Comprobaciones y diferencias

```bash
python pruebas_integracion.py --estado propuesta
python pruebas_integracion.py --estado solucion
python comparar.py
python verificar.py --salida trabajo/primera_verificacion
```

El primer comando debe terminar con código 1 por I01 e I07. La solución debe
aprobar sus 17 casos I. `comparar.py` muestra la diferencia preparada y conserva
los archivos originales. Los 17 casos corresponden a ocho criterios con subcasos;
no son 17 criterios nuevos.

Sin `--navegador`, el verificador ejecuta dominio, terminal, HTTP e integración,
pero marca el alcance completo **NO EJECUTADO**. El código 0 en esa modalidad
no acredita la interfaz. Para la verificación completa necesitas Node 20 o
posterior, Playwright 1.62.1 y Chromium; la instalación opcional usa la red:

```bash
npm install --ignore-scripts --package-lock=false
npx --no-install playwright install chromium
python verificar.py --navegador --salida trabajo/verificacion_completa
python soporte/huellas_evidencia.py trabajo/verificacion_completa
```

Cada salida debe ser una carpeta nueva. No reutilices ni sobrescribas la evidencia
histórica. El comprobador de huellas sólo lee; el verificador valida la captura,
sanea y calcula hashes sobre los bytes finales. No normaliza LF/CRLF para ocultar
discrepancias. Comprueba todas las referencias declaradas sin imponer el total
histórico 34. La verificación autónoma completa declara 30 huellas de procesos.

Patrón de aceptación del laboratorio 7:

| Estado | C/B/N | P | HTTP | Navegador | I |
| --- | ---: | ---: | ---: | ---: | --- |
| base | 20 APROBADO | 6 APROBADO | 5 APROBADO | 3 APROBADO | 17 NO EJECUTADO |
| propuesta | 20 APROBADO | 6 APROBADO | 5 APROBADO | 3 APROBADO | 15 APROBADO; I01/I07 FALLIDO |
| solución | 20 APROBADO | 6 APROBADO | 5 APROBADO | 3 APROBADO | 17 APROBADO |

Con navegador se esperan 15 baterías y 136 ejecuciones: 134 aprobaciones, dos
fallos didácticos y 17 NO EJECUTADO en la base. La solución satisface 51 casos de
40 criterios: los 32 criterios anteriores y ocho I. Los resultados observados
están documentados en `evidencia/RESULTADOS.md`; las expectativas no sustituyen
esa evidencia. Un fallo diferente del patrón produce FALLIDO; un navegador que
no puede iniciarse produce BLOQUEADO.

## Practica en una copia

```bash
python -c "import shutil; shutil.copytree('estados/solucion', 'mi_practica')"
python pruebas_integracion.py --directorio mi_practica
python pruebas_resumen.py --directorio mi_practica
python pruebas_http.py --directorio mi_practica
python mi_practica/pruebas.py
python demostrar.py --directorio mi_practica --archivo datos/actualizacion_valida.csv --almacen ALFA --repeticiones 2
```

La copia debe ser nueva. El verificador de referencias examina `estados/`, no
modificaciones que hagas en otra carpeta. La web heredada puede iniciarse con
`python mi_practica/servidor.py --puerto 8000` y conserva sus datos predeterminados.
No tiene pantalla de importación ni comparte la conexión del comando demostrativo.
El incremento verifica importación y consulta real por terminal, no persistencia
entre procesos o integración de un CSV con un navegador abierto.

## Límites

Todo es sintético y local. No se implementan reservas, usuarios, API externa,
despliegue ni acceso productivo. I06 verifica el rechazo de entradas y una escritura
rechazada mediante un trigger temporal de prueba; no demuestra recuperación ante
cortes físicos, concurrencia ni pruebas de carga. Las ejecuciones
no acreditan uso de Codex, Copilot o Grok Build. El reto editorial se evalúa por
separado y no forma parte del código entregado.
