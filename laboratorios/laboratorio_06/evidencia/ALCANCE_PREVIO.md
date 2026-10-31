# Contrato previo del laboratorio 6

**Versión:** 1.0. **Fecha editorial:** 30 de octubre de 2026.
Este contrato se registra antes de implementar la aplicación. Describe expectativas;
los resultados observados se documentan por separado. El escenario y el código son
didácticos y sintéticos. Su producción local no acredita una sesión de Grok Build.

## Punto de partida y conservación

La solución del laboratorio 5 consulta artículos disponibles por almacén y nombre,
permite obtener un código exacto y produce un resumen por función o terminal.
Se conservan sus cuatro artículos y los 26 criterios C01–C04, B01–B06, N01–N10
y P01–P06, sin cambiar entradas ni expectativas.

Los nueve archivos de `estados/solucion/` del laboratorio anterior se copiarán sin
cambios a los tres estados nuevos. También se conserva `pruebas_resumen.py`.
Para comprobar P01–P06 en la nueva base se utilizará `--directorio estados/base`:
la base de este capítulo ya incluye `resumen.py`. No se utilizará el selector
histórico `--estado base`, que representaba un incremento todavía ausente en el
laboratorio 5. Esta es una adaptación de invocación, no de expectativas.

## Incremento y componentes

Se añade una aplicación web local de lectura. Un formulario permite elegir ALFA
o BETA, escribir un nombre opcional y consultar. El servidor llama a
`resumir_catalogo(almacen, texto="")`; la interfaz presenta el almacén devuelto,
el número de artículos y sus códigos. `total` cuenta artículos, no unidades.
La regla SQL, el filtro `strip().casefold()` por nombre y la coincidencia exacta
por código conservan sus contratos.

- `estados/base/`: solución del laboratorio 5, sin servidor ni interfaz web.
- `estados/propuesta/`: servidor correcto e interfaz con un defecto deliberado:
  conserva el almacén ALFA inicial al enviar consultas después de seleccionar BETA.
- `estados/solucion/`: misma aplicación con lectura del almacén elegido en cada envío.
- `servidor.py` de los estados web: adaptador HTTP y recursos estáticos permitidos.
- `web/index.html`, `web/app.js`, `web/estilos.css`: formulario, interacción y presentación.
- `pruebas_http.py`: solicitudes reales a un servidor local iniciado durante la prueba.
- `pruebas_navegador.cjs`: interacción en Chromium mediante Playwright.
- `verificar.py`: captura por estado y capa y comprueba el patrón esperado.

No se añaden datos, autenticación, usuarios, reservas, cantidades solicitadas,
pagos, persistencia adicional, servicios externos ni despliegue público.
La elección de Python estándar y recursos web locales corresponde al ejercicio;
no determina el stack definitivo de la aplicación del libro.

## Contrato HTTP

El servidor escucha exclusivamente en la interfaz local. `--puerto 8000` es el
valor de demostración; `--puerto 0` permite elegir un puerto local libre para las
pruebas. No expone el directorio completo del laboratorio.

`GET /api/resumen?almacen=ALFA&nombre=...` admite un almacén de cadena no vacía
y un nombre opcional, cuyo valor predeterminado es cadena vacía. La interfaz ofrece
ALFA y BETA explícitamente. La frontera HTTP rechaza un almacén ausente o vacío
(incluidos solo espacios) con estado 400 y este cuerpo:

```json
{"error":{"codigo":"ALMACEN_REQUERIDO","mensaje":"Selecciona un almacén."}}
```

Una consulta válida devuelve 200 y las tres claves `almacen`, `total`, `codigos`.
Una lista vacía es un resultado válido. No se elige un almacén implícito. Un valor
no vacío fuera del catálogo conserva el comportamiento del dominio (lista vacía);
esta versión no certifica entradas arbitrarias, Unicode exhaustivo ni parámetros
duplicados. No se modifica la validación de la función ni de la terminal heredada.

