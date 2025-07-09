from typing import Literal
from pydantic import BaseModel
from datetime import date

# Used when creating a new transaction
class TransactionCreate(BaseModel):
    date: date
    type: Literal["income", "expense"]
    category_id: int
    description: str
    amount: float

# Used when returning transaction data via API
class TransactionOut(BaseModel):
    id: int
    date: date
    type: str
    category_id: int
    description: str
    amount: float

    class Config:
        orm_mode = True  # Allows returning SQLAlchemy models directly