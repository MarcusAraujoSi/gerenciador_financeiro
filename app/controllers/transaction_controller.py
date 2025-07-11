from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.transaction import TransactionCreate
from app.models.transaction import Transaction
from app.repositories.transaction_repository import (
    save_transaction,
    get_all_transactions,
    get_transactions_by_month
)

def create_transaction(transaction_data: TransactionCreate, db: Session) -> Transaction:
    try:
        return save_transaction(db, transaction_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while creating transaction: {str(e)}")

def get_all(db: Session):
    try:
        return get_all_transactions(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching transactions: {str(e)}")

def get_by_month(year: int, month: int, db: Session):
    try:
        return get_transactions_by_month(year, month, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching monthly transactions: {str(e)}")

def get_by_id(transaction_id: int, db: Session):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
