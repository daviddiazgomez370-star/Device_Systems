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



from fastapi import FastAPI

from app.database.connection import (
    Base,
    engine
)

from app.models.user_model import User

from app.routes.user_routes import router as user_router


# Crear las tablas de la base de datos
Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="device_systems API",
    description=(
        "API REST para la gestión de usuarios "
        "del sistema device_systems utilizando "
        "FastAPI, SQLAlchemy y SQLite."
    ),
    version="3.0.0",
    contact={
        "name": "Aprendiz SENA",
        "email": "aprendiz@example.com"
    }
)


# Registrar rutas
app.include_router(
    user_router
)


@app.get(
    "/",
    tags=["General"],
    summary="Verificar estado de la API",
    description=(
        "Comprueba que la API "
        "device_systems esté funcionando."
    ),
    response_description="Estado de la API"
)
def root():
    return {
        "message": "API device_systems funcionando correctamente",
        "version": "3.0.0",
        "database": "SQLite",
        "orm": "SQLAlchemy"
    }