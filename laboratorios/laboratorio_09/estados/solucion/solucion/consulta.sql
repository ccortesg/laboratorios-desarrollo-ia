SELECT a.codigo, a.nombre
FROM articulos AS a
WHERE a.habilitado = 1
  AND EXISTS (
      SELECT 1
      FROM existencias AS e
      WHERE e.articulo = a.codigo
        AND e.almacen = :almacen
        AND e.cantidad > 0
  )
ORDER BY a.codigo;
