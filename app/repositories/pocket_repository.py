from sqlalchemy.orm import Session
from app.models import Pocket, Transaction, TransactionPocket
from app.schemas.pocket import PocketCreate


def create_pocket(db: Session, pocket_data: PocketCreate) -> Pocket:
    new_pocket = Pocket(**pocket_data.model_dump())
    db.add(new_pocket)
    db.commit()
    db.refresh(new_pocket)
    return new_pocket

def get_all_pockets(db: Session) -> list[Pocket]:
    return db.query(Pocket).all()

def get_pocket_by_id(db: Session, pocket_id: int) -> Pocket | None:
    return db.query(Pocket).filter(Pocket.id == pocket_id).first()
