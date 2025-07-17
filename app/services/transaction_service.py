from sqlalchemy.orm import Session
from app.models import Transaction, TransactionPocket
from app.repositories import transaction_repository, transaction_pocket_repository
from app.schemas import TransactionCreate, TransactionOut

def create_transaction_with_pockets(data: TransactionCreate, db: Session) -> TransactionOut:
    # Create the transaction
    transaction = transaction_repository.save_transaction(db, data)

    # Link to pockets only (no value update)
    if data.pocket_ids:
        for pocket_id in data.pocket_ids:
            transaction_pocket_repository.create_transaction_pocket(
                db,
                TransactionPocket(transaction_id=transaction.id, pocket_id=pocket_id)
            )

    return TransactionOut(
        id=transaction.id,
        date=transaction.date,
        category_id=transaction.category_id,
        description=transaction.description,
        amount=transaction.amount,
        type=transaction.type,
        pocket_ids=data.pocket_ids or []
    )