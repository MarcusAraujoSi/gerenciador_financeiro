from typing import Literal, Optional
from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    """Shared properties between create and return."""
    date: date
    category_id: int
    description: str
    amount: float
    pocket_id: Optional[int] = None

# Used when creating a new transaction
class TransactionCreate(TransactionBase):
    type: Literal["income", "expense"]
    

# Used when returning transaction data via API
class TransactionOut(TransactionBase):
    id: int
    type: str
    
    class Config:
        orm_mode = True  # Allows returning SQLAlchemy models directly