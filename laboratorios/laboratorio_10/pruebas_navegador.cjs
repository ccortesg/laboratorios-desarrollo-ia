"use strict";
/* W05-W06: interacción real de Chromium, no un DOM simulado. */

const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");
const argumentos = process.argv.slice(2);
const valor = (nombre) => {
  const i = argumentos.indexOf(nombre);
  return i < 0 ? null : argumentos[i + 1];
};
const url = valor("--url");
const destino = valor("--json");
const estado = valor("--estado") || "solucion";
const captura = valor("--captura");
const CASOS = ["W05", "W06.a", "W06.b"];
let navegadorVersion = null;
let playwrightVersion = null;
const pruebas = [];

function guardar() {
  const registro = {
    bateria: "navegador", estado_codigo: estado,
    casos_registrados: pruebas.length, criterios_distintos: 2,
    ejecutados: pruebas.filter((p) => ["APROBADO", "FALLIDO"].includes(p.estado)).length,
    aprobados: pruebas.filter((p) => p.estado === "APROBADO").length,
    fallidos: pruebas.filter((p) => p.estado === "FALLIDO").length,
    fallos_de_asercion: pruebas.filter((p) => p.tipo_error === "AssertionError").length,
    errores_de_ejecucion: pruebas.filter((p) => p.estado === "FALLIDO" && p.tipo_error !== "AssertionError").length,
    bloqueados: pruebas.filter((p) => p.estado === "BLOQUEADO").length,
    no_ejecutados: 0,
    entorno: { node: process.version, playwright: playwrightVersion, navegador: "Chromium", version_navegador: navegadorVersion },
    pruebas,
    alcance: "Navegador real contra servidor local; W06.b interrumpe la petición con route.abort('failed').",
  };
  if (destino) {
    fs.mkdirSync(path.dirname(destino), { recursive: true });
    fs.writeFileSync(destino, JSON.stringify(registro, null, 2) + "\n", "utf8");
  }
  for (const prueba of pruebas) console.log(`${prueba.id}: ${prueba.estado}`);
  console.log(JSON.stringify({ ejecutados: registro.ejecutados, aprobados: registro.aprobados,
    fallidos: registro.fallidos, bloqueados: registro.bloqueados, no_ejecutados: 0 }));
  process.exitCode = registro.bloqueados ? 2 : (registro.fallidos ? 1 : 0);
}

async function leer(page) {
  return {
    estado: await page.locator("#mensaje").getAttribute("data-estado"),
    almacen: await page.locator("#almacen-resultado").innerText(),
    total: await page.locator("#total").innerText(),
    codigos: await page.locator("#codigos li").allTextContents(),
    resultado_visible: await page.locator("#resultado").isVisible(),
    error_visible: await page.locator("#error").isVisible(),
    mensaje: await page.locator("#mensaje").innerText(),
    error: await page.locator("#error").innerText(),
  };
}

async function consultar(page, almacen, nombre) {
  await page.locator("#almacen").selectOption(almacen);
  await page.locator("#nombre").fill(nombre);
  await page.getByRole("button", { name: "Consultar catálogo" }).click();
  await page.waitForFunction(() => !document.querySelector("#consultar").disabled
    && ["exito", "vacio", "error"].includes(document.querySelector("#mensaje").dataset.estado));
  return leer(page);
}

