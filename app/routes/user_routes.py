from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    Response,
    status
)

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserUpdate,
    UserPatch
)

from app.services.user_service import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    patch_user,
    delete_user
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/",
    response_model=list[UserResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar usuarios",
    description=(
        "Obtiene todos los usuarios registrados. "
        "Permite filtrar por rol y estado, "
        "además de ordenar por nombre o fecha de creación."
    ),
    response_description="Lista de usuarios"
)
def list_users(
    role: str | None = Query(
        default=None,
        description="Filtrar usuarios por rol"
    ),
    is_active: bool | None = Query(
        default=None,
        description="Filtrar usuarios por estado"
    ),
    sort_by: str | None = Query(
        default=None,
        description="Campo para ordenar: name o created_at"
    ),
    order: str = Query(
        default="asc",
        description="Orden: asc o desc"
    ),
    db: Session = Depends(get_db)
):
    """
    Lista usuarios utilizando filtros y ordenamiento.
    """

    if sort_by not in (
        None,
        "name",
        "created_at"
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "sort_by debe ser 'name' "
                "o 'created_at'"
            )
        )

    if order not in ("asc", "desc"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "order debe ser 'asc' o 'desc'"
            )
        )

    return get_all_users(
        db=db,
        role=role,
        is_active=is_active,
        sort_by=sort_by,
        order=order
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar usuario",
    description="Obtiene un usuario mediante su ID.",
    response_description="Usuario encontrado"
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene un usuario por ID.
    """

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear usuario",
    description="Registra un nuevo usuario en la base de datos.",
    response_description="Usuario creado correctamente"
)
def create_new_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Crea un usuario.
    """

    new_user = create_user(
        db,
        user_data
    )

    if new_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "El correo electrónico "
                "ya está registrado"
            )
        )

    return new_user


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar usuario completamente",
    description=(
        "Reemplaza completamente la información "
        "de un usuario."
    ),
    response_description="Usuario actualizado correctamente"
)
def update_user_complete(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualización completa mediante PUT.
    """

    result = update_user(
        db,
        user_id,
        user_data
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    if result == "email_exists":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "El correo electrónico "
                "ya está registrado"
            )
        )

    return result


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar usuario parcialmente",
    description=(
        "Actualiza únicamente los campos "
        "enviados en la solicitud."
    ),
    response_description="Usuario actualizado correctamente"
)
def update_user_partial(
    user_id: int,
    user_data: UserPatch,
    db: Session = Depends(get_db)
):
    """
    Actualización parcial mediante PATCH.
    """

    result = patch_user(
        db,
        user_id,
        user_data
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    if result == "empty":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Debe enviar al menos "
                "un campo para actualizar"
            )
        )

    if result == "email_exists":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "El correo electrónico "
                "ya está registrado"
            )
        )

    return result


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar usuario",
    description="Elimina un usuario de la base de datos.",
    response_description="Usuario eliminado correctamente"
)
def remove_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Elimina un usuario.
    """

    user = delete_user(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )