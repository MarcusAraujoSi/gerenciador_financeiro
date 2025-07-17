from sqlalchemy import Column, Integer, ForeignKey
from app.database.connection import Base

class TransactionPocket(Base):
    __tablename__ = "transaction_pocket"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id", ondelete="CASCADE"), nullable=False)
    pocket_id = Column(Integer, ForeignKey("pockets.id", ondelete="CASCADE"), nullable=False)