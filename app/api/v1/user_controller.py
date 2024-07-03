from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.services.user_service import UserService
from infrastructure.db.user_repository import UserRepository
from infrastructure.db.database import get_db
from schemas.user import UserCreate, UserRead

router = APIRouter()

user_service = UserService(UserRepository())

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.create_user(db, user)
    return db_user

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
