# from pydantic import BaseModel, EmailStr, Field, field_validator
# from datetime import datetime
# from typing import Literal, Optional
# class UserBase(BaseModel):
#     name: str = Field(..., min_length=3)
#     email: EmailStr
#     role: Literal["admin", "support", "user"]
#     is_activate: bool = True
# class UserCreate(UserBase):
#     pass
# class UserResponse(UserBase):
#     id: int
# class UserUpdate(UserBase):
#     pass
# class UserPatch(BaseModel):
#     name: str | None = Field(default=None, min_length=3)
#     email: EmailStr | None = None
#     role: Literal["admin", "support", "user"] | None = None
#     is_activate: bool | None = None
# class CursoBase(BaseModel):
#     nombre: str = Field(..., min_length=3, max_length=100)
#     descripcion: Optional[str] = Field(None, max_length=300)
#     horas: int = Field(0, ge=0, le=500)
#     activo: bool = True

#     @field_validator("nombre")
#     @classmethod
#     def nombre_sin_espacios_extra(cls, v: str) -> str:
#         return v.strip()



from sqlalchemy.orm import Session
from models import Usuario
from schemas import UsuarioCreate

def crear_usuario(db: Session, usuario_data: UsuarioCreate):
    db_usuario = Usuario(
        nombre =    usuario_data.nombre,
        email =     usuario_data.email,
        edad =      usuario_data.edad
    )

    db.add(db_usuario)

    db.commit()

    db.refresh(db_usuario)

    return db_usuario

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def actualizar_usuario(db: Session, usuario_id: int, usuario_data: UsuarioCreate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if db_usuario:
        db_usuario.nombre = usuario_data.nombre
        db_usuario.email = usuario_data.email
        db_usuario = usuario_data.edad

        db.commit()
        db.refresh(db_usuario)

    return db_usuario

def eliminar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if db_usuario:
        db.delete(db_usuario)
        db.commit()