from sqlalchemy.orm import Session
from app.schemas.pocket import PocketCreate, PocketOut
from app.repositories import pocket_repository


def create_pocket_controller(db: Session, pocket_data: PocketCreate) -> PocketOut:
    return pocket_repository.create_pocket(db, pocket_data)


def list_pockets_controller(db: Session) -> list[PocketOut]:
    return pocket_repository.get_all_pockets(db)