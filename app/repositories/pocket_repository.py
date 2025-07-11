from sqlalchemy.orm import Session
from app.models.pocket import Pocket
from app.schemas.pocket import PocketCreate


def create_pocket(db: Session, pocket_data: PocketCreate) -> Pocket:
    new_pocket = Pocket(**pocket_data.model_dump())
    db.add(new_pocket)
    db.commit()
    db.refresh(new_pocket)
    return new_pocket


def get_all_pockets(db: Session) -> list[Pocket]:
    return db.query(Pocket).all()