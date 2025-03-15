from sqlalchemy import Column, ForeignKey, Float, Integer, DateTime
from datetime import datetime
from app.core.database import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)
    
    payments = relationship("Payment", back_populates="account")
    user = relationship("User", back_populates="accounts")
    
from app.models.user import User
from app.models.payment import Payment