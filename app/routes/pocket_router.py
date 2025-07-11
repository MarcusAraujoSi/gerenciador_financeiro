from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.pocket import PocketCreate, PocketOut
from app.controllers import pocket_controller

router = APIRouter(prefix="/pockets", tags=["Pockets"])


@router.post("/", response_model=PocketOut)
def create_pocket(pocket_data: PocketCreate, db: Session = Depends(get_db)):
    return pocket_controller.create_pocket_controller(db, pocket_data)


@router.get("/", response_model=list[PocketOut])
def list_pockets(db: Session = Depends(get_db)):
    return pocket_controller.list_pockets_controller(db)