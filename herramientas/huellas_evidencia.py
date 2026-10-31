"""Comprueba huellas de evidencia; el cierre sólo se usa en una ejecución nueva.

La línea de comandos es de sólo lectura. No repara registros históricos.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path


class ErrorHuellas(Exception):
    """Registro incompleto, referencia insegura o discrepancia de integridad."""


def _archivos(salida):
    salida = Path(salida)
    if salida.is_symlink() or not salida.is_dir():
        raise ErrorHuellas("Se requiere una carpeta de evidencia existente sin enlaces.")
    archivos = sorted(salida.rglob("*"))
    if any(p.is_symlink() for p in archivos):
        raise ErrorHuellas("No se admiten enlaces dentro de la evidencia.")
    return [p for p in archivos if p.is_file()]


def _referencias(archivos):
    documentos, referencias = [], []
    for archivo in archivos:
        if archivo.name != "comandos.json":
            continue
        try:
            datos = json.loads(archivo.read_bytes().decode("utf-8"))
            registros = datos["registros"]
        except (ValueError, TypeError, KeyError) as error:
            raise ErrorHuellas("El registro de comandos no tiene la estructura esperada.") from error
        if not isinstance(registros, list):
            raise ErrorHuellas("El registro de comandos debe contener una lista.")
        documentos.append((archivo, datos))
        for registro in registros:
            if not isinstance(registro, dict):
                raise ErrorHuellas("Hay un comando con estructura incorrecta.")
            for flujo in ("stdout", "stderr"):
                clave = "sha256_" + flujo
                if flujo not in registro and clave not in registro:
                    continue
                nombre, huella = registro.get(flujo), registro.get(clave)
                if (not isinstance(nombre, str) or not nombre
                        or nombre in {".", "..", "comandos.json"}
                        or any(c in nombre for c in "/\\:")
                        or not isinstance(huella, str)
                        or re.fullmatch(r"[0-9a-f]{64}", huella) is None):
                    raise ErrorHuellas("Una referencia de salida o su huella es inválida.")
                destino = archivo.parent / nombre
                if destino not in archivos or not destino.is_file():
                    raise ErrorHuellas("Falta un archivo de salida declarado.")
                referencias.append((registro, flujo, destino))
    return documentos, referencias


def comprobar_huellas(salida):
    """Compara SHA declarados con bytes recibidos, sin escribir ningún archivo."""
    _, referencias = _referencias(_archivos(salida))
    discrepancias = []
    for registro, flujo, destino in referencias:
        observado = hashlib.sha256(destino.read_bytes()).hexdigest()
        esperado = registro["sha256_" + flujo]
        if observado != esperado:
            discrepancias.append({
                "archivo": destino.relative_to(salida).as_posix(),
                "declarado": esperado, "observado": observado,
            })
    total = len(referencias)
    return {"estado": "FALLIDO" if discrepancias else "APROBADO" if total else "NO EJECUTADO",
            "comprobadas": total, "coincidentes": total - len(discrepancias),
            "discrepancias": discrepancias}


def cerrar_evidencia(salida, transformar):
    """Sanea la salida recién creada y calcula huellas de los bytes finales.

    Valida la captura antes de escribir. No corrige discrepancias previas.
    La carpeta nueva y la exclusión de históricos las exige verificar_todo.py.
    """
    salida = Path(salida)
    archivos = _archivos(salida)
    documentos, _ = _referencias(archivos)
    if comprobar_huellas(salida)["discrepancias"]:
        raise ErrorHuellas("Las huellas de captura no coinciden; se conserva la evidencia sin reescribir.")

    # Preparar todos los textos antes de escribir evita una conversión implícita
    # LF/CRLF y permite detectar UTF-8 inválido sin cambios parciales por ese motivo.
    nuevos = {p: transformar(p.read_bytes().decode("utf-8")).encode("utf-8")
              for p in archivos if p.suffix in {".json", ".txt", ".diff"}}
    for archivo, datos in documentos:
        for registro in datos["registros"]:
            for flujo in ("stdout", "stderr"):
                clave = "sha256_" + flujo
                if clave in registro:
                    registro.setdefault(clave + "_capturado", registro[clave])
        datos.setdefault("convenciones_del_productor", datos.get("convenciones", ""))
        datos["convenciones"] = (
            "Copia de integración saneada: sha256_stdout/stderr identifican los bytes finales "
            "guardados; los campos *_capturado conservan la huella de captura. "
            "Se preservan LF/CRLF salvo sustituciones explícitas de saneamiento. "
            "Las entradas sin salidas no adquieren archivos ni huellas."
        )
        nuevos[archivo] = transformar(json.dumps(datos, ensure_ascii=False, indent=2) + "\n").encode("utf-8")

    for archivo, contenido in nuevos.items():
        archivo.write_bytes(contenido)

    # Leer lo realmente guardado; no calcular sobre una representación previa.
    for archivo, _ in documentos:
        datos = json.loads(archivo.read_bytes().decode("utf-8"))
        for registro in datos["registros"]:
            for flujo in ("stdout", "stderr"):
                if "sha256_" + flujo in registro:
                    registro["sha256_" + flujo] = hashlib.sha256(
                        (archivo.parent / registro[flujo]).read_bytes()).hexdigest()
        archivo.write_bytes((json.dumps(datos, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    resultado = comprobar_huellas(salida)
    if resultado["discrepancias"]:
        raise ErrorHuellas("Las huellas finales no coinciden; revisar esta ejecución nueva.")
    return resultado


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("carpeta", type=Path)
    parser.add_argument("--esperadas", type=int,
                        help="Número de huellas exigido; la integración completa actual declara 34.")
    opciones = parser.parse_args()
    try:
        resultado = comprobar_huellas(opciones.carpeta)
    except (ErrorHuellas, OSError, ValueError):
        print("FALLIDO: no se pudo validar la estructura de evidencia; no se modificó ningún archivo.")
        return 1
    if opciones.esperadas is not None and resultado["comprobadas"] != opciones.esperadas:
        resultado["estado"] = "FALLIDO"
    print("{estado}: {coincidentes}/{comprobadas} huellas stdout/stderr coinciden con los bytes finales."
          .format(**resultado))
    for diferencia in resultado["discrepancias"]:
        print("FALLIDO: " + diferencia["archivo"])
    if opciones.esperadas is not None and resultado["comprobadas"] != opciones.esperadas:
        print("FALLIDO: el número de huellas no coincide con el requerido.")
    print("Comprobación de sólo lectura; no se modificó la evidencia.")
    return {"APROBADO": 0, "FALLIDO": 1, "NO EJECUTADO": 2}[resultado["estado"]]


if __name__ == "__main__":
    raise SystemExit(main())
