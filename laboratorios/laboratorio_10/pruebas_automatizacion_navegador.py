"""T08: observa la operación nueva mediante HTTP y navegador reales."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from soporte_procesos import BASE, Escenario, BloqueoEntorno, snapshot


def sin_ejecucion(estado, clasificacion, motivo):
    return {"bateria": "automatizacion_navegador", "estado_codigo": estado,
            "casos_registrados": 1, "criterios_distintos": 1, "ejecutados": 0,
            "aprobados": 0, "fallidos": 0, "fallos_de_asercion": 0, "errores_de_ejecucion": 0,
            "bloqueados": int(clasificacion == "BLOQUEADO"),
            "no_ejecutados": int(clasificacion == "NO EJECUTADO"),
            "pruebas": [{"id": "T08", "estado": clasificacion, "detalle": motivo, "tipo_error": None}]}


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
    destino_recibo = a.json.parent / (a.json.stem + "_recibo")
    if destino_recibo.exists():
        p.error("El destino de recibo ya existe; utiliza una salida nueva.")
    if not (codigo / "operar.py").is_file():
        datos = sin_ejecucion(estado, "NO EJECUTADO", "El estado base todavía no implementa el operador.")
        retorno = 0
    else:
        with tempfile.TemporaryDirectory(prefix="lab10_ui_") as temporal:
            trabajo = Path(temporal)
            base = trabajo / "principal.sqlite"
            recibo = trabajo / "recibo"
            e = Escenario(codigo, trabajo)
            rc, _ = e.cli("iniciar", base)
            if rc != 0:
                raise RuntimeError("La inicialización sintética no terminó correctamente.")
            try:
                with e.servidor(base) as (url, log):
                    destino = trabajo / "navegador.json"
                    comando = [a.node, str(BASE / "pruebas_automatizacion_navegador.cjs"),
                        "--url", url, "--json", str(destino), "--codigo", str(codigo),
                        "--base", str(base), "--archivo", str(BASE / "datos/actualizacion_valida.csv"),
                        "--recibo", str(recibo), "--python", sys.executable]
                    r = subprocess.run(comando, cwd=BASE, env=e.entorno,
                                       capture_output=True, timeout=90)
                    retorno = r.returncode
                    datos = json.loads(destino.read_text(encoding="utf-8"))
                    datos["proceso_navegador"] = {
                        "comando": [e.sanear(v).replace(url, "<URL_LOCAL>") for v in comando],
                        "codigo_salida": r.returncode,
                        "stdout": e.sanear(r.stdout.decode("utf-8")),
                        "stderr": e.sanear(r.stderr.decode("utf-8"))}
                datos["estado_persistido_final"] = snapshot(base)
                datos["operaciones_controlador"] = e.operaciones
                if recibo.is_dir():
                    destino_recibo.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copytree(recibo, destino_recibo)
                    datos["recibo_conservado"] = destino_recibo.name
            except (BloqueoEntorno, FileNotFoundError):
                datos = sin_ejecucion(estado, "BLOQUEADO", "No se pudo iniciar el servidor local o Node.")
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
