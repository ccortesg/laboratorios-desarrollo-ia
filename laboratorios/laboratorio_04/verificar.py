"""Comprueba los commits etiquetados del laboratorio, no las ediciones actuales."""

import argparse
import hashlib
import io
import json
import os
import platform
import shutil
import sqlite3
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent
REPO = BASE / "repositorio"
HEREDADOS = ["C01", "C02", "C03", "C04", "B01", "B02", "B03", "B04", "B05", "B06"]
NUEVOS = ["N%02d" % n for n in range(1, 11)]
CAMBIOS = ["contexto/ARQUITECTURA.md", "contexto/CONTEXTO.md",
           "contexto/CONTINUIDAD.md", "contexto/DECISIONES.md",
           "detalle.py", "pruebas.py", "pruebas_detalle.py"]


def guardar(carpeta, nombre, datos):
    (carpeta / nombre).write_text(
        json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def entorno_git():
    variables = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    variables.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
                     GIT_TERMINAL_PROMPT="0", GIT_OPTIONAL_LOCKS="0")
    return variables


def ejecutar_git(argumentos, binario=False):
    resultado = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *argumentos],
        cwd=REPO, env=entorno_git(), capture_output=True, check=False,
    )
    if binario:
        return resultado
    return {"comando": "git " + " ".join(argumentos),
            "codigo_salida": resultado.returncode,
            "salida": resultado.stdout.decode("utf-8", errors="replace"),
            "stderr_presente": bool(resultado.stderr)}


def extraer_referencia(ref, destino):
    resultado = ejecutar_git(["archive", "refs/tags/" + ref], binario=True)
    if resultado.returncode:
        raise RuntimeError("No se pudo extraer la referencia " + ref + ".")
    with tarfile.open(fileobj=io.BytesIO(resultado.stdout), mode="r:") as archivo:
        for miembro in archivo.getmembers():
            relativo = Path(miembro.name)
            if relativo.is_absolute() or ".." in relativo.parts:
                raise RuntimeError("El archivo Git contiene una ruta no admitida.")
            destino_archivo = destino / relativo
            if miembro.isdir():
                destino_archivo.mkdir(parents=True, exist_ok=True)
            elif miembro.isfile():
                destino_archivo.parent.mkdir(parents=True, exist_ok=True)
                origen = archivo.extractfile(miembro)
                if origen is None:
                    raise RuntimeError("No se pudo leer un archivo del commit.")
                destino_archivo.write_bytes(origen.read())
            else:
                raise RuntimeError("Se admiten sólo directorios y archivos regulares.")


