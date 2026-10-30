# Encargo de refactorización

**Ejemplos didácticos preparados para el libro.** No acreditan una sesión comercial ni una mejora de productividad. Usa una copia de trabajo si encargas modificaciones reales y conserva el paquete distribuido como referencia.

## Primera versión insuficiente

> Mejora el código del buscador y déjalo más limpio.

El objetivo no expresa qué responsabilidad necesita separarse ni qué comportamiento debe conservarse. La petición podría mezclar cambios de estilo, nuevas validaciones, optimizaciones o reglas diferentes. La revisión resultaría más difícil porque faltaría un límite concreto para la modificación.

## Versión con CLARO

```text
Refactoriza la búsqueda mediante una extracción acotada.

C: Lee ALCANCE.md, contexto/ARQUITECTURA.md,
   estados/generado.py y pruebas.py.
   El comportamiento esperado está fijado en C01 a C04
   y B01 a B06; confirma primero su estado actual.
L: Crea estados/refactorizado.py desde generado.py.
   Extrae el filtro a filtrar_por_nombre(articulos, texto).
   Conserva el mismo bucle y la normalización existentes.
   No cambies SQL, datos, pruebas ni interfaz pública.
A: buscar_catalogo(almacen, texto) debe conservar
   entradas de cadena, registros, orden y disponibilidad.
   El filtro recibe una lista y no consulta la base.
   Los diez criterios deben seguir aprobando sin cambios.
R: Ejecuta la batería de generado antes de modificar.
   Extrae el bloque y revisa la diferencia completa.
O: Ejecuta python pruebas.py --estado refactorizado.
   Explica qué se conservó por prueba y qué se inspeccionó.
   No atribuyas equivalencia universal a diez escenarios.
```

La transformación prevista extrae el mismo bucle; no lo convierte a otra construcción ni agrega validaciones. El motivo es poder examinar una responsabilidad a la vez. En otro proyecto sería necesario decidir si una extracción mejora de verdad la claridad; no toda función breve necesita más funciones.

## Cierre revisable

Compara ambos estados con `python comparar.py --paso refactorizar`. Relaciona la extracción con el objetivo y comprueba que la llamada a la consulta mantiene el almacén. Un resultado favorable sólo acredita los casos ejecutados; las propiedades no cubiertas necesitan revisión o criterios adicionales antes de ampliar la afirmación.
