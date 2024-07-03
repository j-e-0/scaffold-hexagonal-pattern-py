from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.services.product_service import ProductService
from infrastructure.db.product_repository import ProductRepository
from infrastructure.db.database import get_db
from schemas.product import ProductCreate, ProductRead

router = APIRouter()

product_service = ProductService(ProductRepository())

@router.post("/", response_model=ProductRead)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = product_service.create_product(db, product)
    return db_product

@router.get("/{product_id}", response_model=ProductRead)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
