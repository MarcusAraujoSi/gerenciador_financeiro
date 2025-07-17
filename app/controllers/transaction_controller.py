from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import TransactionCreate, TransactionOut
from app.models import Transaction
from app.repositories import transaction_repository, transaction_pocket_repository
from app.services import transaction_service

def create_transaction(transaction_data: TransactionCreate, db: Session) -> TransactionOut:
    try:
        return transaction_service.create_transaction_with_pockets(transaction_data, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while creating transaction: {str(e)}")

def get_all(db: Session) -> list[TransactionOut]:
    try:
        transactions = transaction_repository.get_all_transactions(db)
        return [TransactionOut.model_validate(t, from_attributes=True) for t in transactions]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching transactions: {str(e)}")

def get_by_month(year: int, month: int, db: Session) -> list[TransactionOut]:
    try:
        transactions = transaction_repository.get_transactions_by_month(year, month, db)
        return [TransactionOut.model_validate(t, from_attributes=True) for t in transactions]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching monthly transactions: {str(e)}")

def get_by_id(transaction_id: int, db: Session) -> TransactionOut:
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return TransactionOut.model_validate(transaction, from_attributes=True)

def get_pocket_ids(transaction_id: int, db: Session) -> list[int]:
    try:
        return transaction_pocket_repository.get_pocket_ids_by_transaction(db, transaction_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching pocket IDs: {str(e)}")