from sqlalchemy.orm import Session
from app.models import TransactionPocket
from typing import List
from app.schemas import TransactionPocketCreate


def create_transaction_pocket(db: Session, data: TransactionPocketCreate) -> TransactionPocket:
    db_obj = TransactionPocket(
        transaction_id=data.transaction_id,
        pocket_id=data.pocket_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# Currently unused. May be useful if we need to edit or delete links manually.
# def get_links_by_transaction(db: Session, transaction_id: int) -> list[TransactionPocket]:
#     return db.query(TransactionPocket).filter(TransactionPocket.transaction_id == transaction_id).all()

# def get_links_by_pocket(db: Session, pocket_id: int) -> List[TransactionPocket]:
#     """
#     Return all TransactionPocket links for a given pocket.
#     Currently unused, but may be useful for future unlinking or auditing.
#     """
#     return db.query(TransactionPocket).filter(TransactionPocket.pocket_id == pocket_id).all()

def get_pocket_ids_by_transaction(db: Session, transaction_id: int) -> list[int]:
    result = (
        db.query(TransactionPocket.pocket_id)
        .filter(TransactionPocket.transaction_id == transaction_id)
        .all()
    )
    return [row.pocket_id for row in result]