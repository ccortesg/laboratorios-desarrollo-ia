# Estado operativo · integración del laboratorio 9 preparada

**Versión documental:** 1.7. **Fecha:** 1 de noviembre de 2026. **Antecedente conservado:** `ESTADO_REPOSITORIO_v1.6.4.md`. **Integración técnica prevista:** 1.5, todavía no publicada.

## Base comprobada

Repositorio sintético autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

La reconsulta de sólo lectura del 1 de noviembre de 2026 a las 21:50:33 UTC confirmó:

| Elemento | Identidad observada |
| --- | --- |
| main, lab-08-v1.0 y repositorio-v1.4 | `9212ee99b88f70f0b289837b88d6bbf34da91a52` |
| Árbol de la base | `d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0` |
| Padre | `46f389bc4acf3e231a8eb1a1bb3972db0fe7e622` |
| Etiquetas existentes | Trece, conservadas; las dos previstas para el 9 estaban ausentes. |
| Rama local de preparación | `integracion/laboratorio-09` |

La terminal no pudo autenticar el clone HTTPS. La copia se recuperó mediante lecturas autorizadas de GitHub y objetos locales del mismo proyecto cotejados por su SHA Git. Los 1.511 archivos de la base y sus objetos coinciden; `git fsck --full --no-reflogs` terminó con cero. No se crearon commits sustitutos ni se cambiaron credenciales o proxies. La recuperación no altera la identidad de la base utilizada.

El árbol preparado y el SHA-256 del parche están en `BASE_INTEGRACION.json` del paquete. Ese registro y la evidencia de aplicación permanecen fuera del árbol descrito para evitar una referencia a su propia identidad. No se creó un commit nuevo, no se integró main, no se crearon ni movieron etiquetas y no se hizo push.

## Cambios incluidos

- Nuevo `laboratorios/laboratorio_09/`, autónomo: 292 archivos, tres estados, datos, contratos, contexto, prompts, diferencias, pruebas y evidencia.
- Distribución `LABORATORIO_09_v1.0.zip`, SHA-256 `6010765d31beab92b35447439864e5af0b321c99962b7bc692a0dacf66ecc17a`.
- Verificador común ampliado con las 27 baterías del laboratorio 9 y nueve regresiones focales del evaluador.
- Actualización de instrucciones, continuidad, procedencia, versiones, atributos y manifiesto de distribuciones.
- Incorporación documental exacta de los estados libro 1.7.4/repositorio 1.6.4, del cierre confirmado del 8 y de `REVISION_CIERRE_LABORATORIO_08_WSL_v1.0.zip`, antes entregados por separado.
- Evidencia nueva en `evidencia_integracion/laboratorio_09_v1.0/`; los antecedentes permanecen en sus rutas y con sus bytes originales.

El recolector `herramientas/huellas_evidencia.py` y sus ocho pruebas no cambian. Se cotejaron los 1.502 archivos existentes fuera de las nueve rutas comunes autorizadas para actualización: no hubo discrepancias. Este conjunto protegido incluye laboratorios 1–8, distribuciones, historiales y evidencia. El maestro editorial no cambia; manuscrito y Word siguen fuera del repositorio técnico.

## Contrato y fallos didácticos

La nueva política de GET `/api/resumen` conserva C/B/N/P/W/I/D y añade S01–S08: entradas válidas, duplicados, claves adicionales, límites, codificación, rechazo y recuperación en navegador, búsqueda literal y error interno genérico recuperable. La base es la solución corregida del laboratorio 8, con sus 62 casos ejecutados en los tres estados.

Base 9 conserva exactamente FALLIDO en S02.a/S02.b/S02.c, S03, S04.a/S04.b, S05.a/S05.b y S06. Esos nueve fallos indican requisitos nuevos ausentes, no regresiones del contrato anterior. La propuesta elimina repeticiones al construir un diccionario prematuramente y falla exclusivamente S02.a/S02.b/S02.c. La solución aprueba 74/74 casos. No se admiten excepciones de infraestructura como fallos esperados.

