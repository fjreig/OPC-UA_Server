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