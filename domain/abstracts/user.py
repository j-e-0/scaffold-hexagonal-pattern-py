from abc import ABC, abstractmethod
from domain.schemas.user import UserCreate

class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, user: UserCreate):
        pass
    
    @abstractmethod
    def get_user(self, user_id: int):
        pass
    
    @abstractmethod
    def get_user_by_username(self, username: str):
        pass