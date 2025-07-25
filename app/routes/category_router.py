from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas import CategoryCreate, CategoryOut
from app.controllers.category_controller import (
    create_category,
    get_all,
    get_by_id,
    update_category  # 🔹 adicionada a função de update
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=CategoryOut, status_code=201)
def create_category_route(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(category, db)

@router.get("/", response_model=List[CategoryOut])
def get_all_categories_route(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{category_id}", response_model=CategoryOut)
def get_category_by_id_route(category_id: int, db: Session = Depends(get_db)):
    return get_by_id(category_id, db)

@router.put("/{category_id}", response_model=CategoryOut)
def update_category_route(category_id: int, category_data: CategoryCreate, db: Session = Depends(get_db)):
    return update_category(category_id, category_data, db)