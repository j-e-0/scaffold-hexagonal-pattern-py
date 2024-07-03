from sqlalchemy.orm import Session
from domain.models.product import Product
from schemas.product import ProductCreate

class ProductRepository:

    def create_product(self, db: Session, product: ProductCreate):
        db_product = Product(name=product.name, price=product.price)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def get_product(self, db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()
