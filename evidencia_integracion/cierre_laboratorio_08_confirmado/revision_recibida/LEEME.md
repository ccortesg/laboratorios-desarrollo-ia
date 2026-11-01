# Revisión del cierre publicado del laboratorio 8

**Resultado:** APROBADO en el alcance de integridad, continuidad y publicación documentadas. Esta entrega es un informe y un archivo de evidencias posterior al cierre; no contiene un parche para volver a aplicarlo.

## Qué contiene

- `REVISION_CIERRE_LABORATORIO_08_WSL_v1.0.md`: dictamen completo, comprobaciones, observaciones y límites.
- `CIERRE_LABORATORIO_08_CONFIRMADO_v1.0.md`: continuidad breve para la siguiente tarea.
- `ESTADO_DEL_LIBRO_v1.7.4.md` y `ESTADO_REPOSITORIO_v1.6.4.md`: copias exactas de los estados recibidos; la precisión WSL frente a la frase heredada «Git Bash» figura en el dictamen y en el cierre confirmado.
- `insumos/`: ZIP recibido y paquete de cierre original recuperado por separado, ambos sin modificaciones.
- `auditoria/`: consulta independiente a GitHub, dos revisiones de integridad y un script de cotejo reproducible.
- `SHA256SUMS` y `VERIFICAR_PAQUETE.py`: inventario y comprobador de sólo lectura de esta entrega.

La consulta remota corresponde al 1 de noviembre de 2026, 20:48:55 UTC. Las cifras funcionales de Windows son históricas. Los capítulos 1–8 siguen pendientes de revisión editorial; el capítulo 9 no se redactó.

## Verificación opcional de este paquete

Después de descomprimirlo, abre una terminal en su carpeta y ejecuta:

```bash
python -B VERIFICAR_PAQUETE.py
```

No necesita instalar dependencias ni conectarse a la red. Lee los archivos y compara sus bytes con el manifiesto. Si se usa un sistema donde el ejecutable se llama `python3`, sustituye `python` por `python3`.

Para reproducir el cotejo de los dos ZIP y de la consulta remota **ya conservada**, puede ejecutarse:

```bash
python -B auditoria/AUDITAR_CIERRE.py \
  --evidencia insumos/EVIDENCIA_CIERRE_LAB08_WSL_01.zip \
  --original insumos/CIERRE_LABORATORIO_08_v1.0.zip \
  --remoto auditoria/REFERENCIAS_REMOTAS_CONFIRMADAS.json \
  --salida ../COTEJO_CIERRE08_REPRODUCIDO.json
```

La ruta de salida debe ser nueva y estar fuera del paquete, para conservar su cobertura exacta. El script no ejecuta código de los ZIP, no realiza una consulta nueva a GitHub y no repite las pruebas del laboratorio. El resultado esperado para los archivos entregados es `APROBADO`, con código cero. La ejecución de este cotejo durante la revisión consta en `auditoria/RESULTADO_COTEJO_CIERRE.json`; su reproducción desde el paquete se comprobó antes de entregar.

## Uso de la continuidad

El cierre técnico del laboratorio 8 ya está publicado. Para la siguiente entrega utiliza los estados 1.7.4/1.6.4 y el cierre confirmado, reconsulta las referencias remotas y conserva cualquier avance posterior. Los comprobantes generados después del push están fuera del commit publicado; su eventual incorporación al repositorio deberá ser una adición documental. Ningún paso de esta revisión requiere desplazar las etiquetas del cierre.
