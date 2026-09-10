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



from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()

@app.post("/usuario/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(db=db, usuario_data=usuario)

@app.get("/usuario/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(db=db, usuario_id=usuario_id):
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

# @app.put("/usuario/{usuario_id}", response_model=UsuarioResponse)