Las respuestas de la API usan `application/json; charset=utf-8`. Las rutas
estáticas permitidas son `/`, `/index.html`, `/app.js` y `/estilos.css`; cualquier
otra ruta devuelve 404. Un error interno devuelve un mensaje genérico sin trazas.
La interfaz usa texto para los datos y distingue espera, consulta, éxito, vacío y error.

## Criterios y subcasos nuevos

| Caso | Capa | Entrada o recorrido | Resultado esperado |
| --- | --- | --- | --- |
| W01 | HTTP | ALFA sin nombre | 200; `{"almacen":"ALFA","total":1,"codigos":["A01"]}` |
| W02 | HTTP | BETA y nombre ` OTRA ` | 200; BETA, total 1 y A04 |
| W03 | HTTP | ALFA y nombre `otra` | 200; ALFA, total 0 y códigos vacíos |
| W04.a | HTTP | Almacén omitido | 400; error ALMACEN_REQUERIDO |
| W04.b | HTTP | Almacén vacío | 400; el mismo error |
| W05 | Navegador | Consultar ALFA; cambiar a BETA; consultar | A01 y luego A04; total 1 y almacén correspondiente, sin resultado anterior |
| W06.a | Navegador | Buscar `inexistente` en ALFA | Mensaje de ausencia, total 0, lista vacía, sin alerta de error |
| W06.b | Navegador | Interrumpir la solicitud a `/api/resumen` desde la prueba | Mensaje de error distinguible del vacío, sin mostrar resultados previos |

Son seis criterios W, desglosados en ocho comprobaciones. W04 y W06 contienen dos
subcasos. Las expectativas son literales, no se calculan con la función evaluada.
W06.b utiliza un fallo de transporte controlado por la prueba del navegador;
no introduce un endpoint defectuoso ni una función de fallo en la aplicación.

La misma batería HTTP y de navegador se usa en propuesta y solución. Solo W05
debe fallar por aserción en la propuesta. La base registra los ocho casos W como
NO EJECUTADO porque no incorpora el incremento web. Los 26 casos heredados se
ejecutan en los tres estados.

## Interpretación de la verificación

`python verificar.py --salida NUEVA` ejecuta dominio, terminal y HTTP. Si estos
casos cumplen el patrón, su alcance ejecutado queda APROBADO, pero el estado global
y el extremo a extremo permanecen NO EJECUTADO porque falta el navegador. Su salida
0 indica únicamente éxito del alcance solicitado; no acredita el recorrido completo.

`python verificar.py --navegador --salida NUEVA` añade Playwright. Solo puede declarar
APROBADO el recorrido completo cuando observa también W05–W06 en Chromium. Si se
solicita navegador y faltan Node, Playwright o Chromium, registra BLOQUEADO y salida 2.
Un fallo inesperado produce FALLIDO y salida 1. Un W05 FALLIDO en la propuesta sigue
siendo FALLIDO en su registro; el patrón didáctico puede quedar APROBADO porque
reproduce precisamente ese defecto. La solución no admite fallos pendientes.

Las cifras previstas con navegador son 12 baterías, 94 ejecuciones, 93 aprobaciones,
un fallo didáctico y ocho NO EJECUTADO en base. Esas cifras son expectativas hasta
contrastar las salidas. Cada estado web tiene 32 criterios, desglosados en 34 casos
(26 heredados y ocho web). El verificador debe informar los conteos observados.

## Límites

El ejercicio no evalúa producción, acceso remoto, carga, concurrencia de usuarios,
autorización, seguridad integral, orden de múltiples resultados ni compatibilidad
general entre navegadores. La prueba automática del navegador requiere Node y
Playwright como dependencias de comprobación; ejecutar la aplicación y sus pruebas
de dominio/HTTP solo requiere Python 3.10 o posterior. Los recursos de la aplicación
son locales y no dependen de una cuenta comercial, CDN ni servicios de modelos.
