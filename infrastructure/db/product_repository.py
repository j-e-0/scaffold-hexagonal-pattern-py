from sqlalchemy.orm import Session
from infrastructure.db.models.product import Product
from domain.schemas.product import ProductCreate
from domain.abstracts.product import ProductAbstract

class ProductRepository(ProductAbstract):
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: ProductCreate):
        db_product = Product(name=product.name, price=product.price)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()
