from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.repositories.summary_repository import get_available_years, get_months_summary_by_year
from app.schemas.summary import YearOut, MonthSummaryOut

router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)

@router.get("/years", response_model=List[YearOut])
def read_available_years(db: Session = Depends(get_db)):
    try:
        years = get_available_years(db)
        return [{"year": y} for y in years]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{year}/months", response_model=List[MonthSummaryOut])
def read_months_summary(year: int, db: Session = Depends(get_db)):
    try:
        return get_months_summary_by_year(year, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))