from sqlalchemy import Column, Integer, String, Float, Date
from app.database.connection import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    category_id = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
