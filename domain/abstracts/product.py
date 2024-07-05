from abc import ABC, abstractmethod
from domain.schemas.product import ProductCreate

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: ProductCreate):
        pass
    
    @abstractmethod
    def get_product(self, product_id: int):
        pass
