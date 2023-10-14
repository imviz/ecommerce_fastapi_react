from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    phone_number: int
    name: str
    password: str
    is_admin: bool = False
    is_active: bool = False
