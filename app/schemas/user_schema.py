from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class UserBase(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    role: Literal["admin", "support", "user"]
    is_activate: bool = True

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id:int

class UserUpdate(UserBase):
    pass

class UserPatch(BaseModel):
    name: str | None = Field(default=None, min_length=3)
    email: EmailStr | None = None
    role: Literal["admin", "support", "user"] | None = None
    is_activate: bool | None = None