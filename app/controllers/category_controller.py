from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate
from app.models.category import Category
from app.schemas import CategoryOut
from app.repositories.category_repository import (
    save_category,
    get_all_categories,
    get_category_by_id,
    update_category_by_id  # 🔹 função chamada do repositório
)

def create_category(category_data: CategoryCreate, db: Session) -> CategoryOut:
    try:
        category = save_category(db, category_data)
        return CategoryOut.model_validate(category, from_attributes=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while creating category: {str(e)}")

def get_all(db: Session) -> list[CategoryOut]:
    try:
        categories = get_all_categories(db)
        return [CategoryOut.model_validate(c, from_attributes=True) for c in categories]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching categories: {str(e)}")

def get_by_id(category_id: int, db: Session) -> CategoryOut:
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return CategoryOut.model_validate(category, from_attributes=True)

def update_category(category_id: int, category_data: CategoryCreate, db: Session) -> CategoryOut:
    category = update_category_by_id(db, category_id, category_data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return CategoryOut.model_validate(category, from_attributes=True)