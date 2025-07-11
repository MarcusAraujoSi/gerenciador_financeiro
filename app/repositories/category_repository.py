from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate

def save_category(db: Session, category_data: CategoryCreate):
    new_category = Category(**category_data.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db: Session):
    return db.query(Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()