# Contexto reutilizable del laboratorio 10

## Problema

Una importación puede fallar y una consulta posterior puede terminar correctamente leyendo el catálogo anterior. Encadenar comandos sin revisar la decisión de cada paso permite declarar una operación correcta que nunca aplicó el archivo recibido.

El incremento reúne dos CLI existentes en una operación fija y conserva un recibo. Su valor observable es aplicar los datos, consultar el mismo origen y detenerse con evidencia si el primer paso falla.

## Archivos pertinentes

1. `CONTRATO_AUTOMATIZACION.md`: precondiciones, T01–T08, estados y límites previos.
2. `estados/solucion/operar.py`: operador correcto, instantánea, procesos y recibo.
3. `estados/propuesta/operar.py`: decisión defectuosa de continuación.
4. `estados/*/persistencia.py` e `importacion.py`: interfaces heredadas exactas.
5. `pruebas_automatizacion.py`: siete casos CLI y conservación de los recibos observados.
6. `pruebas_automatizacion_navegador.py/.cjs`: T08 sobre servidor, SQLite y Chromium reales.
7. `verificar.py`, `PROCEDENCIA.json` y `soporte/huellas_evidencia.py`: patrón exacto, conservación e integridad.
8. `diferencias/`, `prompts/` y `evidencia/`: cambio revisable, encargos didácticos y resultados identificados.

## Entradas y expectativas

Datos de referencia: almacenes ALFA/BETA y artículos A01–A04. La actualización válida deja A01/A03 disponibles en ALFA; A02 permanece deshabilitado. Cada comprobación crea sus propias bases. El código no utiliza servicios externos ni datos del trabajo real del autor.

La base del laboratorio 10 ya incorpora la persistencia y política HTTP corregidas. Los contratos anteriores mantienen sus identificadores, subcasos y expectativas. Sus descripciones de estados se refieren a los laboratorios donde nacieron, no a los estados de esta entrega.

## Resultado terminado

Debe conservarse la solución 9 en las tres copias, aprobar los 74 heredados por estado, registrar T01–T08 NO EJECUTADO en base, detectar sólo T02 en propuesta y aprobar los ocho T en solución. El recorrido completo exige navegador real. Las pruebas, operaciones del cierre, auditorías y manuscrito tienen estados distintos.
