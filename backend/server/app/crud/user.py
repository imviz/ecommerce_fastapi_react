from app import models
from app.crud.base import CRUDBase
from app.schema.user import UserCreate


class CRUDUser(CRUDBase[models.User, UserCreate, UserCreate]):
    pass


user = CRUDBase(models.User)
