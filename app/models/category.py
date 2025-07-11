from sqlalchemy import String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base
import enum

class PocketTypeEnum(str, enum.Enum):
    investment = "investment"
    debt = "debt"

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    pocket_type: Mapped[PocketTypeEnum | None] = mapped_column(Enum(PocketTypeEnum), nullable=True)