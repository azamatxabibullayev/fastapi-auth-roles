import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import Enum as SAEnum
from sqlalchemy.sql import func
from db.base import Base

class RoleEnum(str, enum.Enum):
    client = "client"
    worker = "worker"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    role = Column(SAEnum(RoleEnum), nullable=False, default=RoleEnum.client)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
