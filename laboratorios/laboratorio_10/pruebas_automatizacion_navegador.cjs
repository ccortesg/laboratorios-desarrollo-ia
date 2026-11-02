"use strict";
/* T08: servidor vivo, operador real en otro proceso y observación en Chromium. */
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");
const { execFileSync } = require("node:child_process");
const args = process.argv.slice(2);
const arg = n => { const i = args.indexOf(n); return i < 0 ? null : args[i + 1]; };
const url = arg("--url"), salida = arg("--json"), codigo = arg("--codigo");
const base = arg("--base"), archivo = arg("--archivo"), recibo = arg("--recibo");
const python = arg("--python");
const registro = {
  id: "T08", entrada: { secuencia: ["servidor vivo", "catálogo inicial", "operador CLI", "catálogo posterior"] },
  esperado: {
    antes: { total: "1", codigos: ["A01"], estado: "exito", http: 200 },
    despues: { total: "2", codigos: ["A01", "A03"], estado: "exito", http: 200 },
    busqueda: { total: "1", codigos: ["A03"], estado: "exito", http: 200 }
  }, observado: {}, estado: "NO EJECUTADO", tipo_error: null, detalle: ""
};
const entorno = { node: process.version, playwright: null, navegador: "Chromium", version_navegador: null };

function guardar() {
  const r = { bateria: "automatizacion_navegador", casos_registrados: 1, criterios_distintos: 1,
    ejecutados: ["APROBADO", "FALLIDO"].includes(registro.estado) ? 1 : 0,
    aprobados: +(registro.estado === "APROBADO"), fallidos: +(registro.estado === "FALLIDO"),
    fallos_de_asercion: +(registro.tipo_error === "AssertionError"),
    errores_de_ejecucion: +(registro.estado === "FALLIDO" && registro.tipo_error !== "AssertionError"),
    bloqueados: +(registro.estado === "BLOQUEADO"), no_ejecutados: +(registro.estado === "NO EJECUTADO"),
    entorno, pruebas: [registro] };
  fs.writeFileSync(salida, JSON.stringify(r, null, 2) + "\n", "utf8");
  console.log("T08: " + registro.estado);
  process.exitCode = r.fallidos ? 1 : r.bloqueados ? 2 : 0;
}

async function consultar(page, nombre) {
  await page.locator("#almacen").selectOption("ALFA");
  await page.locator("#nombre").fill(nombre);
  const [respuesta] = await Promise.all([
    page.waitForResponse(r => new URL(r.url()).pathname === "/api/resumen" && r.request().method() === "GET"),
    page.locator("#consultar").click()
  ]);
  await page.waitForFunction(() => !document.querySelector("#consultar").disabled
    && ["exito", "vacio", "error"].includes(document.querySelector("#mensaje").dataset.estado));
  const visible = { total: await page.locator("#total").innerText(),
    codigos: await page.locator("#codigos li").allTextContents(),
    estado: await page.locator("#mensaje").getAttribute("data-estado"), http: respuesta.status() };
  const contenido = await respuesta.json();
  registro.observado.respuestas_http.push(contenido);
  assert.equal(String(contenido.total), visible.total);
  assert.deepEqual(contenido.codigos, visible.codigos);
  return visible;
}

async function main() {
  if (!url || new URL(url).hostname !== "127.0.0.1") throw new Error("Sólo se admite loopback.");
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
    registro.detalle = "No fue posible iniciar Chromium; revisa dependencias y permisos.";
    guardar(); return;
  }
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
    page.setDefaultTimeout(10000);
    await page.goto(url, { waitUntil: "networkidle" });
    registro.observado.respuestas_http = [];
    registro.observado.antes = await consultar(page, "");
    const texto = execFileSync(python, ["-B", path.join(codigo, "operar.py"),
      "--base", base, "--archivo", archivo, "--almacen", "ALFA", "--salida", recibo], {
      cwd: codigo, env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONDONTWRITEBYTECODE: "1" },
      encoding: "utf8", timeout: 50000
    });
    registro.observado.operador = { codigo_salida: 0, resultado: JSON.parse(texto),
      comando: ["python", "-B", "<CODIGO>/operar.py", "--base", "<BASE>",
        "--archivo", "datos/actualizacion_valida.csv", "--almacen", "ALFA", "--salida", "<RECIBO>"] };
    registro.observado.despues = await consultar(page, "");
    registro.observado.busqueda = await consultar(page, " AGOTADO ");
    registro.observado.mismo_servidor = true;
    for (const clave of Object.keys(registro.esperado)) assert.deepEqual(registro.observado[clave], registro.esperado[clave]);
    assert.equal(registro.observado.operador.resultado.estado, "APROBADO");
    assert.equal(registro.observado.operador.resultado.importacion_confirmada, true);
    assert.deepEqual(registro.observado.operador.resultado.resumen, registro.observado.respuestas_http[1]);
    registro.estado = "APROBADO";
  } catch (error) {
    registro.estado = "FALLIDO";
    registro.tipo_error = error.name === "AssertionError" ? "AssertionError" : error.name;
    registro.detalle = registro.tipo_error === "AssertionError"
      ? "La operación o el catálogo visible no coinciden con el contrato."
      : "Error inesperado al ejecutar el recorrido; no se acepta como defecto didáctico.";
  } finally { await browser.close(); }
  guardar();
}

main().catch(error => {
  registro.estado = "FALLIDO"; registro.tipo_error = error.name;
  registro.detalle = "No se completó la preparación del recorrido real."; guardar();
});
