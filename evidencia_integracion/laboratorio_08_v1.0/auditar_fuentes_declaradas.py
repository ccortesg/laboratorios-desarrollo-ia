"""Cotejo independiente de las declaraciones de fuentes de un pase conjunto.

Lee los originales y la evidencia; sólo escribe un informe nuevo fuera de ambos.
Las declaraciones repetidas no se deduplican. Los hashes de salidas y los
diagnósticos de bases/CSV temporales se verifican en otros alcances.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repositorio", type=Path, required=True)
    parser.add_argument("--evidencia", type=Path, required=True)
    parser.add_argument("--salida", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repositorio.resolve()
    evidencia = args.evidencia.resolve()
    if args.salida.exists():
        raise SystemExit("FALLIDO: el informe de destino ya existe.")
    declaraciones = []
    git_refs = []

    def add(archivo, campo, fuente, esperado, contenido, categoria):
        if not isinstance(esperado, str) or not re.fullmatch(r"[0-9a-f]{64}", esperado):
            raise ValueError("La declaración no tiene formato SHA-256.")
        observado = hashlib.sha256(contenido).hexdigest()
        declaraciones.append({
            "evidencia": archivo.relative_to(evidencia).as_posix(),
            "campo": campo,
            "categoria": categoria,
            "fuente": fuente,
            "sha256_declarado": esperado,
            "sha256_observado": observado,
            "estado": "APROBADO" if esperado == observado else "FALLIDO",
        })

    def leer_relativo(raiz, relativo):
        ruta = raiz / relativo
        if not ruta.resolve().is_relative_to(raiz.resolve()) or ruta.is_symlink():
            raise ValueError("La referencia sale del alcance de lectura autorizado.")
        return ruta.read_bytes()

    for archivo in sorted(evidencia.rglob("sha256_fuentes.json")):
        lab = archivo.parent.name
        for relativo, esperado in json.loads(archivo.read_text(encoding="utf-8")).items():
            fuente = "laboratorios/" + lab + "/" + relativo
            add(archivo, relativo, fuente, esperado,
                leer_relativo(repo, fuente), "manifiestos_fuentes")

    for archivo in sorted(evidencia.rglob("sha256_herramientas.json")):
        lab = archivo.parent.name
        for relativo, esperado in json.loads(archivo.read_text(encoding="utf-8")).items():
            fuente = "laboratorios/" + lab + "/" + relativo
            add(archivo, relativo, fuente, esperado,
                leer_relativo(repo, fuente), "manifiestos_fuentes")

    # El SHA-256 de un archivo histórico se calcula sobre el blob, no sobre
    # su identificador de objeto Git. La copia temporal sólo recibe objetos.
    entorno = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    entorno.update({"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
                    "GIT_TERMINAL_PROMPT": "0", "GIT_OPTIONAL_LOCKS": "0"})
    preparacion = evidencia / "preparacion_laboratorio_04.json"
    prep = json.loads(preparacion.read_text(encoding="utf-8"))
    bundle = repo / prep["bundle"]
    with tempfile.TemporaryDirectory(prefix="cotejo_fuentes_", dir=args.salida.parent) as temporal:
        copia = Path(temporal) / "objetos.git"
        plantilla = Path(temporal) / "plantilla"
        plantilla.mkdir()

        def git(*argumentos):
            proceso = subprocess.run(
                ["git", "-c", "core.hooksPath=" + os.devnull, *argumentos],
                env=entorno, capture_output=True, check=False)
            if proceso.returncode:
                raise RuntimeError("Git no pudo leer los objetos sintéticos del bundle.")
            return proceso.stdout

        git("init", "--quiet", "--bare", "--template=" + str(plantilla), str(copia))
        anunciado = git("-C", str(copia), "bundle", "unbundle", str(bundle)).decode("ascii")
        referencias_bundle = dict(line.split(" ", 1)[::-1] for line in anunciado.splitlines())
        for archivo in sorted(evidencia.rglob("sha256_referencias.json")):
            referencias = json.loads((archivo.parent / "referencias_git.json").read_text(encoding="utf-8"))
            for nombre, archivos in json.loads(archivo.read_text(encoding="utf-8")).items():
                ref = referencias[nombre]
                if not re.fullmatch(r"[0-9a-f]{40}", ref):
                    raise ValueError("Identificador Git no admitido.")
                anunciado = referencias_bundle.get("refs/tags/" + nombre)
                git_refs.append({"nombre": nombre, "commit_declarado": ref,
                                 "commit_bundle": anunciado,
                                 "estado": "APROBADO" if ref == anunciado else "FALLIDO"})
                for relativo, esperado in archivos.items():
                    contenido = git("-C", str(copia), "cat-file", "blob", ref + ":" + relativo)
                    fuente = prep["bundle"] + "@" + ref + ":" + relativo
                    add(archivo, nombre + "/" + relativo, fuente, esperado,
                        contenido, "manifiestos_fuentes")

    add(preparacion, "sha256_bundle", prep["bundle"], prep["sha256_bundle"],
        bundle.read_bytes(), "preparacion_repetida")
    for relativo, esperado in prep["sha256_archivos_del_repositorio"].items():
        fuente = prep["fuente"] + "/repositorio/" + relativo
        add(preparacion, "sha256_archivos_del_repositorio/" + relativo,
            fuente, esperado, leer_relativo(repo, fuente), "preparacion_repetida")

    for archivo in sorted(evidencia.rglob("conservacion_heredados.json")):
        lab = archivo.parent.name
        d = json.loads(archivo.read_text(encoding="utf-8"))
        clave = "registros" if "registros" in d else "archivos"
        registros = d[clave]
        for i, registro in enumerate(registros):
            fuente = "laboratorios/" + lab + "/" + registro["archivo"]
            contenido = leer_relativo(repo, fuente)
            for campo in ("sha256_esperado", "sha256_observado", "esperado", "observado"):
                if campo in registro:
                    add(archivo, clave + "/" + str(i) + "/" + campo, fuente,
                        registro[campo], contenido, "conservacion_repetida")

    categorias = {}
    for categoria in sorted({d["categoria"] for d in declaraciones}):
        seleccion = [d for d in declaraciones if d["categoria"] == categoria]
        categorias[categoria] = {
            "declaraciones": len(seleccion),
            "coincidentes": sum(d["estado"] == "APROBADO" for d in seleccion),
            "fallidas": sum(d["estado"] == "FALLIDO" for d in seleccion),
        }
    aprobadas = sum(d["estado"] == "APROBADO" for d in declaraciones)
    resultado = {
        "estado": "APROBADO" if aprobadas == len(declaraciones)
                  and all(r["estado"] == "APROBADO" for r in git_refs) else "FALLIDO",
        "fecha_hora_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "ejecucion_cotejada": "conjunto_01",
        "metodo": "SHA-256 de bytes crudos de fuentes actuales o blobs del bundle local; sólo lectura de evidencia y originales.",
        "criterio_de_conteo": "Cada campo con una huella de fuente es una declaración; se mantienen todas las repeticiones.",
        "declaraciones": len(declaraciones),
        "coincidentes": aprobadas,
        "fallidas": len(declaraciones) - aprobadas,
        "categorias": categorias,
        "declaraciones_por_documento": dict(sorted(Counter(d["evidencia"] for d in declaraciones).items())),
        "referencias_git_comprobadas": git_refs,
        "alcance": [
            "Todos los sha256_fuentes.json, sha256_herramientas.json y sha256_referencias.json de este pase.",
            "También la preparación de laboratorio 4 y cada campo esperado/observado de conservacion_heredados.json, separados de los manifiestos principales.",
            "Las referencias Git se cotejan con los objetos importados en una carpeta temporal sin modificar referencias del proyecto.",
        ],
        "limites": [
            "Las huellas de stdout/stderr tienen su auditoría separada; no se suman a estas declaraciones de fuentes.",
            "No se cotejan aquí hashes de bases o CSV temporales incrustados en resultados funcionales: esos archivos pertenecen a bases aisladas eliminadas tras sus pruebas.",
            "No se reevalúa ni reescribe evidencia histórica; no se normalizan saltos de línea ni texto.",
            "Este cotejo verifica correspondencia de bytes; no añade casos funcionales ni acredita una ejecución en Windows o en una herramienta comercial.",
        ],
        "registros": declaraciones,
    }
    args.salida.write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: resultado[k] for k in ("estado", "declaraciones", "coincidentes", "fallidas", "categorias")}, ensure_ascii=False))
    return 0 if resultado["estado"] == "APROBADO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
