from sqlalchemy.orm import Session
from infrastructure.db.models.user import User
from domain.schemas.user import UserCreate
from domain.abstracts.user import UserAbstract

class UserRepository(UserAbstract):
    def __init__(self, db: Session):
        self.db = db
        
    def create_user(self, user: UserCreate):
        db_user = User(username=user.username, email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()