async function main() {
  if (!url || !["127.0.0.1", "localhost"].includes(new URL(url).hostname)) {
    throw new Error("Se requiere una URL local de la aplicación de laboratorio.");
  }
  let chromium;
  let browser;
  try {
    ({ chromium } = require("playwright"));
    playwrightVersion = require("playwright/package.json").version;
    const opciones = { headless: true };
    if (process.env.LAB06_CHROMIUM) opciones.executablePath = process.env.LAB06_CHROMIUM;
    browser = await chromium.launch(opciones);
    navegadorVersion = browser.version();
  } catch (error) {
    let detalle = "No fue posible iniciar Chromium; revisa instalación y permisos del entorno.";
    if (error.code === "MODULE_NOT_FOUND") detalle = "Playwright no está disponible para este Node.";
    else if (/Executable doesn't exist/.test(error.message)) detalle = "Chromium no está instalado en la ubicación resuelta por Playwright.";
    for (const id of CASOS) pruebas.push({ id, estado: "BLOQUEADO", tipo_error: error.name, detalle });
    guardar();
    return;
  }
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  async function caso(id, entrada, esperado, ejecutar) {
    const page = await context.newPage();
    page.setDefaultTimeout(10000);
    const registro = { id, entrada, esperado, observado: null };
    try {
      await page.goto(url, { waitUntil: "networkidle" });
      await ejecutar(page, registro);
      registro.estado = "APROBADO";
      registro.tipo_error = null;
      registro.detalle = "";
    } catch (error) {
      registro.estado = "FALLIDO";
      registro.tipo_error = error.name === "AssertionError" ? "AssertionError" : error.name;
      registro.detalle = error.name === "AssertionError"
        ? "El comportamiento observado no coincide con la expectativa literal."
        : "Error durante la interacción del navegador; consulta la observación del caso.";
    } finally {
      pruebas.push(registro);
      await page.close();
    }
  }
  try {
    await caso("W05", { consultas: [{ almacen: "ALFA", nombre: "" }, { almacen: "BETA", nombre: "" }] },
      { primera: { almacen: "ALFA", total: "1", codigos: ["A01"] }, segunda: { almacen: "BETA", total: "1", codigos: ["A04"] } },
      async (page, r) => {
        const primera = await consultar(page, "ALFA", "");
        const segunda = await consultar(page, "BETA", "");
        r.observado = { primera, segunda };
        for (const [clave, observado] of Object.entries(r.observado)) {
          assert.equal(observado.estado, "exito");
          assert.equal(observado.resultado_visible, true);
          assert.equal(observado.error_visible, false);
          assert.deepEqual({ almacen: observado.almacen, total: observado.total, codigos: observado.codigos }, r.esperado[clave]);
        }
        if (captura && estado === "solucion") await page.screenshot({ path: captura, fullPage: true });
      });
    await caso("W06.a", { almacen: "ALFA", nombre: "inexistente" },
      { estado: "vacio", total: "0", codigos: [], error_visible: false },
      async (page, r) => {
        r.observado = await consultar(page, "ALFA", "inexistente");
        for (const [clave, valorEsperado] of Object.entries(r.esperado)) assert.deepEqual(r.observado[clave], valorEsperado);
        assert.equal(r.observado.resultado_visible, true);
        assert.equal(r.observado.mensaje, "No hay artículos disponibles que coincidan con la búsqueda.");
      });
    await caso("W06.b", { consulta_inicial: "ALFA", fallo_controlado: "route.abort('failed') en /api/resumen" },
      { estado: "error", resultado_visible: false, error_visible: true, codigos: [] },
      async (page, r) => {
        await consultar(page, "ALFA", "");
        await page.route("**/api/resumen?**", (route) => route.abort("failed"));
        r.observado = await consultar(page, "ALFA", "");
        for (const [clave, valorEsperado] of Object.entries(r.esperado)) assert.deepEqual(r.observado[clave], valorEsperado);
        assert.equal(r.observado.error, "No fue posible consultar el catálogo. Inténtalo de nuevo.");
      });
  } finally {
    await context.close();
    await browser.close();
  }
  guardar();
}

main().catch((error) => {
  for (const id of CASOS.filter((id) => !pruebas.some((p) => p.id === id))) {
    pruebas.push({ id, estado: "FALLIDO", tipo_error: error.name,
      detalle: "Error en la preparación del recorrido; no se obtuvo una observación válida." });
  }
  guardar();
});
