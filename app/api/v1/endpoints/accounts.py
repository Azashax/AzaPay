from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.models.account import Account
from app.models.user import User
from app.services.auth import get_current_user
from app.schemas.account import AccountResponse
from typing import List

router = APIRouter()

@router.get("/me", response_model=List[AccountResponse])
async def get_user_accounts(
    current_user: User = Depends(get_current_user), 
    db: AsyncSession = Depends(get_db)
):
    """Возвращает список счетов и балансов пользователя"""

    # ✅ Асинхронный запрос на получение счетов пользователя
    result = await db.execute(select(Account).where(Account.user_id == current_user.id))
    accounts = result.scalars().all()

    return [
        AccountResponse(
            id=acc.id, 
            user_id=acc.user_id,  # ✅ Добавляем `user_id`
            balance=acc.balance,  
            created_at=acc.created_at
        ) 
        for acc in accounts
    ]

