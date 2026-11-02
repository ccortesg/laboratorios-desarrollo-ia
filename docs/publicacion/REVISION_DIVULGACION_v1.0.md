# Revisión para divulgación · v1.0

**Fecha: 2 de noviembre de 2026. Alcance: sólo este repositorio sintético autorizado.** La revisión apoya la preparación; no autoriza cambiar visibilidad ni demuestra ausencia absoluta de datos sensibles.

## Método y cobertura

Se enumeran las referencias de ramas locales, remotas y etiquetas consultadas, y todos sus objetos alcanzables mediante for-each-ref, rev-list --objects y cat-file --batch. Se examinan blobs y metadatos de commits y etiquetas; se conserva el inventario de referencias y huellas en la entrega. No se modifican objetos, referencias ni el historial.

Se recorren recursivamente los ZIP, incluidos paquetes históricos, correcciones y evidencias anidadas, sus nombres, comentarios y campos adicionales. Se deduplica el contenido por SHA-256. Los objetos sueltos de Git del paquete 4 se descomprimen y los del bundle se leen con index-pack/cat-file en un directorio temporal aislado. No se ejecutan scripts de archivos recibidos. Los nuevos documentos y metadatos de las imágenes QR se incluyen en el pase final.

Las reglas buscan claves privadas, formatos de tokens de proveedores, credenciales incrustadas en URL, asignaciones de secretos, correos, rutas de usuario, rutas operativas y direcciones IP privadas. Los candidatos se registran por ubicación, regla, línea y huella, sin copiar valores sensibles. Se revisan manualmente los candidatos y la documentación de entrada, procedencia y cierre. No se consultan otros proyectos, cuentas ni sistemas productivos.

La base contiene ocho commits alcanzables, 373 árboles y 1.184 blobs: 1.565 objetos en total. El primer pase deduplicó 5.726 contenidos, recorrió 23 ZIP únicos, un bundle único y 31 objetos Git sueltos del ZIP; los 24 objetos de contenido del bundle se examinaron aparte. Los totales del pase final añaden los recursos nuevos y se registran en la evidencia externa; no se fijan como un umbral de aprobación.

## Resultados y excepciones

Los ocho candidatos del material histórico se revisaron como falsos positivos: notación pública de transporte Git, direcciones sintéticas de pruebas y expresiones de saneamiento de rutas. No se identificaron credenciales reales ni datos operativos privados en esos candidatos. Los identificadores autorizados del repositorio y su URL se conservan; la atribución Git se trata como atribución, no como una ruta operativa privada. No se reescriben autores ni historia para alterar esa atribución.

Un primer intento del instrumento volvió a interpretar una cabecera de bundle como un bundle completo y registró IndexError de cobertura. Se corrigió la condición del instrumento y se repitió el pase; no se modificó el bundle. La incidencia y su resolución se conservan, sin contarlas como un defecto didáctico ni como una inspección aprobada de aquel subintento.

No se encontró una decisión de anonimización adicional sustentada por los candidatos examinados. La elección editorial sobre la atribución Git y los identificadores autorizados debe conservarse consciente antes de abrir el repositorio. Si surge un hallazgo real después, su ubicación y corrección se tratarán en evidencia privada, sin publicar el valor ni reescribir historia automáticamente.

## Límites

El análisis combina reglas sintácticas y revisión documental acotada; no reconoce todos los nombres de personas, clientes, sistemas o combinaciones identificables posibles. No se realiza OCR ni reconocimiento de personas en imágenes. Se inspeccionaron visualmente las cuatro capturas históricas únicas del laboratorio 6 (escritorio, móvil, vacío y error): muestran el catálogo sintético, sin personas ni datos operativos identificados. Sus duplicados en los ZIP se relacionan por huella. Los recursos QR nuevos se generan desde URLs autorizadas y también se inspeccionan visualmente. Se extraen los metadatos PNG/JPEG con Pillow. Los archivos binarios se buscan por patrones y se abren sus contenedores conocidos; esto no equivale a interpretar todo formato binario imaginable.

Quedan fuera objetos inalcanzables, forks, clones ajenos, comentarios e incidencias de GitHub, registros del servidor, secretos de la cuenta y archivos externos al proyecto. Tampoco es una auditoría integral de vulnerabilidades o licencias de todas las dependencias. Estas limitaciones no se convierten en garantías ni en hallazgos inventados. El autor debe revisar el alcance y aprobar la futura apertura pública por separado.
