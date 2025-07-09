from typing import List
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.repositories.transaction_repository import save_transaction, get_all_transactions, get_transactions_by_month
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.models.transaction import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# POST: Create a transaction
@router.post("/", response_model=TransactionOut)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    try:
        return save_transaction(db, transaction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET: Get all transactions
@router.get("/", response_model=List[TransactionOut])
def read_transactions(db: Session = Depends(get_db)):
    try:
        return get_all_transactions(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/by-month", response_model=List[TransactionOut])
def read_transactions_by_month(
    year: int = Query(..., ge=1900, le=2100),
    month: int = Query(..., ge=1, le=12),
    db: Session = Depends(get_db)
):
    try:
        transactions = get_transactions_by_month(year, month, db)
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET: Get transaction by ID
@router.get("/{transaction_id}", response_model=TransactionOut)
def read_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
