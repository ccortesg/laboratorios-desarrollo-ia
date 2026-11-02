# Guía para lectores

Material de acompañamiento de **Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro**. Los diez ejercicios son locales y sintéticos. Empieza por la [ficha 1](laboratorio_01.md); no necesitas verificar todo el repositorio para comenzar.

| Capítulo y ficha | Versión recomendada | Descarga fijada a commit |
| --- | --- | --- |
| [01 · El nuevo oficio del desarrollador: del código al resultado](laboratorio_01.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_01_v1.0.zip) |
| [02 · Contexto y arquitectura: preparar el terreno para la IA](laboratorio_02.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_02_v1.0.zip) |
| [03 · Ingeniería de prompts para generar, refactorizar y depurar](laboratorio_03.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_03_v1.0.zip) |
| [04 · Codex en acción: trabajar sobre un repositorio real](laboratorio_04.md) | 1.1 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_04_v1.1.zip) |
| [05 · GitHub Copilot: de la sugerencia al trabajo delegado](laboratorio_05.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_05_v1.0.zip) |
| [06 · Grok Build: de la idea a una aplicación de extremo a extremo](laboratorio_06.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_06_v1.0.zip) |
| [07 · Datos e integraciones: cuando los sistemas deben ponerse de acuerdo](laboratorio_07.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_07_v1.0.zip) |
| [08 · Depuración con evidencia: investigar errores entre entornos y servicios](laboratorio_08.md) | 1.0.1 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_08_v1.0.1.zip) |
| [09 · Confiabilidad y seguridad del software generado por IA](laboratorio_09.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_09_v1.0.zip) |
| [10 · Automatización, agentes y operación: prepararse para lo que sigue](laboratorio_10.md) | 1.0 | [ZIP](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_10_v1.0.zip) |

El laboratorio 8 recomienda **1.0.1**; 1.0 conserva su condición de antecedente. El laboratorio 4 utiliza el preparador Git del repositorio completo. Los diez títulos se cotejaron con el índice del maestro editorial 1.0 y los encabezados de los capítulos 2–5 facilitados por el autor.

Cada ZIP es autónomo. Desde su raíz sigue los comandos de su ficha; para practicar conserva los originales y usa una carpeta nueva. Las fichas distinguen el primer recorrido de los ensayos completos de navegador. Los laboratorios 1–3 no requieren Git ni Node; el 4 requiere Git; el 5 sólo Python estándar; el 6 añade navegador manual; del 7 al 10 se requiere Python 3.11+. La automatización web requiere Node 20+, Playwright y Chromium según el README técnico, con descargas públicas durante la preparación.

## Descargas, acceso y QR

El [mapa único](mapa_laboratorios.json) registra versiones, SHA-256, commit del ZIP y destinos. Comprueba el hash del archivo descargado antes de extraerlo. Los QR abren la guía mantenible bajo main, que ofrece instrucciones y descarga fija; conservaremos las diez rutas para el libro. Las fichas también contienen enlaces de texto. No hay acortadores ni seguimiento.

**Visibilidad observada el 2 de noviembre de 2026: privada.** Una decodificación correcta del QR no prueba acceso anónimo. La lectura autenticada se comprueba por separado; el acceso anónimo queda pendiente de una futura apertura autorizada. GitHub puede pedir iniciar sesión para descargar los ZIP.

## Resultados y evidencia

Lee los resultados esperados de tu ficha antes de ejecutar. Los defectos didácticos siguen FALLIDO; la verificación puede aprobar el recorrido porque reproduce el patrón exacto. Un fallo adicional o un error de ejecución es un problema pendiente, no otro ejemplo aceptado. Guarda siempre tu evidencia en una carpeta nueva. Los resultados históricos y los ensayos locales nuevos tienen atribuciones separadas; ninguno implica uso de Codex, Copilot o Grok Build sin su evidencia específica.

## Correcciones y soporte

Consulta primero [VERSIONES](../../VERSIONES.md), [CONTINUIDAD](../../CONTINUIDAD.md), la ficha correspondiente y las notas de corrección del laboratorio. Las expresiones de cierre preparado en esos documentos son antecedentes de sus fechas; el [estado de preparación actual](../publicacion/ESTADO_PREPARACION_PUBLICA_v1.0.md) explica la base consultada.

Puedes consultar o comunicar una incidencia mediante [Issues del repositorio](https://github.com/ccortesg/laboratorios-desarrollo-ia/issues) cuando tu acceso lo permita. Indica laboratorio, versión, sistema, versión de Python, comando, salida esperada y observada, código de salida y una reproducción sintética. Omite credenciales y datos personales. No se promete un plazo de respuesta ni se asigna un responsable inexistente. Esta preparación no abrió incidencias ni envió mensajes.

La licencia sigue pendiente de decisión del autor. Preparar estas guías no concede una licencia nueva ni equivale a declarar el proyecto open source. Los capítulos 1–10 continúan pendientes de revisión editorial.
