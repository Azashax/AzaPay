from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.models.account import Account
from app.models.payment import Payment
from app.schemas.webhook import WebhookPaymentRequest
from app.services.payment import generate_signature

router = APIRouter()

@router.post("/")
async def process_payment_webhook(data: WebhookPaymentRequest, db: AsyncSession = Depends(get_db)):
    """Обрабатывает платежный вебхук, проверяет подпись и обновляет баланс"""

    # ✅ Проверяем корректность подписи
    expected_signature = generate_signature(data.account_id, data.amount, data.transaction_id, data.user_id)
    print(expected_signature)
    if expected_signature != data.signature:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid signature")

    # ✅ Проверяем, была ли уже обработана эта транзакция
    existing_payment = await db.execute(select(Payment).where(Payment.transaction_id == data.transaction_id))
    if existing_payment.scalars().first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Transaction already processed")

    # ✅ Проверяем существование счёта
    account_query = await db.execute(select(Account).where(Account.id == data.account_id))
    account = account_query.scalars().first()

    # ✅ Если счёта нет, создаём новый
    if not account:
        account = Account(id=data.account_id, user_id=data.user_id, balance=0.0)
        db.add(account)
        await db.commit()

    # ✅ Создаём запись в истории платежей
    payment = Payment(
        transaction_id=data.transaction_id,
        user_id=data.user_id,
        account_id=data.account_id,
        amount=data.amount
    )
    db.add(payment)

    # ✅ Обновляем баланс счёта
    account.balance += float(data.amount)
    await db.commit()

    return {"status": "success", "message": "Payment processed"}
