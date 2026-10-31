# Laboratorio 5: de la sugerencia al trabajo delegado

Práctica autónoma del libro **Desarrollo de Software en la Era de la IA**.
Todos los datos y escenarios son sintéticos. El incremento y la propuesta con
defecto se prepararon localmente para enseñar revisión; **no son resultados de
una sesión de GitHub Copilot**. La ejecución funcional no necesita una cuenta.

## Qué vas a entregar

Un resumen del catálogo con almacén, cantidad de artículos coincidentes y códigos.
La función y la terminal deben respetar la búsqueda por nombre y la disponibilidad
existentes. El contrato está en `ALCANCE.md`; léelo antes de editar.

El ejercicio permite comparar un encargo puntual —una función— con uno delegado
que incluye función, terminal, comprobaciones, diferencias y cierre. Los prompts
son ejemplos preparados para el libro, no transcripciones.

## Requisitos y preparación

Python 3.10 o posterior con SQLite y biblioteca estándar. No hay instalaciones,
servicios, red ni dependencias externas. Descomprime el ZIP, abre una terminal y
sitúate en la carpeta `laboratorio_05`, donde está este archivo.

```bash
python --version
python verificar.py --salida mi_evidencia
```

Si tu equipo usa `python3` o `py -3`, sustituye `python` en **todos** los comandos.
El segundo comando necesita una carpeta nueva; si ya existe `mi_evidencia`, usa
otro nombre. El verificador conserva cada stdout, stderr, resultado por criterio,
código de salida, entorno y huellas. No sobrescribe evidencias anteriores.

El resultado esperado del recorrido completo es `Verificación: APROBADO`, con
72 ejecuciones, 70 aprobaciones y dos fallos intencionales, además de seis criterios
NO EJECUTADO en la base. Ese dictamen reconoce el defecto previsto; no convierte
sus dos fallos en aprobaciones. Consulta la evidencia incluida para lo observado
durante la producción.

## Tres estados que puedes inspeccionar

| Carpeta | Contenido | Patrón esperado |
| --- | --- | --- |
| `estados/base/` | Solución heredada; aún sin `resumen.py` | 20 heredados aprobados; P01–P06 NO EJECUTADO |
| `estados/propuesta/` | Propuesta didáctica que omite el filtro de nombre | 20 heredados y 4 nuevos aprobados; P04 y P05 FALLIDO |
| `estados/solucion/` | Incremento corregido | 20 heredados y 6 nuevos aprobados |

Los ocho archivos heredados son idénticos en los tres estados. Los cuatro artículos
siguen siendo A01–A04 y los almacenes ALFA y BETA. No se agregan registros.

## Observa primero el defecto

Desde la raíz del laboratorio:

```bash
python estados/propuesta/resumen.py --almacen ALFA --nombre otra
python pruebas_resumen.py --estado propuesta
```

El primer comando debería producir un resumen vacío según P04. La propuesta
defectuosa devuelve A01 porque consulta disponibilidad e ignora el nombre.
La batería termina con salida 1 y falla exactamente en P04 y P05. Es un defecto
deliberado del material didáctico; no se atribuye a una herramienta comercial.

## Comprueba la solución y revisa la diferencia

```bash
python estados/solucion/resumen.py --almacen ALFA --nombre otra
python estados/solucion/resumen.py --almacen BETA --nombre " OTRA "
python estados/solucion/pruebas.py
python pruebas_resumen.py --estado solucion
python comparar.py --desde propuesta --hasta solucion
```

La primera consulta debe devolver `{"almacen": "ALFA", "total": 0, "codigos": []}`.
La segunda debe devolver BETA, total 1 y A04. Las dos baterías comprueban las veinte
reglas heredadas y los seis criterios nuevos, por separado. La corrección utiliza
`buscar_catalogo(almacen, texto)` para conservar tanto la ubicación como el nombre.

