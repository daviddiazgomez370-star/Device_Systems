from fastapi import (
    APIRouter,
    Depends,
    Query,
    Response,
    status
)

from app.schemas.user_schema import(
    UserCreate,
    UserResponse,
    UserUpdate,
    UserPatch
)

from app.services.user_service import (
    get_all_users,
    create_user,
    update_user,
    patch_user,
    delete_user
)

from app.dependencies.user_dependencies import get_user_dependency

router = APIRouter(
    prefix="/users",
    tags=["users"]
)



@router.get(
    "/",
    response_model=list[UserResponse],
    summary="Listar usuarios",
    description="Obtiene todos los usuarios registrados.",
    response_description="Lista de usuarios"
)

def get_users(
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None)
):
    users = get_all_users()

    if role is not None:
        users = [
            user for user in users
            if user["role"] == role
        ]

    if is_active is not None:
        users = [
            user for user in users
            if user["is_active"] == is_active
        ]

    return users

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Consultar usuario",
    description="Obtiene un usuario mediante su ID",
    response_description="Usuario encontrado"
)

def get_user(
    user: dict =  Depends(get_user_dependency)
):
    return user

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear usuario",
    description="Registra un nuevo usuario",
    response_description="Usuario creado correctamente"
)

def create_new_user(
    user_data: UserCreate,
    response: Response
):
    new_user = create_user(user_data)

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "2.0"

    return new_user

@router.put(
    "/{user_id}",
    response_model=UserResponse,
    summary="Actualizar usuario completamente",
    description="Reemplaza completamente la información de un usuario",
    response_description="Usuario actualizado correctamente"
)
def update_user_complete(
    user_data: UserUpdate,
    user: dict = Depends(get_user_dependency)
):
    return update_user(user["id"], user_data)

@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="Actualizar usuario parcialmente",
    description="Actualiza únicamente los campos enviados",
    response_description="Usuario actualizado parcialmente"
)
def update_user_partial(
    user_data: UserPatch,
    user: dict = Depends(get_user_dependency)
):
    return patch_user(user["id"], user_data)

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar usuario",
    description="Elimina un usuario existente"
)
def remove_user(
    user: dict = Depends(get_user_dependency)
):
    delete_user(user["id"])

    return Response(status_code=status.HTTP_204_NO_CONTENT)