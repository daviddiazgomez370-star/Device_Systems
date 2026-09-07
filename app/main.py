# from fastapi import FastAPI
# from app.routes.user_routes import router as user_router


# app = FastAPI(
#     title="device_systems API",
#     description="API REST para la gestión de usuarios",
#     version="1.0"
# )

# app.include_router(user_router)

# @app.get(
#     "/",
#     tags=["General"],
#     summary="Verificar estado de la API",
#     description="Comprueba que la API device_systems esté funcionando",
#     response_description="Mensaje de estado"
# )
# def root():
#     return{
#         "message": "API device_systems funcionando correctamente",
#         "Version": "2.0.0"
#     }

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, create_tables

app = FastAPI()

create_tables()

@app.get("/")
def root():
    return {"mensaje": "API con SQLAlchemy funcionando"}

@app.get("/test-db/")
def test_database(db: Session = Depends(get_db)):
    try:
        result = db.execute("SELECT 1")
        return {"Estado": "Conexión exitosa", "resultado": result.scalar()}
    except Exception as e:
        return {"error": f"Error de conexión:{str(e)}"}