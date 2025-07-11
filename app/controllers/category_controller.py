from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate
from app.models.category import Category
from app.repositories.category_repository import (
    save_category,
    get_all_categories,
    get_category_by_id
)

def create_category(category_data: CategoryCreate, db: Session) -> Category:
    try:
        return save_category(db, category_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while creating category: {str(e)}")

def get_all(db: Session):
    try:
        return get_all_categories(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching categories: {str(e)}")

def get_by_id(category_id: int, db: Session):
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category