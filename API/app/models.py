from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()

class Modelo_opc(Base):
    __tablename__ = "opc"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    variable = Column(String)
    valor = Column(Float)

class Modelo_bbdd_opc(Base):
    __tablename__ = "bbdd_opc"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    variable = Column(String)
    valor = Column(Float)

class OPCRequest(BaseModel):
    variable: str
    valor: int

    class Config:
        json_schema_extra = {
            "example": {
                'variable': 'ns=2;s=freeopcua.Tags.pressure',
                'valor': 2
            }
        }

class InversorRequest(BaseModel):
    inversor: int
    pa: float = None
    pa_peak: float = None
    ea: float = None
    ea_hoy: float = None
    estado: int = None
    temperatura: float = None
    raislamiento: float = None
    V1: float = None
    V2: float = None
    V3: float = None
    I1: float = None
    I2: float = None
    I3: float = None
    vs1: float = None
    vs2: float = None
    vs3: float = None
    vs4: float = None
    vs5: float = None
    vs6: float = None
    vs7: float = None
    vs8: float = None
    vs9: float = None
    vs10: float = None
    is1: float = None
    is2: float = None
    is3: float = None
    is4: float = None
    is5: float = None
    is6: float = None
    is7: float = None
    is8: float = None
    is9: float = None
    is10: float = None

    class Config:
        json_schema_extra = {
            "example": {
                'inversor': 1,
                'pa' : 0,
                'pa_peak' : 0,
                'ea' : 0,
                'ea_hoy' : 0,
                'estado' : 0,
                'temperatura' : 0,
                'raislamiento' : 0,
                'v1' : 0,
                'v2' : 0,
                'v3' : 0,
                'i1' : 0,
                'i2' : 0,
                'i3' : 0,
                'vs1' : 0,
                'vs2' : 0,
                'vs3' : 0,
                'vs4' : 0,
                'vs5' : 0,
                'vs6' : 0,
                'vs7' : 0,
                'vs8' : 0,
                'vs9' : 0,
                'vs10' : 0,
                'is1' : 0,
                'is2' : 0,
                'is3' : 0,
                'is4' : 0,
                'is5' : 0,
                'is6' : 0,
                'is7' : 0,
                'is8' : 0,
                'is9' : 0,
                'is10' : 0
            }
        }

class AARRRequest(BaseModel):
    aarr: int
    pa: float = None
    pa1: float = None
    pa2: float = None
    pa3: float = None
    ea: float = None
    v1: float = None
    v2: float = None
    v3: float = None
    i1: float = None
    i2: float = None
    i3: float = None

    class Config:
        json_schema_extra = {
            "example": {
                'aarr': 1,
                'pa' : 0,
                'pa1' : 0,
                'pa2' : 0,
                'pa3' : 0,
                'ea' : 0,
                'v1' : 0,
                'v2' : 0,
                'v3' : 0,
                'i1' : 0,
                'i2' : 0,
                'i3' : 0
            }
        }

class EMIRequest(BaseModel):
    emi: int
    rad1: float = None
    rad2: float = None
    tamb: float = None
    tpanel: float = None

    class Config:
        json_schema_extra = {
            "example": {
                'emi': 1,
                'rad1' : 0,
                'rad2' : 0,
                'tamb' : 0,
                'tpanel' : 0
            }
        }

class BombaRequest(BaseModel):
    bomba: int
    estado: float = None
    pa: float = None
    frecuencia: float = None
    horas: float = None

    class Config:
        json_schema_extra = {
            "example": {
                'bomba': 1,
                'estado' : 0,
                'pa' : 0,
                'frecuencia' : 0,
                'horas' : 0
            }
        }

class PCSRequest(BaseModel):
    pcs: int
    pa_carga: float = None
    pa_descarga: float = None
    estado: int = None
    pa: float = None
    temperatura: float = None
    raislamiento: float = None
    ea: float = None
    ea_hoy: float = None
    regulacion: float = None
    v1: float = None
    v2: float = None
    v3: float = None
    i1: float = None
    i2: float = None
    i3: float = None

    class Config:
        json_schema_extra = {
            "example": {
                'pcs': 1,
                'pa_carga': 0,
                'pa_descarga': 0,
                'estado': 0,
                'pa': 0,
                'temperatura': 0,
                'raislamiento': 0,
                'ea': 0,
                'ea_hoy': 0,
                'regulacion': 0,
                'v1': 0,
                'v2': 0,
                'v3': 0,
                'i1': 0,
                'i2': 0,
                'i3': 0,
            }
        }

class bateriaRequest(BaseModel):
    bateria: int
    bcu1_estado: int = None
    bcu1_v: float = None
    bcu1_i: float = None
    bcu1_pa: float = None 
    bcu1_soc: float = None 
    bcu1_soh: float = None 
    bcu1_soe: float = None 
    bcu1_dod: float = None 
    bcu1_capacidad_carga: float = None 
    bcu1_capacidad_descarga: float = None
    bcu2_estado: int = None 
    bcu2_v: float = None 
    bcu2_i: float = None 
    bcu2_pa: float = None 
    bcu2_soc: float = None 
    bcu2_soh: float = None 
    bcu2_soe: float = None 
    bcu2_dod: float = None 
    bcu2_capacidad_carga: float = None 
    bcu2_capacidad_descarga: float = None
    temp_Cabin1: float = None 
    temp_Cabin2: float = None 
    temp_Cabin3: float = None 
    temp_Cabin4: float = None 
    estado_cont1: int = None 
    estado_cont2: int = None 
    estado_cont3: int = None
    soc: float = None 
    pa: float = None 
    ea_carga: float = None 
    ea_descarga: float = None 
    ea_carga_hoy: float = None 
    ea_descarga_hoy: float = None 
    capacidad_carga: float = None 
    capacidad_descarga: float = None
    v1: float = None 
    v2: float = None
    v3 : float = None
    i1: float = None 
    i2: float = None 
    i3: float = None

    class Config:
        json_schema_extra = {
            "example": {
                'bateria':1,
                'bcu1_estado':0,
                'bcu1_v':0,
                'bcu1_i':0,
                'bcu1_pa':0, 
                'bcu1_soc':0, 
                'bcu1_soh':0, 
                'bcu1_soe':0, 
                'bcu1_dod':0, 
                'bcu1_capacidad_carga':0, 
                'bcu1_capacidad_descarga':0,
                'bcu2_estado':0, 
                'bcu2_v':0, 
                'bcu2_i':0, 
                'bcu2_pa':0, 
                'bcu2_soc':0, 
                'bcu2_soh':0, 
                'bcu2_soe':0, 
                'bcu2_dod':0, 
                'bcu2_capacidad_carga':0, 
                'bcu2_capacidad_descarga':0,
                'temp_Cabin1':0, 
                'temp_Cabin2':0, 
                'temp_Cabin3':0, 
                'temp_Cabin4':0, 
                'estado_cont1':0, 
                'estado_cont2':0, 
                'estado_cont3':0,
                'soc':0, 
                'pa':0, 
                'ea_carga':0, 
                'ea_descarga':0, 
                'ea_carga_hoy':0, 
                'ea_descarga_hoy':0, 
                'capacidad_carga':0, 
                'capacidad_descarga':0,
                'v1':0, 
                'v2':0,
                'v3' :0,
                'i1':0, 
                'i2':0, 
                'i3':0
            }
        }