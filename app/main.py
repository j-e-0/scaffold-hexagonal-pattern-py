from fastapi import FastAPI
from app.api.v1.user_router import router as user_router
from app.api.v1.product_router import router as product_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
