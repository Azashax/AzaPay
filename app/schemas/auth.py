from pydantic import BaseModel, EmailStr

class TokenRequest(BaseModel):
    email: EmailStr
    password: str

class RefreshRequest(BaseModel):
    refresh_token: str
    
  
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str