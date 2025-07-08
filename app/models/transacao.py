from pydantic import BaseModel
from datetime import date
from typing import Literal

class Transacao(BaseModel):
    data: date
    tipo: Literal['despesa', 'receita']
    categoria: str
    descricao: str
    valor: float