`total` cuenta artículos: las siete unidades de A01 no se convierten en siete
artículos. La nueva terminal exige `--almacen`; omitirlo debe terminar con salida 2
y un mensaje de uso en stderr. No se cambia el valor predeterminado histórico de
`laboratorio.py`; se define explícitamente el contrato de la nueva interfaz.

## Practica los dos encargos

Lee `prompts/01_insuficiente.md`, `02_puntual.md` y `03_delegado.md`. Para una
sugerencia puntual, entrega la firma, las entradas y la responsabilidad de la
función. Para el encargo delegado, añade archivos, límites, CLI, pruebas y evidencia
esperada. Revisa el contexto necesario antes de aceptar cualquier cambio.

Si deseas implementarlo tú, crea una copia de trabajo nueva y entrega esa carpeta
al encargo. `copytree` se detiene si el destino ya existe:

```bash
python -c "import shutil; shutil.copytree('estados/base', 'mi_practica')"
```

Después de añadir `mi_practica/resumen.py`, evalúa exactamente tu copia:

```bash
python mi_practica/pruebas.py
python pruebas_resumen.py --directorio mi_practica
```

La segunda batería es la misma de seis criterios. En `--directorio`, la ausencia
del módulo produce fallos; sólo `--estado base` registra los seis como NO EJECUTADO.
Los comandos del verificador completo siguen comprobando las tres referencias
distribuidas, no tu copia. Conserva la procedencia de cada ejecución. Si usas
Copilot, registra esa sesión por separado y no reemplaces la evidencia local.

## Mapa de archivos

- `ALCANCE.md`: contrato escrito antes de implementar.
- `PROCEDENCIA.json`: origen y huellas de los ocho archivos heredados.
- `contexto/`: reglas, responsabilidades, decisiones y continuidad.
- `prompts/`: encargos didácticos comparables.
- `estados/`: base, propuesta incorrecta y solución.
- `pruebas_resumen.py`: seis comprobaciones nuevas con expectativas literales.
- `comparar.py` y `diferencias/`: comparación regenerable y diferencias de referencia.
- `verificar.py`: ejecución aislada por proceso, registro y contraste del patrón.
- `evidencia/`: resultados locales, contrato previo y comprobación del acceso.

## Límites y reto

La evidencia funcional cubre los escenarios enumerados, con cero o una coincidencia.
No comprueba múltiples artículos disponibles en un almacén, orden entre varios
resultados, Unicode exhaustivo, rendimiento, concurrencia, reservas, autorización
ni producción. El sistema sólo usa SQLite en memoria.

**Reto no implementado:** crea otra copia de `estados/solucion/`, por ejemplo
`mi_reto`, y cambia sólo la llamada de `main()` para usar
`resumir_catalogo(opciones.almacen)`, omitiendo `opciones.nombre`. Antes de ejecutar,
predice qué criterio debería fallar: P05, porque la función permanece correcta pero
la terminal pierde el filtro. Los otros veinticinco deberían aprobar.

Comprueba tu predicción con `python mi_reto/pruebas.py` y
`python pruebas_resumen.py --directorio mi_reto`. Después redacta un encargo de
corrección acotado, restaura la transmisión del nombre y verifica 26/26. Evalúa el
reto por la predicción, el aislamiento del defecto en la frontera de terminal, la
diferencia revisable y las dos capturas de evidencia. No cambies datos ni expectativas.

## Evidencia y estados

APROBADO significa que se cumplió el criterio comprobado. FALLIDO indica que el
resultado no coincide; P04/P05 de la propuesta son los únicos fallos intencionales.
BLOQUEADO identifica una operación impedida. NO EJECUTADO indica que no se realizó.
Los criterios P de base se omiten porque la función aún no existe.

El informe `evidencia/RESULTADOS.md` distingue expectativas y observaciones. El
registro de acceso de Copilot explica qué interfaz no pudo utilizarse; no determina
la suscripción ni las capacidades de otra sesión del lector.
