from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import transaction_router, category_router, summary_router, pocket_router
from app.cors_config import configure_cors
from app.database.connection import create_tables

# Initialize the FastAPI application
app = FastAPI()

# Configure CORS settings
configure_cors(app)

# Automatically create all database tables at startup
create_tables()

# Register all API routers with the /api prefix
app.include_router(transaction_router.router, prefix="/api")
app.include_router(category_router.router, prefix="/api")
app.include_router(summary_router.router, prefix="/api")
app.include_router(pocket_router.router, prefix="/api")

@app.get("/", tags=["Status"])
def read_root():
    return {"message": "Olá, Chiclete! Your API is running 🚀"}