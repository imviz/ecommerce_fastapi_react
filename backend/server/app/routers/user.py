import logging

from fastapi import APIRouter

from app.schema.user import UserCreate

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/")
async def root(data: UserCreate):
    return "social media"
