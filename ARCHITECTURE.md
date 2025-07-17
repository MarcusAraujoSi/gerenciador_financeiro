
# 🧱 Project Architecture – Financial Manager

This project follows a layered architecture designed for clarity, modularity, and scalability. The goal is to keep each part of the system cleanly separated, easy to test, and easy to extend in the future.

---

## 📁 Folder Structure

```
app/
├── controllers/        # Orchestrates incoming requests and delegates to services
├── services/           # Business logic layer (complex operations, rule coordination)
├── repositories/       # Handles all communication with the database (using SQLAlchemy)
├── models/             # SQLAlchemy ORM models (database tables)
├── schemas/            # Pydantic schemas for input/output validation
├── routes/             # FastAPI route definitions (exposed endpoints)
├── database/           # Database connection and engine
├── config.py           # Application configuration (env, constants, etc)
```

---

## 🔄 Layer Responsibilities

### 🎮 Controller
- Entry point for requests
- Only responsible for orchestration
- **Does not contain business logic**
- Delegates complex flows to the `services` layer

### ⚙️ Service
- Contains **business rules** and process orchestration
- Can coordinate multiple repositories, validations, conditional flows, etc.
- Keeps logic **out of controllers and repositories**
- Optional for simple operations, **but recommended when logic grows**

### 🗃️ Repository
- Handles direct access to the database using SQLAlchemy ORM
- Contains basic CRUD operations
- **Does not contain business rules** or validations

### 🧱 Model
- Defines the shape of database tables using SQLAlchemy
- Includes relationships and constraints (e.g., `ForeignKey`, `CheckConstraint`, etc.)

### 📦 Schema
- Validates and documents incoming/outgoing data using Pydantic
- Keeps API contracts clear (e.g., `TransactionCreate`, `TransactionOut`)

### 🌐 Route
- Defines the public-facing endpoints using FastAPI
- Delegates logic to the controller

---

## 🧠 Example: Transaction Flow (with pockets)

### Creating a Transaction:

1. 📲 A request is received by a route: `POST /transactions`
2. 📥 The route calls: `create_transaction()` in `TransactionController`
3. 🧠 The controller delegates to: `create_transaction_with_pockets()` in `TransactionService`
4. 🗄️ The service:
   - Saves the transaction using `TransactionRepository`
   - Links it to multiple pockets via `TransactionPocketRepository`
5. 📤 A `TransactionOut` schema is returned to the client

---

## ✅ Architecture Rules

- ✅ All complex operations should go through the **services layer**
- ✅ Simple operations **may** access repositories directly, but:
  - Prefer services for consistency and scalability
- 🚫 No business logic inside controllers or repositories
- ✅ All external data is validated using **Pydantic schemas**
- ✅ All controller methods should raise `HTTPException` in case of errors

---

## 🧪 Testing & Future Growth

- The architecture was designed to support:
  - Unit tests on services and repositories
  - Route tests using FastAPI’s test client
  - Modular growth: new features fit naturally into the structure
- Future layers can be added:
  - `validators/` for rule validation
  - `utils/` for shared helpers
  - `middlewares/` for logging, authentication, etc.

---

## 📚 Conventions

- All class, file and variable names are in **English**
- All routes use **snake_case** and meaningful naming
- All transaction-pocket relationships are handled via a **many-to-many** join table (`transaction_pocket`)
