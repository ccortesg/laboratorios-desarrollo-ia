# Laboratorio 8 · Depuración con evidencia

**Distribución 1.0.1 · corrección de cierre de conexiones en pruebas.** Consulta [CORRECCION_WINDOWS_v1.0.md](CORRECCION_WINDOWS_v1.0.md). La versión 1.0 y sus resultados históricos se conservan como antecedentes.

Material sintético autónomo del capítulo «Depuración con evidencia: investigar errores entre entornos y servicios».
Practica cómo seguir una importación desde su proceso hasta el archivo SQLite, la respuesta HTTP y la pantalla.
La base conserva el alcance correcto del laboratorio 7; la persistencia entre procesos es el incremento nuevo.

## Preparación

La aplicación requiere Python 3.11 o posterior con SQLite estándar. Las pruebas HTTP no necesitan paquetes Python.
El navegador automatizado requiere Node 20 o posterior, Playwright 1.62.1 y Chromium o Chrome compatible.
Todos los comandos siguientes parten de esta carpeta después de descomprimir el laboratorio.
En Windows con Git Bash usa `python`; donde corresponda puedes sustituirlo por `python3`.

Lee `contexto/CONTRATO_DEPURACION.md` antes del código. Los CSV y los SQL son sintéticos.
No necesitas cuentas comerciales. La aplicación sólo escucha en loopback; no es un servicio de producción.

## Primer recorrido manual

Crea una carpeta de trabajo nueva y una base explícita:

```bash
mkdir trabajo
python estados/solucion/persistencia.py iniciar --base trabajo/catalogo.sqlite
python estados/solucion/servidor.py --base trabajo/catalogo.sqlite --puerto 8000 --diagnostico trabajo/servidor.jsonl
```

Abre la URL local anunciada por el servidor. Consulta ALFA: se espera A01.
Mantén el servidor abierto y, desde otra terminal situada en esta misma carpeta, importa:

```bash
python estados/solucion/persistencia.py importar --base trabajo/catalogo.sqlite --archivo datos/actualizacion_valida.csv
python estados/solucion/persistencia.py consultar --base trabajo/catalogo.sqlite --almacen ALFA --diagnostico trabajo/consulta.jsonl
```

La consulta directa muestra existencias 5, 8, 3 y 0. A02 continúa deshabilitado.
Vuelve a enviar el formulario en la pantalla: ALFA debe mostrar A01 y A03; BETA, vacío.
Buscar ` AGOTADO ` en ALFA debe devolver A03. El total representa artículos, no unidades.

Detén el servidor con Ctrl+C. Reiniciarlo contra la misma base debe conservar los datos.
Las rutas relativas se interpretan desde el directorio de invocación; al cambiar de directorio,
utiliza la ruta absoluta del mismo archivo entre comillas. No hay una ruta privada fija en el ejercicio.

La inicialización rechaza un destino existente. Consultar, importar o servir no crean la base ni cargan semillas.
Un archivo inexistente o un esquema incompatible se rechazan con un código y mensaje público.
El diagnóstico debe tener un destino diferente de la base; la colisión también se rechaza.

## Reproducir el resultado que parecía correcto

Utiliza otra carpeta o archivo de trabajo para conservar la primera práctica.
Repite el recorrido con `estados/propuesta`. La importación CLI queda persistida, pero
la pantalla vuelve a mostrar la referencia: A01 en ALFA y A04 en BETA. El servidor responde HTTP 200.

Compara el JSON de consulta directa, el contenido HTTP y los registros de origen.
La propuesta anuncia un archivo configurado pero su consulta efectiva utiliza memoria.
La diferencia funcional entre propuesta y solución es transmitir `conexion=conexion`
al resumen HTTP. `diferencias/propuesta_a_solucion.diff` permite revisarla.

El diagnóstico se obtiene dentro de la consulta que ejecuta el SQL, después de elegir su conexión.
No se limita a repetir la opción `--base`. Los alias sustituyen rutas; un mismo alias de
origen no configurado sólo tiene significado dentro de ese proceso, no entre ejecuciones distintas.

