import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.crud.user import user
from app.db.session import get_db
from app.schema.user import UserCreate

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/")
async def root(data: UserCreate, db: Session = Depends(get_db)):

    if user.get_by_email(db, data.email) is None:
        hashed_password = get_password_hash(data.password)
        data.password = hashed_password
        user.create(db, data)

    # if user.get()
    return data
