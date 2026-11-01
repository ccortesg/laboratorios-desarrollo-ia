# Instrucciones del laboratorio 9

Lee README y contexto/CONTRATO_SEGURIDAD.md antes de cambiar código. Todo el material es sintético y local. Practica en una copia, conserva estados, datos, diferencias y evidencia.

Base copia exactamente la solución corregida del laboratorio 8. Propuesta pierde repeticiones al convertir pares a dict antes de validarlos. Solución conserva los pares hasta detectar duplicados. Sólo cambian servidor.py y politica_consulta.py; catálogo, importación, persistencia y pantalla mantienen sus contratos.

Conserva los 62 casos heredados en los tres estados. Los doce casos S representan ocho criterios nuevos. Fallos admitidos: base S02.a/S02.b/S02.c/S03/S04.a/S04.b/S05.a/S05.b/S06; propuesta S02.a/S02.b/S02.c. Deben ser AssertionError; una avería de infraestructura no es el defecto esperado. La solución aprueba 74 casos con navegador.

La evidencia completa exige HTTP y Chromium reales. Sin navegador, el global es NO EJECUTADO. Conserva los bytes de captura y verifica los bytes finales tras sanear. Nunca reescribas históricos ni recalcules hashes para ocultar una divergencia.

Distingue expectativas, ejecución local, ejemplos didácticos, auditorías y sesiones comerciales. No atribuyas estas pruebas a una herramienta comercial ni a Windows sin evidencia específica. No accedas a sistemas externos, no publiques y no implementes el reto ni capítulos siguientes.
