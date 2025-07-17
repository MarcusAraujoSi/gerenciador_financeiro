from sqlalchemy.orm import Session
from app.schemas import PocketCreate, PocketOut, TransactionOut
from app.repositories import pocket_repository, transaction_repository


def create_pocket_controller(db: Session, pocket_data: PocketCreate) -> PocketOut:
    pocket = pocket_repository.create_pocket(db, pocket_data)
    return PocketOut.model_validate(pocket, from_attributes=True)


def list_pockets_controller(db: Session) -> list[PocketOut]:
    pockets = pocket_repository.get_all_pockets(db)
    return [PocketOut.model_validate(p, from_attributes=True) for p in pockets]


def get_transactions_by_pocket(db: Session, pocket_id: int) -> list[TransactionOut]:
    transactions = transaction_repository.get_transactions_by_pocket(db, pocket_id)
    return [TransactionOut.model_validate(t, from_attributes=True) for t in transactions]