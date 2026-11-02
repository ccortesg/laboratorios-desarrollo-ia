"""Verificación de lectura: fichas, enlaces locales, ZIP y QR.

No modifica mapa, QR, ZIP ni resultados anteriores. Escribe sólo --salida, nueva.
No hace peticiones de red ni ejecuta código de los laboratorios.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit
import zipfile

import cairosvg
from PIL import Image, ImageChops
import zxingcpp

ROOT = Path(__file__).resolve().parents[2]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--salida', required=True, type=Path)
    args=parser.parse_args()
    if args.salida.exists():
        parser.error('La salida debe ser nueva; no se reemplazan resultados')
    data=json.loads((ROOT/'docs/lectores/mapa_laboratorios.json').read_text(encoding='utf-8'))
    checks=[]

    def check(name, passed, **details):
        checks.append({'comprobacion':name,'estado':'APROBADO' if passed else 'FALLIDO', **details})

    labs=data['laboratorios']
    check('diez_correspondencias',[x['numero'] for x in labs]==list(range(1,11)))
    manifest=dict((line.split()[1],line.split()[0]) for line in (ROOT/'distribuciones/SHA256SUMS').read_text().splitlines() if line.strip())
    # Todas las distribuciones declaradas, incluida la versión 1.0 histórica del 8.
    for filename,expected in manifest.items():
        package=ROOT/'distribuciones'/filename
        blob=package.read_bytes()
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            bad=archive.testzip()
        check('manifiesto:'+filename,digest(blob)==expected and bad is None,sha256=digest(blob),crc=bad is None)
    for lab in labs:
        n=lab['numero']
        expected_version='1.1' if n==4 else '1.0.1' if n==8 else '1.0'
        check(f'version_{n:02}',lab['version']==expected_version)
        check(f'ficha_{n:02}',(ROOT/lab['ficha']).is_file() and (ROOT/lab['readme_tecnico']).is_file())
        local=(ROOT/lab['zip']).read_bytes()
        remote_version=subprocess.run(['git','show',lab['commit_zip']+':'+lab['zip']],cwd=ROOT,capture_output=True)
        check(f'zip_commit_{n:02}',remote_version.returncode==0 and digest(local)==lab['sha256']==digest(remote_version.stdout))
        expected_url='https://raw.githubusercontent.com/ccortesg/laboratorios-desarrollo-ia/'+lab['commit_zip']+'/'+lab['zip']
        guide=f'https://github.com/ccortesg/laboratorios-desarrollo-ia/blob/main/docs/lectores/laboratorio_{n:02}.md'
        check(f'url_{n:02}',lab['url_descarga']==expected_url and lab['url_guia']==lab['destino_qr']==guide)
        image=Image.open(ROOT/lab['qr_png']).convert('RGBA')
        result=zxingcpp.read_barcode(image)
        colors=set(image.convert('RGB').getdata())
        check(f'qr_png_{n:02}',bool(result) and result.text==lab['destino_qr'] and colors=={(0,0,0),(255,255,255)} and image.getchannel('A').getextrema()==(255,255) and digest((ROOT/lab['qr_png']).read_bytes())==lab['qr_png_sha256'],destino=result.text if result else None,pixeles=list(image.size))
        margin=data['qr']['borde_modulos']*data['qr']['escala_png']
        strips=[image.crop((0,0,image.width,margin)),image.crop((0,image.height-margin,image.width,image.height)),image.crop((0,0,margin,image.height)),image.crop((image.width-margin,0,image.width,image.height))]
        check(f'margen_qr_{n:02}',all(set(x.convert('RGB').getdata())=={(255,255,255)} for x in strips),modulos=data['qr']['borde_modulos'])
        rendered=cairosvg.svg2png(url=str(ROOT/lab['qr_svg']))
        svg_image=Image.open(io.BytesIO(rendered)).convert('RGBA')
        svg_result=zxingcpp.read_barcode(svg_image)
        equal=image.size==svg_image.size and ImageChops.difference(image.convert('RGB'),svg_image.convert('RGB')).getbbox() is None
        check(f'qr_svg_{n:02}',bool(svg_result) and svg_result.text==lab['destino_qr'] and equal and digest((ROOT/lab['qr_svg']).read_bytes())==lab['qr_svg_sha256'],igualdad_pixeles_png=equal,destino=svg_result.text if svg_result else None)
        side=round(data['qr']['lado_editorial_mm']/25.4*300)
        reduced=image.resize((side,side),Image.Resampling.LANCZOS)
        small=zxingcpp.read_barcode(reduced)
        check(f'qr_42mm_300dpi_{n:02}',bool(small) and small.text==lab['destino_qr'],pixeles=side,nota='Simulación digital; no prueba física')
    docs=[ROOT/'README.md',*(ROOT/'docs/lectores').glob('*.md'),*(ROOT/'docs/publicacion').glob('*.md')]
    links=[]
    for file in docs:
        for dest in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
            parsed=urlsplit(dest.strip('<>'))
            if parsed.scheme or not parsed.path:
                continue
            target=(file.parent/unquote(parsed.path)).resolve()
            links.append({'origen':str(file.relative_to(ROOT)),'destino':dest,'existe':target.exists()})
    check('enlaces_locales',all(x['existe'] for x in links),comprobados=len(links),discrepancias=[x for x in links if not x['existe']])
    sheet=(ROOT/'docs/lectores/qr/hoja_revision.svg').read_bytes()
    check('hoja_diez_qr',sheet.count(b'viewBox="0 0 ')==11 and b'210mm' in sheet and b'297mm' in sheet)
    report={'fecha_utc':datetime.now(timezone.utc).isoformat(),'estado':'APROBADO' if all(x['estado']=='APROBADO' for x in checks) else 'FALLIDO','comprobaciones':checks,'alcance':'Local, de lectura. Acceso remoto autenticado, anonimato y prueba impresa se registran por separado.'}
    args.salida.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    failed=[x['comprobacion'] for x in checks if x['estado']=='FALLIDO']
    print(json.dumps({'estado':report['estado'],'comprobaciones':len(checks),'fallidas':failed},ensure_ascii=False))
    raise SystemExit(1 if failed else 0)


if __name__=='__main__':
    main()
