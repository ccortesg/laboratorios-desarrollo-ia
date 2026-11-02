# PROMPT_CAPITULO_10_v1.0

Continuemos con la décima etapa de producción del libro:

“Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro”.

Completa el capítulo 10: **“Automatización, agentes y operación: prepararse para lo que sigue”**. Construye primero su laboratorio autónomo, ejecuta las comprobaciones y redacta después el capítulo a partir de los resultados observados. Termina con la integración local preparada para revisión.

## 1. Recupera la continuidad y comprueba la base

Localiza y lee:

- DOCUMENTO_MAESTRO_EDITORIAL_v1.0.md.
- ESTADO_DEL_LIBRO_v1.8.3.md.
- ESTADO_REPOSITORIO_v1.7.3.md.
- CIERRE_LABORATORIO_09_CONFIRMADO_v1.0.md.
- REVISION_CIERRE_LABORATORIO_09_WSL_v1.0.zip.
- CAPITULO_09_v1.0.md, CAPITULO_09_v1.0.docx y LABORATORIO_09_v1.0.zip.

Revisa también las instrucciones del repositorio, su continuidad, el contexto del laboratorio 9 y los verificadores comunes. Los estados posteriores al cierre y su revisión se entregaron por separado: no presupongas que estén dentro de GitHub. Busca entre los archivos disponibles y el repositorio autorizado; no inventes insumos ni sustituyas versiones silenciosamente. Si falta alguno, completa el trabajo independiente y documenta el bloqueo concreto.

Repositorio sintético autorizado: https://github.com/ccortesg/laboratorios-desarrollo-ia

Último cierre confirmado:

- Commit: `6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3`.
- Árbol: `790e875fc95495c39ea2b5ebe7621a4ae1afa30f`.
- `main`, `lab-09-v1.0` y `repositorio-v1.5` coincidían con ese commit.
- Las trece etiquetas anteriores conservaron su identidad.

Consulta nuevamente las referencias remotas. Registra fecha, commit, árbol y referencias utilizados. Si `main` avanzó, conserva sus cambios y adapta el trabajo sin retroceder ramas ni forzar referencias.

## 2. Define un incremento de automatización acotado

Parte de la solución del laboratorio 9. Conserva los contratos heredados, los datos de referencia y el recorrido real:

**CSV → importador CLI → SQLite persistente → HTTP → navegador.**

Elige un incremento pequeño que enseñe a automatizar una operación repetible con límites claros, detenerse ante un fallo y producir evidencia útil para continuar o investigar. Debe aportar un comportamiento comprobable; no basta con renombrar el verificador existente ni describir una plataforma futura.

Antes de implementarlo, documenta objetivo, entradas, precondiciones, acciones permitidas, estado afectado, criterios de aceptación, casos negativos y comportamiento ante errores. Define qué requiere intervención humana y qué queda fuera. Evita ejecutar instrucciones arbitrarias procedentes de datos o respuestas de un modelo.

Mantén una base identificable, una propuesta con un defecto didáctico acotado y una solución. Explica el defecto antes de introducirlo. Ejecuta las mismas comprobaciones pertinentes sobre propuesta y solución; conserva el fallo que demuestra el problema.

Prioriza herramientas estándar y pocas dependencias. No incorpores servicios externos, credenciales, despliegues ni consumo comercial. Distingue una automatización determinista de un agente que decide acciones; no presentes como agente comercial una secuencia local de comandos.

## 3. Conserva contratos y verifica resultados

Revisa los identificadores y subcasos reales del laboratorio 9 antes de ampliar las pruebas. Su solución acreditaba 74 casos: 62 heredados y 12 de seguridad. Conserva esas expectativas sobre datos intactos y añade únicamente comprobaciones necesarias para el incremento, con datos y directorios aislados.

Amplía la verificación conjunta e incluye navegador cuando el entorno lo permita. Conserva el recolector de huellas y ejecuta sus ocho pruebas existentes. Comprueba los bytes finales guardados después del saneamiento, distinguiendo hashes capturados y finales. No reescribas evidencia anterior.

