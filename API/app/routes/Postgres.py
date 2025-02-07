from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import Date, cast
from opcua import ua

from app.models import OPCRequest, Modelo_bbdd_opc
from app.conexion import cliente_opc_create
from app.database import SessionLocal

router = APIRouter()
client = cliente_opc_create()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/Read/bbdd/{variable}", summary="Leer variable de la BBDD a OPC")
async def read_notification_id(variable: str, db: Session = Depends(get_db)):
    result = db.query(Modelo_bbdd_opc).\
        filter(Modelo_bbdd_opc.variable == variable).order_by(Modelo_bbdd_opc.id.desc()).first()
    node = client.get_node(result.variable)
    try:
        node.set_value(ua.DataValue(ua.Variant(result.valor, ua.VariantType.Double)))
    except:
        node.set_value(ua.DataValue(ua.Variant(result.valor, ua.VariantType.Int64)))
    return(result)

@router.post("/Write/bbdd/{variable}", summary="Escribir datos a la BBDD")
async def create_notification(necesidades_req: OPCRequest, db: Session = Depends(get_db)):
    result = Modelo_bbdd_opc(
        variable=necesidades_req.variable,
        valor=necesidades_req.valor)
    db.add(result)
    db.commit()
    db.refresh(result)
    return {"status": "Plant created", "data": necesidades_req}