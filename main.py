from fastapi import FastAPI
from app.routes import transacoes_router

app = FastAPI()

app.include_router(transacoes_router.router)