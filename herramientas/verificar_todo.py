"""Ejecuta los ocho recorridos en copias temporales y conserva evidencia nueva.

Los fallos didácticos esperados se evalúan por identificador y tipo de error.
La evidencia histórica distribuida nunca se sobrescribe. Requiere Python 3.10+
y Git. Los laboratorios 6 a 8 usan HTTP local; --navegador requiere Node, Playwright
y Chromium instalados. No descarga dependencias ni contacta servicios externos.
"""

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from huellas_evidencia import ErrorHuellas, cerrar_evidencia

from preparar_laboratorio_04 import (
    RAIZ, REFERENCIAS, ErrorPreparacion, entorno_local, guardar_json,
    huellas_archivos, preparar,
)


C = ["C%02d" % n for n in range(1, 5)]
B = ["B%02d" % n for n in range(1, 7)]
N = ["N%02d" % n for n in range(1, 11)]
P = ["P%02d" % n for n in range(1, 7)]
W_HTTP = ["W01", "W02", "W03", "W04.a", "W04.b"]
W_NAVEGADOR = ["W05", "W06.a", "W06.b"]
I = (["I01"] + ["I02." + c for c in "abcde"]
     + ["I03." + c for c in "abc"] + ["I04." + c for c in "abcd"]
     + ["I05", "I06", "I07", "I08"])
D = ["D01", "D02", "D03", "D05", "D06.a", "D06.b", "D07.a", "D07.b", "D08.a", "D08.b"]
D_NAVEGADOR = ["D04"]


def leer_json(ruta):
    return json.loads(ruta.read_text(encoding="utf-8"))


def sanear(texto, raiz, salida, temporal):
    reemplazos = [(str(salida), "SALIDA"), (str(temporal), "TEMPORAL"),
                  (str(raiz), "REPOSITORIO"), (str(sys.executable), "python")]
    for original, sustituto in sorted(reemplazos, key=lambda item: len(item[0]), reverse=True):
        texto = texto.replace(original, sustituto)
        texto = texto.replace(original.replace("\\", "\\\\"), sustituto)
    return re.sub(r'File "([^\"]+)"',
                  lambda m: 'File "' + m.group(1).replace("\\", "/").split("/")[-1] + '"',
                  texto)


def ejecutar(argumentos, carpeta, raiz, salida, temporal, registro, entorno_extra=None):
    entorno = entorno_local()
    if entorno_extra:
        entorno.update(entorno_extra)
    resultado = subprocess.run(
        [sys.executable, *argumentos], cwd=carpeta, env=entorno,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        check=False,
    )
    registro.write_text(sanear(resultado.stdout + resultado.stderr, raiz, salida, temporal),
                        encoding="utf-8")
    return resultado.returncode


