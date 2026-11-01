"""Comprueba SHA-256 e inventario del paquete; sólo lectura y sin red."""
import hashlib
from pathlib import Path, PurePosixPath
import re


def main():
    raiz = Path(__file__).resolve().parent
    try:
        declarados = {}
        for linea in (raiz / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
            huella, nombre = linea.split('  ', 1)
            ruta = PurePosixPath(nombre)
            if (not re.fullmatch('[0-9a-f]{64}', huella) or ruta.is_absolute()
                    or '..' in ruta.parts or '\\' in nombre or ':' in nombre
                    or nombre in declarados or nombre == 'SHA256SUMS'):
                raise ValueError('Entrada inválida.')
            declarados[nombre] = huella
        entradas = list(raiz.rglob('*'))
        if any(p.is_symlink() for p in entradas):
            raise ValueError('No se admiten enlaces.')
        reales = {p.relative_to(raiz).as_posix() for p in entradas
                  if p.is_file() and p != raiz / 'SHA256SUMS'}
        if set(declarados) != reales or not reales:
            raise ValueError('Cobertura incompleta.')
        for nombre, esperado in declarados.items():
            if hashlib.sha256((raiz / nombre).read_bytes()).hexdigest() != esperado:
                raise ValueError('Huella diferente.')
    except (OSError, UnicodeError, ValueError):
        print('FALLIDO: el paquete no coincide con su manifiesto; conserva el archivo y revisa su procedencia.')
        return 1
    print(f'APROBADO: {len(declarados)} archivos; SHA256 coincidente y cobertura completa del paquete.')
    print('Verificación de lectura, sin acceso a red ni cambios de archivos.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
