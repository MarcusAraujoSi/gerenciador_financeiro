from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.summary import YearOut, MonthSummaryOut
from app.controllers.summary_controller import (
    fetch_available_years,
    fetch_months_summary
)

router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)

@router.get("/years", response_model=List[YearOut])
def route_get_years(db: Session = Depends(get_db)):
    return fetch_available_years(db)

@router.get("/{year}/months", response_model=List[MonthSummaryOut])
def route_get_months_summary(year: int, db: Session = Depends(get_db)):
    return fetch_months_summary(year, db)