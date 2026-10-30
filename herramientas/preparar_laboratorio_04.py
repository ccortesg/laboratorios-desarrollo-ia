"""Reconstruye una copia independiente del laboratorio 4 desde su bundle local.

Requiere Python 3.10 o posterior y Git. No usa red ni modifica los materiales
de referencia. Un destino existente se rechaza, aunque esté vacío.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
REFERENCIAS = {
    "inicio": "25f9b7a6d09341b6419d3d27237f1f1b68a6b64d",
    "solucion": "d7782e31acff5bd599f70ce6bb288f0a4219f775",
}


class ErrorPreparacion(Exception):
    def __init__(self, mensaje, estado="BLOQUEADO"):
        super().__init__(mensaje)
        self.estado = estado


def entorno_local():
    """Aísla Git de configuración personal sin leer secretos del equipo."""
    entorno = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    entorno.update({
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_OPTIONAL_LOCKS": "0",
        "GIT_AUTHOR_NAME": "Laboratorio",
        "GIT_AUTHOR_EMAIL": "sintetico",
        "GIT_COMMITTER_NAME": "Laboratorio",
        "GIT_COMMITTER_EMAIL": "sintetico",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONIOENCODING": "utf-8",
    })
    return entorno


def git(argumentos, cwd):
    proceso = subprocess.run(
        ["git", "-c", "core.hooksPath=" + os.devnull,
         "-c", "core.autocrlf=false", "-c", "core.logAllRefUpdates=false",
         *argumentos],
        cwd=cwd, env=entorno_local(), capture_output=True,
        text=True, encoding="utf-8", errors="replace", check=False,
    )
    if proceso.returncode:
        # No se publica stderr, que puede incorporar rutas del equipo.
        raise ErrorPreparacion("Git no pudo completar " + argumentos[0] + ".")
    return proceso.stdout


def huellas_archivos(carpeta):
    resultado = {}
    for archivo in sorted(carpeta.rglob("*")):
        relativo = archivo.relative_to(carpeta)
        if ".git" in relativo.parts:
            continue
        if archivo.is_symlink():
            raise ErrorPreparacion("No se admiten enlaces simbólicos en el material de referencia.")
        if archivo.is_file():
            resultado[relativo.as_posix()] = hashlib.sha256(archivo.read_bytes()).hexdigest()
    return resultado


def guardar_json(ruta, contenido):
    ruta.write_text(json.dumps(contenido, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def preparar(destino, raiz=RAIZ):
    """Crea el destino una vez; si algo falla deja la copia parcial para revisión."""
    destino = Path(destino).resolve()
    raiz = Path(raiz).resolve()
    fuente = raiz / "laboratorios" / "laboratorio_04"
    bundle = raiz / "historiales" / "laboratorio_04.bundle"
    if destino.exists():
        raise ErrorPreparacion("El destino ya existe; elige una carpeta nueva.")
    if ".git" in destino.parts:
        raise ErrorPreparacion("El destino no puede quedar dentro de metadatos Git.")
    if not shutil.which("git"):
        raise ErrorPreparacion("Git no está disponible en PATH.")
    if not fuente.is_dir() or not (fuente / "repositorio").is_dir() or not bundle.is_file():
        raise ErrorPreparacion("Faltan el laboratorio visible o su bundle local.")
    if (destino.is_relative_to(raiz / "laboratorios")
            or destino.is_relative_to(raiz / "historiales")):
        raise ErrorPreparacion("El destino debe estar fuera del material de referencia.")

    # Recorre antes de copiar para rechazar enlaces y establecer la referencia.
    huellas_archivos(fuente)
    esperado = huellas_archivos(fuente / "repositorio")
    if not esperado:
        raise ErrorPreparacion("El repositorio visible está vacío.")
    destino.mkdir(parents=True, exist_ok=False)
    for archivo in sorted(fuente.rglob("*")):
        relativo = archivo.relative_to(fuente)
        if relativo.parts[0] == "repositorio":
            continue
        if archivo.is_dir():
            (destino / relativo).mkdir(parents=True, exist_ok=True)
        elif archivo.is_file():
            (destino / relativo).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(archivo, destino / relativo)

    repositorio = destino / "repositorio"
    plantilla = destino / "plantilla_git_vacia"
    plantilla.mkdir()
    git(["clone", "--quiet", "--no-checkout", "--branch", "main",
         "--template", str(plantilla), str(bundle), str(repositorio)], cwd=destino)
    plantilla.rmdir()
    git(["remote", "remove", "origin"], cwd=repositorio)
    git(["config", "core.autocrlf", "false"], cwd=repositorio)
    git(["config", "core.logAllRefUpdates", "false"], cwd=repositorio)
    git(["config", "user.name", "Laboratorio"], cwd=repositorio)
    git(["config", "user.email", "sintetico"], cwd=repositorio)
    git(["config", "commit.gpgsign", "false"], cwd=repositorio)
    git(["checkout", "--quiet", "main"], cwd=repositorio)

    observadas = {ref: git(["rev-parse", "refs/tags/" + ref + "^{commit}"],
                           cwd=repositorio).strip()
                  for ref in REFERENCIAS}
    if observadas != REFERENCIAS:
        raise ErrorPreparacion("Las etiquetas no coinciden con el laboratorio distribuido.", "FALLIDO")
    if git(["rev-parse", "HEAD"], cwd=repositorio).strip() != REFERENCIAS["solucion"]:
        raise ErrorPreparacion("La rama main no apunta a la solución esperada.", "FALLIDO")
    if git(["remote"], cwd=repositorio).strip():
        raise ErrorPreparacion("La copia conserva un remoto inesperado.", "FALLIDO")
    git(["fsck", "--no-reflogs"], cwd=repositorio)
    observado = huellas_archivos(repositorio)
    if observado != esperado:
        raise ErrorPreparacion("Los archivos visibles no coinciden con la solución del historial.", "FALLIDO")
    if git(["status", "--porcelain=v1", "--untracked-files=all"], cwd=repositorio):
        raise ErrorPreparacion("El árbol reconstruido no está limpio.", "FALLIDO")

    registro = {
        "estado": "APROBADO",
        "fecha_hora_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fuente": "laboratorios/laboratorio_04",
        "bundle": "historiales/laboratorio_04.bundle",
        "sha256_bundle": hashlib.sha256(bundle.read_bytes()).hexdigest(),
        "referencias": observadas,
        "rama": "main",
        "arbol_limpio": True,
        "remotos": [],
        "archivos_comparados": len(observado),
        "contenido_visible_identico_a_solucion": True,
        "sha256_archivos_del_repositorio": observado,
        "pruebas_funcionales": "NO EJECUTADO por este preparador",
        "red": "No utilizada",
        "limite": "Comprueba reconstrucción e integridad; ejecutar las pruebas por separado.",
    }
    guardar_json(destino / "PREPARACION.json", registro)
    return registro


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destino", type=Path, default=RAIZ / "trabajo" / "laboratorio_04",
                        help="Carpeta nueva; por defecto trabajo/laboratorio_04 en este repositorio.")
    opciones = parser.parse_args()
    try:
        registro = preparar(opciones.destino)
    except ErrorPreparacion as error:
        print(error.estado + ": " + str(error))
        return 1 if error.estado == "FALLIDO" else 2
    except (OSError, ValueError):
        print("BLOQUEADO: no se pudo completar la copia local. Los originales no se modificaron.")
        return 2
    print("APROBADO: copia independiente creada en el destino indicado.")
    print("Etiquetas inicio y solucion conservadas; main en solucion; árbol limpio; sin remoto.")
    print(str(registro["archivos_comparados"]) + " archivos visibles coinciden con el historial.")
    print("Desde la copia: python verificar.py --salida nueva_evidencia")
    print("Desde su carpeta repositorio: python pruebas.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
