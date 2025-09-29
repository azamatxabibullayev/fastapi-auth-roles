from pydantic import BaseModel, EmailStr
from enum import Enum


class RoleEnum(str, Enum):
    client = "client"
    ishchi = "ishchi"
    admin = "admin"


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None
    role: RoleEnum

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
