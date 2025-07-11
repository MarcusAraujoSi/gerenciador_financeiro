from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.summary_repository import (
    get_available_years,
    get_months_summary_by_year
)

def fetch_available_years(db: Session):
    try:
        years = get_available_years(db)
        return [{"year": y} for y in years]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching years: {str(e)}")

def fetch_months_summary(year: int, db: Session):
    try:
        return get_months_summary_by_year(year, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching summary for year {year}: {str(e)}")