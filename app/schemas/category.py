from pydantic import BaseModel

class CategoryCreate(BaseModel):
    """Schema for creating a new category."""
    name: str

class CategoryOut(BaseModel):
    """Schema for returning a category with its ID."""
    id: int
    name: str

    class Config:
        orm_mode = True