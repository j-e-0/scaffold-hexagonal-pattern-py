from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.services.user_service import UserService
from infrastructure.db.user_repository import UserRepository
from infrastructure.db.database import get_db
from domain.schemas.user import UserCreate, UserRead

router = APIRouter()

def get_service(db):
    return UserService(UserRepository(db))

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = get_service(db)
    db_user = user_service.create_user(user)
    return db_user

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service = get_service(db)
    db_user = user_service.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
