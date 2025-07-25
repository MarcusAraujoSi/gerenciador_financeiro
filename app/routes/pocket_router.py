from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas import PocketCreate, PocketOut, TransactionOut
from app.controllers import pocket_controller
from typing import List

router = APIRouter(prefix="/pockets", tags=["Pockets"])


@router.post("/", response_model=PocketOut)
def create_pocket_route(pocket_data: PocketCreate, db: Session = Depends(get_db)):
    return pocket_controller.create_pocket_controller(db, pocket_data)


@router.get("/", response_model=List[PocketOut])
def list_pockets_route(db: Session = Depends(get_db)):
    return pocket_controller.list_pockets_controller(db)

@router.get("/{pocket_id}/transactions", response_model=List[TransactionOut])
def get_transactions_by_pocket_route(pocket_id: int, db: Session = Depends(get_db)):
    """
    Get all transactions associated with a given pocket.

    - **pocket_id**: ID of the pocket you want to inspect
    - Returns a list of transactions linked to this pocket via TransactionPocket
    """
    return pocket_controller.get_transactions_by_pocket(db, pocket_id)

@router.put("/{pocket_id}", response_model=PocketOut)
def update_pocket_route(pocket_id: int, pocket_data: PocketCreate, db: Session = Depends(get_db)):
    return pocket_controller.update_pocket_controller(db, pocket_id, pocket_data)