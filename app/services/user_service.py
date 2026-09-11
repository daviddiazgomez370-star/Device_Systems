from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserPatch
)


def get_all_users(
    db: Session,
    role: str | None = None,
    is_active: bool | None = None,
    sort_by: str | None = None,
    order: str = "asc"
):
    """
    Obtiene todos los usuarios de la base de datos.

    Permite filtrar por:
    - role
    - is_active

    Permite ordenar por:
    - name
    - created_at
    """

    query = db.query(User)

    # Filtro por rol
    if role is not None:
        query = query.filter(User.role == role)

    # Filtro por estado
    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    # Ordenamiento
    if sort_by == "name":
        if order == "desc":
            query = query.order_by(User.name.desc())
        else:
            query = query.order_by(User.name.asc())

    elif sort_by == "created_at":
        if order == "desc":
            query = query.order_by(User.created_at.desc())
        else:
            query = query.order_by(User.created_at.asc())

    return query.all()


def get_user_by_id(
    db: Session,
    user_id: int
):
    """
    Busca un usuario por su ID.
    """

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_email(
    db: Session,
    email: str
):
    """
    Busca un usuario por su correo electrónico.
    """

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(db: Session, user_data: UserCreate):
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        return None

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
        is_active=user_data.is_active
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):
    """
    Actualiza completamente un usuario.
    """

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        return None

    # Verificar correo duplicado
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if (
        existing_user
        and existing_user.id != user_id
    ):
        return "email_exists"

    # Actualización completa
    user.name = user_data.name
    user.email = user_data.email
    user.role = user_data.role
    user.is_active = user_data.is_active

    db.commit()
    db.refresh(user)

    return user


def patch_user(
    db: Session,
    user_id: int,
    user_data: UserPatch
):
    """
    Actualiza parcialmente un usuario.
    """

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        return None

    # Obtener solamente los campos enviados
    update_data = user_data.model_dump(
        exclude_unset=True
    )

    # Verificar PATCH vacío
    if not update_data:
        return "empty"

    # Verificar correo duplicado
    if "email" in update_data:

        existing_user = get_user_by_email(
            db,
            update_data["email"]
        )

        if (
            existing_user
            and existing_user.id != user_id
        ):
            return "email_exists"

    # Actualizar los campos
    for field, value in update_data.items():
        setattr(
            user,
            field,
            value
        )

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int
):
    """
    Elimina un usuario.
    """

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        return None

    db.delete(user)

    db.commit()

    return user