# Implementar: prompt didáctico preparado para el libro

Este texto no acredita una generación de código en Grok Build. Su uso exige
que el plan se haya revisado en la sesión real del lector.

```text
Implementa en mi_practica/ el incremento delimitado en ALCANCE.md.
Conserva sin cambios los módulos, datos y comprobaciones heredados.

Primero crea servidor.py. Debe escuchar solo en la interfaz local,
servir únicamente /, /index.html, /app.js y /estilos.css y exponer
GET /api/resumen?almacen=...&nombre=... . Reutiliza resumir_catalogo.
Rechaza almacén ausente o vacío con el error JSON y el 400 del contrato.

Después crea web/index.html, web/estilos.css y web/app.js. Ofrece ALFA y
BETA, un nombre opcional y un botón Consultar catálogo. Lee la selección
en cada envío. Muestra el almacén devuelto, el total y los códigos.
Distingue espera, consulta, éxito, vacío y error; oculta resultados previos
al iniciar otra consulta y evita solicitudes simultáneas desde el formulario.

Ejecuta pruebas heredadas, resumen y HTTP sobre mi_practica. Informa los
comandos y resultados antes de continuar a navegador. Después arranca
ese servidor y ejecuta pruebas_navegador.cjs contra su URL local.
Si falta una dependencia, declara BLOQUEADO o NO EJECUTADO según proceda.
No cambies expectativas ni uses capturas como sustituto de las pruebas.

Entrega archivos cambiados, diferencias, evidencia y límites. No publiques.
```

El nombre de la carpeta importa: ejecutar el verificador de las referencias no
comprueba automáticamente la implementación que se creó en `mi_practica/`.
