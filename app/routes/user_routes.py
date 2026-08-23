from fastapi import APIRouter, HTTPException, Query, Response
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

users = [
    {
        "id": 1,
        "name": "Cristian Mesa",
        "email": "Cristianmesa@example.com",
        "role": "support",
        "is_activate": True
    },
    {
        "id": 2,
        "name": "David Díaz",
        "email": "daviddiaz@example.com",
        "role": "admin",
        "is_activate": True
    },
    {
        "id": 3,
        "name": "Andrés Rodríguez",
        "email": "andresrodriguez@example.com",
        "role": "user",
        "is_activate": False
    }
]

@router.get("/", response_model=list[UserResponse])
def get_users(
    role: str | None = Query(default=None),
    is_activate: bool | None = Query(default=None)
):
    result = users

    if role is not None:
        result = [
            user for user in result 
            if user["role"] == role
        ]

    if is_activate is not None:
        result = [
            user for user in result
            if user["is_activate"] == is_activate
        ]
    
    return result


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
        
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate):
    for user in users:
        if user["email"] == user_data.email:
            raise HTTPException(
                status_code=400,
                detail="El correo electronico ya esta registrado"
            )
        
    new_user = {
        "id": len(users) + 1,
        **user_data.model_dump()
    }

    users.append(new_user)

    return new_user