from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    phone_number: int
    name: str
    password: str
    is_admin: bool = False
    is_active: bool = False
