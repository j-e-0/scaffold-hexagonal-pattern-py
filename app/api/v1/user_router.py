from fastapi import APIRouter
from .user_controller import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
