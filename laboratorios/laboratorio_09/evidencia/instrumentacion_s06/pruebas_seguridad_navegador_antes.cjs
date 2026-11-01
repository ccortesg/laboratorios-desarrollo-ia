"use strict";
/* S06: rechazo HTTP real, estado visible y recuperación sobre el mismo servidor. */
const fs = require("node:fs");
const assert = require("node:assert/strict");
const args = process.argv.slice(2);
const arg = (n) => { const i = args.indexOf(n); return i < 0 ? null : args[i + 1]; };
const url = arg("--url");
const salida = arg("--json");
const registro = {
  id: "S06", entrada: { almacen: "ALFA", nombre_largo_puntos_codigo: 81,
    secuencia: ["consulta válida", "consulta demasiado larga", "consulta válida"] },
  esperado: { antes: { http: 200, estado: "exito", codigos: ["A01", "A03"] },
    rechazo: { http: 400, codigo: "NOMBRE_DEMASIADO_LARGO", estado: "error",
      resultado_oculto: true, error_visible: true, codigos: [], controles_habilitados: true },
    despues: { http: 200, estado: "exito", codigos: ["A03"], error_visible: false } },
  observado: {}, estado: "NO EJECUTADO", tipo_error: null, detalle: ""
};
const entorno = { node: process.version, playwright: null, navegador: "Chromium", version_navegador: null };
function guardar() {
  const datos = { bateria: "seguridad_navegador", casos_registrados: 1, criterios_distintos: 1,
    ejecutados: ["APROBADO", "FALLIDO"].includes(registro.estado) ? 1 : 0,
    aprobados: registro.estado === "APROBADO" ? 1 : 0,
    fallidos: registro.estado === "FALLIDO" ? 1 : 0,
    fallos_de_asercion: registro.tipo_error === "AssertionError" ? 1 : 0,
    errores_de_ejecucion: registro.estado === "FALLIDO" && registro.tipo_error !== "AssertionError" ? 1 : 0,
    bloqueados: registro.estado === "BLOQUEADO" ? 1 : 0,
    no_ejecutados: registro.estado === "NO EJECUTADO" ? 1 : 0,
    entorno, pruebas: [registro] };
  fs.writeFileSync(salida, JSON.stringify(datos, null, 2) + "\n", "utf8");
  console.log("S06: " + registro.estado);
  process.exitCode = datos.fallidos ? 1 : datos.bloqueados ? 2 : 0;
}
async function consultar(page, nombre) {
  await page.locator("#almacen").selectOption("ALFA");
  await page.locator("#nombre").fill(nombre);
  const [respuesta] = await Promise.all([
    page.waitForResponse(r => new URL(r.url()).pathname === "/api/resumen"),
    page.locator("#consultar").click()
  ]);
  await page.waitForFunction(() => !document.querySelector("#consultar").disabled
    && ["exito", "vacio", "error"].includes(document.querySelector("#mensaje").dataset.estado));
  return {
    http: respuesta.status(), json: await respuesta.json(),
    estado: await page.locator("#mensaje").getAttribute("data-estado"),
    codigos: await page.locator("#codigos li").allTextContents(),
    resultado_oculto: await page.locator("#resultado").isHidden(),
    error_visible: await page.locator("#error").isVisible(),
    mensaje_error: await page.locator("#error").textContent(),
    controles_habilitados: (await page.locator("#consultar").isEnabled())
      && (await page.locator("#almacen").isEnabled()) && (await page.locator("#nombre").isEnabled()),
    ocupado: await page.locator("#panel-resultados").getAttribute("aria-busy")
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
    registro.estado = "BLOQUEADO"; registro.tipo_error = error.name;
    registro.detalle = "No fue posible iniciar Chromium; comprueba instalación y permisos.";
    guardar(); return;
  }
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
    page.setDefaultTimeout(10000);
    await page.goto(url, { waitUntil: "networkidle" });
    registro.observado.antes = await consultar(page, "");
    registro.observado.rechazo = await consultar(page, "x".repeat(81));
    registro.observado.despues = await consultar(page, " AGOTADO ");
    registro.observado.mismo_servidor = true;
    const { antes, rechazo, despues } = registro.observado;
    assert.equal(antes.http, 200); assert.equal(antes.estado, "exito");
    assert.deepEqual(antes.codigos, ["A01", "A03"]);
    assert.equal(rechazo.http, 400);
    assert.equal(rechazo.json.error.codigo, "NOMBRE_DEMASIADO_LARGO");
    assert.equal(rechazo.estado, "error");
    assert.equal(rechazo.resultado_oculto, true); assert.equal(rechazo.error_visible, true);
    assert.deepEqual(rechazo.codigos, []); assert.equal(rechazo.controles_habilitados, true);
    assert.equal(rechazo.ocupado, "false"); assert.ok(rechazo.mensaje_error.length > 0);
    assert.equal(despues.http, 200); assert.equal(despues.estado, "exito");
    assert.deepEqual(despues.codigos, ["A03"]);
    assert.equal(despues.error_visible, false); assert.equal(despues.resultado_oculto, false);
    assert.equal(despues.controles_habilitados, true);
    registro.estado = "APROBADO";
  } catch (error) {
    registro.estado = "FALLIDO";
    registro.tipo_error = error.name === "AssertionError" ? "AssertionError" : error.name;
    registro.detalle = registro.tipo_error === "AssertionError"
      ? "El rechazo o la recuperación observados no coinciden con el contrato."
      : "Error inesperado durante el recorrido; no es el defecto didáctico.";
  } finally { await browser.close(); }
  guardar();
}
main().catch(error => {
  registro.estado = "FALLIDO"; registro.tipo_error = error.name;
  registro.detalle = "Error al preparar el recorrido; no hubo observación válida."; guardar();
});
