from fastapi import APIRouter
from .product_controller import router as product_router

router = APIRouter()
router.include_router(product_router, prefix="/products", tags=["products"])
