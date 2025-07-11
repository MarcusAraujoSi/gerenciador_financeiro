# 💸 Gerenciador Financeiro

Este projeto é uma API de back-end construída com FastAPI para gerenciar finanças pessoais. O objetivo é permitir o controle de transações, categorias, investimentos e dívidas, com uma estrutura de código organizada em múltiplas camadas.

---

## 📁 Estrutura do Projeto

```
gerenciador_financeiro_back/
│
├── app/                     # Código principal da aplicação
│   ├── controllers/         # Regras de negócio (ex: transaction_controller.py)
│   ├── models/              # Modelos SQLAlchemy (ex: transaction.py, category.py)
│   ├── repositories/        # Acesso ao banco de dados e queries
│   ├── routes/              # Definição das rotas da API
│   ├── schemas/             # Modelos Pydantic para validação de entrada e saída
│   ├── database/            # Configuração da conexão com o banco de dados
│   ├── config/              # Configuração de CORS e variáveis de ambiente
│   └── main.py              # Ponto de entrada da aplicação
│
└── README.md                # Este arquivo
```

---

## 🚀 Como Rodar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/gerenciador_financeiro_back.git
cd gerenciador_financeiro_back
```

2. **Crie um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Rode o servidor de desenvolvimento:**

```bash
uvicorn app.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs) para ver a documentação automática (Swagger).

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **SQLite (para desenvolvimento local)**

---

## ✨ Funcionalidades

- Cadastro de categorias (com suporte a "investimento" e "dívida")
- Cadastro de transações (income/expense)
- Cadastro de pockets (caixinhas de dívida ou investimento)
- Suporte a API RESTful com rotas organizadas
- Separação em camadas (controller, routes, repositories, schemas, models)

---

## 🔒 Segurança e Produção

O projeto está preparado para rodar em ambiente de desenvolvimento. Para uso em produção, é recomendado:

- Configurar HTTPS com Nginx, Caddy ou outro servidor
- Utilizar variáveis de ambiente para senhas e caminhos
- Implementar autenticação e autorização de usuários

---

## 📌 Observações Finais

Este projeto faz parte de um estudo pessoal do desenvolvedor. A estrutura foi pensada para ser clara, didática e com boas práticas de organização, servindo de base para projetos futuros.

---

Desenvolvido com 💙 por Chiclete

