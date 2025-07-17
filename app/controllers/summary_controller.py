from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.summary_repository import (
    get_available_years,
    get_months_summary_by_year
)
from app.schemas.summary import YearOut, MonthSummaryOut


def fetch_available_years(db: Session) -> list[YearOut]:
    try:
        years = get_available_years(db)
        return [YearOut(year=y) for y in years]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching years: {str(e)}")


def fetch_months_summary(year: int, db: Session) -> list[MonthSummaryOut]:
    try:
        summaries = get_months_summary_by_year(year, db)
        return [MonthSummaryOut.model_validate(s, from_attributes=True) for s in summaries]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching summary for year {year}: {str(e)}")