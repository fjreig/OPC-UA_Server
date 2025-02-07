from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from opcua import ua

from app.models import Modelo_opc
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

@router.get("/Nodes/", summary="Mostrar todas las variables")
async def read_notification_id():
    root = client.get_root_node()
    children = root.get_children()
    child_of_children=children[0].get_children()
    c_child_of_children=child_of_children[2].get_children()
    variables = {}
    for i in range(len(c_child_of_children)):
        variables.update({i : str(client.get_node(c_child_of_children[i]))})
    return(variables)

@router.get("/Read/{variable}", summary="Leer variable")
async def read_notification_id(variable: str, db: Session = Depends(get_db)):
    value = client.get_node(variable)
    value = value.get_value()
    result = Modelo_opc(
        variable = variable,
        valor = value)
    db.add(result)
    db.commit()
    db.refresh(result)
    return({"Variable": variable, 'Valor': value})

@router.post("/Write/{variable}/{valor}", summary="Modificar variable")
async def create_notification(variable: str, valor: float):
    node = client.get_node(variable)
    value1 = node.get_value()
    try:
        node.set_value(ua.DataValue(ua.Variant(valor, ua.VariantType.Double)))
    except:
        node.set_value(ua.DataValue(ua.Variant(valor, ua.VariantType.Int64)))
    value2 = node.get_value()
    return({"Variable": variable, 'Valor_anterior': value1, 'Valor': value2})