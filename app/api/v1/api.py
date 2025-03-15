from fastapi import APIRouter
from app.api.v1.endpoints import users, admin, accounts, auth, webhook, payment

api_v1_router = APIRouter(prefix="/v1")

# Подключаем маршруты
api_v1_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_v1_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
api_v1_router.include_router(webhook.router, prefix="/webhook", tags=["Webhook"])
api_v1_router.include_router(payment.router, prefix="/payment", tags=["Payment"])
api_v1_router.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
api_v1_router.include_router(users.router, prefix="/users", tags=["Users"])

