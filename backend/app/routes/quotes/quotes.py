# backend/app/routes/quotes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.quote import Quote as QuoteModel
from app.schemas.quote import QuoteCreate, Quote, QuoteUpdate

router = APIRouter()

@router.post("/quotes/", response_model=Quote)
def create_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    db_quote = QuoteModel(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

@router.get("/quotes/", response_model=List[Quote])
def read_quotes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(QuoteModel).offset(skip).limit(limit).all()

@router.get("/quotes/{quote_id}", response_model=Quote)
def read_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = db.query(QuoteModel).filter(QuoteModel.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

@router.put("/quotes/{quote_id}", response_model=Quote)
def update_quote(quote_id: int, quote_update: QuoteUpdate, db: Session = Depends(get_db)):
    quote = db.query(QuoteModel).filter(QuoteModel.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    for key, value in quote_update.dict(exclude_unset=True).items():
        setattr(quote, key, value)
    db.commit()
    db.refresh(quote)
    return quote

@router.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = db.query(QuoteModel).filter(QuoteModel.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    db.delete(quote)
    db.commit()
    return {"detail": "Quote deleted"}
