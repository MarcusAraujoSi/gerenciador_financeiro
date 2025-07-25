from sqlalchemy.orm import Session
from app.schemas import PocketOut
from app.repositories import pocket_repository, transaction_repository

def get_all_with_balance(db: Session) -> list[PocketOut]:
    pockets = pocket_repository.get_all_pockets(db)
    result = []

    for p in pockets:
        transactions = transaction_repository.get_transactions_by_pocket(db, p.id)

        total = p.initial_amount or 0.0
        for tx in transactions:
            is_positive = (
                (p.pocket_type == "investment" and tx.type == "expense") or
                (p.pocket_type == "debt" and tx.type == "income")
            )
            total += tx.amount if is_positive else -tx.amount

        pocket_out = PocketOut.model_validate(p, from_attributes=True)
        pocket_out.final_balance = total

        result.append(pocket_out)

    return result