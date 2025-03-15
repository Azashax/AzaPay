import hashlib
from app.core.config import settings

def generate_signature(account_id: int, amount: float, transaction_id: str, user_id: int) -> str:
    """Генерация подписи SHA256 по требованиям ТЗ"""
    secret_key = settings.SECRET_KEY
    raw_string = f"{account_id}{amount}{transaction_id}{user_id}{secret_key}"
    return hashlib.sha256(raw_string.encode()).hexdigest()
