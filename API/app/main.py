import uvicorn
from fastapi import FastAPI, Depends
from app.database import init_db

from app.routes.Opc import router as Opc
from app.routes.Postgres import router as Postgres

# Initialize the database
init_db()

tags_metadata = [
    {
        "name": "Opc",
        "description": "Control Opc-UA Server",
    },{
        "name": "Postgres",
        "description": "Consulta de datos de la BBDD",
    }
]

app = FastAPI()

app.include_router(Opc, tags=["Opc"], prefix="/Opc")
app.include_router(Postgres, tags=["Postgres"], prefix="/Postgres")