# Laboratorio 02 Contexto y arquitectura

Este paquete enseña a preparar información suficiente para retomar un trabajo con IA. Contiene un catálogo local ya corregido y un conjunto pequeño de documentos que explican su propósito, reglas, responsabilidades y estado. Los datos y escenarios son sintéticos; el ejercicio no se conecta a servicios externos.

## Qué vas a entregar

Al completar el recorrido podrás redactar un encargo que identifique qué existe, qué debe mantenerse, dónde comprobarlo y qué queda pendiente. La entrega de aprendizaje es un contexto revisable, un mapa mínimo y una nota de continuidad. El catálogo permite comprobar que preparar esa información no alteró los cuatro comportamientos heredados.

## Preparación

Usa Python 3.12 con `sqlite3` y `unittest` disponibles, un editor y una terminal. La ejecución incluida acredita las versiones de `evidencia/entorno.json`; otros entornos necesitan su propia comprobación. No hay paquetes adicionales que instalar ni cuentas que configurar.

Descomprime el ZIP y abre la terminal dentro de `laboratorio_02`, donde está este README. Conserva juntas las subcarpetas. `python` representa el intérprete: en tu equipo puede ser `python3` o `py -3`. Usa la misma variante en todos los comandos.

```text
python --version
python -c "import sqlite3, unittest; print(sqlite3.sqlite_version)"
```

Si falta un módulo necesario, registra la preparación como BLOQUEADO y utiliza una instalación que lo incluya antes de evaluar la lógica. Los scripts ejecutan SQLite en memoria y cierran la base después de cada consulta; no crean una base persistente.

## Recorrido

1. Lee solamente [el encargo insuficiente](contexto/ENCARGO_INSUFICIENTE.md). Anota qué información tendrías que recuperar antes de actuar. No inventes esa información ni cambies código todavía.
2. Lee [CONTEXTO](contexto/CONTEXTO.md), [ARQUITECTURA](contexto/ARQUITECTURA.md) y [DECISIONES](contexto/DECISIONES.md). Contrasta las afirmaciones con el SQL, los datos y las cuatro pruebas referenciadas. Sigue el caso A04 desde su dato hasta su exclusión.
3. Ejecuta el catálogo y la batería. Para ALFA, la expectativa es A01 y cuatro criterios aprobados:

```text
python laboratorio.py --version solucion --almacen ALFA
python pruebas.py --version solucion
python verificar.py --salida mi_evidencia
```

4. Revisa [CONTINUIDAD](contexto/CONTINUIDAD.md) y compara la evidencia incluida con la carpeta que acabas de crear. Conserva qué cambió, qué se ejecutó y qué sigue fuera del alcance.
5. Utiliza [el encargo con CLARO](contexto/ENCARGO_CLARO.md) para practicar la transferencia del contexto. Es un prompt didáctico; el paquete no acredita haberlo ejecutado en una herramienta comercial.

## Cómo evaluar el contexto

La revisión documental aplica seis criterios: K01, objetivo y estado actual; K02, reglas y cuatro criterios trazables; K03, responsabilidades y contrato; K04, límites y estados de implementación o propuesta; K05, ejecución y evidencia; K06, decisiones y continuidad. Revisa el significado y la coherencia. Contar palabras, archivos o encabezados no demuestra que el contexto sea suficiente. El registro separado de la lectura realizada para esta entrega está en `evidencia/revision_contexto.json`; no lo genera el verificador automático.

Puedes pedir a otra persona que explique, usando estos archivos, por qué A04 no aparece, dónde se aplica la ubicación, qué comando comprueba C04, qué arquitectura existe y cuál sería el siguiente paso. Si requiere datos ausentes, registra la carencia. Esta lectura no reemplaza las pruebas ni constituye una medición de productividad.

## Fuentes del ejercicio y adaptaciones

`datos/esquema.sql`, `datos/ejemplos.sql` y `solucion/consulta.sql` se copiaron sin cambios del laboratorio 1. Las cuatro funciones de prueba conservan literalmente sus cuerpos y aserciones. El ejecutor y la entrada de pruebas sólo admiten ahora `solucion`; se ajustaron sus textos y el valor inicial de selección. La consulta defectuosa no se distribuye en este paquete.

`evidencia/procedencia.json` conserva la comparación efectuada con el piloto. Esta comparación documenta la procedencia durante la preparación; la reproducción del laboratorio 2 no necesita descargar el piloto ni consultar archivos externos.

## Evidencia y estados

`verificar.py` requiere `--salida` y rechaza una carpeta que ya exista, para conservar ejecuciones anteriores. Utiliza un nombre nuevo, como `mi_evidencia_02`, para repetirlo. El script escribe entorno, resultados por criterio, salidas de consola, resumen y huellas SHA-256 de los trece archivos fuente y documentos.

El resultado será APROBADO cuando se ejecuten las cuatro pruebas sin fallos ni omisiones y la demostración devuelva A01. Un resultado distinto o una excepción durante una prueba será FALLIDO; una precondición ausente será BLOQUEADO; una actividad que no se realizó será NO EJECUTADO. La revisión del contenido documental se registra aparte: este script no comprende ni certifica la calidad del contexto.

Los hashes vinculan evidencia con archivos concretos; no certifican seguridad. Los tiempos de `unittest` no miden productividad. Usa los archivos de resultados de cada ejecución para sostener sus conclusiones.

## Límites

El laboratorio no implementa interfaz web, API HTTP, persistencia entre consultas, reservas, concurrencia, autenticación ni despliegue. Tampoco implementa el reto de cantidades solicitadas. La elección de Python y SQLite sirve a este ejercicio y no fija el stack de la aplicación futura. La ejecución local no acredita uso de Codex, GitHub Copilot o Grok Build.
