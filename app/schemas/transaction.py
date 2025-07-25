import datetime
from typing import Literal, Optional, List
from pydantic import BaseModel

class TransactionBase(BaseModel):
    date: datetime.date
    category_id: int
    description: str
    amount: float

class TransactionCreate(TransactionBase):
    type: Literal["income", "expense"]
    pocket_ids: Optional[List[int]] = None

class TransactionUpdate(BaseModel):
    description: Optional[str] = None
    type: Optional[Literal["income", "expense"]] = None
    amount: Optional[float] = None
    category_id: Optional[int] = None
    date: Optional[datetime.date] = None
    pocket_ids: Optional[List[int]] = None

class TransactionOut(TransactionBase):
    id: int
    type: str
    pocket_ids: Optional[List[int]] = []