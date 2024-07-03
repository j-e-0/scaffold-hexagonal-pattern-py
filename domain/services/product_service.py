from sqlalchemy.orm import Session
from infrastructure.db.product_repository import ProductRepository
from schemas.product import ProductCreate, ProductRead

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def create_product(self, db: Session, product: ProductCreate):
        return self.product_repository.create_product(db, product)

    def get_product(self, db: Session, product_id: int):
        return self.product_repository.get_product(db, product_id)
