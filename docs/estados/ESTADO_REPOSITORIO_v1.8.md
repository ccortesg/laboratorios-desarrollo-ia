# Estado operativo · laboratorio 10 preparado para revisión

**Versión:** 1.8. **Fecha:** 2 de noviembre de 2026, UTC. **Antecedente vigente recibido:** ESTADO_REPOSITORIO_v1.7.3.md. Estado editorial asociado: ESTADO_DEL_LIBRO_v1.9.md; maestro 1.0 sin cambios.

## Base y referencias

Repositorio sintético autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

| Identidad | Valor utilizado |
| --- | --- |
| Commit de partida | `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3` |
| Árbol de partida | `790e875fc95495c39ea2b5ebe7621a4ae1afa30f` |
| Rama local de preparación | `integracion/laboratorio-10` |
| Reconsulta remota | 2026-11-02 00:20:41 UTC; main sin avance respecto a la consulta inicial de 00:00:29 UTC. |
| lab-09-v1.0 y repositorio-v1.5 | Conservan el commit de partida. |
| Quince etiquetas existentes | Identidades conservadas; consultas de lectura. |
| lab-10-v1.0 / repositorio-v1.6 | Nombres previstos, ausentes y pendientes de creación posterior. |

GitHub se utilizó como fuente de lectura. El transporte Git CLI no estaba disponible con autenticación en este entorno; se recuperó la base mediante objetos locales previos y el conector autorizado de lectura, comprobando el commit y árbol exactos. Se conservó el límite de historia superficial de la copia; no se inventaron padres ni metadatos Git. El parche utiliza el contenido de la base exacta, no un snapshot aproximado. La recuperación y sus límites están documentados en la auditoría de producción.

## Cambios preparados

Se añade laboratorio_10 autónomo, distribución 1.0, contexto, contrato previo, propuesta y solución, ocho casos T, recibos y evidencia nueva. Se amplía herramientas/verificar_todo.py, se añaden nueve regresiones de su evaluador para el 10 y se actualizan las referencias de continuidad y procedencia. Los 17 archivos de solución 9 coinciden en los tres estados; propuesta/solución sólo añaden operar.py. El manifiesto autónomo contrasta además 71 archivos heredados. El recolector herramientas/huellas_evidencia.py y sus ocho pruebas se conservan exactos.

El incremento ejecuta acciones fijas mediante Python, sin shell ni comandos de modelos. La única diferencia didáctica entre operadores es continuar o detenerse después del rechazo del importador. No se amplía el servicio web; T08 mantiene un servidor vivo y comprueba en Chromium los datos de la misma SQLite modificada por el operador.

Se incorporan exactos los documentos posteriores al cierre 9, estados 1.8.3/1.7.3, CIERRE_LABORATORIO_09_CONFIRMADO_v1.0.md y REVISION_CIERRE_LABORATORIO_09_WSL_v1.0.zip. Sus antecedentes de preparación permanecen intactos y rotulados como históricos. El control de conservación contrasta 2.285 archivos protegidos de la base; no se sustituyen los laboratorios 1–9, distribuciones, historial, estados ni evidencias anteriores. El manifiesto de distribuciones añade la entrada nueva conservando su prefijo anterior.

Distribución nueva: **LABORATORIO_10_v1.0.zip**, 450 archivos; SHA-256 `5e39d5fb92e2408684003809d65f753b16929c7ad649e70f1c8eec0e26eb54f3`.

## Verificación nueva

| Alcance | Resultado |
| --- | --- |
| Autónomo con navegador | APROBADO, salida 0: 33 baterías, 238 ejecuciones, 237 aprobaciones, T02 FALLIDO esperado, ocho NO EJECUTADO en base, cero bloqueos/errores. |
| Solución 10 | 82/82 APROBADO; 64 criterios distintos. |
| Conjunto 1–10 con navegador | APROBADO, salida 0: 125 baterías, 1.043 ejecuciones, 1.018 aprobaciones, 25 fallos didácticos, cero bloqueos; 56 NO EJECUTADO y diez ausentes aparte. |
| Huellas de salidas | Autónomo 116/116; conjunto 272/272; comprobación independiente de lectura APROBADO. |
| ZIP descomprimido | APROBADO: ejecución real completa con navegador, patrón idéntico y 116/116 huellas. |
| Infraestructura | Recolector 8, evaluador 9: 9, evaluador 10: 9, recursos SQLite: 4, RO01: 1 método con dos estados; APROBADO por separado. |
| Revisión independiente | APROBADO: contrato, casos, identidades, código, fuentes ejecutadas y evidencia. Observación menor de continuidad del README resuelta. |

Los 25 fallos didácticos son los 24 de los nueve laboratorios anteriores, acotados a sus estados históricos, más T02 en propuesta 10. En los tres estados del 10 todos los casos S heredados deben aprobar. Las baterías conservan FALLIDO individualmente; no aceptan errores de ejecución como sustituto del defecto. Los totales son ejecuciones repetidas por estado, no una cantidad de requisitos únicos.

La infraestructura, las focales de desarrollo, la revisión de cinco bloques CLI del capítulo y los ensayos de empaquetado son registros separados. Las 805 ejecuciones WSL históricas y el cierre WSL posterior conservan su atribución. La ejecución nueva del subconjunto 1–9 coincidió en sus recuentos, pero se ejecutaron otra vez sus procesos. No se suman ensayos para aparentar más cobertura.

## Paquete y reproducción

INTEGRACION_LABORATORIO_10_v1.0.zip incluye el parche binario, BASE_INTEGRACION.json, SHA256SUMS, verificador de cobertura, auxiliares de registro/verificación/empaquetado, evidencia y guía exacta de Git Bash. Incluye también PROMPT_INTEGRACION_CODEX_LAB10_v1.0.md. El árbol preparado, las rutas y el hash del parche se registran fuera del propio árbol para evitar autorreferencias. La auditoría externa del paquete documenta su aplicación sobre copia limpia y el resultado compuesto que efectivamente se ejecutó.

El procedimiento utiliza salidas nuevas. Comprueba el paquete y la ascendencia; compara main y etiquetas; prepara una rama que conserve avances; distingue git apply --check --index de la aplicación real; verifica infraestructura y conjunto con navegador; comprueba todas las huellas declaradas y empaqueta evidencia. Una base avanzada puede requerir adaptación y revisión semántica; no se sustituye BASE_INTEGRACION.json para aparentar identidad. Ningún auxiliar fuerza referencias ni descarta cambios.

Entorno nuevo: Linux, Python 3.12.14, SQLite 3.53.1, Git 2.51.1, Node 24.22.1, Playwright 1.62.1, Chrome for Testing 151.0.7922.34. Windows nativo y la futura sesión del autor en Codex están NO EJECUTADO aquí. Las instrucciones se preparan para esos entornos sin atribuirles este ensayo.

## Límites y punto de cierre

No se creó un commit nuevo de producción, no se integró en main, no se crearon o movieron etiquetas ni se hizo push. El futuro cierre necesita su propio encargo y consultas remotas actualizadas. No hay bloqueos pendientes de las comprobaciones funcionales ejecutadas. La operación local presupone ejecución secuencial; no demuestra concurrencia, fallos físicos, autenticación ni producción. Timeout revisado en código, no inducido como caso nuevo. Un resultado sin confirmación no garantiza ausencia de efectos; no hay transacción global ni reintentos automáticos.

Los capítulos 1–10 siguen pendientes de revisión editorial. Próxima tarea: ejecutar el prompt de integración en Codex sobre la copia del autor, entregar el ZIP de evidencia y auditarlo antes de autorizar cualquier publicación.
