from pydantic import BaseModel
from app.models.category import PocketTypeEnum
from typing import Optional

class CategoryBase(BaseModel):
    """Shared properties between create and return."""
    name: str
    pocket_type: Optional[PocketTypeEnum] = None

class CategoryCreate(CategoryBase):
    """Schema for creating a new category."""
    pass

class CategoryOut(CategoryBase):
    """Schema for returning a category with its ID."""
    id: int
    
    class Config:
        orm_mode = True