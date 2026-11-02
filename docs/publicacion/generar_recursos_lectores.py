"""Genera QR y recuadros exclusivamente desde el mapa de lectores.

Desde la raíz: python docs/publicacion/generar_recursos_lectores.py
Dependencia de generación: requirements-generacion-qr.txt. Sin acceso de red.
"""
from pathlib import Path
import json
import textwrap
import xml.etree.ElementTree as ET

import segno

ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / 'docs/lectores/mapa_laboratorios.json'
SVG_NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG_NS)


def main():
    data = json.loads(MAP.read_text(encoding='utf-8'))
    policy = data['qr']
    labs = data['laboratorios']
    if [x['numero'] for x in labs] != list(range(1, 11)):
        raise ValueError('El mapa debe contener exactamente los diez laboratorios ordenados')
    sheet = ET.Element(f'{{{SVG_NS}}}svg', {
        'width': '210mm', 'height': '297mm', 'viewBox': '0 0 210 297',
        'role': 'img', 'aria-label': 'Diez QR de las guías de laboratorio, a 42 mm'})
    ET.SubElement(sheet, f'{{{SVG_NS}}}rect', {'width':'210','height':'297','fill':'white'})

    def label(text, x, y, size=3):
        node=ET.SubElement(sheet, f'{{{SVG_NS}}}text', {
            'x': str(x), 'y': str(y), 'font-family': 'sans-serif',
            'font-size': str(size), 'fill': 'black'})
        node.text=text

    label('Revisión editorial · diez guías de laboratorio', 10, 10, 4)
    label('QR de 42 × 42 mm, incluida la zona blanca. Repositorio privado al preparar.', 10, 16, 2.7)
    intro = '''# Integración de QR en el libro · recursos v1.0

Recursos para la siguiente revisión editorial de **Desarrollo de Software en la Era de la IA: Domina Codex, Grok Build y las Herramientas del Futuro**. Estos recuadros no se han insertado en los diez capítulos ni en el Word consolidado. Maestro editorial 1.0 sin cambios; capítulos 1–10 pendientes de revisión. El capítulo 1 conserva su título original.

Fuente única: [mapa de laboratorios](../lectores/mapa_laboratorios.json). Los títulos completos de 2–5 requieren cotejo editorial; las denominaciones técnicas existentes permiten preparar sus recursos sin inventar manuscritos. Cada QR abre una guía bajo main; el autor se compromete a conservar esa ruta durante el acompañamiento del libro. El contenido de la guía es mantenible, mientras la descarga está fijada a un commit existente.

Ubicación propuesta: sección **Preparación del laboratorio** de cada capítulo. Colocar el QR a **42 × 42 mm**, incluyendo sus cuatro módulos de margen blanco, sin recortar, deformar ni superponer elementos. Preferir SVG para maquetación; conservar el PNG como alternativa. Los módulos son negros y el fondo blanco opaco. El QR es complementario: conservar ambos enlaces de texto en papel y enlaces activos en la edición digital.

La [hoja de revisión](../lectores/qr/hoja_revision.svg) representa los diez QR a ese tamaño en A4. La decodificación digital y la inspección visual no sustituyen un escaneo físico de una prueba de imprenta. Mientras el repositorio sea privado, el QR no concede acceso; acceso anónimo y apertura pública siguen pendientes de otro encargo.

'''
    blocks=[]
    for index, lab in enumerate(labs):
        if lab['destino_qr'] != lab['url_guia']:
            raise ValueError('El destino QR debe ser la guía mantenible')
        qr=segno.make_qr(lab['destino_qr'], error=policy['correccion'],
                         mode='byte', encoding='utf-8', boost_error=False)
        for key in ('qr_png','qr_svg'):
            dest=ROOT/lab[key]
            dest.parent.mkdir(parents=True,exist_ok=True)
            qr.save(str(dest), scale=policy['escala_png'], border=policy['borde_modulos'],
                    dark=policy['modulos'], light=policy['fondo'])
        # Anidación vectorial del SVG exacto del QR, sin recursos remotos.
        node=ET.fromstring((ROOT/lab['qr_svg']).read_bytes())
        width=int(node.attrib['width'])
        height=int(node.attrib['height'])
        x=10+(index%2)*96
        y=23+(index//2)*53
        node.attrib.update({'x':str(x), 'y':str(y), 'width':'42','height':'42',
                            'viewBox':f'0 0 {width} {height}'})
        sheet.append(node)
        label(f"Laboratorio {lab['numero']:02}", x+44, y+5, 3.2)
        label('Versión '+lab['version'], x+44, y+10, 2.8)
        for n,line in enumerate(textwrap.wrap(lab['destino_qr'],width=29,
                                              break_long_words=True,break_on_hyphens=False)):
            label(line,x+44,y+16+n*3.6,2.1)
        label('Destino: guía mantenible',x+44,y+40,2.2)
        first=lab['comandos_minimos'][0]
        blocks.append(f'''## Capítulo {lab['numero']} · Preparación del laboratorio

> **Laboratorio {lab['numero']:02} · versión {lab['version']}**
>
> {lab['objetivo']}
>
> QR: [SVG](../../{lab['qr_svg']}) · [PNG](../../{lab['qr_png']}); archivo identificado: `{Path(lab['qr_svg']).name}`.
>
> Guía: [{lab['url_guia']}]({lab['url_guia']})
>
> Descarga directa: [ZIP {lab['version']}]({lab['url_descarga']})
>
> Requisitos esenciales: {lab['requisitos']}
>
> Primer paso: descarga y extrae en una carpeta nueva. Carpeta de ejecución: {lab['carpeta_ejecucion']}. Ejecuta `{first}`. Sigue el recorrido completo de la guía y no reemplaces evidencia anterior.
>
> Texto alternativo digital: «Código QR que abre la guía del laboratorio {lab['numero']:02}, versión {lab['version']}, con requisitos, descarga y correcciones. El enlace de texto a la guía ofrece el mismo acceso».

SHA-256 del ZIP: `{lab['sha256']}`. Commit de descarga: `{lab['commit_zip']}`.

''')
    label('Prueba física de escaneo: NO EJECUTADO. Conservar enlaces de texto en el libro.',10,293,2.5)
    ET.ElementTree(sheet).write(ROOT/'docs/lectores/qr/hoja_revision.svg', encoding='utf-8',xml_declaration=True)
    (ROOT/'docs/publicacion/INTEGRACION_QR_EN_LIBRO_v1.0.md').write_text((intro+''.join(blocks)).rstrip()+'\n',encoding='utf-8')
    print('Generados 10 PNG, 10 SVG, hoja A4 y 10 recuadros desde el mapa.')


if __name__ == '__main__':
    main()
