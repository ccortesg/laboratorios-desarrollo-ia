# Revisión del cierre del laboratorio 8 desde WSL

**Versión:** 1.0. **Fecha de revisión:** 1 de noviembre de 2026.

**Dictamen: APROBADO para el cierre técnico y la publicación.** El archivo recibido es íntegro, sus registros son coherentes y la consulta independiente a GitHub confirma el commit, su árbol y las referencias publicadas. La ejecución funcional completa continúa acreditada por la evidencia histórica de Windows; este cierre no añade otra ejecución de esa batería. Los capítulos 1–8 siguen pendientes de revisión editorial del autor. [E1–E5]

## 1. Identidad del cierre confirmado

| Elemento | Identidad comprobada |
|---|---|
| Commit publicado | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |
| Árbol publicado | `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0` |
| Padre del commit publicado | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| Árbol corregido auditado previamente en Windows | `9ea6109fe8e89a2785bdce255252ffaabea1d122` |
| Referencias publicadas coincidentes | `main`, `lab-08-v1.0`, `repositorio-v1.4` |
| Referencias históricas | Once etiquetas conservan sus identidades anteriores |
| Fecha de consulta remota independiente | 2026-11-01, 20:48:55 UTC |

La consulta se realizó sobre el [repositorio sintético autorizado](https://github.com/ccortesg/laboratorios-desarrollo-ia). El [commit publicado](https://github.com/ccortesg/laboratorios-desarrollo-ia/commit/9212ee99b88f70f0b289837b88d6bbf34da91a52) tiene el árbol que ya declaraba el paquete de cierre original. Su único padre es el commit de partida confirmado. Los registros del autor y la consulta independiente coinciden en las trece etiquetas resultantes: las once anteriores y las dos nuevas. [E2, E3]

El árbol Windows y el árbol publicado son distintos porque el cierre incorpora documentación. El paquete original define ese cambio y su árbol final antes de la publicación. No se interpreta esta diferencia de árboles como un cambio funcional del laboratorio. [E2, E4]

## 2. Integridad del ZIP y procedencia del auxiliar

Se leyó directamente `EVIDENCIA_CIERRE_LAB08_WSL_01.zip`, sin ejecutar el código que contiene. Su SHA-256 observado es:

```text
0cc40f48d9ce456c9f88cc333fb5ec1a6614cc332b7ee43a10804a751198d37f
```

Coincide con el valor aportado por el autor. El ZIP contiene **116 archivos**; `SHA256_ARCHIVOS.json` cubre exactamente los otros **115**, sin archivos faltantes ni adicionales. Las 115 huellas coinciden con los bytes recibidos. Se comprobaron además la integridad CRC y la ausencia de nombres duplicados, rutas que salgan del paquete y enlaces simbólicos. [E1, E4, E5]

La copia `paquete_original/` contiene **27 archivos**: los 26 declarados en `SHA256SUMS` y el propio manifiesto. Se recuperó por separado la entrega original `CIERRE_LABORATORIO_08_v1.0.zip`, cuyo SHA-256 es `9b7326bfc365631765ae6f9213ecb7dce77454debcb6472b045f73020b9c62cd`. Los 27 archivos incorporados son idénticos, byte por byte, a esa entrega. Esto permite contrastar el auxiliar, el contrato y el parche con un antecedente independiente del ZIP recién recibido. [E2, E4]

Los seis enlaces de huellas entre configuración, manifiesto original, registro inicial, preparación, prepublicación y cierre también coinciden. No se normalizaron saltos de línea ni se recalcularon huellas históricas para hacerlas pasar. [E4, E5]

## 3. Operaciones efectivamente acreditadas

Hay **23 capturas de operaciones**: 22 terminaron con código cero y una conserva un fallo temporal resuelto. La secuencia registra preparación, revisión del índice, commit, consulta remota, incorporación de los antecedentes de `main`, avance rápido, comprobación previa a publicar, creación de las dos etiquetas y publicación. `registrar` queda acreditado además por su registro de comandos y por el resultado final. [E1, E4, E5]

La captura `operaciones/22_push_atomico/` conserva el comando siguiente con código de salida cero:

```bash
git push --atomic --no-follow-tags origin \
  refs/heads/main:refs/heads/main \
  refs/tags/lab-08-v1.0:refs/tags/lab-08-v1.0 \
  refs/tags/repositorio-v1.4:refs/tags/repositorio-v1.4
```

Su salida registra el avance de `main` y la creación de esas dos etiquetas. La consulta posterior capturada y la consulta independiente de esta revisión corroboran el resultado. El ensayo previo con `--dry-run` se distingue de esta publicación efectiva. El auxiliar `GESTIONAR_CIERRE_08.py` observó y registró las fases; los comandos mutadores se ejecutaron separadamente y tienen capturas propias. [E1, E3–E5]

El estado final local registrado es `main`, sin cambios pendientes ni archivos sin seguimiento. Esta afirmación corresponde al instante de la captura del autor; esta auditoría no inspecciona su ordenador en tiempo real. [E1]

## 4. Conservación del código y las evidencias

El contrato separa **25 rutas documentales** de **1.486 archivos protegidos**. Los mapas son disjuntos. Las capturas de preparación, revisión del índice y comprobación final declaran el cotejo satisfactorio de los contenidos y modos protegidos. El índice completo registra 549 rutas cambiadas respecto al commit de partida: incluye la integración del laboratorio 8 que ya estaba preparada, además del cierre documental. No deben confundirse esas 549 rutas con las 25 del incremento de cierre. [E1, E2, E5]

Esta revisión cotejó el mapa y las capturas con el paquete original, y comprobó que el árbol publicado coincide exactamente con el árbol documental previsto. **No recalculó de forma independiente los SHA-256 de los 1.486 blobs remotos.** La conclusión de conservación se apoya en la identidad del árbol Git, el contrato original y las comprobaciones capturadas; no se presenta como una nueva ejecución de ese cotejo sobre otra copia completa del repositorio. [E2–E5]

Se mantienen las distribuciones 1.0 y 1.0.1, las evidencias de los intentos previos y las once etiquetas históricas. `lab-08-v1.0` identifica la primera publicación del laboratorio 8 y contiene su distribución corregida 1.0.1. La presencia de la distribución original conserva la trazabilidad del defecto y su corrección. [E1–E3]

## 5. Entorno, pruebas y cifras que deben mantenerse separadas

| Actividad | Procedencia | Resultado o límite |
|---|---|---|
| Cierre y publicación | WSL2/Linux del autor | APROBADO; Git 2.34.1 y Python 3.10.12 para auxiliares |
| Ocho pruebas del recolector | Nueva captura WSL | APROBADO; ocho casos `ok`, resumen `OK` y salida cero |
| Batería funcional completa | Windows histórico ya auditado | 65 baterías, 583 ejecuciones, 571 aprobaciones y doce fallos didácticos previstos |
| Otros estados del conjunto Windows | Mismo antecedente | Cero bloqueos y errores de ejecución; 48 NO EJECUTADO y diez criterios ausentes aparte |
| Pruebas auxiliares Windows | Antecedente separado | Ocho del recolector, cuatro de recursos y nueve del evaluador; no se suman a las 583 |
| Nueva batería funcional completa en WSL | Cierre actual | NO EJECUTADO |
| Auditoría del ZIP y consulta remota | Esta revisión | APROBADO en su alcance documental; sin ejecutar scripts recibidos |

Las cifras funcionales proceden del antecedente Windows conservado en los estados y registros. Esta auditoría no vuelve a ejecutar esos casos ni convierte la preservación de código en una nueva ejecución en WSL. La captura de las ocho pruebas WSL del recolector constituye evidencia nueva y permanece separada. [E1, E4, E5]

El ajuste `git config --local core.filemode false` está registrado como modificación local de configuración, motivada por el montaje NTFS. El árbol final coincide con el previsto y las capturas de conservación no registran cambios de modo del índice fuera del contrato. No se deduce de este ajuste una nueva validación funcional entre sistemas operativos. [E1–E4]

## 6. Fallo temporal resuelto y cobertura de huellas

La captura 06 conserva un error `index.lock` con código 128. La captura 07 conserva el mismo refresco del índice con código cero. El resultado de la operación posterior queda acreditado y no hay un bloqueo pendiente. La explicación sobre qué proceso retenía el bloqueo procede del ejecutor; las capturas acreditan directamente el bloqueo y el reintento exitoso, sin identificar por sí mismas al propietario del lock. Este incidente no es uno de los fallos didácticos del catálogo. [E1, E5]

Los 23 comandos capturados conservan **46 archivos stdout/stderr** cubiertos por el manifiesto final. Las operaciones 08–23 declaran además huellas separadas de captura y resultado final: se comprobaron sus **32/32 huellas finales explícitas**. Las siete primeras operaciones conservan sus 14 flujos bajo el manifiesto general, pero no incluyen aquellas dos huellas separadas. `NOTAS_ENTORNO_Y_ALCANCE.md` lo declara expresamente. No se inventaron hashes de captura ausentes. [E1, E4, E5]

La coincidencia de una huella final comprueba los bytes guardados frente a su valor declarado. No permite reconstruir un flujo anterior al saneamiento cuando esos bytes originales no se conservan. Esta precisión no invalida el cierre ni sus referencias publicadas. [E4, E5]

## 7. Precisión documental que queda resuelta en esta continuidad

Los estados `ESTADO_DEL_LIBRO_v1.7.4.md`, `ESTADO_REPOSITORIO_v1.6.4.md` y el campo `metodo_subida` del resultado contienen una frase heredada del auxiliar que menciona una «salida de Git Bash». En esta ejecución, el entorno acreditado es **WSL2/Linux, bash y Git Linux**. Las notas ya explican la diferencia y las capturas la corroboran. [E1]

La referencia correcta para continuar es: **pruebas funcionales históricas en Windows; cierre y publicación posterior desde WSL2/Linux mediante la ejecución de Codex aportada por el autor**. Los documentos recibidos se conservan intactos y esta precisión se recoge en `CIERRE_LABORATORIO_08_CONFIRMADO_v1.0.md`. No es necesario repetir la publicación ni mover etiquetas por esta frase. [E1, E6]

Los estados 1.7.4 y 1.6.4 se generaron después de publicar y, por diseño, permanecen fuera del commit que describen. Son continuidad operativa vigente junto con esta revisión. Su incorporación posterior al repositorio debe hacerse como una adición documental, conservando los antecedentes. [E1, E6]

## 8. Continuidad y siguiente tarea

El cierre técnico queda confirmado. Para continuar deben utilizarse el maestro editorial v1.0, los estados 1.7.4 del libro y 1.6.4 del repositorio, este dictamen y el registro de cierre confirmado. El próximo trabajo puede preparar el capítulo 9, «Confiabilidad y seguridad del software generado por IA», a partir de la solución corregida del laboratorio 8. Antes de realizar nuevos cambios deberá reconsultarse `main` y conservar cualquier avance posterior al commit confirmado. [E6]

No hay una corrección funcional ni una publicación del laboratorio 8 pendiente derivada de esta revisión. Permanece pendiente la revisión editorial del autor de los capítulos 1–8. La aceptación de la integración y sus pruebas no equivale a aprobar los manuscritos. [E1, E6]

## Fuentes y evidencia incluidas

- **[E1]** ZIP recibido sin modificaciones: `insumos/EVIDENCIA_CIERRE_LAB08_WSL_01.zip`; registros `antes.json`, `preparado.json`, `prepublicacion.json`, `RESULTADO_CIERRE.json`, capturas `operaciones/`, estados y notas.
- **[E2]** Entrega original recuperada por separado, sin modificaciones: `insumos/CIERRE_LABORATORIO_08_v1.0.zip`; contrato `BASE_CIERRE.json`, mapa protegido, parche y manifiesto.
- **[E3]** Consulta independiente de GitHub: `auditoria/REFERENCIAS_REMOTAS_CONFIRMADAS.json`; APIs de referencia de `main`, listado de etiquetas y commit, consultadas el 1 de noviembre de 2026.
- **[E4]** Cotejo reproducible de esta revisión: `auditoria/AUDITAR_CIERRE.py` y `auditoria/RESULTADO_COTEJO_CIERRE.json`. Lee los archivos y la consulta conservada; al reproducirlo no vuelve a consultar GitHub.
- **[E5]** Segunda revisión independiente de sólo lectura: `auditoria/AUDITORIA_INDEPENDIENTE.json` y `.md`; 36 comprobaciones documentales aprobadas. No se suman a las métricas funcionales.
- **[E6]** Registro operativo nuevo: `CIERRE_LABORATORIO_08_CONFIRMADO_v1.0.md`.
