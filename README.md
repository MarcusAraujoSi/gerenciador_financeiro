# 💸 Financial Manager

This project is a back-end API built with FastAPI to manage personal finances. The goal is to provide control over transactions, categories, investments, and debts, with an organized multi-layer code structure.

---

## 📁 Project Structure

```
gerenciador_financeiro_back/
│
├── app/                     # Main application code
│   ├── controllers/         # Business logic (e.g., transaction_controller.py)
│   ├── models/              # SQLAlchemy models (e.g., transaction.py, category.py)
│   ├── repositories/        # Database access and queries
│   ├── routes/              # API route definitions
│   ├── schemas/             # Pydantic models for input and output validation
│   ├── database/            # Database connection configuration
│   ├── config/              # CORS and environment variables configuration
│   └── main.py              # Application entry point
│
└── README.md                # This file
```

---

## 🚀 How to Run the Project

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/gerenciador_financeiro_back.git
cd gerenciador_financeiro_back
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the development server:**

```bash
uvicorn app.main:app --reload
```

Access: [http://localhost:8000/docs](http://localhost:8000/docs) to see the automatic documentation (Swagger).

---

## 🛠️ Technologies Used

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **SQLite (for local development)**

---

## ✨ Features

- Category registration (supporting "investment" and "debt")
- Transaction registration (income/expense)
- Pocket registration (investment or debt boxes)
- RESTful API support with organized routes
- Layer separation (controller, routes, repositories, schemas, models)

---

## 🔒 Security and Production

The project is prepared to run in a development environment. For production use, it is recommended to:

- Configure HTTPS with Nginx, Caddy, or another server
- Use environment variables for passwords and paths
- Implement user authentication and authorization

---

## 📌 Final Notes

This project is part of a personal study by the developer. The structure was designed to be clear, educational, and organized with good practices, serving as a foundation for future projects.

---

Developed with 💙 by Chiclete

