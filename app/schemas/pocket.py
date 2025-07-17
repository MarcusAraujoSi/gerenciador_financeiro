from pydantic import BaseModel
from typing import Literal

class PocketBase(BaseModel):
    """Shared attributes between create and return schemas."""
    name: str
    pocket_type: Literal["investment", "debt"]
    initial_amount: float

class PocketCreate(PocketBase):
    """Schema used to create a new Pocket."""
    pass

class PocketOut(PocketBase):
    """Schema used to return a Pocket with its ID."""
    id: int