from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.services.product_service import ProductService
from infrastructure.db.product_repository import ProductRepository
from infrastructure.db.database import get_db
from domain.schemas.product import ProductCreate, ProductRead

router = APIRouter()

def get_service(db):
    return ProductService(ProductRepository(db))

@router.post("/", response_model=ProductRead)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product_service = get_service(db)
    db_product = product_service.create_product(product)
    return db_product

@router.get("/{product_id}", response_model=ProductRead)
def read_product(product_id: int,  db: Session = Depends(get_db)):
    product_service = get_service(db)
    db_product = product_service.get_product(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
