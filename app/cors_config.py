from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Você pode restringir isso depois para segurança
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )