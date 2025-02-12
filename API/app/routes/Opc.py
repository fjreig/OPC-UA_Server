from fastapi import FastAPI, Depends, APIRouter, Body
from sqlalchemy.orm import Session
from fastapi import Query

from app.models import Modelo_opc, InversorRequest, AARRRequest, EMIRequest
from app.database import SessionLocal
from app.src.opc import (
    obtenerNodos, 
    leerNodo, 
    escribirNodo, 
    ObtenerInversor,
    ObtenerAARR,
    ObtenerEMI,
    escribirInversor,
    escribirAARR,
    escribirEMI
)

router = APIRouter()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/Nodes/", summary="Mostrar todas las variables")
async def read_notification_id():
    variables = obtenerNodos()
    return(variables)

@router.get("/Read/{variable}", summary="Leer variable")
async def read_notification_id(variable: str, db: Session = Depends(get_db)):
    value = leerNodo(variable)
    result = Modelo_opc(variable = variable,valor = value)
    db.add(result)
    db.commit()
    db.refresh(result)
    return({"Variable": variable, 'Valor': value})

@router.get("/Read/Equipo/{num_equipo}", summary="Leer variable por equipo")
async def read_notification_id(num_equipo: int, equipo: str = Query("Inversor", enum=['Inversor', 'AARR', 'EMI']), db: Session = Depends(get_db)):
    if equipo == 'Inversor':
        valores = ObtenerInversor(num_equipo)
    elif equipo == 'AARR':
        valores = ObtenerAARR(num_equipo)
    elif equipo == 'EMI':
        valores = ObtenerEMI(num_equipo)
    return(valores)

@router.post("/Write/{variable}/{valor}", summary="Modificar variable")
async def create_notification(variable: str, valor: float):
    (value1, value2) = escribirNodo(valor, variable)
    return({"Variable": variable, 'Valor_anterior': value1, 'Valor': value2})

@router.post("/Write/Inversor/{num_equipo}", summary="Modificar variables del Inversor")
async def create_notification(num_equipo: int,data: InversorRequest = Body(...)):
    escribirInversor(num_equipo, data)
    return(data)

@router.post("/Write/AARR/{num_equipo}", summary="Modificar variable del AARR")
async def create_notification(num_equipo: int,data: AARRRequest = Body(...)):
    escribirAARR(num_equipo, data)
    return(data)

@router.post("/Write/EMI/{num_equipo}", summary="Modificar variable de la EMI")
async def create_notification(num_equipo: int,data: EMIRequest = Body(...)):
    escribirEMI(num_equipo, data)
    return(data)