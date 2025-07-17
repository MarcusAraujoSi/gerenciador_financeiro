from sqlalchemy.orm import Session
from sqlalchemy import extract
from app.models import Transaction, TransactionPocket
from app.schemas import TransactionCreate
from typing import List

def save_transaction(db: Session, transaction_data: TransactionCreate) -> Transaction:
    """Create and persist a new transaction."""
    new_transaction = Transaction(
        date=transaction_data.date,
        type=transaction_data.type,
        category_id=transaction_data.category_id,
        description=transaction_data.description,
        amount=transaction_data.amount
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

def get_all_transactions(db: Session) -> List[Transaction]:
    """Retrieve all transactions from the database."""
    return db.query(Transaction).all()

def get_transactions_by_month(year: int, month: int, db: Session) -> List[Transaction]:
    """Retrieve transactions filtered by year and month."""
    return (
        db.query(Transaction)
        .filter(extract("year", Transaction.date) == year)
        .filter(extract("month", Transaction.date) == month)
        .all()
    )

def get_transactions_by_ids(db: Session, transaction_ids: List[int]) -> List[Transaction]:
    """Retrieve multiple transactions by a list of IDs."""
    return db.query(Transaction).filter(Transaction.id.in_(transaction_ids)).all()

def get_transactions_by_pocket(db: Session, pocket_id: int) -> List[Transaction]:
    """Retrieve all transactions linked to a specific pocket."""
    return (
        db.query(Transaction)
        .join(TransactionPocket, Transaction.id == TransactionPocket.transaction_id)
        .filter(TransactionPocket.pocket_id == pocket_id)
        .all()
    )