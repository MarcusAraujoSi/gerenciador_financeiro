from fastapi import FastAPI
from app.routes import transactions_router, category_router, summary_router
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://192.168.68.106:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the transaction and category routers under the /api prefix
app.include_router(transactions_router.router, prefix="/api")
app.include_router(category_router.router, prefix="/api")
app.include_router(summary_router.router, prefix="/api")

# Root endpoint (health check or welcome message)
@app.get("/")
def read_root():
    return {"message": "Olá, Chiclete! Your API is running 🚀"}