from pydantic import BaseModel
from datetime import datetime

class PaymentsRead(BaseModel):
  account_id: int
  transaction_id: str
  amount: float
  created_at: datetime
  
  class Config:
    from_attributes = True