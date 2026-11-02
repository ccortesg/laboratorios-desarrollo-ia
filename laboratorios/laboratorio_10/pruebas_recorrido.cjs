"use strict";
/* D04: mismo servidor vivo, importación real por otro proceso y observación en Chromium. */
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");
const { execFileSync } = require("node:child_process");
const args = process.argv.slice(2);
const arg = (n) => { const i = args.indexOf(n); return i < 0 ? null : args[i + 1]; };
const url = arg("--url");
const salida = arg("--json");
const codigo = arg("--codigo");
const base = arg("--base");
const archivo = arg("--archivo");
const python = arg("--python");
const registro = {
  id: "D04", entrada: { archivo: "datos/actualizacion_valida.csv", base: "principal",
    secuencia: ["servidor vivo", "consulta inicial", "importacion CLI", "consulta posterior"] },
  esperado: {
    antes: { almacen: "ALFA", total: "1", codigos: ["A01"], estado: "exito" },
    despues: { almacen: "ALFA", total: "2", codigos: ["A01", "A03"], estado: "exito" },
    beta: { almacen: "BETA", total: "0", codigos: [], estado: "vacio" },
    busqueda: { almacen: "ALFA", total: "1", codigos: ["A03"], estado: "exito" }
  },
  observado: {}, estado: "NO EJECUTADO", tipo_error: null, detalle: ""
};
const entorno = { node: process.version, playwright: null, navegador: "Chromium", version_navegador: null };
function guardar() {
  const r = { bateria: "depuracion_navegador", casos_registrados: 1, criterios_distintos: 1,
    ejecutados: ["APROBADO", "FALLIDO"].includes(registro.estado) ? 1 : 0,
    aprobados: registro.estado === "APROBADO" ? 1 : 0,
    fallidos: registro.estado === "FALLIDO" ? 1 : 0,
    fallos_de_asercion: registro.tipo_error === "AssertionError" ? 1 : 0,
    errores_de_ejecucion: registro.estado === "FALLIDO" && registro.tipo_error !== "AssertionError" ? 1 : 0,
    bloqueados: registro.estado === "BLOQUEADO" ? 1 : 0,
    no_ejecutados: registro.estado === "NO EJECUTADO" ? 1 : 0,
    entorno, pruebas: [registro] };
  fs.writeFileSync(salida, JSON.stringify(r, null, 2) + "\n", "utf8");
  console.log("D04: " + registro.estado);
  process.exitCode = r.fallidos ? 1 : r.bloqueados ? 2 : 0;
}
async function consultar(page, almacen, nombre) {
  await page.locator("#almacen").selectOption(almacen);
  await page.locator("#nombre").fill(nombre);
  await page.locator("#consultar").click();
  await page.waitForFunction(() => !document.querySelector("#consultar").disabled
    && ["exito", "vacio", "error"].includes(document.querySelector("#mensaje").dataset.estado));
  return {
    almacen: await page.locator("#almacen-resultado").innerText(),
    total: await page.locator("#total").innerText(),
    codigos: await page.locator("#codigos li").allTextContents(),
    estado: await page.locator("#mensaje").getAttribute("data-estado")
  };
}
async function main() {
  if (!url || new URL(url).hostname !== "127.0.0.1") throw new Error("La prueba requiere loopback.");
  let browser;
  try {
    const { chromium } = require("playwright");
    entorno.playwright = require("playwright/package.json").version;
    const opciones = { headless: true };
    if (process.env.LAB06_CHROMIUM) opciones.executablePath = process.env.LAB06_CHROMIUM;
    browser = await chromium.launch(opciones);
    entorno.version_navegador = browser.version();
  } catch (error) {
    registro.estado = "BLOQUEADO";
    registro.tipo_error = error.name;
    registro.detalle = "No fue posible iniciar Chromium; comprueba instalación y permisos.";
    guardar();
    return;
  }
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
    page.setDefaultTimeout(10000);
    await page.goto(url, { waitUntil: "networkidle" });
    registro.observado.antes = await consultar(page, "ALFA", "");
    const cli = execFileSync(python, ["-B", path.join(codigo, "persistencia.py"), "importar",
      "--base", base, "--archivo", archivo], {
      cwd: codigo, env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONDONTWRITEBYTECODE: "1" },
      encoding: "utf8", timeout: 20000
    });
    registro.observado.importacion = {
      proceso: "CLI separado del servidor y del navegador",
      comando: ["python", "-B", "<CODIGO>/persistencia.py", "importar",
        "--base", "<BASE_PERSISTENTE>", "--archivo", "datos/actualizacion_valida.csv"],
      codigo_salida: 0, informe: JSON.parse(cli)
    };
    registro.observado.despues = await consultar(page, "ALFA", "");
    registro.observado.beta = await consultar(page, "BETA", "");
    registro.observado.busqueda = await consultar(page, "ALFA", " AGOTADO ");
    registro.observado.mismo_servidor = true;
    for (const key of Object.keys(registro.esperado)) assert.deepEqual(registro.observado[key], registro.esperado[key]);
    assert.equal(registro.observado.importacion.informe.estado, "APLICADO");
    assert.equal(registro.observado.importacion.informe.filas_aplicadas, 4);
    registro.estado = "APROBADO";
  } catch (error) {
    registro.estado = "FALLIDO";
    registro.tipo_error = error.name === "AssertionError" ? "AssertionError" : error.name;
    registro.detalle = registro.tipo_error === "AssertionError"
      ? "La pantalla observada no coincide con la expectativa del recorrido persistente."
      : "Error inesperado al ejecutar el recorrido real; no se atribuye al defecto didáctico.";
  } finally {
    await browser.close();
  }
  guardar();
}
main().catch(error => {
  registro.estado = "FALLIDO"; registro.tipo_error = error.name;
  registro.detalle = "Error al preparar el recorrido; no hubo observación válida.";
  guardar();
});
