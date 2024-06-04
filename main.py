from fastapi import FastAPI
from app.controllers.addition_controller import router as addition_router

app = FastAPI()

app.include_router(addition_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)