Los doce fallos históricos del conjunto 1–8 permanecen: C04 en inicial 1; B05/B06 en defecto 3; P04/P05 en propuesta 5; W05 en propuesta 6; I01/I07 en propuesta 7; D03/D04/D05/D08.a en propuesta 8. Los que requieren navegador se contabilizan sólo al ejecutarlo. El conjunto ampliado contiene 24 fallos didácticos exactos.

## Verificación nueva observada

Entorno: Linux, Python 3.12.14, SQLite 3.53.1, Git 2.51.1, Node 24.22.1, Playwright 1.62.1 y Chrome for Testing 151.0.7922.34. Se utilizó la versión prevista por Playwright descargada de su origen oficial alternativo; el CDN no había entregado un ZIP utilizable. Las pruebas accedieron sólo a la aplicación sintética local.

| Alcance | Resultado |
| --- | --- |
| Autónomo final | APROBADO, código 0; 27 baterías; 222 ejecuciones; 210 APROBADO y 12 FALLIDO previstos; 54/54 huellas. |
| Conjunto 1–9 | APROBADO, código 0; 92 baterías; 805 ejecuciones; 781 APROBADO; 24 FALLIDO previstos; cero bloqueos. |
| Omisiones por alcance histórico | 48 NO EJECUTADO en baterías y diez criterios ausentes aparte. |
| Huellas del conjunto funcional | 156/156 coinciden con los bytes finales. Las cuatro huellas de sus capturas externas se cuentan aparte. |
| Infraestructura | Ocho pruebas del recolector, nueve del evaluador y cuatro de recursos SQLite APROBADO, separadas de las cifras funcionales. |
| ZIP nuevo descomprimido | APROBADO; 292 archivos idénticos después de ejecutar; reprodujo 222/210/12 y 54/54 huellas funcionales. |

Se conservan el primer autónomo FALLIDO y los diagnósticos de dos TimeoutExpired inesperados. La observación S06 se corrigió sin cambiar la aplicación ni sus expectativas: HTTP, DOM, controles y recuperación siguen exigidos; el cuerpo JSON exacto se comprueba por HTTP en S04.a. No se atribuye la causa interna a una versión de navegador. La cronología y diferencias están en `laboratorios/laboratorio_09/evidencia/INDICE.md`.

Las huellas capturadas y finales permanecen diferenciadas. No se reescribieron ni recalcularon evidencias históricas para cambiar sus conclusiones. El subconjunto 1–8 se ejecutó otra vez en Linux; sus 583 resultados coinciden numéricamente con el antecedente Windows, pero son registros distintos. La publicación WSL del laboratorio 8 sigue siendo un cierre documental anterior, sin nueva batería funcional atribuida a él.

## Paquete de integración y siguiente operación

`INTEGRACION_LABORATORIO_09_v1.0.zip` reúne parche, base registrada, manifiesto SHA-256, verificador de cobertura, instrucciones exactas para Git Bash y auxiliares de registro, ejecución y empaquetado. Incluye el prompt para Codex, los estados, la evidencia y el ensayo de aplicación sobre una copia limpia. El ensayo del parche y sus capturas son posteriores al árbol preparado y se conservan en el paquete, sin incorporarlas recursivamente al propio parche.

El auxiliar de ejecución exige observar 8/9/4 pruebas de infraestructura, respectivamente, además del conjunto completo y sus huellas. Conserva el código de salida original de cada proceso y rechaza omisiones aunque exista una salida cero. El procedimiento crea una rama condicionalmente; un nombre de rama ya ocupado no permite avanzar main por accidente.

**NO EJECUTADO:** nueva ejecución Windows/WSL del laboratorio 9, integración en main, etiquetas nuevas, push, GitHub Actions y uso comercial nuevo de Codex/Copilot/Grok Build. `lab-09-v1.0` y `repositorio-v1.5` son sólo nombres previstos. No existe una evaluación integral de seguridad productiva ni una implementación del reto de cabeceras.

El siguiente encargo debe aplicar y verificar en el entorno real del autor, preservar avances posteriores de main y entregar evidencia nueva para revisión. Un árbol adaptado a una base avanzada requiere su propia revisión y comprobación; no se fuerza la identidad del árbol antiguo. La publicación se autorizará por separado. Los capítulos 1–9 siguen pendientes de revisión editorial y no se redactó el capítulo 10.
