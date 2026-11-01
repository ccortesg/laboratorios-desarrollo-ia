#!/usr/bin/env python3
"""Cotejo de solo lectura: ZIP recibido, paquete original y consulta conservada.

No ejecuta contenido recibido, comandos Git ni solicitudes de red. El resultado
remoto corresponde a la fecha declarada en la instantanea que se proporciona.
Solo escribe --salida si ese archivo aun no existe.
"""
import argparse
import hashlib
import json
import stat
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ZIP_ESPERADO = "0cc40f48d9ce456c9f88cc333fb5ec1a6614cc332b7ee43a10804a751198d37f"
ORIGINAL_ESPERADO = "9b7326bfc365631765ae6f9213ecb7dce77454debcb6472b045f73020b9c62cd"
COMMIT = "9212ee99b88f70f0b289837b88d6bbf34da91a52"
ARBOL = "d7cc2ce8b1502daa6c53c14f2aa1c8fb6984aaf0"
BASE = "46f389bc4acf3e231a8eb1a1bb3972db0fe7e622"
WINDOWS = "9ea6109fe8e89a2785bdce255252ffaabea1d122"


def sha(datos):
    return hashlib.sha256(datos).hexdigest()


def pares_unicos(pares):
    salida = {}
    for clave, valor in pares:
        if clave in salida:
            raise ValueError("Clave JSON duplicada: " + clave)
        salida[clave] = valor
    return salida


def json_bytes(datos):
    return json.loads(datos.decode("utf-8"), object_pairs_hook=pares_unicos)


def leer_zip(ruta):
    datos = ruta.read_bytes()
    with zipfile.ZipFile(ruta) as paquete:
        miembros = paquete.infolist()
        nombres = [i.filename for i in miembros]
        if len(nombres) != len(set(nombres)):
            raise ValueError("Nombres ZIP duplicados")
        if sum(i.file_size for i in miembros) > 20 * 1024 * 1024:
            raise ValueError("Tamano descomprimido fuera del alcance del cotejo")
        raices = set()
        archivos = {}
        for entrada in miembros:
            nombre = entrada.filename
            p = PurePosixPath(nombre)
            if (p.is_absolute() or ".." in p.parts or "\\" in nombre
                    or ":" in nombre or len(p.parts) < 2
                    or stat.S_ISLNK(entrada.external_attr >> 16)):
                raise ValueError("Entrada ZIP fuera del contrato")
            raices.add(p.parts[0])
            if not entrada.is_dir():
                archivos[PurePosixPath(*p.parts[1:]).as_posix()] = paquete.read(entrada)
        if len(raices) != 1 or paquete.testzip() is not None:
            raise ValueError("Estructura o CRC de ZIP incorrecto")
    return datos, archivos


