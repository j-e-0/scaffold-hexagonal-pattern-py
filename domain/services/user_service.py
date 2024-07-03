from sqlalchemy.orm import Session
from infrastructure.db.user_repository import UserRepository
from schemas.user import UserCreate, UserRead

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db: Session, user: UserCreate):
        return self.user_repository.create_user(db, user)

    def get_user(self, db: Session, user_id: int):
        return self.user_repository.get_user(db, user_id)
