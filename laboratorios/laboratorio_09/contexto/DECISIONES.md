# Decisiones y supuestos

Fecha del contrato: 1 de noviembre de 2026. Los detalles normativos están en `CONTRATO_SEGURIDAD.md`; este registro explica su finalidad.

- La amenaza concreta elegida es una entrada HTTP ambigua o fuera de contrato. Se limita a un servidor de práctica en loopback y no se extiende a escanear sistemas externos.
- Rechazar duplicados evita que dos componentes elijan silenciosamente valores distintos. Se hace después de decodificar las claves, antes de convertir a diccionario.
- El límite de 2.048 bytes corresponde a la query recibida. El límite de 80 corresponde a puntos de código Unicode del nombre decodificado, antes de `strip()`/`casefold()`. Son decisiones didácticas, no constantes universales.
- La sintaxis percent se valida expresamente: el analizador de query no garantiza por sí solo rechazar toda secuencia mal formada. UTF-8 usa errores estrictos y se decodifica una sola vez.
- Las claves desconocidas se rechazan; los almacenes desconocidos no vacíos conservan la búsqueda exacta anterior y su resultado vacío. No se inventa una política de autorización.
- El HTTP mantiene sus mensajes públicos genéricos; el detalle técnico se obtiene en pruebas controladas. La aplicación no registra la query del lector.
- El dominio, CSV, conexiones y web mantienen sus bytes originales salvo el adaptador HTTP de los dos estados nuevos. Las pruebas heredadas no se debilitan para admitir la corrección.
- La propuesta incluye una sola decisión defectuosa: colapsar pares a diccionario antes de validarlos. Las fallas de base son brechas de la nueva política; sus contratos anteriores siguen aprobando.
- Un resultado `APROBADO` del verificador completo significa que se reprodujo exactamente el patrón definido. No significa que los casos defectuosos hayan aprobado ni que se haya demostrado seguridad integral.

No se modificó el documento maestro editorial por este incremento técnico. Los manuscritos anteriores permanecen pendientes de revisión del autor. Las fuentes primarias del material se registran por separado.
