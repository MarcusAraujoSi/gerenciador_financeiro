from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import PocketCreate, PocketOut, TransactionOut
from app.repositories import pocket_repository, transaction_repository
from app.services import pocket_service  # 🔹 importa o service

def create_pocket_controller(db: Session, pocket_data: PocketCreate) -> PocketOut:
    pocket = pocket_repository.create_pocket(db, pocket_data)
    return PocketOut.model_validate(pocket, from_attributes=True)

def list_pockets_controller(db: Session) -> list[PocketOut]:
    return pocket_service.get_all_with_balance(db)

def get_transactions_by_pocket(db: Session, pocket_id: int) -> list[TransactionOut]:
    transactions = transaction_repository.get_transactions_by_pocket(db, pocket_id)
    return [TransactionOut.model_validate(t, from_attributes=True) for t in transactions]

def update_pocket_controller(db: Session, pocket_id: int, pocket_data: PocketCreate) -> PocketOut:
    pocket = pocket_repository.update_pocket_by_id(db, pocket_id, pocket_data)
    if not pocket:
        raise HTTPException(status_code=404, detail="Pocket not found")
    return PocketOut.model_validate(pocket, from_attributes=True)