## Comprobaciones

Para comprobar los diez casos D de terminal y HTTP:

```bash
python pruebas_depuracion.py --estado propuesta --json trabajo/propuesta_d.json
python pruebas_depuracion.py --estado solucion --json trabajo/solucion_d.json
```

La propuesta debe FALLAR exactamente D03, D05 y D08.a por aserciones. Su batería termina con código 1.
La solución debe aprobar los diez casos. D02 aprueba en ambos estados cuando describe fielmente
el origen realmente consultado, aunque la observación permita descubrir el defecto.

Para el recorrido continuo de navegador D04 y las pruebas web heredadas:

```bash
npm install --ignore-scripts --package-lock=false
npx --no-install playwright install chromium
python pruebas_recorrido.py --estado solucion --json trabajo/solucion_d04.json
python verificar.py --navegador --salida trabajo/verificacion_01
```

La preparación descarga dependencias públicas. Las comprobaciones se ejecutan localmente.
Si ya dispones de un ejecutable compatible, `LAB06_CHROMIUM` puede indicar su ruta; el
registro debe conservar la versión realmente iniciada. No se empaquetan navegadores ni node_modules.

El verificador exige una carpeta de salida nueva. Sin `--navegador`, puede aprobar el alcance
ejecutado pero el global permanece NO EJECUTADO. Si se solicita una dependencia que no puede
iniciarse, queda BLOQUEADO. Un error interno inesperado es FALLIDO y nunca se acepta como
defecto didáctico. Un código de salida 0 sin navegador no demuestra CSV→pantalla.

| Estado | 51 casos heredados C/B/N/P/W/I | 11 casos D |
| --- | --- | --- |
| base | Deben aprobar | NO EJECUTADO: persistencia ausente |
| propuesta | Deben aprobar | Siete deben aprobar; D03, D04, D05 y D08.a deben fallar |
| solucion | Deben aprobar | Deben aprobar los once |

La solución reúne 48 criterios distintos y 62 casos. Cada batería registra sus ejecuciones.
Los totales observados están en `evidencia/RESULTADOS.md`, junto a la ejecución saneada;
la tabla anterior expresa el contrato, no sustituye ese resultado.

## Practicar sobre una copia

```bash
python -c "import shutil; shutil.copytree('estados/propuesta', 'mi_practica')"
python pruebas_depuracion.py --directorio mi_practica --json trabajo/practica_d.json
python pruebas_recorrido.py --directorio mi_practica --json trabajo/practica_d04.json
```

Conserva las referencias distribuidas. Para revisar también los contratos anteriores en tu copia:

```bash
python mi_practica/pruebas.py
python pruebas_resumen.py --directorio mi_practica
python pruebas_http.py --directorio mi_practica
python pruebas_integracion.py --directorio mi_practica
```

Las baterías heredadas conservan sus selectores históricos. Usa `--directorio` para
evaluar cualquier estado del laboratorio 8, incluida su base, sin interpretar etiquetas
de etapas anteriores. `verificar.py` ya utiliza esa forma.
Las comprobaciones de tus cambios deben señalar la copia que realmente modificaste.

## Evidencia y límites

El registro de investigación vincula entrada, consultas, observaciones e hipótesis en
`evidencia/INVESTIGACION.md`. Los JSON de casos contienen comandos saneados y salidas.
El recolector conserva huellas capturadas y finales; no altera históricos.

D04 inicia el servidor como proceso, observa la UI inicial, ejecuta una importación CLI
desde otro proceso y vuelve a consultar la misma página contra ese servidor vivo.
No simula HTTP ni reemplaza respuestas. W06.b conserva su fallo de transporte controlado
como prueba heredada independiente.

Cambiar de directorio y reiniciar no acredita otro sistema operativo. La evidencia no
certifica producción, múltiples escritores, carga, recuperación física ni seguridad integral.
No demuestra uso comercial de Codex, Copilot o Grok Build. Los capítulos siguen pendientes
de revisión editorial. El reto de comparar dos informes de diagnóstico queda NO EJECUTADO.
