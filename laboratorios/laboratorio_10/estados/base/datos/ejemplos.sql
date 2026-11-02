-- Todos los registros y nombres pertenecen al laboratorio sintetico.
INSERT INTO almacenes (codigo) VALUES ('ALFA'), ('BETA');

INSERT INTO articulos (codigo, nombre, habilitado) VALUES
    ('A01', 'Articulo local', 1),
    ('A02', 'Articulo deshabilitado', 0),
    ('A03', 'Articulo agotado', 1),
    ('A04', 'Articulo de otra ubicacion', 1);

INSERT INTO existencias (articulo, almacen, cantidad) VALUES
    ('A01', 'ALFA', 7),
    ('A02', 'ALFA', 4),
    ('A03', 'ALFA', 0),
    ('A04', 'BETA', 9);
