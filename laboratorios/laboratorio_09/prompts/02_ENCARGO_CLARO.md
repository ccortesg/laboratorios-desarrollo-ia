# Ejemplo didáctico preparado para el libro · CLARO

## C · Contextualiza

Trabaja en esta copia sintética del catálogo. Lee README, contexto/CONTEXTO.md, contexto/CONTRATO_SEGURIDAD.md y contexto/TRAZABILIDAD.md. La base es la solución corregida anterior; importa el CSV por CLI y consulta ese mismo archivo SQLite desde HTTP y navegador.

## L · Limita

Añade únicamente la frontera de validación GET /api/resumen descrita en el contrato. Conserva catálogo, CSV, persistencia, pantalla y los 62 casos heredados. No introduzcas autenticación, dependencias de aplicación, servicios externos ni despliegue. No modifiques base ni evidencias anteriores.

## A · Acuerda

S01–S08 y sus doce casos definen el resultado observable: consultas válidas, duplicados, claves desconocidas, tamaños, codificación, recuperación de pantalla, texto parecido a SQL y error interno genérico. Mantén exactamente los fallos previstos de la base y de la propuesta didáctica. No clasifiques una avería de ejecución como defecto esperado.

## R · Resuelve

Revisa primero la información que se perdería al pasar de pares a diccionario. Implementa propuesta y solución como cambios pequeños y compara las diferencias. Ejecuta las mismas comprobaciones HTTP y de navegador contra ambos estados. Ejecuta también los contratos heredados sobre la solución real.

## O · Observa

Guarda comandos, entorno, stdout/stderr, códigos de salida, casos y límites en una carpeta nueva. Conserva FALLIDO en los casos defectuosos, registra BLOQUEADO o NO EJECUTADO cuando corresponda y verifica los bytes finales después del saneamiento. Explica qué demuestra el recorrido y qué riesgos quedan fuera. No atribuyas la ejecución a una herramienta comercial sin evidencia.

Este prompt se preparó para el libro; no representa una conversación histórica ni una sesión comercial acreditada.