def evaluar_bateria(registro, identificador, ids, codigo, fallos=(), no_ejecutados=(),
                     permitir_bloqueo=False, bloqueos_parciales=()):
    """Evalúa un contrato observable; un error ajeno nunca cuenta como fallo esperado."""
    fallos, no_ejecutados = set(fallos), set(no_ejecutados)
    esperado = {i: ("FALLIDO" if i in fallos else
                   "NO EJECUTADO" if i in no_ejecutados else "APROBADO") for i in ids}
    casos = registro["pruebas"]
    observados = {}
    for caso in casos:
        coincidencia = re.match(r"test_([cbnp]\d{2})_", caso.get("prueba", ""))
        clave = caso.get("id") or (coincidencia.group(1).upper() if coincidencia else "DESCONOCIDO")
        if clave in observados:
            raise ValueError("Criterio duplicado")
        observados[clave] = caso["estado"]
    bloqueo_total = permitir_bloqueo and observados == {i: "BLOQUEADO" for i in ids}
    ids_bloqueados = {i for i, estado in observados.items() if estado == "BLOQUEADO"}
    bloqueo_parcial = (permitir_bloqueo and bool(ids_bloqueados)
                       and ids_bloqueados <= set(bloqueos_parciales))
    bloqueados = bloqueo_total or bloqueo_parcial
    if bloqueados:
        fallos -= ids_bloqueados
        no_ejecutados -= ids_bloqueados
        esperado.update({i: "BLOQUEADO" for i in ids_bloqueados})
    ejecutados = len(ids) - len(no_ejecutados) - (len(ids_bloqueados) if bloqueados else 0)
    conteos = {
        "aprobados": ejecutados - len(fallos), "fallidos": len(fallos),
        "fallos_de_asercion": len(fallos), "errores_de_ejecucion": 0,
        "bloqueados": len(ids_bloqueados) if bloqueados else 0, "no_ejecutados": len(no_ejecutados),
    }
    correcto = (
        (codigo == (2 if bloqueados else 1 if fallos else 0)
         or (codigo is None and (bloqueo_total or no_ejecutados == set(ids))))
        and len(casos) == len(ids) and observados == esperado
        and all(registro[k] == valor for k, valor in conteos.items())
        and registro.get("total", registro.get("criterios_registrados",
                         registro.get("casos_registrados"))) == len(ids)
        and registro.get("ejecutados", ejecutados) == ejecutados
        and all(p.get("tipo_error") == "AssertionError"
                for p in casos if p["estado"] == "FALLIDO")
    )
    return {
        "bateria": identificador,
        "evaluacion_del_recorrido": ("BLOQUEADO" if bloqueados else "APROBADO")
        if correcto else "FALLIDO",
        "codigo_salida_bateria": codigo,
        "ejecutados": registro.get("ejecutados", registro.get("total")),
        "aprobados": registro["aprobados"], "fallidos": registro["fallidos"],
        "no_ejecutados": registro["no_ejecutados"],
        "bloqueados": registro["bloqueados"],
        "errores_de_ejecucion": registro["errores_de_ejecucion"],
        "fallos_intencionales_esperados": sorted(fallos),
        "criterios_observados": observados,
    }


def evaluar_laboratorio(numero, evidencia):
    resumen = leer_json(evidencia / "resumen.json")
    baterias = []
    if numero == 1:
        correcto = resumen["estado_del_recorrido_didactico"] == "APROBADO"
        for estado in ["inicial", "solucion"]:
            baterias.append(evaluar_bateria(
                leer_json(evidencia / ("pruebas_" + estado + ".json")),
                "laboratorio_01/" + estado, C,
                resumen["versiones"][estado]["codigo_salida_pruebas"],
                fallos=["C04"] if estado == "inicial" else [],
            ))
    elif numero == 2:
        correcto = resumen["estado"] == "APROBADO"
        baterias.append(evaluar_bateria(
            leer_json(evidencia / "pruebas_solucion.json"), "laboratorio_02/solucion", C,
            resumen["pruebas"]["codigo_salida"],
        ))
    elif numero == 3:
        correcto = resumen["estado"] == "APROBADO"
        por_estado = {b["estado_codigo"]: b for b in resumen["baterias"]}
        for estado in ["base", "generado", "refactorizado", "defecto", "corregido"]:
            baterias.append(evaluar_bateria(
                leer_json(evidencia / ("pruebas_" + estado + ".json")),
                "laboratorio_03/" + estado, C + B,
                por_estado[estado]["codigo_salida"],
                fallos=["B05", "B06"] if estado == "defecto" else [],
                no_ejecutados=B if estado == "base" else [],
            ))
    elif numero == 5:
        comandos = leer_json(evidencia / "comandos.json")["registros"]
        codigos = {comando["id"]: comando["codigo_salida"] for comando in comandos}
        ids_comandos = {estado + "_" + grupo
                       for estado in ["base", "propuesta", "solucion"]
                       for grupo in ["heredados", "resumen"]}
        estados_baterias = {(b["estado_codigo"], b["bateria"])
                           for b in resumen["baterias"]}
        correcto = (
            resumen["estado"] == "APROBADO"
            and resumen["conservacion_heredados"] == "APROBADO"
            and resumen["base_sin_incremento"] == "APROBADO"
            and len(comandos) == 6 and set(codigos) == ids_comandos
            and len(resumen["baterias"]) == 6
            and estados_baterias == {(estado, grupo)
                                     for estado in ["base", "propuesta", "solucion"]
                                     for grupo in ["heredados", "resumen"]}
            and resumen["totales"] == {
                "ejecutados": 72, "aprobados": 70, "fallidos": 2,
                "no_ejecutados": 6, "errores_de_ejecucion": 0,
            }
        )
        for estado in ["base", "propuesta", "solucion"]:
            for grupo, ids in [("heredados", C + B + N), ("resumen", P)]:
                nombre = estado + "_" + grupo
                baterias.append(evaluar_bateria(
                    leer_json(evidencia / (nombre + ".json")),
                    "laboratorio_05/" + nombre, ids, codigos[nombre],
                    fallos=["P04", "P05"]
                    if grupo == "resumen" and estado == "propuesta" else [],
                    no_ejecutados=P
                    if grupo == "resumen" and estado == "base" else [],
                ))
    else:
        raise ValueError("Laboratorio sin contrato de verificación")
    return correcto and all(b["evaluacion_del_recorrido"] == "APROBADO" for b in baterias), baterias


