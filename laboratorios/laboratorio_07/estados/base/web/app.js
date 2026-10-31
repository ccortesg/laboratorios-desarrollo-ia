"use strict";

const formulario = document.querySelector("#consulta");
const selector = document.querySelector("#almacen");
const nombre = document.querySelector("#nombre");
const boton = document.querySelector("#consultar");
const mensaje = document.querySelector("#mensaje");
const error = document.querySelector("#error");
const resultado = document.querySelector("#resultado");
const panel = document.querySelector("#panel-resultados");
const codigos = document.querySelector("#codigos");

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  const almacen = selector.value;
  const parametros = new URLSearchParams({ almacen, nombre: nombre.value });
  boton.disabled = selector.disabled = nombre.disabled = true;
  panel.setAttribute("aria-busy", "true");
  resultado.hidden = true;
  error.hidden = true;
  error.textContent = "";
  codigos.replaceChildren();
  mensaje.dataset.estado = "cargando";
  mensaje.textContent = "Consultando disponibilidad…";
  try {
    const respuesta = await fetch(`/api/resumen?${parametros}`);
    if (!respuesta.ok) throw new Error("Consulta no disponible");
    const datos = await respuesta.json();
    document.querySelector("#almacen-resultado").textContent = datos.almacen;
    document.querySelector("#total").textContent = String(datos.total);
    for (const codigo of datos.codigos) {
      const elemento = document.createElement("li");
      elemento.textContent = codigo;
      codigos.append(elemento);
    }
    resultado.hidden = false;
    mensaje.dataset.estado = datos.total === 0 ? "vacio" : "exito";
    mensaje.textContent = datos.total === 0
      ? "No hay artículos disponibles que coincidan con la búsqueda."
      : "Consulta completada.";
  } catch {
    mensaje.dataset.estado = "error";
    mensaje.textContent = "La consulta no se completó.";
    error.textContent = "No fue posible consultar el catálogo. Inténtalo de nuevo.";
    error.hidden = false;
  } finally {
    boton.disabled = selector.disabled = nombre.disabled = false;
    panel.setAttribute("aria-busy", "false");
  }
});
