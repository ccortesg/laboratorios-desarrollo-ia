"""Opera una actualización local mediante dos CLI fijas y un recibo nuevo."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

from persistencia import abrir_base, validar_alias, ErrorBase

CODIGO = Path(__file__).resolve().parent
LABORATORIO = CODIGO.parent.parent
sys.path.insert(0, str(LABORATORIO))
from soporte.huellas_evidencia import cerrar_evidencia, ErrorHuellas

PROTEGIDOS = ("estados", "datos", "contexto", "prompts", "diferencias",
              "soporte", "evidencia", "node_modules")


class ErrorPrecondicion(Exception):
    def __init__(self, codigo, mensaje):
        super().__init__(mensaje)
        self.codigo = codigo


def ahora():
    return datetime.now(timezone.utc).isoformat()


def guardar_json(ruta, datos):
    contenido = (json.dumps(datos, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    with ruta.open("xb") as archivo:
        archivo.write(contenido)


def prevalidar(opciones):
    base = opciones.base.resolve()
    archivo = opciones.archivo.resolve()
    destino_original = opciones.salida
    salida = destino_original.resolve()
    validar_alias(opciones.alias)
    if salida == LABORATORIO or any(
            salida == LABORATORIO / nombre or LABORATORIO / nombre in salida.parents
            for nombre in PROTEGIDOS):
        raise ErrorPrecondicion("SALIDA_PROTEGIDA", "El recibo debe quedar fuera de los componentes del laboratorio.")
    if destino_original.is_symlink() or salida.exists():
        raise ErrorPrecondicion("SALIDA_EXISTENTE", "El destino del recibo ya existe; usa una carpeta nueva.")
    if not archivo.is_file() or archivo == base:
        raise ErrorPrecondicion("ARCHIVO_INVALIDO", "Selecciona un CSV existente distinto de la base.")
    conexion = abrir_base(base)
    conexion.close()
    contenido = archivo.read_bytes()
    return base, archivo, salida, contenido


def operar(opciones):
    base, archivo, salida, contenido = prevalidar(opciones)
    # La reserva exclusiva ocurre antes de iniciar el paso que modifica SQLite.
    salida.mkdir(parents=True, exist_ok=False)
    instantanea = salida / "entrada.csv"
    with instantanea.open("xb") as copia:
        copia.write(contenido)
    fuente = {"archivo": "entrada.csv", "bytes": len(contenido),
              "sha256": hashlib.sha256(contenido).hexdigest()}
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    registros = []

    def sanear(texto):
        reemplazos = ((base, "<BASE>"), (instantanea, "<RECIBO>/entrada.csv"),
                      (archivo, "<CSV_ORIGINAL>"), (salida, "<RECIBO>"),
                      (CODIGO, "<CODIGO>"), (LABORATORIO, "<LABORATORIO>"),
                      (Path.home(), "<USUARIO>"))
        for ruta, alias in reemplazos:
            for forma in (str(ruta).replace("\\", "\\\\"), str(ruta), ruta.as_posix()):
                texto = texto.replace(forma, alias)
        return texto.replace(sys.executable, "python")

    def ejecutar(paso, argumentos, esperado):
        comando = [sys.executable, "-B", str(CODIGO / "persistencia.py"),
                   *map(str, argumentos)]
        registro = {"id": paso, "inicio_utc": ahora(),
                    "comando": [sanear(valor) for valor in comando],
                    "directorio": "<CODIGO>", "codigo_salida": None}
        try:
            proceso = subprocess.run(comando, cwd=CODIGO, env=entorno,
                                     capture_output=True, shell=False, timeout=20)
            stdout, stderr = proceso.stdout, proceso.stderr
            registro["codigo_salida"] = proceso.returncode
        except subprocess.TimeoutExpired as error:
            stdout, stderr = error.stdout or b"", error.stderr or b""
            registro.update(estado="BLOQUEADO", motivo="TIEMPO_AGOTADO")
        except OSError:
            registro.update(estado="BLOQUEADO", motivo="PROCESO_NO_DISPONIBLE", fin_utc=ahora())
            registros.append(registro)
            return registro, None
        for flujo, datos in (("stdout", stdout), ("stderr", stderr)):
            nombre = paso + "." + flujo + ".txt"
            with (salida / nombre).open("xb") as captura:
                captura.write(datos)
            registro[flujo] = nombre
            registro["sha256_" + flujo] = hashlib.sha256(datos).hexdigest()
        registro["fin_utc"] = ahora()
        try:
            datos = json.loads(stdout.decode("utf-8"))
        except (ValueError, UnicodeError):
            datos = None
        if "estado" not in registro:
            correcto = (registro["codigo_salida"] == 0 and isinstance(datos, dict)
                        and datos.get("estado") == esperado)
            registro["estado"] = "APROBADO" if correcto else "FALLIDO"
        registros.append(registro)
        return registro, datos

    importacion, informe = ejecutar("importar", ["importar", "--base", base,
        "--archivo", instantanea, "--alias", opciones.alias], "APLICADO")
    confirmada = importacion["estado"] == "APROBADO"
    # Defecto didáctico: una importación rechazada se ignora y se consulta el estado anterior.
    continuar = confirmada or (importacion["codigo_salida"] == 1
        and isinstance(informe, dict) and informe.get("estado") == "RECHAZADO")
    if continuar:
        consulta, datos_consulta = ejecutar("consultar", ["consultar", "--base", base,
            "--almacen", opciones.almacen, "--nombre", opciones.nombre,
            "--alias", opciones.alias], "CONSULTADO")
    else:
        consulta = {"id": "consultar", "estado": "NO EJECUTADO", "comando": None,
                    "codigo_salida": None, "motivo": "La importación no terminó confirmada."}
        datos_consulta = None
        registros.append(consulta)
    estado = (consulta["estado"] if continuar else importacion["estado"])
    codigo = 0 if estado == "APROBADO" else 2 if estado == "BLOQUEADO" else 1
    resultado = {
        "estado": estado, "codigo_salida": codigo, "fecha_hora_utc": ahora(),
        "entrada": fuente, "base": "archivo:" + opciones.alias,
        "almacen": opciones.almacen, "importacion_confirmada": confirmada,
        "pasos": [{"paso": r["id"], "estado": r["estado"],
                   "codigo_salida": r["codigo_salida"]} for r in registros],
        "resumen": (datos_consulta["resumen"] if consulta["estado"] == "APROBADO" else None),
        "limite": "Cada CLI tiene su propio alcance. Una importación confirmada no se revierte si falla después la consulta. Sin confirmación observada, una interrupción tampoco demuestra que SQLite permaneció sin cambios.",
    }
    guardar_json(salida / "comandos.json", {"registros": registros,
        "convenciones": "Comandos fijos; rutas sustituidas por alias. Las capturas se registraron inicialmente como bytes."})
    try:
        huellas = cerrar_evidencia(salida, sanear)
        guardar_json(salida / "huellas.json", huellas)
        if (huellas["estado"] == "FALLIDO"
                or (huellas["estado"] == "NO EJECUTADO" and estado != "BLOQUEADO")):
            resultado.update(estado="FALLIDO", codigo_salida=1, error="HUELLAS_NO_VERIFICADAS")
    except ErrorHuellas:
        resultado.update(estado="FALLIDO", codigo_salida=1, error="HUELLAS_INVALIDAS")
    guardar_json(salida / "resultado.json", resultado)
    return resultado


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--archivo", type=Path, required=True)
    parser.add_argument("--almacen", required=True)
    parser.add_argument("--salida", type=Path, required=True)
    parser.add_argument("--nombre", default="")
    parser.add_argument("--alias", default="principal")
    opciones = parser.parse_args()
    try:
        resultado = operar(opciones)
    except (ErrorPrecondicion, ErrorBase) as error:
        resultado = {"estado": "RECHAZADO", "codigo_salida": 2,
                     "error": {"codigo": error.codigo, "mensaje": str(error)}}
    except OSError:
        resultado = {"estado": "RECHAZADO", "codigo_salida": 2,
                     "error": {"codigo": "OPERACION_LOCAL_FALLIDA",
                               "mensaje": "No fue posible completar la operación local; conserva y revisa los archivos existentes."}}
    print(json.dumps(resultado, ensure_ascii=False))
    return resultado["codigo_salida"]


if __name__ == "__main__":
    raise SystemExit(main())
