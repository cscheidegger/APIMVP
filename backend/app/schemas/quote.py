from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.models.quote import QuoteStatus

class QuoteBase(BaseModel):
    description: Optional[str] = None

class QuoteCreate(QuoteBase):
    pass

class QuoteUpdate(BaseModel):
    status: Optional[QuoteStatus] = None
    estimated_price: Optional[float] = None

class Quote(QuoteBase):
    id: int
    user_id: Optional[int] = None
    status: QuoteStatus
    estimated_price: Optional[float] = None
    created_at: datetime

    class Config:
        orm_mode = True
