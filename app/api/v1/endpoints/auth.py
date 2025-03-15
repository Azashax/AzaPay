from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from app.services.auth import create_access_token, create_refresh_token, verify_token
from app.core.config import settings
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.auth import TokenRequest, RefreshRequest, TokenResponse
from sqlalchemy.future import select
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/token", response_model=TokenResponse)
async def login_for_access_token(
    data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    print("A")
    """Аутентификация пользователя и выдача токенов"""
    result = await db.execute(select(User).where(User.email == data.username))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=403, detail="Invalid credentials")

    if not user or not user.verify_password(data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.email})
    refresh_token = create_refresh_token({"sub": user.email})

    return TokenResponse(access_token=access_token, refresh_token=refresh_token, token_type="bearer")  # ✅ Теперь возвращаем `TokenResponse`


@router.post("/refresh")
async def refresh_access_token(data: RefreshRequest):
    """Обновление access токена по refresh токену"""
    payload = verify_token(data.refresh_token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    new_access_token = create_access_token({"sub": payload["sub"]})
    return {"access_token": new_access_token, "token_type": "bearer"}