def huellas_laboratorio_web(carpeta):
    """Excluye dependencias y salidas del lector, que no forman parte del paquete."""
    resultado = {}
    for directorio, subdirectorios, archivos in os.walk(carpeta):
        subdirectorios[:] = sorted(n for n in subdirectorios
                                   if n not in {".git", "node_modules", "__pycache__", "trabajo"})
        if any((Path(directorio) / nombre).is_symlink() for nombre in subdirectorios):
            raise ErrorPreparacion("No se admiten enlaces simbólicos en las referencias.")
        for nombre in sorted(archivos):
            archivo = Path(directorio) / nombre
            if archivo.is_symlink():
                raise ErrorPreparacion("No se admiten enlaces simbólicos en las referencias.")
            if archivo.suffix not in {".pyc", ".pyo"}:
                resultado[archivo.relative_to(carpeta).as_posix()] = hashlib.sha256(
                    archivo.read_bytes()).hexdigest()
    return resultado


def evaluar_laboratorio_web(evidencia, navegador, numero=6):
    resumen = leer_json(evidencia / "resumen.json")
    comandos = leer_json(evidencia / "comandos.json")["registros"]
    codigos = {comando["id"]: comando["codigo_salida"] for comando in comandos}
    grupos = {"heredados": C + B + N, "resumen": P,
              "http": W_HTTP, "navegador": W_NAVEGADOR}
    if numero in {7, 8}:
        grupos["integracion"] = I
    if numero == 8:
        grupos["depuracion"] = D
        grupos["depuracion_navegador"] = D_NAVEGADOR
    estados = ["base", "propuesta", "solucion"]
    ids_comandos = {estado + "_" + grupo for estado in estados for grupo in grupos}
    pares = {(estado, grupo) for estado in estados for grupo in grupos}
    estructura = (len(comandos) == len(ids_comandos) and set(codigos) == ids_comandos
                  and len(resumen["baterias"]) == len(ids_comandos)
                  and {(b["estado_codigo"], b["bateria"])
                       for b in resumen["baterias"]} == pares
                  and resumen["conservacion_heredados"] == "APROBADO"
                  and resumen[{6: "base_sin_incremento_web",
                               7: "base_sin_incremento_integracion",
                               8: "base_sin_incremento_depuracion"}[numero]] == "APROBADO"
                  and resumen["navegador_solicitado"] == navegador)
    baterias = []
    declaradas = {(b["estado_codigo"], b["bateria"]): b for b in resumen["baterias"]}
    for estado in estados:
        for grupo, ids in grupos.items():
            nombre = estado + "_" + grupo
            sin_incremento = (estado == "base" and (
                (numero == 6 and grupo in {"http", "navegador"})
                or (numero == 7 and grupo == "integracion")
                or (numero == 8 and grupo in {"depuracion", "depuracion_navegador"})))
            no_ejecutados = ids if sin_incremento or (
                grupo in {"navegador", "depuracion_navegador"} and not navegador) else []
            fallos = (["W05"] if numero == 6 and estado == "propuesta"
                      and grupo == "navegador" and navegador else
                      ["I01", "I07"] if numero == 7 and estado == "propuesta"
                      and grupo == "integracion" else
                      ["D03", "D05", "D08.a"] if numero == 8 and estado == "propuesta"
                      and grupo == "depuracion" else
                      ["D04"] if numero == 8 and estado == "propuesta"
                      and grupo == "depuracion_navegador" and navegador else [])
            baterias.append(evaluar_bateria(
                leer_json(evidencia / (nombre + ".json")), "laboratorio_%02d/" % numero + nombre,
                ids, codigos[nombre],
                fallos=fallos, no_ejecutados=no_ejecutados,
                permitir_bloqueo=not no_ejecutados,
                bloqueos_parciales={"D02", "D03", "D05", "D08.a"}
                if numero == 8 and grupo == "depuracion" else (),
            ))
            declarada = declaradas[(estado, grupo)]
            observada = baterias[-1]
            estructura = (estructura and declarada["resultado"] == nombre + ".json"
                          and declarada["patron"]["estado"] == observada["evaluacion_del_recorrido"]
                          and all(declarada[clave] == observada[clave] for clave in
                                  ["ejecutados", "aprobados", "fallidos", "bloqueados",
                                   "no_ejecutados", "errores_de_ejecucion"]))
    fallo = any(b["evaluacion_del_recorrido"] == "FALLIDO" for b in baterias)
    bloqueo = any(b["evaluacion_del_recorrido"] == "BLOQUEADO" for b in baterias)
    esperado = ("FALLIDO" if fallo else "BLOQUEADO" if bloqueo else
                "APROBADO" if navegador else "NO EJECUTADO")
    alcance = "FALLIDO" if fallo else "BLOQUEADO" if bloqueo else "APROBADO"
    totales = {clave: sum(b[clave] or 0 for b in baterias)
               for clave in ["ejecutados", "aprobados", "fallidos", "bloqueados",
                              "no_ejecutados", "errores_de_ejecucion"]}
    correcto = (estructura and resumen["estado"] == esperado
                and resumen["extremo_a_extremo"] == esperado
                and resumen["alcance_ejecutado"] == alcance
                and resumen["totales"] == totales)
    return correcto, baterias, esperado


