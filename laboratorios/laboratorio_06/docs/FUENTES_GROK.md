# Fuentes oficiales y alcance de las afirmaciones sobre Grok Build

Consulta editorial y nueva consulta de las fuentes: **31 de octubre de 2026 (UTC)**, conforme al contexto vigente del cliente. El registro inicial de acceso mantiene su timestamp y la corrección de fecha editorial está documentada por separado.

## Modalidad recomendada para el recorrido didáctico

**Interpretación editorial:** el agente de terminal resulta la modalidad principal más congruente con este laboratorio, porque el encargo parte de archivos Python y SQL, conserva pruebas existentes y exige revisar cambios. La experiencia web/móvil se presenta como otra modalidad documentada. No se ha observado una sesión de generación en ninguna de ellas. Esta elección pedagógica no acredita acceso comercial.

## F1 Grok Build overview

- Título: **Grok Build**.
- URL: https://docs.x.ai/build/overview
- La documentación presenta un agente con interfaz de terminal interactiva, uso sin interfaz interactiva y soporte ACP para integración con otras aplicaciones. El comando mostrado para iniciar la terminal es `grok` desde la carpeta del proyecto. También documenta `grok -p` para un encargo y formatos de salida.
- Límite: la presencia de esas instrucciones no prueba que el ejecutable, la autenticación o un modelo concreto estén disponibles en el entorno del lector. No trasladar capacidades de esa terminal al constructor web.

## F2 Grok Build on web and mobile

- Título: **Grok Build on web and mobile**.
- URL: https://x.ai/news/grok-build-for-everyone
- Fecha de publicación mostrada: **19 de agosto de 2026**.
- El anuncio describe construir aplicaciones desde una conversación en web, iOS y Android. Enumera publicación mediante enlace y exportación a GitHub, entre otras funciones.
- Límite: es una descripción pública de la modalidad web/móvil. No acredita la disponibilidad efectiva en una cuenta, una exportación realizada ni que un proyecto Python pueda trasladarse sin adaptación. En este encargo no se publica ni se exporta a GitHub desde el servicio.

## F3 Reglas del proyecto

- Título: **AGENTS.md**.
- URL: https://docs.x.ai/build/features/project-rules
- Última actualización mostrada: **4 de julio de 2026**.
- La documentación del agente describe archivos Markdown de reglas del proyecto, incluidos `AGENTS.md`, para convenciones, comandos de construcción y pruebas, y notas de arquitectura. Describe alcance por subárbol y un comando `grok inspect` que informa sobre las reglas encontradas.
- Uso pedagógico: relacionar el paquete de contexto del libro con un punto de entrada persistente que remite al contrato y a los comandos del laboratorio. No afirmar que esas reglas sustituyen la revisión ni que el agente las obedeció en esta producción.

## F4 Modo de planificación

- Título: **Plan Mode**.
- URL: https://docs.x.ai/build/features/plan-mode
- Última actualización mostrada: **21 de julio de 2026**.
- La documentación presenta `/plan` para explorar y proponer un plan antes de pasar a las ediciones. La revisión del plan tiene su propia interfaz.
- **Matiz que debe conservarse:** la sección de advertencias limita las herramientas de edición, pero aclara que esto no constituye una barrera para todas las escrituras: la terminal sigue sus permisos y puede escribir mediante redirecciones; los subagentes no heredan ese bloqueo específico de edición. Por tanto, no escribir que “plan mode garantiza que nada cambia” ni usarlo como control de seguridad general.

## F5 Permisos y sandbox

- Título: **Permissions**.
- URL: https://docs.x.ai/build/features/permissions
- Última actualización mostrada: **21 de julio de 2026**.
- Distingue las decisiones de autorización para invocar herramientas de las restricciones del sandbox sobre archivos y red. Describe varios modos de autorización y reglas de permitir/denegar.
- Uso pedagógico: el contrato debe delimitar el trabajo y el entorno debe acotar sus capacidades. No aconsejar desactivar aprobaciones o ampliar permisos para completar este laboratorio. No se cambió configuración alguna durante la comprobación de acceso.

## F6 Ejecución no interactiva

- Título: **Headless & Scripting**.
- URL: https://docs.x.ai/build/cli/headless-scripting
- Última actualización mostrada: **10 de junio de 2026**.
- Documenta `grok -p "..."`, selección de directorio y salidas `plain`, `json` y `streaming-json`. También describe ACP como un canal diferente para integrar el agente con otras herramientas.
- Límite: un archivo JSON producido por las pruebas del laboratorio no es una salida de Grok. La posibilidad documentada de emitir eventos no acredita que se capturaran eventos comerciales en esta entrega.

## Criterios de redacción y citas

Estas fuentes se utilizan para afirmaciones concretas y breves. La mayor parte del capítulo debe explicar el laboratorio y el criterio del desarrollador con material original. No reproducir las páginas ni extensos fragmentos. Conservar bibliografía breve con URL y fecha de consulta; colocar la referencia junto a la afirmación respaldada.

No se investigaron precios ni se confirmó una suscripción del autor. El estado de acceso observado está en `../evidencia/acceso_grok.json`. Una página pública del producto y una pantalla genérica de chat no acreditan una sesión de Grok Build.
