from typing import Literal, Optional, List
from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    """Shared properties between create and return."""
    date: date
    category_id: int
    description: str
    amount: float

# Used when creating a new transaction
class TransactionCreate(TransactionBase):
    type: Literal["income", "expense"]
    pocket_ids: Optional[List[int]] = None 

# Used when returning transaction data via API
class TransactionOut(TransactionBase):
    id: int
    type: str
    pocket_ids: Optional[List[int]] = []  # Pockets linked to this transaction