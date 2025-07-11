from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite connection URL
DATABASE_URL = "sqlite:///./database.db"

# SQLAlchemy base class for models
class Base(DeclarativeBase):
    pass

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create all tables based on models
def create_tables():
    from app.models import transaction, category, pocket  # Ensure all models are imported
    Base.metadata.create_all(bind=engine)