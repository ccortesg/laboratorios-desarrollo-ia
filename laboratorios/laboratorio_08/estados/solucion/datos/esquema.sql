PRAGMA foreign_keys = ON;

CREATE TABLE articulos (
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    habilitado INTEGER NOT NULL CHECK (habilitado IN (0, 1))
);

CREATE TABLE almacenes (
    codigo TEXT PRIMARY KEY
);

CREATE TABLE existencias (
    articulo TEXT NOT NULL REFERENCES articulos(codigo),
    almacen TEXT NOT NULL REFERENCES almacenes(codigo),
    cantidad INTEGER NOT NULL
        CHECK (typeof(cantidad) = 'integer' AND cantidad >= 0),
    PRIMARY KEY (articulo, almacen)
);
