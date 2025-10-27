from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from models.user import RoleEnum

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: Optional[RoleEnum] = RoleEnum.client

class UserRead(UserBase):
    id: int
    role: RoleEnum
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    role: Optional[RoleEnum] = None
    is_active: Optional[bool] = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: Optional[str] = None
