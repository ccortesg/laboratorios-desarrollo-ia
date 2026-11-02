# Propuesta de licencia · v1.0

**Consulta de fuentes: 2 de noviembre de 2026. Estado: decisión del autor pendiente.** La consulta autenticada de GitHub devuelve `license: null`; no hay una licencia del proyecto aprobada en la base examinada. Este documento es una propuesta: no instala una licencia ni atribuye la titularidad de las contribuciones.

## Recomendación para el código propio

Propongo **MIT** para el código propio de los ejercicios y las herramientas propias que el autor confirme que puede licenciar. Permite usar, modificar y redistribuir el software, incluso comercialmente, conservando los avisos de copyright y de licencia, y contiene una exclusión de garantías. Su sencillez facilita reutilizar los ejemplos en prácticas y otros proyectos. No obliga a publicar las modificaciones. El autor debe valorar si esa reutilización amplia coincide con su intención. [Texto primario de MIT, Open Source Initiative](https://opensource.org/license/mit).

La elección debe identificar rutas incluidas, titular o titulares y año antes de añadir un archivo LICENSE. Deben revisarse los derechos de las contribuciones existentes y la procedencia de cada componente. No se propone aplicar MIT indiscriminadamente a todos los documentos y archivos históricos del repositorio.

## Materiales con decisiones distintas

| Material | Propuesta y alcance por decidir |
| --- | --- |
| Código propio, SQL sintético y herramientas propias | MIT, si el titular confirma los derechos y las rutas. Aclarar que los ejemplos no ofrecen garantías. |
| Guías, contexto y documentación didáctica propia | Considerar **CC BY 4.0** para los textos expresamente identificados si se desea permitir adaptación y redistribución, incluso comercial, con atribución, enlace a la licencia e indicación de cambios. Es una decisión separada de MIT. |
| Manuscrito, Word consolidado, maestro editorial y futuras ediciones del libro | Fuera de esta propuesta y de cualquier licencia automática del repositorio. Confirmar derechos y condiciones editoriales por separado. No se incorporan aquí. |
| Evidencias históricas, informes recibidos y bundles | Confirmar derechos de redistribución y qué licencia corresponde a cada pieza. Su presencia en Git no acredita una autorización general del titular. Conservar atribuciones y procedencia. |
| Dependencias y componentes de terceros | Conservan sus licencias y avisos originales. No se relicencian mediante una decisión sobre código propio. |

La opción documental anterior deriva de [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) y su [texto legal](https://creativecommons.org/licenses/by/4.0/legalcode). Creative Commons recomienda licencias de software para el código; no propone sus licencias como sustituto de una licencia de software. [FAQ oficial](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software).

## Dependencias de los QR

El generador usa Segno y no incorpora su código fuente al repositorio. La verificación usa CairoSVG, Pillow y zxing-cpp, además de las dependencias transitivas fijadas en los archivos requirements separados de los laboratorios. La instalación resuelve esos componentes desde sus distribuciones originales; no se incluyen entornos virtuales ni paquetes descargados en la entrega. Sus metadatos y avisos se inventarían por separado antes de redistribuir componentes. Los archivos requirements fijan versiones, no cambian sus condiciones de licencia.

## Decisión que requiere el autor

1. Confirmar titularidad y derechos de las contribuciones propias y recibidas.
2. Aprobar o rechazar MIT para el código y delimitar sus rutas, titular y año.
3. Elegir condiciones para documentación, datos sintéticos, evidencias y QR; decidir por separado si adopta CC BY 4.0 para textos concretos.
4. Mantener explícita la exclusión del manuscrito y resolver cualquier condición editorial o aviso de terceros.
5. Autorizar después la instalación de las licencias acordadas y, en otro paso expreso, la apertura pública.

La preparación puede subirse al repositorio privado sin resolver esas decisiones. Hacer visible el repositorio no lo convierte por sí solo en open source: GitHub distingue acceso al repositorio y permisos concedidos por una licencia. [Documentación primaria de GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
