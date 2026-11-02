# Revisión independiente de Git y procedencia · laboratorio 10 WSL

**Resultado: APROBADO.** Fecha de revisión: 01/11/2026, 18:45:03 (America/Hermosillo). Fecha técnica UTC en el JSON adjunto.

## Identidad preparada

Se contrastó el inventario recibido con los objetos Git confiables de la producción anterior. Los **3.660 archivos** tienen rutas, modos Git, OID y SHA-256 coincidentes. Además, se reconstruyó el árbol en memoria a partir de nombres, modos y OID del inventario: **78b136a253cb3cb79143a0c81ee09f7892efa40f**, idéntico al árbol probado del paquete.

La base permanece en **6a5fdaf36e225c9fd0fac8181e4fda45a987fdd3**, árbol **790e875fc95495c39ea2b5ebe7621a4ae1afa30f**. Las **1.372 rutas** corresponden exactamente al parche: **1.363 adiciones**, **nueve modificaciones existentes** y **cero eliminaciones**. La rama registrada es `codex/integracion-laboratorio-10`. El SHA-256 del parche coincide con el original: `60a0f636ebb254fb5e1a98724127780069209ee9d0f690966566dd8f80e2a808`.

## Conservación

Los **2.297 hashes** del inventario anterior coinciden con los blobs de la base. Los **2.288 archivos protegidos** permanecen idénticos entre los árboles base y preparado. Este alcance incluye íntegramente los 2.285 protegidos de producción y añade tres: `docs/CORRECCION_RECOLECTOR_v1.0.md`, `herramientas/preparar_laboratorio_04.py` y `herramientas/pruebas/test_evaluador_laboratorio_09.py`.

Los **3.156 archivos históricos de trabajo** tienen inventarios antes/después coherentes y controles afirmativos de conservación. Sus bytes originales no están incluidos individualmente en este envío: esta auditoría comprueba sus declaraciones, no accede a esos archivos de la máquina del autor.

El informe declara que el inventario leyó contenido antes de aplicar el parche y completó después los metadatos Git. El cotejo confirma que los hashes corresponden al contenido de la base, incluidos los nueve archivos que después se modifican. Esta auditoría no verifica el instante de cada lectura ni debe describir el inventario como una captura atómica del estado Git y el contenido. Los modos Git sí se cotejaron; los modos del sistema de archivos WSL se conocen por los controles registrados, sin acceso directo a ese entorno.

## Referencias y operaciones

Los registros iniciales, preparados y finales concuerdan en HEAD, main y las **quince etiquetas históricas**. Las etiquetas `lab-10-v1.0` y `repositorio-v1.6` están ausentes. El único nombre local nuevo en los listados recibidos es la rama de integración. Las 28 operaciones registradas tienen código 0 y no contienen commit, push, creación de etiquetas, reset, clean ni merge.

Esto acredita la coherencia de la evidencia aportada. No constituye acceso en vivo a la copia WSL. La consulta remota independiente del agente principal, revisada en `REFERENCIAS_REMOTAS_RECONSULTADAS.json`, confirma el mismo main, árbol y quince etiquetas, sin las etiquetas previstas nuevas, al 1 de noviembre de 2026 a las 18:43:25 de Hermosillo. No se observó avance posterior.

## Distribución

La distribución autónoma recibida en la producción anterior conserva SHA-256 `5e39d5fb92e2408684003809d65f753b16929c7ad649e70f1c8eec0e26eb54f3`. Sus **450 archivos** coinciden entre ZIP, inventario WSL y blobs Git del árbol preparado; CRC correcto. Este cotejo no es una nueva ejecución funcional autónoma.

## Límites

No se ejecutaron scripts adjuntos, baterías funcionales ni escrituras Git. Los originales recibidos permanecen intactos. Las verificaciones sobre bytes accesibles y objetos Git aprobaron; no se identificaron divergencias materiales dentro del alcance.
