from fastapi import FastAPI
from app.routes import transactions_router, category_router, summary_router

# Initialize the FastAPI application
app = FastAPI()

# Include the transaction and category routers under the /api prefix
app.include_router(transactions_router.router, prefix="/api")
app.include_router(category_router.router, prefix="/api")
app.include_router(summary_router.router, prefix="/api")

# Root endpoint (health check or welcome message)
@app.get("/")
def read_root():
    return {"message": "Olá, Chiclete! Your API is running 🚀"}