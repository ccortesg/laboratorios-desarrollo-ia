"""S06: servidor persistente real, navegador y recuperación después de un rechazo."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from soporte_procesos import BASE, Escenario, BloqueoEntorno, snapshot


def sin_ejecucion(estado, clasificacion, motivo, tipo=None):
    return {"bateria": "seguridad_navegador", "estado_codigo": estado,
        "casos_registrados": 1, "criterios_distintos": 1,
        "ejecutados": int(clasificacion == "FALLIDO"), "aprobados": 0,
        "fallidos": int(clasificacion == "FALLIDO"), "fallos_de_asercion": 0,
        "errores_de_ejecucion": int(clasificacion == "FALLIDO"),
        "bloqueados": int(clasificacion == "BLOQUEADO"),
        "no_ejecutados": int(clasificacion == "NO EJECUTADO"),
        "pruebas": [{"id": "S06", "estado": clasificacion, "detalle": motivo,
                     "tipo_error": tipo}]}


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
    with tempfile.TemporaryDirectory(prefix="lab09_ui_") as temporal:
        trabajo = Path(temporal)
        base = trabajo / "principal.sqlite"
        e = Escenario(codigo, trabajo)
        try:
            rc, _ = e.cli("iniciar", base)
            if rc:
                raise RuntimeError("No se pudo inicializar la base aislada.")
            rc, informe = e.cli("importar", base, "--archivo", BASE / "datos/actualizacion_valida.csv")
            if rc or informe.get("estado") != "APLICADO":
                raise RuntimeError("No se completó la importación del escenario.")
            antes = snapshot(base)
            with e.servidor(base) as (url, _):
                destino = trabajo / "navegador.json"
                comando = [a.node, str(BASE / "pruebas_seguridad_navegador.cjs"),
                           "--url", url, "--json", str(destino)]
                r = subprocess.run(comando, cwd=BASE, env=e.entorno,
                                   capture_output=True, timeout=70)
                retorno = r.returncode
                datos = json.loads(destino.read_text(encoding="utf-8"))
                datos["proceso_navegador"] = {
                    "comando": [e.sanear(v).replace(url, "<URL_LOCAL>") for v in comando],
                    "codigo_salida": r.returncode,
                    "stdout": e.sanear(r.stdout.decode("utf-8")),
                    "stderr": e.sanear(r.stderr.decode("utf-8"))}
            datos["base_sin_modificaciones"] = antes == snapshot(base)
            if not datos["base_sin_modificaciones"]:
                datos = sin_ejecucion(estado, "FALLIDO", "El recorrido alteró la base.", "EstadoModificado")
                retorno = 1
        except (BloqueoEntorno, FileNotFoundError) as error:
            datos = sin_ejecucion(estado, "BLOQUEADO", "No pudo iniciarse el servidor o Node.", type(error).__name__)
            retorno = 2
        except Exception as error:
            datos = sin_ejecucion(estado, "FALLIDO", "Error inesperado en el controlador de navegador.", type(error).__name__)
            retorno = 1
        datos["operaciones_controlador"] = e.operaciones
        datos["estado_codigo"] = estado
    a.json.parent.mkdir(parents=True, exist_ok=True)
    a.json.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for caso in datos["pruebas"]:
        print(caso["id"] + ": " + caso["estado"])
    return retorno


if __name__ == "__main__":
    raise SystemExit(main())
