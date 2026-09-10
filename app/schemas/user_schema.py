from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from typing import Literal, Optional
class UserBase(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    role: Literal["admin", "support", "user"]
    is_activate: bool = True
class UserCreate(UserBase):
    pass
class UserResponse(UserBase):
    id: int
class UserUpdate(UserBase):
    pass
class UserPatch(BaseModel):
    name: str | None = Field(default=None, min_length=3)
    email: EmailStr | None = None
    role: Literal["admin", "support", "user"] | None = None
    is_activate: bool | None = None
class CursoBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=300)
    horas: int = Field(0, ge=0, le=500)
    activo: bool = True

    @field_validator("nombre")
    @classmethod
    def nombre_sin_espacios_extra(cls, v: str) -> str:
        return v.strip()

class CursoCreate(CursoBase):
    pass
