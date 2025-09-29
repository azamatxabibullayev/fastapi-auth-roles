from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps import get_db, require_admin
from models.user import User
from schemas.user import UserResponse

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db), _: User = Depends(require_admin)):
    return db.query(User).all()
