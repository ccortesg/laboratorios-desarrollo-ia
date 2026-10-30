# Continuidad del incremento implementado

**Estado:** `solucion`, laboratorio 4. No se han recibido observaciones ni aprobación editorial del autor; los borradores siguen pendientes de revisión.

Se añadió `detalle.py` con `obtener_articulo(almacen, codigo)`, que devuelve un artículo disponible por código exacto o `None`. `pruebas_detalle.py` expresa N01–N10 y `pruebas.py` incorpora esa batería. Se actualizaron los cuatro documentos de contexto. `ALCANCE.md` mantiene el contrato previo y el resto del catálogo conserva su contenido.

El recorrido Git tiene dos referencias: `inicio`, con diez pruebas heredadas y el contrato todavía sin implementar; `solucion`, con los veinte criterios. Para revisar el incremento, usa `git diff inicio solucion --`. Para evaluar tus ediciones actuales, ejecuta `python pruebas.py` aquí y revisa `git status --short`, `git diff` y `git diff --cached`, además de los archivos sin seguimiento.

El verificador del directorio superior extrae y comprueba los dos commits etiquetados. Sus resultados y huellas están en la evidencia externa al repositorio; no certifican modificaciones posteriores del árbol de trabajo. Un `git diff` vacío en el paquete limpio no significa que inicio y solución sean iguales.

La comprobación de acceso a Codex se registra por separado. La sesión comercial no se realizó en esta entrega. Los prompts son didácticos y las pruebas son ejecuciones locales. La arquitectura de una aplicación completa, cantidades, reservas, red, concurrencia y despliegue siguen sin implementar. No se han realizado mediciones de productividad ni pruebas con lectores humanos.
