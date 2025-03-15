from pydantic import BaseModel, condecimal, constr

class WebhookPaymentRequest(BaseModel):
  account_id: int
  user_id: int
  transaction_id: str
  amount: condecimal(gt=0)
  signature: constr(min_length=64, max_length=64)
  
  