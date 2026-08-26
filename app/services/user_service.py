from fastapi import HTTPException
from app.data.users_db import users
from app.schemas.user_schema import UserCreate, UserUpdate, UserPatch

def get_all_users():
    return users

def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
        
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

def create_user(user_data: UserCreate):
    for user in users:
        if user["email"] == user_data.email:
            raise HTTPException(
                status_code=400,
                detail="El correo electrónico ya esta registrado"
            )
        
    new_user = {
        "id": max([user["id"] for user in users], default=0) + 1,
        **user_data.model_dump()
    }

    user.append(new_user)

    return new_user

def update_user(user_id: int, user_data: UserUpdate):
    user = get_user_by_id(user_id)

    for existing_user in users:
        if(
            existing_user["email"] == user_data.email
            and existing_user["id"] != user_id
        ):
            raise HTTPException(
                status_code=400,
                detail="El correo electrónico ya está registrado"
            )
        
    user.update(user_data.model_dump())

    return user

def patch_user(user_id: int, user_data: UserPatch):
    user = get_user_by_id(user_id)

    update_data = user_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Debe enviar al menos un campo para actualizar"
        )
    
    if "email" in update_data:
        for existing_user in users:
            if(
                existing_user["email"] == update_data["email"]
                and existing_user["id"] != user_id
            ):
                raise HTTPException(
                    status_code=400,
                    detail="El correo electrónico ya esta registrado"
                )
            
    user.update(update_data)

    return user

def delete_user(user_id: int):
    user = get_user_by_id(user_id)

    users.remove(user)

    return user