def verificar(salida, raiz=RAIZ, navegador=False, node="node"):
    raiz, salida = Path(raiz).resolve(), Path(salida).resolve()
    if salida.exists():
        raise ErrorPreparacion("La carpeta de salida ya existe; elige otra.")
    if ".git" in salida.parts:
        raise ErrorPreparacion("La salida no puede quedar dentro de metadatos Git.")
    if not shutil.which("git"):
        raise ErrorPreparacion("Git no está disponible en PATH.")
    if salida.is_relative_to(raiz / "laboratorios") or salida.is_relative_to(raiz / "historiales"):
        raise ErrorPreparacion("La evidencia nueva debe quedar fuera de las referencias distribuidas.")
    salida.mkdir(parents=True, exist_ok=False)
    version_git = subprocess.run(["git", "--version"], capture_output=True,
                                  text=True, encoding="utf-8", errors="replace", check=False)
    guardar_json(salida / "entorno.json", {
        "fecha_hora_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sistema": platform.system(), "python": platform.python_version(),
        "implementacion_python": platform.python_implementation(),
        "sqlite": sqlite3.sqlite_version, "git": version_git.stdout.strip(),
        "dependencias": "Python estándar y Git; Node, Playwright y Chromium si se solicita navegador",
        "red": "Solo HTTP de las aplicaciones locales de los laboratorios 6 a 8",
        "navegador_solicitado": navegador,
        "modalidad": "Comprobaciones locales ejecutadas en copias temporales",
    })

    resultados, baterias = [], []
    with tempfile.TemporaryDirectory(prefix="verificacion_laboratorios_") as carpeta_temporal:
        temporal = Path(carpeta_temporal)
        for numero in [1, 2, 3]:
            nombre = "laboratorio_%02d" % numero
            fuente, copia = raiz / "laboratorios" / nombre, temporal / nombre
            evidencia = salida / nombre
            try:
                anteriores = huellas_archivos(fuente)
                if not anteriores or not (fuente / "verificar.py").is_file():
                    raise ErrorPreparacion("Faltan materiales de " + nombre + ".")
                shutil.copytree(fuente, copia)
                codigo = ejecutar(["verificar.py", "--salida", str(evidencia)], copia,
                                   raiz, salida, temporal, salida / (nombre + ".txt"))
                correcto, casos = evaluar_laboratorio(numero, evidencia)
                baterias.extend(casos)
                conservado = anteriores == huellas_archivos(fuente)
                resultados.append({
                    "laboratorio": nombre,
                    "estado": "APROBADO" if codigo == 0 and correcto and conservado else "FALLIDO",
                    "comando_en_copia": "python verificar.py --salida SALIDA/" + nombre,
                    "codigo_salida_verificador": codigo,
                    "referencia_original_conservada": conservado,
                    "evidencia": nombre + "/resumen.json",
                })
            except (OSError, ValueError, KeyError, TypeError, ErrorPreparacion) as error:
                estado = error.estado if isinstance(error, ErrorPreparacion) else "FALLIDO"
                resultados.append({"laboratorio": nombre, "estado": estado,
                                   "motivo": "No se completó o no se pudo validar el registro del recorrido.",
                                   "tipo_error": type(error).__name__})

        nombre = "laboratorio_04"
        try:
            fuente = raiz / "laboratorios" / nombre
            anteriores = huellas_archivos(fuente)
            copia = temporal / nombre
            preparacion = preparar(copia, raiz)
            guardar_json(salida / "preparacion_laboratorio_04.json", preparacion)
            evidencia = salida / nombre
            codigo = ejecutar(["verificar.py", "--salida", str(evidencia)], copia,
                               raiz, salida, temporal, salida / (nombre + ".txt"))
            resumen = leer_json(evidencia / "resumen.json")
            correcto = (codigo == 0 and resumen["estado"] == "APROBADO"
                        and resumen["referencias"] == REFERENCIAS
                        and resumen["arbol_actual_limpio"] is True)
            for referencia, ids in [("inicio", C + B), ("solucion", C + B + N)]:
                info = next(b for b in resumen["baterias"] if b["referencia"] == referencia)
                baterias.append(evaluar_bateria(
                    leer_json(evidencia / ("pruebas_" + referencia + ".json")),
                    nombre + "/" + referencia, ids, info["codigo_salida"],
                ))
            archivo_actual = evidencia / "pruebas_arbol_actual.json"
            codigo_actual = ejecutar(["pruebas.py", "--json", str(archivo_actual)],
                                      copia / "repositorio", raiz, salida, temporal,
                                      evidencia / "pruebas_arbol_actual.txt")
            bateria_actual = evaluar_bateria(leer_json(archivo_actual), nombre + "/arbol_actual",
                                              C + B + N, codigo_actual)
            baterias.append(bateria_actual)
            conservado = anteriores == huellas_archivos(fuente)
            correcto = correcto and conservado and all(
                b["evaluacion_del_recorrido"] == "APROBADO" for b in baterias
                if b["bateria"].startswith(nombre + "/"))
            resultados.append({
                "laboratorio": nombre, "estado": "APROBADO" if correcto else "FALLIDO",
                "comandos_en_copia": ["python verificar.py --salida SALIDA/laboratorio_04",
                                       "python pruebas.py --json SALIDA/laboratorio_04/pruebas_arbol_actual.json (desde repositorio/)"],
                "codigo_salida_verificador": codigo,
                "codigo_salida_arbol_actual": codigo_actual,
                "referencia_original_conservada": conservado,
                "evidencia": nombre + "/resumen.json",
                "criterios_ausentes_en_inicio": N,
                "estado_de_criterios_ausentes_en_inicio": "NO EJECUTADO",
            })
        except (OSError, ValueError, KeyError, TypeError, StopIteration, ErrorPreparacion) as error:
            estado = error.estado if isinstance(error, ErrorPreparacion) else "FALLIDO"
            resultados.append({"laboratorio": nombre, "estado": estado,
                               "motivo": "No se completó o no se pudo validar la reconstrucción o sus pruebas.",
                               "tipo_error": type(error).__name__})

        nombre = "laboratorio_05"
        fuente, copia = raiz / "laboratorios" / nombre, temporal / nombre
        evidencia = salida / nombre
        try:
            anteriores = huellas_archivos(fuente)
            if not anteriores or not (fuente / "verificar.py").is_file():
                raise ErrorPreparacion("Faltan materiales de " + nombre + ".")
            shutil.copytree(fuente, copia)
            codigo = ejecutar(["verificar.py", "--salida", str(evidencia)], copia,
                               raiz, salida, temporal, salida / (nombre + ".txt"))
            correcto, casos = evaluar_laboratorio(5, evidencia)
            baterias.extend(casos)
            conservado = anteriores == huellas_archivos(fuente)
            resultados.append({
                "laboratorio": nombre,
                "estado": "APROBADO" if codigo == 0 and correcto and conservado else "FALLIDO",
                "comando_en_copia": "python verificar.py --salida SALIDA/" + nombre,
                "codigo_salida_verificador": codigo,
                "referencia_original_conservada": conservado,
                "evidencia": nombre + "/resumen.json",
            })
        except (OSError, ValueError, KeyError, TypeError, ErrorPreparacion) as error:
            estado = error.estado if isinstance(error, ErrorPreparacion) else "FALLIDO"
            resultados.append({"laboratorio": nombre, "estado": estado,
                               "motivo": "No se completó o no se pudo validar el registro del recorrido.",
                               "tipo_error": type(error).__name__})

        for numero in [6, 7, 8]:
            nombre = "laboratorio_%02d" % numero
            fuente, copia = raiz / "laboratorios" / nombre, temporal / nombre
            evidencia = salida / nombre
            try:
                anteriores = huellas_laboratorio_web(fuente)
                if not anteriores or not (fuente / "verificar.py").is_file():
                    raise ErrorPreparacion("Faltan materiales de " + nombre + ".")
                shutil.copytree(fuente, copia, ignore=shutil.ignore_patterns(
                    "node_modules", "__pycache__", "trabajo", "*.pyc", "*.pyo"))
                argumentos = ["verificar.py", "--salida", str(evidencia)]
                if navegador:
                    argumentos += ["--navegador", "--node", node]
                # La copia temporal no duplica dependencias. Se usa la instalación del
                # laboratorio original y, en segundo lugar, el NODE_PATH ya configurado.
                rutas_node = [str(fuente / "node_modules"),
                              str(raiz / "laboratorios" / "laboratorio_06" / "node_modules"),
                              str(raiz / "laboratorios" / "laboratorio_07" / "node_modules"),
                              str(raiz / "laboratorios" / "laboratorio_08" / "node_modules")]
                if os.environ.get("NODE_PATH"):
                    rutas_node.append(os.environ["NODE_PATH"])
                codigo = ejecutar(argumentos, copia, raiz, salida, temporal,
                                   salida / (nombre + ".txt"),
                                   {"NODE_PATH": os.pathsep.join(rutas_node)})
                correcto, casos, estado = evaluar_laboratorio_web(evidencia, navegador, numero)
                baterias.extend(casos)
                conservado = anteriores == huellas_laboratorio_web(fuente)
                codigo_esperado = {"APROBADO": 0, "NO EJECUTADO": 0,
                                   "FALLIDO": 1, "BLOQUEADO": 2}[estado]
                valido = correcto and conservado and codigo == codigo_esperado
                resultados.append({
                    "laboratorio": nombre, "estado": estado if valido else "FALLIDO",
                    "alcance_ejecutado": ("APROBADO" if estado == "NO EJECUTADO" else estado)
                    if valido else "FALLIDO",
                    "comando_en_copia": "python verificar.py --salida SALIDA/" + nombre
                    + (" --navegador --node node" if navegador else ""),
                    "codigo_salida_verificador": codigo,
                    "referencia_original_conservada": conservado,
                    "evidencia": nombre + "/resumen.json",
                    "navegador_solicitado": navegador,
                    "dependencias": "No se copian node_modules; se resuelven en el original o NODE_PATH.",
                })
            except (OSError, ValueError, KeyError, TypeError, ErrorPreparacion) as error:
                estado = error.estado if isinstance(error, ErrorPreparacion) else "FALLIDO"
                resultados.append({"laboratorio": nombre, "estado": estado,
                                   "motivo": "No se completó o no se pudo validar el recorrido web.",
                                   "tipo_error": type(error).__name__})

        # Validar captura, sanear sin conversión de saltos y calcular las huellas
        # de los bytes finales. Sólo se procesa esta carpeta de ejecución nueva.
        try:
            huellas_salidas = cerrar_evidencia(
                salida, lambda texto: sanear(texto, raiz, salida, temporal))
        except ErrorHuellas as error:
            raise ErrorPreparacion(str(error), estado="FALLIDO") from error

    estado_final = ("FALLIDO" if any(r["estado"] == "FALLIDO" for r in resultados)
                    else "BLOQUEADO" if any(r["estado"] == "BLOQUEADO" for r in resultados)
                    else "NO EJECUTADO" if any(r["estado"] == "NO EJECUTADO" for r in resultados)
                    else "APROBADO")
    resumen_general = {
        "estado": estado_final,
        "fecha_hora_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "objeto": "Integración local de los ocho laboratorios distribuidos",
        "alcance_ejecutado": "APROBADO" if estado_final == "NO EJECUTADO" else estado_final,
        "extremo_a_extremo_laboratorio_06": next(
            (r["estado"] for r in resultados if r["laboratorio"] == "laboratorio_06"), "NO EJECUTADO"),
        "extremo_a_extremo_laboratorio_07": next(
            (r["estado"] for r in resultados if r["laboratorio"] == "laboratorio_07"), "NO EJECUTADO"),
        "extremo_a_extremo_laboratorio_08": next(
            (r["estado"] for r in resultados if r["laboratorio"] == "laboratorio_08"), "NO EJECUTADO"),
        "criterio": "Patrones exactos de resultados, reconstrucción Git y conservación de referencias.",
        "laboratorios": resultados, "baterias": baterias,
        "totales": {
            "laboratorios": len(resultados), "baterias": len(baterias),
            "ejecutados": sum((b.get("ejecutados") or 0) for b in baterias),
            "aprobados": sum(b["aprobados"] for b in baterias),
            "fallidos": sum(b["fallidos"] for b in baterias),
            "bloqueados": sum(b["bloqueados"] for b in baterias),
            "no_ejecutados_en_baterias": sum(b["no_ejecutados"] for b in baterias),
            "no_ejecutados_fuera_de_baterias": sum(
                len(r.get("criterios_ausentes_en_inicio", [])) for r in resultados),
        },
        "fallos_intencionales": {"laboratorio_01/inicial": ["C04"],
                                  "laboratorio_03/defecto": ["B05", "B06"],
                                  "laboratorio_05/propuesta_resumen": ["P04", "P05"],
                                  "laboratorio_06/propuesta_navegador": ["W05"],
                                  "laboratorio_07/propuesta_integracion": ["I01", "I07"],
                                  "laboratorio_08/propuesta_depuracion": ["D03", "D05", "D08.a"],
                                  "laboratorio_08/propuesta_depuracion_navegador": ["D04"]},
        "interpretacion": "Un recorrido APROBADO conserva FALLIDO en sus criterios defectuosos esperados; no tolera otros errores. "
        "Sin --navegador, salida 0 aprueba únicamente el alcance ejecutado y el estado global es NO EJECUTADO.",
        "evidencia_historica": "Conservada en cada laboratorio; estos archivos describen una ejecución nueva.",
        "huellas_salidas": huellas_salidas,
        "herramientas_comerciales": "NO EJECUTADO por este verificador",
        "GitHub_Actions": "NO EJECUTADO por este verificador",
        "limites": ["No revisa semánticamente el manuscrito ni los prompts.",
                    "No valida rendimiento, seguridad integral, producción ni servicios externos.",
                    "No coteja los registros ausentes de la sesión de Codex aportada por el autor.",
                    "El árbol actual del laboratorio 4 es una copia limpia de la referencia distribuida; no se evalúa otra copia de práctica."],
    }
    guardar_json(salida / "resumen.json", resumen_general)
    return resumen_general


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, default=RAIZ / "trabajo" / "verificacion",
                        help="Carpeta nueva; por defecto trabajo/verificacion en este repositorio.")
    parser.add_argument("--navegador", action="store_true",
                        help="Ejecuta Chromium real para W05/W06 y D04; necesario para APROBADO global.")
    parser.add_argument("--node", default="node", help="Ejecutable Node para las pruebas de navegador.")
    opciones = parser.parse_args()
    try:
        registro = verificar(opciones.salida, navegador=opciones.navegador, node=opciones.node)
    except ErrorPreparacion as error:
        print(error.estado + ": " + str(error))
        return 1 if error.estado == "FALLIDO" else 2
    except (OSError, ValueError):
        print("BLOQUEADO: no se pudo crear o completar el registro local.")
        return 2
    print(registro["estado"] + ": verificación conjunta.")
    print("Alcance ejecutado: " + registro["alcance_ejecutado"] + ".")
    print("Extremo a extremo del laboratorio 6: " + registro["extremo_a_extremo_laboratorio_06"] + ".")
    print("Extremo a extremo del laboratorio 7: " + registro["extremo_a_extremo_laboratorio_07"] + ".")
    print("Extremo a extremo del laboratorio 8: " + registro["extremo_a_extremo_laboratorio_08"] + ".")
    print("Huellas de salidas: {estado}; {coincidentes}/{comprobadas} coinciden con los bytes finales."
          .format(**registro["huellas_salidas"]))
    for bateria in registro["baterias"]:
        print("{bateria}: {aprobados} aprobados, {fallidos} fallidos, {no_ejecutados} no ejecutados; recorrido {evaluacion_del_recorrido}.".format(**bateria))
    print("Totales: {baterias} baterías, {ejecutados} ejecuciones, {aprobados} aprobados, "
          "{fallidos} fallidos, {bloqueados} bloqueados, {no_ejecutados_en_baterias} no ejecutados en baterías; "
          "{no_ejecutados_fuera_de_baterias} criterios ausentes registrados aparte."
          .format(**registro["totales"]))
    print("Fallos intencionales admitidos exclusivamente: C04 en inicial del laboratorio 1; "
          "B05 y B06 en defecto del laboratorio 3; P04 y P05 en propuesta del laboratorio 5; "
          "W05 en propuesta del laboratorio 6, únicamente al ejecutar navegador; "
          "I01 e I07 en propuesta del laboratorio 7; "
          "D03, D05 y D08.a en propuesta del laboratorio 8, y D04 únicamente al ejecutar navegador.")
    print("Evidencia nueva guardada en la carpeta indicada; evidencia histórica conservada.")
    return {"APROBADO": 0, "NO EJECUTADO": 0, "FALLIDO": 1, "BLOQUEADO": 2}[registro["estado"]]


if __name__ == "__main__":
    raise SystemExit(main())
