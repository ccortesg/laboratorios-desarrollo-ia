"""D04: controla base aislada y servidor como proceso; Chromium importa desde otra CLI."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from soporte_procesos import BASE, Escenario, BloqueoEntorno, snapshot


def sin_ejecucion(estado, clasificacion, motivo):
    return {"bateria": "depuracion_navegador", "estado_codigo": estado,
            "casos_registrados": 1, "criterios_distintos": 1, "ejecutados": 0,
            "aprobados": 0, "fallidos": 0, "fallos_de_asercion": 0, "errores_de_ejecucion": 0,
            "bloqueados": int(clasificacion == "BLOQUEADO"),
            "no_ejecutados": int(clasificacion == "NO EJECUTADO"),
            "pruebas": [{"id": "D04", "estado": clasificacion, "detalle": motivo,
                        "tipo_error": None}]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    selector = p.add_mutually_exclusive_group(required=True)
    selector.add_argument("--estado", choices=("base", "propuesta", "solucion"))
    selector.add_argument("--directorio", type=Path)
    p.add_argument("--node", default="node")
    p.add_argument("--json", type=Path, required=True)
    a = p.parse_args()
    estado = a.estado or "copia_del_lector"
    codigo = (BASE / "estados" / a.estado if a.estado else a.directorio).resolve()
    if not (codigo / "persistencia.py").is_file():
        datos = sin_ejecucion(estado, "NO EJECUTADO", "La base todavía no implementa persistencia.")
        retorno = 0
    else:
        with tempfile.TemporaryDirectory(prefix="lab08_ui_") as temporal:
            trabajo = Path(temporal)
            base = trabajo / "principal.sqlite"
            e = Escenario(codigo, trabajo)
            rc, inicializacion = e.cli("iniciar", base)
            if rc != 0:
                raise RuntimeError("La inicialización del escenario no terminó correctamente.")
            try:
                with e.servidor(base) as (url, log):
                    destino = trabajo / "navegador.json"
                    comando = [a.node, str(BASE / "pruebas_recorrido.cjs"),
                        "--url", url, "--json", str(destino), "--codigo", str(codigo),
                        "--base", str(base), "--archivo", str(BASE / "datos/actualizacion_valida.csv"),
                        "--python", sys.executable]
                    r = subprocess.run(comando, cwd=BASE, env=e.entorno,
                                       capture_output=True, timeout=70)
                    retorno = r.returncode
                    datos = json.loads(destino.read_text(encoding="utf-8"))
                    datos["proceso_navegador"] = {
                        "comando": [e.sanear(v).replace(url, "<URL_LOCAL>") for v in comando],
                        "codigo_salida": r.returncode,
                        "stdout": e.sanear(r.stdout.decode("utf-8")),
                        "stderr": e.sanear(r.stderr.decode("utf-8"))}
                datos["estado_persistido_final"] = snapshot(base)
                datos["operaciones_controlador"] = e.operaciones
            except (BloqueoEntorno, FileNotFoundError) as error:
                datos = sin_ejecucion(estado, "BLOQUEADO",
                    "No fue posible iniciar el servidor local o el ejecutable Node.")
                datos["operaciones_controlador"] = e.operaciones
                retorno = 2
            datos["estado_codigo"] = estado
    a.json.parent.mkdir(parents=True, exist_ok=True)
    a.json.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for caso in datos["pruebas"]:
        print(caso["id"] + ": " + caso["estado"])
    return retorno


if __name__ == "__main__":
    raise SystemExit(main())
