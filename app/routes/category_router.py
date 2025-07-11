from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.category import CategoryCreate, CategoryOut
from app.controllers.category_controller import (
    create_category,
    get_all,
    get_by_id
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=CategoryOut, status_code=201)
def route_create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(category, db)

@router.get("/", response_model=List[CategoryOut])
def route_get_all_categories(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{category_id}", response_model=CategoryOut)
def route_get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return get_by_id(category_id, db)