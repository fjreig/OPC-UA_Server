-- Cambiar a Monitorizacion
\connect Monitorizacion;

-- Tabla OPC
CREATE TABLE IF NOT EXISTS opc (
  id serial,
  fecha timestamp,
  vs1 float,
  vs2 float,
  vs3 float,
  vs4 float,
  vs5 float,
  PRIMARY KEY (id)
);