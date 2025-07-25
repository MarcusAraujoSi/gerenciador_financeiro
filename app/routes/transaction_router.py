from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas import TransactionCreate, TransactionOut, TransactionUpdate
from app.controllers import transaction_controller

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# POST: Create a transaction
@router.post("/", response_model=TransactionOut, status_code=201)
def create_transaction_route(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return transaction_controller.create_transaction(transaction, db)

# GET: Get all transactions
@router.get("/", response_model=List[TransactionOut])
def get_all_transactions_route(db: Session = Depends(get_db)):
    return transaction_controller.get_all(db)

# GET: Get transactions by month
@router.get("/by-month", response_model=List[TransactionOut])
def get_transactions_by_month_route(
    year: int = Query(..., ge=1900, le=2100),
    month: int = Query(..., ge=1, le=12),
    db: Session = Depends(get_db)
):
    return transaction_controller.get_by_month(year, month, db)

# GET: Get transaction by ID
@router.get("/{transaction_id}", response_model=TransactionOut)
def get_transaction_by_id_route(transaction_id: int, db: Session = Depends(get_db)):
    return transaction_controller.get_by_id(transaction_id, db)

# GET: Get pocket IDs by transaction
@router.get("/{transaction_id}/pockets", response_model=List[int])
def get_pocket_ids_by_transaction_route(transaction_id: int, db: Session = Depends(get_db)):
    """
    Get all pocket IDs linked to a specific transaction.

    - **transaction_id**: ID of the transaction to inspect
    - Returns a list of pocket IDs linked to the transaction
    """
    return transaction_controller.get_pocket_ids(transaction_id, db)

# PUT: Update transaction by ID
@router.put("/{transaction_id}", response_model=TransactionOut)
def update_transaction_route(transaction_id: int, transaction_data: TransactionUpdate, db: Session = Depends(get_db)):
    return transaction_controller.update_transaction(transaction_id, transaction_data, db)