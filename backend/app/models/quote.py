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
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    description = Column(Text, nullable=False)
    files = Column(ARRAY(String), nullable=True)
    status = Column(Enum(QuoteStatus), default=QuoteStatus.pending, nullable=False)
    estimated_price = Column(Float, nullable=True)
    admin_notes = Column(Text, nullable=True)
    drive_url = Column(String, nullable=True)
    meta_info = Column(JSON, nullable=True)  # Renomeado para evitar conflito com 'metadata'
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship
    user = relationship("User", back_populates="quotes")
