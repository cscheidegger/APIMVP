from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Enum, ARRAY, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base

class QuoteStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Quote(Base):
    __tablename__ = "quotes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    description = Column(Text)
    files = Column(ARRAY(String))
    status = Column(Enum(QuoteStatus), default=QuoteStatus.pending)
    estimated_price = Column(Float, nullable=True)
    admin_notes = Column(Text, nullable=True)
    drive_url = Column(String, nullable=True)
    meta_info = Column(JSON, nullable=True)  # ✅ Corrigido aqui
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("User")
