# Encargo de generación

**Ejemplos didácticos preparados para el libro.** No son transcripciones históricas ni prompts cuya ejecución se haya acreditado dentro de una herramienta comercial. Los módulos incluidos son implementaciones de referencia. Si utilizas este encargo con un asistente, trabaja en una copia del paquete, conserva otra intacta y registra sus resultados por separado.

## Primera versión insuficiente

> Añade un buscador al catálogo. Que sea sencillo y funcione bien.

Faltan la entrada pública, qué campo se busca, el tipo de coincidencia, qué significa disponible, el caso vacío, los límites y el criterio de cierre. Una respuesta podría construir una pantalla, modificar SQL o incluir artículos que no están disponibles.

## Versión con CLARO

```text
Genera una función de búsqueda pequeña para este laboratorio.

C: Lee README.md, ALCANCE.md y contexto/CONTEXTO.md.
   Revisa laboratorio.py, datos/ejemplos.sql,
   solucion/consulta.sql y pruebas.py.
   Ya existe consultar_catalogo("solucion", almacen).
L: Implementa buscar_catalogo(almacen, texto) en
   estados/generado.py. Recibe dos cadenas.
   Reutiliza la consulta; no cambies datos, SQL ni pruebas.
   No añadas interfaz, servicios ni dependencias.
A: Busca una subcadena del nombre sobre lo disponible.
   Normaliza texto con strip().casefold() y nombres con
   casefold(). Texto vacío o blanco devuelve lo disponible.
   Conserva registros codigo/nombre y orden de entrada.
   Satisface C01 a C04 y B01 a B06 de ALCANCE.md.
R: Resume el contrato y señala cualquier contradicción.
   Implementa una variante pequeña, sin cambios ajenos.
O: Ejecuta python pruebas.py --estado generado.
   Entrega diferencia, resultados observados y límites.
   Si no puedes ejecutar, declara NO EJECUTADO y el motivo.
```

La regla de disponibilidad está definida en el contexto. Las pruebas C verifican que el incremento no amplíe indebidamente los artículos ofrecidos. Las B expresan el nuevo comportamiento. No ajustes los resultados esperados para hacer que una propuesta apruebe.

## Cierre revisable

El cierre debe identificar el archivo nuevo, explicar cómo reutiliza la consulta y conservar el comando y su salida. La función incluida puede compararse mediante `python comparar.py --paso generar`; el comando sólo muestra texto. El resultado de la sesión del lector necesita su propia evidencia, aunque coincida con la referencia.
