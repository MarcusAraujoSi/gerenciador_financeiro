from sqlalchemy.orm import Session
from sqlalchemy import extract, func, case
from app.models.transaction import Transaction

def get_available_years(db: Session) -> list[int]:
    years = (
        db.query(extract('year', Transaction.date).label("year"))
        .distinct()
        .order_by(extract('year', Transaction.date).label("year").desc())
        .all()
    )
    return [int(y.year) for y in years]

def get_months_summary_by_year(year: int, db: Session):
    results = (
        db.query(
            extract('month', Transaction.date).label("month"),
            func.sum(
                case(
                    (Transaction.type == "income", Transaction.amount),
                    else_=-Transaction.amount
                )
            ).label("balance")
        )
        .filter(extract('year', Transaction.date) == year)
        .group_by(extract('month', Transaction.date))
        .order_by(extract('month', Transaction.date))
        .all()
    )

    return [{"month": month, "balance": float(balance)} for month, balance in results]