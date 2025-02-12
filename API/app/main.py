import uvicorn
from fastapi import FastAPI, Depends
from app.database import init_db

from app.routes.Opc import router as Opc
from app.routes.Postgres import router as Postgres

# Initialize the database
init_db()

description = """
Pavener OPC-UA API. 🚀
"""

tags_metadata = [
    {
        "name": "Opc",
        "description": "Control Opc-UA Server",
    },{
        "name": "Postgres",
        "description": "Consulta de datos de la BBDD",
    }
]

app = FastAPI(
    root_path="/api",
    #docs_url=None, 
    redoc_url=None,
    title="API OPC-UA",
    #lifespan=_lifespan,
    description=description,
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Pavener Servicios Energeticos SLU",
        "url": "https://www.pavener.com/contacto/",
        "email": "info@pavener.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

app.include_router(Opc, tags=["Opc"], prefix="/Opc")
app.include_router(Postgres, tags=["Postgres"], prefix="/Postgres")