from sqlalchemy import String, Integer, Float, Date, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base

class Transaction(Base):
    __tablename__ = "transactions"
    __table_args__ = (
        CheckConstraint("type IN ('income', 'expense')", name="check_transaction_type"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
