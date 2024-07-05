from domain.abstracts.user import UserAbstract
from domain.schemas.user import UserCreate, UserRead

class UserService:
    def __init__(self, user_repository: UserAbstract):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate):
        return self.user_repository.create_user(user)

    def get_user(self, user_id: int):
        return self.user_repository.get_user(user_id)
