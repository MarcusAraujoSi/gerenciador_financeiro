from pydantic import BaseModel

class YearOut(BaseModel):
    year: int

class MonthSummaryOut(BaseModel):
    month: int
    balance: float