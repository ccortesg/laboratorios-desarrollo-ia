# Continuidad entre sesiones

## Punto que se conserva

El laboratorio contiene una base funcional heredada, una propuesta web con un
defecto deliberado y una solución. Los nombres de estados describen versiones
didácticas; no atribuyen autoría comercial. El contrato inicial está en `ALCANCE.md`
y su huella previa a la implementación en `evidencia/contrato_previo.json`.

Antes de continuar, lee este contexto y `evidencia/RESULTADOS.md`. Si ese archivo
remite a un resultado no ejecutado o bloqueado, conserva el límite: no conviertas
las expectativas del contrato en resultados observados. Las pruebas nuevas de
una sesión deben quedar en una carpeta de salida nueva.

## Cómo retomar una práctica propia

1. Identifica si estás leyendo una referencia de `estados/` o tu copia de trabajo.
2. Expresa el cambio esperado y los criterios afectados antes de editar.
3. Conserva C01–C04, B01–B06, N01–N10 y P01–P06 y limita las adiciones al contrato.
4. Ejecuta pruebas sobre la copia modificada, no solo el verificador de referencia.
5. Revisa las diferencias y registra comandos, códigos de salida y límites.

El capítulo propone empezar con `mi_practica/`, una copia de `estados/base/`.
Sus pruebas heredadas se ejecutan allí; P usa `--directorio mi_practica`; las
pruebas HTTP usan el mismo parámetro una vez creado `servidor.py`. Para W05–W06
hay que arrancar el servidor de esa copia y pasar su URL al script del navegador.

## Plantilla de cierre para el lector

```text
Estado revisado y carpeta:
Contrato o criterios afectados:
Archivos cambiados y motivo:
Comandos ejecutados y códigos de salida:
Resultados observados (APROBADO / FALLIDO / BLOQUEADO / NO EJECUTADO):
Fallos intencionales separados de problemas pendientes:
Decisiones nuevas y supuestos:
Limitaciones de la verificación:
Siguiente trabajo concreto:
```

No copies rutas privadas, cuentas, datos de producción ni credenciales a un cierre
publicable. Mantén la evidencia anterior y enlaza los resultados nuevos por sus
nombres relativos. Ninguna ejecución de este laboratorio aprueba editorialmente
los capítulos anteriores ni autoriza publicar o subir cambios a GitHub.
