from sqlalchemy import Column, Integer, String, Enum
from db.session import Base
import enum


class RoleEnum(str, enum.Enum):
    client = "client"
    ishchi = "ishchi"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(Enum(RoleEnum), default=RoleEnum.client, nullable=False)
