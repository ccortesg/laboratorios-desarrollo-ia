"""Adaptador CSV local: valida el contrato y aplica cantidades absolutas."""

import csv
import hashlib
import io
from pathlib import Path
import re
import sqlite3

CABECERA = ["codigo_articulo", "almacen", "existencias"]
MAX_EXISTENCIAS = 2147483647


def error(fila, campo, codigo, mensaje):
    return {"fila": fila, "campo": campo, "codigo": codigo, "mensaje": mensaje}


def leer_csv(contenido):
    """Interpreta bytes UTF-8; no interpreta las reglas de negocio."""
    try:
        texto = contenido.decode("utf-8-sig")
    except UnicodeDecodeError:
        return [], [error(None, "archivo", "CODIFICACION", "Se requiere UTF-8 válido.")]
    lector = csv.reader(io.StringIO(texto, newline=""), delimiter=",", strict=True)
    registros = []
    try:
        cabecera = next(lector, None)
        if cabecera != CABECERA:
            return [], [error(1, "cabecera", "CABECERA", "El encabezado debe coincidir con el contrato.")]
        for campos in lector:
            registros.append((lector.line_num, campos))
    except csv.Error:
        return registros, [error(lector.line_num, "archivo", "SINTAXIS_CSV", "CSV no interpretable.")]
    if not registros:
        return [], [error(1, "archivo", "SIN_DATOS", "Se requiere al menos una fila de datos.")]
    return registros, []


def validar_filas(conexion, registros):
    """Traduce filas válidas a tuplas internas sin escribir en la base."""
    articulos = {fila[0] for fila in conexion.execute("SELECT codigo FROM articulos")}
    almacenes = {fila[0] for fila in conexion.execute("SELECT codigo FROM almacenes")}
    validas, errores, vistos = [], [], set()
    for numero, campos in registros:
        anteriores = len(errores)
        if len(campos) != 3:
            errores.append(error(numero, "fila", "COLUMNAS", "Se requieren exactamente tres campos."))
            continue
        articulo, almacen, cantidad = campos
        if articulo not in articulos:
            errores.append(error(numero, "codigo_articulo", "ARTICULO_DESCONOCIDO", "El código exacto no existe."))
        if almacen not in almacenes:
            errores.append(error(numero, "almacen", "ALMACEN_DESCONOCIDO", "El almacén exacto no existe."))
        if not re.fullmatch(r"[0-9]+", cantidad) or len(cantidad.lstrip("0")) > 10:
            errores.append(error(numero, "existencias", "CANTIDAD_INVALIDA", "Se requiere un entero entre 0 y 2147483647."))
            numero_cantidad = None
        else:
            numero_cantidad = int(cantidad.lstrip("0") or "0")
            if numero_cantidad > MAX_EXISTENCIAS:
                errores.append(error(numero, "existencias", "CANTIDAD_INVALIDA", "Se requiere un entero entre 0 y 2147483647."))
        par = (articulo, almacen)
        if par in vistos:
            errores.append(error(numero, "fila", "PAR_DUPLICADO", "El par artículo–almacén está repetido."))
        vistos.add(par)
        if len(errores) == anteriores:
            validas.append((articulo, almacen, numero_cantidad))
    return validas, errores


def aplicar_filas(conexion, filas):
    """Confirma todos los cambios o revierte si falla una escritura."""
    cambios = 0
    with conexion:
        conexion.execute("BEGIN")
        for articulo, almacen, cantidad in filas:
            previo = conexion.execute(
                "SELECT cantidad FROM existencias WHERE articulo = ? AND almacen = ?",
                (articulo, almacen)).fetchone()
            cantidad_final = cantidad
            if previo is None or previo[0] != cantidad_final:
                cambios += 1
            conexion.execute(
                "INSERT INTO existencias (articulo, almacen, cantidad) VALUES (?, ?, ?) "
                "ON CONFLICT (articulo, almacen) DO UPDATE SET cantidad = excluded.cantidad",
                (articulo, almacen, cantidad_final))
    return cambios


def importar_existencias(conexion, archivo):
    """El llamador conserva su conexión; el informe no contiene rutas privadas."""
    informe = {"estado": "RECHAZADO", "sha256_fuente": None,
               "filas_leidas": 0, "filas_validadas": 0,
               "filas_aplicadas": 0, "filas_sin_cambio": 0, "errores": []}
    if conexion.in_transaction:
        informe["errores"] = [error(None, "conexion", "TRANSACCION_PREVIA", "Confirma los cambios previos antes de importar.")]
        return informe
    try:
        contenido = Path(archivo).read_bytes()
    except OSError:
        informe["errores"] = [error(None, "archivo", "LECTURA", "No fue posible leer el archivo de entrada.")]
        return informe
    informe["sha256_fuente"] = hashlib.sha256(contenido).hexdigest()
    registros, errores_lectura = leer_csv(contenido)
    filas, errores_validacion = validar_filas(conexion, registros)
    informe.update(filas_leidas=len(registros), filas_validadas=len(filas),
                   errores=errores_lectura + errores_validacion)
    if informe["errores"]:
        return informe
    try:
        cambios = aplicar_filas(conexion, filas)
    except sqlite3.Error:
        informe["errores"] = [error(None, "base", "ESCRITURA", "No se aplicó el archivo; la transacción se revirtió.")]
        return informe
    informe.update(estado="APLICADO", filas_aplicadas=cambios,
                   filas_sin_cambio=len(filas) - cambios)
    return informe
