from pydantic import BaseModel
from datetime import datetime

class AccountBase(BaseModel):
    user_id: int
    balance: float


class AccountResponse(AccountBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
