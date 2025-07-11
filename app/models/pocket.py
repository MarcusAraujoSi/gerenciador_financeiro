from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Enum, Float
from app.database.connection import Base
from app.models.category import PocketTypeEnum

class Pocket(Base):
    __tablename__ = "pockets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    pocket_type: Mapped[PocketTypeEnum] = mapped_column(Enum(PocketTypeEnum), nullable=False)
    initial_amount: Mapped[float] = mapped_column(Float, default=0.0)