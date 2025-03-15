from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import load_only
from app.core.database import get_db
from app.models.payment import Payment
from app.models.user import User
from app.services.auth import get_current_user
from app.schemas.payments import PaymentsRead
from typing import List

router = APIRouter()

@router.get("/me", response_model=List[PaymentsRead])
async def get_user_payments(
    current_user: User = Depends(get_current_user), 
    db: AsyncSession = Depends(get_db)
):
    """Возвращает список платежей пользователя"""

    result = await db.execute(
        select(Payment)
        .where(Payment.user_id == current_user.id)
        .order_by(Payment.created_at.desc())  # Сортируем от новых к старым
        .options(load_only(Payment.id, Payment.account_id, Payment.transaction_id, Payment.amount, Payment.created_at))
    )

    payments = result.scalars().all()
    return [PaymentsRead.from_orm(payment) for payment in payments]

