from pydantic import BaseModel

class SummaryBase(BaseModel):
    """Shared properties between create and return."""
    pass

class YearOut(SummaryBase):
    year: int

class MonthSummaryOut(SummaryBase):
    month: int
    balance: float