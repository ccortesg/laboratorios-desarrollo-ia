# Auditoría independiente de evidencia Windows corregida

## Dictamen

**APROBADO para el alcance funcional y la identidad preparada acreditados por la evidencia recibida.** La ejecución Windows fue realizada por el autor. Esta auditoría releyó y comprobó sus archivos; no ejecutó nuevamente las pruebas funcionales en Windows ni ejecutó código incluido en el ZIP.

## Identidad e integridad

- ZIP: `EVIDENCIA_CORRECCION_LAB08_WINDOWS_02.zip`.
- SHA-256: `2e8503f199f85184ef55de2c8808cda7b358e4dd75554a03371be51b4d7b1445`.
- 254 archivos, sin entradas repetidas ni rutas inseguras.
- Manifiesto: 253/253 hashes coincidentes; el archivo 254 es el propio manifiesto, excluido justificadamente de su cobertura.
- Salidas del conjunto: 102/102 SHA-256 coincidentes con los bytes recibidos.
- Capturas auxiliares: 10/10 SHA-256 coincidentes, contabilizadas aparte.
- 112 campos de hash capturado presentes; en esta ejecución coinciden con sus hashes finales. Se compararon los bytes sin normalizar LF/CRLF.
- El mapa de 244 hashes del antecedente coincide exactamente con los 244 archivos del diagnóstico Windows fallido aportado anteriormente.

## Resultados funcionales cotejados

Se contrastaron las 65 entradas del resumen con los respectivos JSON de casos, utilizando sus IDs y estados individuales. Resultado: 631 registros, de los cuales 583 se ejecutaron: 571 APROBADO y 12 FALLIDO; 48 NO EJECUTADO. No hay BLOQUEADO, IDs repetidos ni errores de ejecución. Los diez criterios N ausentes en el inicio del laboratorio 4 se registran aparte.

Los doce fallos son exactamente C04 del inicial1; B05/B06 del defecto3; P04/P05 de propuesta5; W05 de propuesta6; I01/I07 de propuesta7; D03/D05/D08.a de propuesta8 y D04 de propuesta8 navegador. Todos los FALLIDO corresponden a AssertionError; no se toleró ningún fallo adicional.

Pruebas auxiliares: ocho del recolector, cuatro de recursos y nueve del evaluador; cada captura termina en OK, con el recuento esperado, sin omisiones y código 0. Se mantienen fuera de los totales funcionales.

D04 de solución contiene observación del mismo servidor vivo antes y después de importar por CLI a la base persistente: ALFA pasa de A01 (1 artículo) a A01+A03 (2 artículos); BETA queda vacío; la búsqueda devuelve A03. La importación registra cuatro filas leídas, validadas y aplicadas; el estado final SQLite coincide. Ya no aparecen PermissionError, WinError32 ni Criterio duplicado en la evidencia nueva del laboratorio8.

## Entorno e identidad Git

Windows; Python3.11.9; SQLite3.45.1; Git2.45.1.windows.1; Node20.20.0; Playwright1.62.1; Chromium151.0.7922.34. El registro final es 2026-11-01T05:48:21.061312Z, equivalente al 31 de octubre de 2026, 22:48:21 en Hermosillo.

La identidad inicial y final coinciden: rama integracion/laboratorio-08; HEAD y main46f389bc4acf3e231a8eb1a1bb3972db0fe7e622; índice9ea6109fe8e89a2785bdce255252ffaabea1d122; sin modificaciones sin preparar. Las once etiquetas locales coinciden con el antecedente original. No acredita todavía commit, integración en main, nuevas etiquetas ni push.

## Fuentes y límites

301 declaraciones de hash de fuentes coinciden con bytes de la copia local corregida, incluidas77 del laboratorio8. El cotejo abarca las fuentes declaradas en sha256_fuentes de los laboratorios1,2,3,5,6,7,8; los archivos Git del laboratorio4 requieren la auditoría específica de su propio formato y no se sumaron aquí. Los resúmenes y casos del laboratorio4 sí se revisaron al cotejar las65 baterías.

No se consultó el remoto, no se modificó el repositorio y no se modificaron los ZIP. La conservación de evidencia previa durante la ejecución es declarada por el auxiliar y respaldada por un mapa de hashes coincidente con el archivo histórico recibido; el ZIP actual no vuelve a incluir todos esos bytes históricos. Los manuscritos siguen pendientes de revisión editorial. No se acredita una ejecución comercial ni GitHubActions, producción, seguridad integral o rendimiento.
