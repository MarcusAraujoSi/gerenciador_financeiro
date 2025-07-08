from sqlalchemy import Column, Integer, String
from app.database.connection import Base  # Isso é a base herdada para criar as tabelas

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)