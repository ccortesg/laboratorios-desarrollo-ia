# Reproducir y comprobar los QR · v1.0

El [mapa](../lectores/mapa_laboratorios.json) es la fuente única de destinos, versiones y recuadros. No se modifica código de los laboratorios. El generador no usa red ni interpreta archivos CSV o instrucciones externas.

Desde la raíz del repositorio, con Python 3.10+ y venv disponibles, crea un entorno nuevo separado de los ejercicios. Elige otro nombre si ya existe:

```bash
python -m venv trabajo/entorno_qr_01
```

Activa ese entorno según tu sistema. Después, para generar únicamente (una dependencia especializada):

```bash
python -m pip install -r docs/publicacion/requirements-generacion-qr.txt
python docs/publicacion/generar_recursos_lectores.py
```

Para decodificar y comprobar, instala las versiones fijadas, incluidas las transitivas, en ese mismo entorno:

```bash
python -m pip install -r docs/publicacion/requirements-verificacion-qr.txt
python docs/publicacion/verificar_recursos_lectores.py --salida trabajo/comprobacion_qr_01.json
```

CairoSVG requiere la biblioteca nativa Cairo de tu sistema. Si no está disponible, registra BLOQUEADO y conserva el resultado de la generación. En esta preparación se observó Cairo 1.16.0; las versiones Python exactas están fijadas en requirements. La instalación descarga dependencias públicas; la generación y verificación no usan la red. No instales estas dependencias para ejecutar el laboratorio 1.

La comprobación es de lectura: exige una salida nueva, comprueba diez fichas, las once distribuciones declaradas (incluida 8 v1.0 histórica), CRC, hashes, identidad del ZIP en el commit indicado, URL, márgenes, fondo opaco, decodificación PNG y SVG y equivalencia de píxeles. También simula 42 mm a 300 dpi. No consulta GitHub ni acredita acceso anónimo. Las lecturas autenticadas se registran por separado.

El generador produce PNG de 684 × 684 píxeles y SVG vectoriales, corrección Q, escala 12, margen de cuatro módulos, negro sobre blanco opaco. Los diez QR de esta preparación tienen 49 × 49 módulos de datos y 57 × 57 con margen. A 42 mm el módulo mide aproximadamente 0,737 mm. No hay logotipos, degradados, acortadores ni seguimiento.

También genera [hoja_revision.svg](../lectores/qr/hoja_revision.svg), A4 de 210 × 297 mm con QR de 42 mm, y los [recuadros editoriales](INTEGRACION_QR_EN_LIBRO_v1.0.md). Para reproducir la vista PNG de la hoja tras generar:

```bash
python -c "import cairosvg; cairosvg.svg2png(url='docs/lectores/qr/hoja_revision.svg', write_to='docs/lectores/qr/hoja_revision.png', output_width=2480, output_height=3508)"
```

Se inspeccionó esa vista de 2480 × 3508 píxeles: diez identificadores, versiones correctas, destinos legibles, separación y ausencia de recortes o deformación. Se comprobó además la geometría vectorial de 42 mm y la decodificación individual a 496 píxeles (42 mm a 300 dpi). La visualización en pantalla puede reescalarse: no se afirma haber medido 42 mm físicos en el monitor. **Prueba física de escaneo de una edición impresa: NO EJECUTADO.**

Los comandos de esta ejecución y sus códigos se conservan en la entrega externa. Se utilizó un entorno temporal aislado en WSL2/Linux con Segno 1.6.6, Pillow 12.0.0, zxing-cpp 2.3.0 y CairoSVG 2.8.2. Los archivos requirements fijan las dependencias Python; la versión de Cairo y el sistema operativo deben registrarse al reproducir. El script no marca por sí solo estados del mapa: el responsable registra resultados observados, sin convertir expectativas en aprobaciones.