def evaluar_ref(ref, salida):
    esperados = HEREDADOS if ref == "inicio" else HEREDADOS + NUEVOS
    with tempfile.TemporaryDirectory(prefix="laboratorio04_") as temporal:
        destino = Path(temporal)
        extraer_referencia(ref, destino)
        huellas = {p.relative_to(destino).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted(destino.rglob("*")) if p.is_file()}
        registro = destino / "resultado_pruebas.json"
        resultado = subprocess.run(
            [sys.executable, "pruebas.py", "--json", str(registro)],
            cwd=destino, capture_output=True, text=True, check=False,
        )
        # Las salidas normales de la batería sólo contienen criterios y datos sintéticos.
        texto = resultado.stdout.replace(temporal, "<temporal>")
        (salida / ("pruebas_" + ref + ".txt")).write_text(texto, encoding="utf-8")
        if not registro.is_file():
            raise RuntimeError("La batería de " + ref + " no produjo un registro.")
        pruebas = json.loads(registro.read_text(encoding="utf-8"))
        guardar(salida, "pruebas_" + ref + ".json", pruebas)
        registros = pruebas.get("pruebas", [])
        aprobada = (
            resultado.returncode == 0 and not resultado.stderr
            and [p["id"] for p in registros] == esperados
            and all(p["estado"] == "APROBADO" for p in registros)
            and pruebas["ejecutados"] == len(esperados)
            and pruebas["aprobados"] == len(esperados)
            and pruebas["fallidos"] == 0
            and pruebas["errores_de_ejecucion"] == 0
            and pruebas["no_ejecutados"] == 0
        )
        resumen = {
            "referencia": ref,
            "comando_en_copia_extraida": "python pruebas.py --json resultado_pruebas.json",
            "estado": "APROBADO" if aprobada else "FALLIDO",
            "codigo_salida": resultado.returncode,
            "ejecutados": pruebas["ejecutados"], "aprobados": pruebas["aprobados"],
            "fallidos": pruebas["fallidos"],
            "errores_de_ejecucion": pruebas["errores_de_ejecucion"],
            "criterios_no_ejecutados": NUEVOS if ref == "inicio" else [],
            "motivo_no_ejecutados": (
                "Detalle y su batería todavía no existen en inicio; no son fallos ni aprobaciones."
                if ref == "inicio" else ""
            ),
            "stderr_presente": bool(resultado.stderr),
        }
        return resumen, huellas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, required=True,
                        help="Carpeta nueva fuera del repositorio")
    opciones = parser.parse_args()
    salida = opciones.salida.resolve()
    if salida.exists():
        print("BLOQUEADO: la carpeta de salida ya existe; elige otra.")
        return 2
    if salida.is_relative_to(REPO.resolve()):
        print("BLOQUEADO: guarda la evidencia fuera del repositorio.")
        return 2
    salida.mkdir(parents=True)
    if not shutil.which("git"):
        guardar(salida, "resumen.json", {"estado": "BLOQUEADO", "motivo": "Git no está disponible en PATH."})
        print("BLOQUEADO: Git no está disponible en PATH.")
        return 2
    if not (REPO / ".git").is_dir():
        guardar(salida, "resumen.json", {"estado": "BLOQUEADO", "motivo": "Falta el directorio .git del paquete."})
        print("BLOQUEADO: falta el directorio .git del paquete.")
        return 2
    try:
        version = ejecutar_git(["--version"])
        entorno = {"fecha_utc": datetime.now(timezone.utc).isoformat(),
                   "sistema": platform.system(), "python": platform.python_version(),
                   "implementacion_python": platform.python_implementation(),
                   "sqlite": sqlite3.sqlite_version, "git": version["salida"].strip(),
                   "modalidad": "Ejecución local de pruebas sobre commits etiquetados",
                   "uso_de_codex": "NO EJECUTADO por este verificador"}
        guardar(salida, "entorno.json", entorno)
        referencias = {}
        for ref in ["inicio", "solucion"]:
            r = ejecutar_git(["rev-parse", "refs/tags/" + ref + "^{commit}"])
            if r["codigo_salida"]:
                raise RuntimeError("Falta una referencia Git válida: " + ref + ".")
            referencias[ref] = r["salida"].strip()
        guardar(salida, "referencias_git.json", referencias)
        revisiones = {
            "status_actual": ejecutar_git(["status", "--porcelain=v1"]),
            "diff_actual": ejecutar_git(["diff", "--"]),
            "diff_preparado": ejecutar_git(["diff", "--cached", "--"]),
            "cambios_entre_referencias": ejecutar_git(["diff", "--name-status", "inicio", "solucion", "--"]),
            "formato_entre_referencias": ejecutar_git(["diff", "--check", "inicio", "solucion", "--"]),
            "integridad_git": ejecutar_git(["fsck", "--no-reflogs"]),
            "remotos": ejecutar_git(["remote"]),
        }
        guardar(salida, "revision_git.json", revisiones)
        diferencia = ejecutar_git(["diff", "inicio", "solucion", "--"])
        (salida / "cambio.diff").write_text(diferencia["salida"], encoding="utf-8")
        nombres = ejecutar_git(["diff", "--name-only", "inicio", "solucion", "--"])
        forma_git = (all(r["codigo_salida"] == 0 for r in revisiones.values())
                     and diferencia["codigo_salida"] == 0
                     and nombres["codigo_salida"] == 0
                     and nombres["salida"].splitlines() == CAMBIOS
                     and revisiones["remotos"]["salida"] == "")
        ejecuciones, huellas = [], {}
        for ref in ["inicio", "solucion"]:
            resultado, hashes = evaluar_ref(ref, salida)
            ejecuciones.append(resultado)
            huellas[ref] = hashes
        guardar(salida, "sha256_referencias.json", huellas)
        guardar(salida, "sha256_herramientas.json", {
            n: hashlib.sha256((BASE / n).read_bytes()).hexdigest()
            for n in ["README.md", "verificar.py"]
        })
        aprobado = forma_git and all(r["estado"] == "APROBADO" for r in ejecuciones)
        resumen = {"estado": "APROBADO" if aprobado else "FALLIDO",
                   "objeto": "Referencias inicio y solucion; no las ediciones actuales",
                   "referencias": referencias, "baterias": ejecuciones,
                   "revision_git": "APROBADO" if forma_git else "FALLIDO",
                   "archivos_del_cambio": nombres["salida"].splitlines(),
                   "arbol_actual_limpio": revisiones["status_actual"]["salida"] == "",
                   "limite_arbol_actual": "El estado y las diferencias se observan; las pruebas se ejecutan en copias de las etiquetas.",
                   "fallos_intencionales": [],
                   "sesion_codex": "NO EJECUTADO por este verificador"}
        guardar(salida, "resumen.json", resumen)
        print(resumen["estado"] + ": referencias Git verificadas.")
        for r in ejecuciones:
            print(r["referencia"] + ": " + str(r["aprobados"]) + "/" + str(r["ejecutados"])
                  + " aprobados; salida " + str(r["codigo_salida"]) + ".")
        print("Las pruebas anteriores no evalúan modificaciones actuales sin commit.")
        return 0 if aprobado else 1
    except (OSError, RuntimeError, ValueError, KeyError, tarfile.TarError) as exc:
        # El tipo se conserva; no se publican trazas con rutas temporales o del equipo.
        detalle = str(exc) if isinstance(exc, RuntimeError) else "No se pudo completar la verificación local."
        guardar(salida, "resumen.json", {"estado": "BLOQUEADO", "motivo": detalle,
                                         "tipo_error": type(exc).__name__})
        print("BLOQUEADO: " + detalle)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
