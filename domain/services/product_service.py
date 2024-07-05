from domain.abstracts.product import ProductAbstract
from domain.schemas.product import ProductCreate, ProductRead

class ProductService:
    def __init__(self, product_repository: ProductAbstract):
        self.product_repository = product_repository

    def create_product(self, product: ProductCreate):
        return self.product_repository.create_product(product)

    def get_product(self, product_id: int):
        return self.product_repository.get_product(product_id)