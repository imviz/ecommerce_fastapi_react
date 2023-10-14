from fastapi import FastAPI

from app.routers import user

app = FastAPI(title="social_media")

app.include_router(user.router, prefix="", tags=["user"])
