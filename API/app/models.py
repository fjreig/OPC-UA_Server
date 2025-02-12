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
    PA: float
    PA_peak: float
    EA: float
    EA_hoy: float
    Estado: int
    Temperatura: float
    Raislamiento: float
    V1: float
    V2: float
    V3: float
    I1: float
    I2: float
    I3: float
    vs1: float
    vs2: float
    vs3: float
    vs4: float
    vs5: float
    vs6: float
    vs7: float
    vs8: float
    vs9: float
    vs10: float
    is1: float
    is2: float
    is3: float
    is4: float
    is5: float
    is6: float
    is7: float
    is8: float
    is9: float
    is10: float

    class Config:
        json_schema_extra = {
            "example": {
                'PA' : 0,
                'PA_peak' : 0,
                'EA' : 0,
                'EA_hoy' : 0,
                'Estado' : 0,
                'Temperatura' : 0,
                'Raislamiento' : 0,
                'V1' : 0,
                'V2' : 0,
                'V3' : 0,
                'I1' : 0,
                'I2' : 0,
                'I3' : 0,
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
    PA: float
    PA1: float
    PA2: float
    PA3: float
    EA: float
    V1: float
    V2: float
    V3: float
    I1: float
    I2: float
    I3: float

    class Config:
        json_schema_extra = {
            "example": {
                'PA' : 0,
                'PA1' : 0,
                'PA2' : 0,
                'PA3' : 0,
                'EA' : 0,
                'V1' : 0,
                'V2' : 0,
                'V3' : 0,
                'I1' : 0,
                'I2' : 0,
                'I3' : 0
            }
        }

class EMIRequest(BaseModel):
    Rad1: float
    Rad2: float
    Tamb: float
    Tpanel: float

    class Config:
        json_schema_extra = {
            "example": {
                'Rad1' : 0,
                'Rad2' : 0,
                'Tamb' : 0,
                'Tpanel' : 0
            }
        }