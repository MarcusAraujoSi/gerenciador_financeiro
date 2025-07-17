from pydantic import BaseModel

class TransactionPocketBase(BaseModel):
    transaction_id: int
    pocket_id: int

class TransactionPocketCreate(TransactionPocketBase):
    pass

class TransactionPocketOut(TransactionPocketBase):
    id: int