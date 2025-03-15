from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_v1_router
from app.core.config import settings
import uvicorn


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)

# Создаем API-роутер с общим `/api`
api_router = APIRouter(prefix="/api")
api_router.include_router(api_v1_router)
app.include_router(api_router)

# CORS настройки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Запуск Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=80, reload=True)
