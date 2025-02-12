-- Cambiar a Monitorizacion
\connect Monitorizacion;

-- Tabla OPC
CREATE TABLE IF NOT EXISTS opc (
  id serial,
  fecha timestamp,
  variable varchar,
  valor float,
  PRIMARY KEY (id)
);