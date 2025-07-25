from pydantic import BaseModel
from app.models.category import PocketTypeEnum
from typing import Optional

class CategoryBase(BaseModel):
    """Shared properties between create and return."""
    name: str

class CategoryCreate(CategoryBase):
    """Schema for creating a new category."""
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    """Schema for returning a category with its ID."""
    id: int