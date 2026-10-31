# Requisitos, datos, componentes y comprobaciones

| Criterio | Datos o situación | Componente principal | Evidencia de comportamiento |
| --- | --- | --- | --- |
| C/B/N/P/W | SQL original intacto | Catálogo, resumen y web heredados | Baterías heredados, resumen, HTTP y navegador por estado. |
| I01 | `actualizacion_valida.csv` | Importador y conexión compartida | Cantidades esperadas, ALFA con A01/A03, BETA vacío y A02 deshabilitado. |
| I02.a–e | Cabecera, columnas, bytes, archivo o fila inválidos | Lector y validador | Rechazo con diagnóstico; las tablas permanecen intactas. |
| I03.a–c | Maestros desconocidos y variantes de código | Validador | No se crean maestros ni se normaliza el identificador. |
| I04.a–d | Negativo, decimal, texto y fuera de rango | Validador | Rechazo previo a escritura. |
| I05 | `par_duplicado.csv` | Validador | El par repetido rechaza todo el archivo. |
| I06 | `error_tardio.csv` y un rechazo SQLite controlado | Coordinador del importador y transacción | Las tres tablas antes y después son iguales en ambos escenarios. |
| I07 | A01/ALFA=5 dos veces | Aplicación sobre misma conexión | Mismo estado final; pares omitidos conservados. |
| I08 | UTF-8 con BOM y CRLF; error en fila 3 | Informe | Huella de bytes, conteos y localización correctos. |

Las pruebas no buscan una cadena concreta en la implementación para decidir su
aprobación. Comparan valores observables. El comprobador de procedencia sí compara
hashes, con un propósito distinto: conservar los archivos heredados declarados.
