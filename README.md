# Laboratorios de desarrollo de software con IA

Material de acompañamiento de **Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro**. Diez ejercicios locales sobre un catálogo ficticio para practicar cómo definir trabajo, revisar cambios y reconocer resultados con evidencia mediante CLARO.

**Licencias aprobadas el 2 de noviembre de 2026:** [MIT para el código propio](LICENSE) y [CC BY 4.0 para la documentación seleccionada](LICENSES/CC-BY-4.0.txt). Consulta [rutas, exclusiones y atribución](LICENCIAS.md). La apertura pública está autorizada después de verificar este incremento; el [registro operativo](docs/publicacion/ESTADO_APERTURA_PUBLICA_v1.0.md) distingue la preparación de la operación administrativa y las comprobaciones anónimas posteriores. Los informes anteriores describen sus fechas y se conservan como antecedentes.

**Estado editorial:** capítulos 1–10 pendientes de revisión del autor; maestro editorial 1.0 vigente. El capítulo 1 conserva el título original «El nuevo oficio del desarrollador: del código al resultado». Los manuscritos se entregan por separado. Este repositorio no publica ni aprueba el libro.

## Empieza con el laboratorio 1

1. Abre la [ficha del laboratorio 1](docs/lectores/laboratorio_01.md) y descarga su [ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_01_v1.0.zip). Consulta junto al ZIP los [avisos de licencia](docs/publicacion/AVISOS_DISTRIBUCIONES_v1.0.md#laboratorio-01), [MIT](LICENSE) y [CC BY 4.0](LICENSES/CC-BY-4.0.txt); el archivo histórico permanece intacto.
2. Extrae el ZIP en una carpeta nueva. Abre una terminal en **laboratorio_01/**, junto a laboratorio.py. Necesitas Python con sqlite3 y unittest (referencia técnica: Python 3.12), editor y terminal. No necesitas pip, Git, Node ni cuentas comerciales para ejecutar este ejercicio.
3. Ejecuta cada comando y observa su resultado. `python` puede llamarse `python3` o `py -3` en tu equipo:

```bash
python -c "import sqlite3, unittest; print('Modulos disponibles; SQLite', sqlite3.sqlite_version)"
python laboratorio.py --version inicial --almacen ALFA
python pruebas.py --version inicial
python laboratorio.py --version solucion --almacen ALFA
python pruebas.py --version solucion
python verificar.py --salida mi_evidencia
```

Inicial devuelve A01/A04: tres criterios aprueban y **C04 falla intencionalmente**, con salida 1 de pruebas.py. Solución devuelve A01 y aprueba los cuatro, con salida 0. El verificador completo devuelve 0 al reconocer exactamente ese patrón; C04 sigue FALLIDO. Un fallo diferente o una excepción inesperada requieren investigación. Usa otra carpeta de salida si mi_evidencia ya existe.

## Los diez ejercicios

Cada ficha indica objetivo, descarga versionada, requisitos, carpeta de ejecución, comandos, resultados esperados y límites.

| Capítulo | Recorrido | Versión recomendada |
| --- | --- | --- |
| [01](docs/lectores/laboratorio_01.md) | El nuevo oficio del desarrollador: del código al resultado | 1.0 |
| [02](docs/lectores/laboratorio_02.md) | Contexto y arquitectura: preparar el terreno para la IA | 1.0 |
| [03](docs/lectores/laboratorio_03.md) | Ingeniería de prompts para generar, refactorizar y depurar | 1.0 |
| [04](docs/lectores/laboratorio_04.md) | Codex en acción: trabajar sobre un repositorio real | 1.1 |
| [05](docs/lectores/laboratorio_05.md) | GitHub Copilot: de la sugerencia al trabajo delegado | 1.0 |
| [06](docs/lectores/laboratorio_06.md) | Grok Build: de la idea a una aplicación de extremo a extremo | 1.0 |
| [07](docs/lectores/laboratorio_07.md) | Datos e integraciones: cuando los sistemas deben ponerse de acuerdo | 1.0 |
| [08](docs/lectores/laboratorio_08.md) | Depuración con evidencia: investigar errores entre entornos y servicios | 1.0.1 |
| [09](docs/lectores/laboratorio_09.md) | Confiabilidad y seguridad del software generado por IA | 1.0 |
| [10](docs/lectores/laboratorio_10.md) | Automatización, agentes y operación: prepararse para lo que sigue | 1.0 |

[Índice de lectores, descargas y correcciones](docs/lectores/README.md) · [mapa único y hashes](docs/lectores/mapa_laboratorios.json).

El 4 necesita Git; su ZIP autónomo incluye repositorio/.git y ofrece el recorrido principal. El preparador del repositorio completo es una alternativa documentada en la ficha. El 5 requiere Python 3.10+; el 6 añade una web local y navegador manual; del 7 al 10 se requiere Python 3.11+. Sólo las comprobaciones automatizadas de navegador requieren Node 20+, Playwright y Chromium. Sigue el README técnico de cada versión para instalarlos. El 8 recomienda **1.0.1** y conserva 1.0 como antecedente de su corrección de recursos SQLite.

## Cómo leer los resultados

APROBADO significa criterio satisfecho; FALLIDO, discrepancia observada; BLOQUEADO, precondición que impide continuar; NO EJECUTADO, actividad ausente. Los defectos intencionales sirven para practicar revisión y permanecen fallidos. Cada ficha identifica los suyos. Una ejecución local de Python o Git no demuestra por sí sola uso de una herramienta comercial ni aprobación editorial.

En los verificadores web, omitir --navegador puede dejar dominio/HTTP APROBADO y devolver 0, mientras el resultado global queda **NO EJECUTADO**. No lo presentes como una prueba de pantalla. Conserva cada evidencia en un destino nuevo y distingue expectativas del contrato de resultados realmente observados.

## Verificación completa opcional

Este recorrido es para mantenimiento o revisión integral, independiente de la primera práctica. Necesita Python 3.11+, Git y las dependencias de navegador preparadas. Desde la raíz del repositorio:

```bash
cd laboratorios/laboratorio_10
npm install --ignore-scripts --package-lock=false
npx --no-install playwright install chromium
cd ../..
python herramientas/verificar_todo.py --navegador --salida trabajo/verificacion_completa
```

Elige un destino nuevo. Sin --navegador el global queda NO EJECUTADO. Consulta [las instrucciones técnicas y la evidencia histórica](docs/lectores/README.md) para interpretar cada batería; esta preparación documental no repitió por rutina el conjunto funcional.

## Materiales, correcciones y soporte

- laboratorios/: código, contratos, contexto y evidencia técnica originales; practica sobre copias.
- distribuciones/: ZIP versionados y [SHA256SUMS](distribuciones/SHA256SUMS).
- historiales/: [historia Git original del laboratorio 4](historiales/README.md).
- evidencia_integracion/: resultados históricos; [revisión WSL del 10](evidencia_integracion/revision_laboratorio_10_wsl/README.md) y [corrección Windows del 8](evidencia_integracion/cierre_laboratorio_08_windows/README.md) mantienen su atribución.
- trabajo/: prácticas y comprobantes nuevos ignorados por Git.
- [VERSIONES](VERSIONES.md), [PROCEDENCIA](PROCEDENCIA.json) y [CONTINUIDAD](CONTINUIDAD.md): antecedentes y trazabilidad técnica.

Para correcciones o incidencias sigue [correcciones y soporte](docs/lectores/README.md#correcciones-y-soporte); no incluyas datos personales ni secretos. La [propuesta histórica de licencia](docs/publicacion/PROPUESTA_LICENCIA_v1.0.md) queda resuelta por las [licencias aprobadas](LICENCIAS.md). Los QR y los [recuadros de integración](docs/publicacion/INTEGRACION_QR_EN_LIBRO_v1.0.md) se preparan para la siguiente revisión editorial: todavía no están insertados en los capítulos.

La cabecera anterior de «cierre preparado» y el README completo se conservan byte por byte como [antecedente identificable](docs/publicacion/antecedentes/README_ANTES_PREPARACION_v1.0.txt). Sus pendientes describen aquel momento y no sustituyen las referencias consultadas en esta preparación.