Calcula los nuevos totales a partir de los registros. La referencia histórica WSL es: 92 baterías, 805 ejecuciones, 781 APROBADO, 24 FALLIDO didácticos, cero bloqueos y errores de ejecución; 48 NO EJECUTADO en baterías y diez criterios ausentes aparte. El cierre posterior volvió a ejecutar las ocho pruebas existentes del recolector; no repitió las 805 funcionales.

Mantén separadas pruebas funcionales, infraestructura, auditorías, evidencia histórica y ejecuciones nuevas. Clasifica APROBADO, FALLIDO, BLOQUEADO o NO EJECUTADO. Admite únicamente los fallos didácticos expresamente definidos. Si falta una comprobación, documenta su alcance y no declares aprobado el conjunto completo.

## 4. Redacta el capítulo después del laboratorio

Conserva promesa, principio rector, público, índice, método CLARO y voz del maestro. Redacta aproximadamente 3.500–5.000 palabras con estas secciones:

1. La situación que reconocerás.
2. Crónica de Adopción Real.
3. Qué aprenderás y qué entregarás.
4. El criterio técnico.
5. Preparación del laboratorio.
6. CLARO en acción.
7. El resultado que parecía correcto.
8. Evidencia y revisión.
9. Llévalo a tu trabajo.
10. Reto y recursos reutilizables.

Incluye una crónica de 400–700 palabras, rotulada como reconstrucción narrativa sintética, con un desarrollador experimentado. Introduce los conceptos antes de exigirlos; desarrolla un encargo insuficiente y su mejora con CLARO, el recorrido práctico completo y un reto acotado con criterios de evaluación, sin implementarlo.

Explica cómo delegar trabajo, limitar acciones, reconocer fallos, conservar decisiones y operar con evidencia. Identifica prompts didácticos y respuestas simuladas. Distingue implementación, propuestas de evolución y uso comercial realmente acreditado. Consulta fuentes primarias cuando corresponda, fecha las consultas y coloca las referencias junto a sus afirmaciones.

## 5. Prepara entregables e integración local

Entrega:

- CAPITULO_10_v1.0.md.
- CAPITULO_10_v1.0.docx.
- LABORATORIO_10_v1.0.zip.
- ESTADO_DEL_LIBRO_v1.9.md.
- ESTADO_REPOSITORIO_v1.8.md.
- INTEGRACION_LABORATORIO_10_v1.0.zip.

Renderiza e inspecciona el Word completo. Comprueba realmente la ejecución del laboratorio desde el ZIP descomprimido y la aplicación del parche sobre una copia limpia de la base registrada.

Incluye en la integración manifiesto SHA-256, verificador, evidencia saneada e instrucciones exactas para Git Bash de Windows, con dependencias de navegador, pruebas del recolector, verificación conjunta y comprobación de huellas. Prepara también un encargo de integración para Codex que preserve cambios y distinga preparación de publicación.

Incorpora documentalmente la continuidad confirmada del laboratorio 9 conservando antecedentes. Actualiza el maestro sólo por una decisión editorial justificada. Revisa coherencia entre requisitos, código, pruebas y texto, reproducibilidad, anonimización y claridad pedagógica. Guarda los entregables y proporciona enlaces descargables.

## 6. Respeta el punto de cierre

Trabaja exclusivamente con materiales sintéticos, en una copia local y una rama identificable. Utiliza GitHub como fuente de lectura. No accedas a sistemas productivos ni repositorios privados. **No integres en `main`, no crees ni muevas etiquetas y no hagas push.**

Los capítulos 1–9 siguen pendientes de revisión editorial del autor. La entrega del capítulo 10 tampoco constituye aprobación del manuscrito completo ni autorización para publicarlo.

Completa las decisiones rutinarias con autonomía. En la respuesta final explica qué quedó terminado, qué se ejecutó, qué límites permanecen y cómo continuar la integración con Codex. No amplíes este encargo a la edición final ni a la publicación del libro.
