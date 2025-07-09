from sqlalchemy.orm import Session
from sqlalchemy import extract
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

def save_transaction(db: Session, transaction_data: TransactionCreate):
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

def get_all_transactions(db: Session):
    return db.query(Transaction).all()

def get_transactions_by_month(year: int, month: int, db: Session):
    return (
        db.query(Transaction)
        .filter(extract("year", Transaction.date) == year)
        .filter(extract("month", Transaction.date) == month)
        .all()
    )