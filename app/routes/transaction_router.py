from typing import List
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.controllers.transaction_controller import (
    create_transaction,
    get_all,
    get_by_month,
    get_by_id
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# POST: Create a transaction
@router.post("/", response_model=TransactionOut)
def route_create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(transaction, db)

# GET: Get all transactions
@router.get("/", response_model=List[TransactionOut])
def route_get_all_transactions(db: Session = Depends(get_db)):
    return get_all(db)

# GET: Get transactions by month
@router.get("/by-month", response_model=List[TransactionOut])
def route_get_by_month(
    year: int = Query(..., ge=1900, le=2100),
    month: int = Query(..., ge=1, le=12),
    db: Session = Depends(get_db)
):
    return get_by_month(year, month, db)

# GET: Get transaction by ID
@router.get("/{transaction_id}", response_model=TransactionOut)
def route_get_by_id(transaction_id: int, db: Session = Depends(get_db)):
    return get_by_id(transaction_id, db)