-- Cambiar a Monitorizacion
\connect Monitorizacion;

-- Tabla Inversores
CREATE TABLE IF NOT EXISTS inversores (
  id serial,
  fecha timestamp,
  inversor int2,
  pa float,
  pa_peak float,
  ea float,
  ea_hoy float,
  estado int4,
  temperatura float,
  raislamiento float,
  v1 float,
  v2 float,
  v3 float,
  i1 float,
  i2 float,
  i3 float,
  vs1 float,
  vs2 float,
  vs3 float,
  vs4 float,
  vs5 float,
  vs6 float,
  vs7 float,
  vs8 float,
  vs9 float,
  vs10 float,
  is1 float,
  is2 float,
  is3 float,
  is4 float,
  is5 float,
  is6 float,
  is7 float,
  is8 float,
  is9 float,
  is10 float,
  PRIMARY KEY (id)
);

-- Tabla AARR
CREATE TABLE IF NOT EXISTS aarr (
  id serial,
  fecha timestamp,
  aarr varchar,
  pa1 float,
  pa2 float,
  pa3 float,
  pa float,
  ea float,
  v1 float,
  v2 float,
  v3 float,
  i1 float,
  i2 float,
  i3 float,
  PRIMARY KEY (id)
);

-- Tabla EMI
CREATE TABLE IF NOT EXISTS emi (
  id serial,
  fecha timestamp,
  emi varchar,
  rad1 float,
  rad2 float,
  tamb float,
  tpanel float,
  PRIMARY KEY (id)
);