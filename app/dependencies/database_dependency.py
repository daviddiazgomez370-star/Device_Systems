# from fastapi import Depends
# from app.services.user_service import get_user_by_id

# def get_user_dependency(user_id: int):
#     return get_user_by_id(user_id)

from app.database.connection import get_db

__all__ = ["get_db"]