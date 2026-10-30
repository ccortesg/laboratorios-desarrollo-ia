# Historia Git del laboratorio 4

`laboratorio_04.bundle` conserva los objetos y las referencias `main`, `inicio` y `solucion` del ejercicio original. Es un bundle autónomo: puede clonarse sin conectarse a un servidor. Los bundles transportan historia y referencias; no son una copia completa de la configuración, el índice o los archivos de trabajo de un directorio `.git`. El ZIP original se conserva por separado. Véase [documentación oficial de git bundle](https://git-scm.com/docs/git-bundle), consultada el 30 de octubre de 2026.

Desde la raíz general, utiliza:

```bash
python herramientas/preparar_laboratorio_04.py
```

El script copia los documentos del paquete y clona el bundle en un destino nuevo dentro de `trabajo/`. Desactiva conversión de finales de línea para conservar bytes, usa una plantilla Git vacía y comprueba las referencias y la solución. Retira el remoto local que crea el clon porque el verificador del ejercicio exige que su repositorio no tenga remotos.

La copia resultante contiene dos commits originales; no importa la historia del repositorio general ni crea commits ficticios de prácticas. Sus configuraciones locales y su índice se reconstruyen: no se afirma identidad byte a byte de esos metadatos con el ZIP. Las huellas de los archivos de la solución sí se comparan una a una.

Realiza ramas y cambios del ejercicio exclusivamente dentro de la copia preparada. `git diff inicio solucion --` permite revisar el incremento original. Para repetir la preparación, elige otro destino con `--destino`; no se borra ni sobrescribe un trabajo previo.