def auditar(evidencia, original, remoto):
    resultados = []

    def comprobar(nombre, condicion, detalle):
        resultados.append({"comprobacion": nombre,
                           "estado": "APROBADO" if condicion else "FALLIDO",
                           "detalle": detalle})

    recibidos, f = leer_zip(evidencia)
    originales, o = leer_zip(original)
    r = json_bytes(remoto.read_bytes())
    comprobar("Identidad del ZIP recibido", sha(recibidos) == ZIP_ESPERADO, sha(recibidos))
    comprobar("Identidad independiente del paquete original", sha(originales) == ORIGINAL_ESPERADO, sha(originales))
    manifest = json_bytes(f["SHA256_ARCHIVOS.json"])
    cobertura = set(f) - {"SHA256_ARCHIVOS.json"}
    comprobar("Cobertura exacta del manifiesto recibido",
              len(f) == 116 and len(manifest) == 115 and set(manifest) == cobertura,
              {"archivos": len(f), "declaraciones": len(manifest)})
    errores_manifest = [n for n, h in manifest.items() if n not in f or sha(f[n]) != h]
    comprobar("Bytes del manifiesto recibido", not errores_manifest, {"coincidentes": len(manifest)-len(errores_manifest), "errores": errores_manifest})
    copia = {n[len("paquete_original/"):]: b for n, b in f.items() if n.startswith("paquete_original/")}
    diferencias = sorted(n for n in set(copia) | set(o) if copia.get(n) != o.get(n))
    comprobar("Copia incorporada frente al original recuperado por separado",
              len(copia) == 27 and not diferencias,
              {"archivos": len(copia), "diferencias": diferencias})
    sumas = {}
    for linea in o["SHA256SUMS"].decode("utf-8").splitlines():
        h, nombre = linea.split("  ", 1)
        if nombre in sumas:
            raise ValueError("Declaracion duplicada en SHA256SUMS")
        sumas[nombre] = h
    comprobar("Manifiesto original", len(sumas) == 26 and set(sumas) == set(o)-{"SHA256SUMS"}
              and all(sha(o[n]) == h for n, h in sumas.items()),
              {"archivos_declarados": len(sumas)})
    base = json_bytes(o["BASE_CIERRE.json"])
    protegidos = json_bytes(o[base["archivo_protegidos"]])
    documentales = base["archivos_documentales"]
    comprobar("Contrato de origen e identidades de arbol",
              (base["base_commit"], base["arbol_verificado"], base["arbol_documental"]) == (BASE, WINDOWS, ARBOL),
              {"base": BASE, "windows": WINDOWS, "documental": ARBOL})
    comprobar("Parche y mapa protegido",
              sha(o[base["parche"]]) == base["sha256_parche"] and sha(o[base["archivo_protegidos"]]) == base["sha256_archivo_protegidos"],
              "Huellas cotejadas con la entrega original; no se ejecuta el parche.")
    comprobar("Separacion del alcance documental y protegido",
              len(protegidos) == 1486 and len(documentales) == 25 and not set(protegidos).intersection(documentales),
              {"protegidos": len(protegidos), "documentales": len(documentales), "recalculo_individual_de_blobs_remotos": "NO EJECUTADO"})
    antes = json_bytes(f["antes.json"])
    preparado = json_bytes(f["preparado.json"])
    prepub = json_bytes(f["prepublicacion.json"])
    cierre = json_bytes(f["RESULTADO_CIERRE.json"])
    enlaces = [
        ("antes/configuracion", antes["sha256_base_cierre"], sha(o["BASE_CIERRE.json"])),
        ("antes/manifiesto", antes["paquete"]["sha256_manifiesto"], sha(o["SHA256SUMS"])),
        ("preparado/antes", preparado["sha256_antes"], sha(f["antes.json"])),
        ("prepublicacion/preparado", prepub["sha256_preparado"], sha(f["preparado.json"])),
        ("cierre/prepublicacion", cierre["sha256_prepublicacion"], sha(f["prepublicacion.json"])),
        ("cierre/configuracion", cierre["sha256_base_cierre"], sha(o["BASE_CIERRE.json"]))]
    comprobar("Seis enlaces de la cadena documental", all(a == b for _, a, b in enlaces),
              [{"enlace": n, "coincide": a == b} for n, a, b in enlaces])
    comprobar("Preparacion y cierre registrados",
              antes["identidad"]["arbol_indice"] == WINDOWS
              and preparado["identidad"]["arbol_indice"] == ARBOL
              and cierre["identidad_git"]["head"] == COMMIT
              and cierre["identidad_git"]["main"] == COMMIT
              and cierre["identidad_git"]["rama"] == "main"
              and cierre["identidad_git"]["arbol_indice"] == ARBOL
              and cierre["identidad_git"]["sin_preparar"] == ""
              and cierre["identidad_git"]["no_seguidos"] == "",
              "La limpieza local corresponde al instante capturado, no a una consulta actual del ordenador del autor.")
    resumen = json_bytes(f["RESUMEN_OPERACIONES.json"])
    capturas, finales, sin_hashes_separados = [], [], []
    for ruta in sorted(n for n in f if n.startswith("operaciones/") and n.endswith("/comando.json")):
        c = json_bytes(f[ruta])
        carpeta = str(PurePosixPath(ruta).parent)
        captura = PurePosixPath(carpeta).name
        capturas.append({"captura": captura, "codigo_salida": c["codigo_salida"], "comando": c["comando"]})
        for flujo in ("stdout", "stderr"):
            archivo = carpeta + "/" + c[flujo]
            if "sha256_finales" in c:
                finales.append({"archivo": archivo, "coincide": sha(f[archivo]) == c["sha256_finales"][flujo]})
            else:
                sin_hashes_separados.append(archivo)
    comprobar("Resumen de 23 operaciones frente a sus capturas", len(capturas) == 23
              and all({k: x[k] for k in ("captura", "codigo_salida", "comando")} == y for x,y in zip(resumen["registros"], capturas))
              and len(resumen["registros"]) == len(capturas), capturas)
    comprobar("Huellas finales explicitamente declaradas", len(finales) == 32 and all(x["coincide"] for x in finales),
              {"declaradas": len(finales), "coincidentes": sum(x["coincide"] for x in finales), "flujos_sin_huella_separada": len(sin_hashes_separados), "cobertura_de_esos_flujos": "Manifiesto general final; no se reconstruyen hashes de captura."})
    fallos = [(x["captura"], x["codigo_salida"]) for x in capturas if x["codigo_salida"]]
    comprobar("Incidencia de indice conservada y resuelta",
              fallos == [("06_refrescar_estadisticas", 128)]
              and b"index.lock" in f["operaciones/06_refrescar_estadisticas/stderr.txt"]
              and capturas[6]["codigo_salida"] == 0,
              {"fallos_registrados": fallos, "reintento": capturas[6]["codigo_salida"]})
    pruebas = f["operaciones/04_pruebas_recolector/stderr.txt"].decode("utf-8")
    comprobar("Ocho pruebas WSL del recolector en captura",
              capturas[3]["codigo_salida"] == 0 and "Ran 8 tests" in pruebas and "\nOK\n" in pruebas,
              "Revision de la salida recibida; las pruebas no se reejecutan en esta auditoria.")
    push = json_bytes(f["operaciones/22_push_atomico/comando.json"])
    argv = ["git", "push", "--atomic", "--no-follow-tags", "origin", "refs/heads/main:refs/heads/main", "refs/tags/lab-08-v1.0:refs/tags/lab-08-v1.0", "refs/tags/repositorio-v1.4:refs/tags/repositorio-v1.4"]
    comprobar("Publicacion atomica exacta registrada", push["comando"] == argv and push["codigo_salida"] == 0,
              {"comando": push["comando"], "codigo_salida": push["codigo_salida"]})
    historicas = base["etiquetas_historicas"]
    nuevas = {"refs/tags/" + n: COMMIT for n in base["etiquetas_previstas"]}
    comprobar("Referencias nuevas e historicas en consulta independiente",
              r["main"] == COMMIT and r["etiquetas"] == dict(historicas, **nuevas),
              {"fecha_consulta": r["fecha_registro_utc"], "historicas": len(historicas), "nuevas": len(nuevas), "main": r["main"]})
    comprobar("Commit remoto y arbol preparado previamente",
              r["commit"]["sha"] == COMMIT and r["commit"]["arbol"] == ARBOL and r["commit"]["padres"] == [BASE],
              r["commit"])
    comprobar("Estado final recibido y observacion remota independiente",
              cierre["consulta_remota"]["referencias"] == dict({"refs/heads/main": r["main"]}, **r["etiquetas"]),
              "La consulta externa confirma las identidades; no constituye una nueva publicacion.")
    comprobar("Originales de entrada conservados", sha(evidencia.read_bytes()) == ZIP_ESPERADO and sha(original.read_bytes()) == ORIGINAL_ESPERADO,
              "Lectura binaria; ningun archivo recibido fue reescrito.")
    return {
        "estado": "APROBADO" if all(x["estado"] == "APROBADO" for x in resultados) else "FALLIDO",
        "fecha_revision_utc": datetime.now(timezone.utc).isoformat(),
        "alcance": "Cotejo documental y de bytes; consulta remota independiente conservada. Sin ejecutar scripts del ZIP ni pruebas funcionales.",
        "comprobaciones": resultados,
        "limites": [
            "No se reejecutaron las 583 pruebas funcionales historicas de Windows.",
            "No se reejecutaron aqui las ocho pruebas WSL del recolector; se reviso su captura.",
            "No se recalcularon individualmente 1.486 blobs remotos: se cotejo su mapa original, sus registros de conservacion y la igualdad del arbol Git remoto con el arbol documental del paquete previo.",
            "No se reconstruyeron hashes capturados ausentes de las primeras siete operaciones.",
            "El codigo no realiza nuevas consultas remotas al reproducir esta auditoria: comprueba la instantanea fechada proporcionada."
        ],
        "observacion_documental": "Las referencias heredadas a Git Bash en dos estados y metodo_subida se precisan como WSL2/Linux en las notas y en la nueva continuidad, sin reescribir originales."
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--evidencia", type=Path, required=True)
    p.add_argument("--original", type=Path, required=True)
    p.add_argument("--remoto", type=Path, required=True)
    p.add_argument("--salida", type=Path, required=True)
    args = p.parse_args()
    if args.salida.exists():
        raise SystemExit("La salida ya existe; se conserva sin modificaciones.")
    resultado = auditar(args.evidencia, args.original, args.remoto)
    with args.salida.open("x", encoding="utf-8", newline="\n") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
        f.write("\n")
    fallidos = [r["comprobacion"] for r in resultado["comprobaciones"] if r["estado"] == "FALLIDO"]
    print(resultado["estado"] + ": cotejo de integridad y continuidad; " + str(len(fallidos)) + " discrepancias.")
    for nombre in fallidos:
        print("FALLIDO: " + nombre)
    raise SystemExit(1 if fallidos else 0)


if __name__ == "__main__":
    main()
