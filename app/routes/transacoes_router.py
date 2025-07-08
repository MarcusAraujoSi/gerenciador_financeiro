from fastapi import APIRouter
from app.models.transacao import Transacao

router = APIRouter()

# Rota para cadastrar uma nova transação
@router.post("/transacoes")
def criar_transacao(transacao: Transacao):
    return {"mensagem": "Transação recebida com sucesso!", "dados": transacao}
