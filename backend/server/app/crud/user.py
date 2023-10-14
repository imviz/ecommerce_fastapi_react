from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models
from app.crud.base import CRUDBase
from app.schema.user import UserCreate


class CRUDUser(CRUDBase[models.User, UserCreate, UserCreate]):
    def get_by_email(self, db_session: Session, email: str):
        user = (
            db_session.query(models.User)
            .filter(func.lower(models.User.email) == email.lower())
            .first()
        )
        return user


user = CRUDUser(models.User)
