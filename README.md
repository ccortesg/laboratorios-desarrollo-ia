# Laboratorios de desarrollo de software con IA

Material de acompañamiento de **Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro**. Diez ejercicios locales sobre un catálogo ficticio para practicar cómo definir trabajo, revisar cambios y reconocer resultados con evidencia mediante CLARO.

**Estado comprobado el 2 de noviembre de 2026:** repositorio privado; base de main `a8b779f5cf5f876bcf4a1a18e906e75e59d003ee`, árbol `69d691ec538807193e6e2437946197da86fd8837`. Las 17 etiquetas, incluidas lab-10-v1.0 y repositorio-v1.6, están presentes; esas dos coinciden con la base. Las guías para lectores y QR son una nueva preparación documental. La subida de este incremento se acredita en un comprobante posterior externo al commit; consulta [su alcance y pendientes](docs/publicacion/ESTADO_PREPARACION_PUBLICA_v1.0.md).

**Estado editorial:** capítulos 1–10 pendientes de revisión del autor; maestro editorial 1.0 vigente. El capítulo 1 conserva el título original «El nuevo oficio del desarrollador: del código al resultado». Los manuscritos se entregan por separado. Este repositorio no publica ni aprueba el libro y todavía no tiene una licencia elegida por el autor.

## Empieza con el laboratorio 1

1. Abre la [ficha del laboratorio 1](docs/lectores/laboratorio_01.md) y descarga su [ZIP 1.0](https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_01_v1.0.zip). Mientras el repositorio sea privado necesitas acceso autorizado; también puedes abrir [el archivo en GitHub](https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/a8b779f5cf5f876bcf4a1a18e906e75e59d003ee/distribuciones/LABORATORIO_01_v1.0.zip) y descargarlo con tu sesión.
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

El 4 necesita Git y usa `python herramientas/preparar_laboratorio_04.py` desde la raíz del repositorio completo; su carpeta visible no es un Git independiente. El 5 requiere Python 3.10+; el 6 añade una web local y navegador manual; del 7 al 10 se requiere Python 3.11+. Sólo las comprobaciones automatizadas de navegador requieren Node 20+, Playwright y Chromium. Sigue el README técnico de cada versión para instalarlos. El 8 recomienda **1.0.1** y conserva 1.0 como antecedente de su corrección de recursos SQLite.

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

Para correcciones o incidencias sigue [correcciones y soporte](docs/lectores/README.md#correcciones-y-soporte); no incluyas datos personales ni secretos. La [propuesta de licencia](docs/publicacion/PROPUESTA_LICENCIA_v1.0.md) requiere decisión del autor. Los QR y los [recuadros de integración](docs/publicacion/INTEGRACION_QR_EN_LIBRO_v1.0.md) se preparan para la siguiente revisión editorial: todavía no están insertados en los capítulos.

La cabecera anterior de «cierre preparado» y el README completo se conservan byte por byte como [antecedente identificable](docs/publicacion/antecedentes/README_ANTES_PREPARACION_v1.0.txt). Sus pendientes describen aquel momento y no sustituyen las referencias consultadas en esta preparación.
