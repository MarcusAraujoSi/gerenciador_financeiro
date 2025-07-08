from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.repositories.transaction_repository import save_transaction, get_all_transactions
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.models.transaction import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# POST: Create a transaction
@router.post("/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    try:
        return save_transaction(db, transaction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET: Get all transactions
@router.get("/", response_model=list[TransactionResponse])
def read_transactions(db: Session = Depends(get_db)):
    try:
        return get_all_transactions(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET: Get transaction by ID
@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction