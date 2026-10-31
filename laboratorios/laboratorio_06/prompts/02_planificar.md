# Planificar: prompt didáctico preparado para el libro

No se envió como sesión acreditada de Grok Build. Adapta las rutas solo si tu
copia tiene un nombre distinto.

```text
Lee ALCANCE.md y contexto/CONTEXTO.md, ARQUITECTURA.md, DECISIONES.md y
CONTINUIDAD.md. Trabaja únicamente en mi_practica/, copia de estados/base/.

C — Contextualiza: el catálogo ya resuelve disponibilidad por almacén,
búsqueda por nombre y resumen. El total cuenta artículos, no existencias.
Revisa resumen.py, catalogo.py, laboratorio.py y los SQL de esa copia.

L — Limita: añade un servidor Python estándar local y HTML/CSS/JavaScript
sin recursos externos. Reutiliza resumir_catalogo(almacen, texto="").
No cambies los datos, las reglas, las pruebas heredadas ni otros estados.
No añadas usuarios, reservas, cantidades solicitadas ni publicación.

A — Acuerda: conserva C01–C04, B01–B06, N01–N10 y P01–P06. Cumple W01–W06
del contrato, incluidos W04.a/b y W06.a/b. El almacén omitido o vacío debe
producir HTTP 400; una consulta válida vacía debe producir HTTP 200.

R — Resuelve: antes de editar, entrega un plan corto por componente y
enumera archivos nuevos, responsabilidades y comandos de verificación.
Separa dominio, HTTP e interacción del navegador.

O — Observa: registra supuestos. No declares probado lo no ejecutado ni
atribuyas el resultado a una herramienta comercial sin evidencia.
```

Revisión del plan: debe referenciar la función existente, prever el cambio de
almacén en el formulario y conservar los estados vacío y error por separado.
