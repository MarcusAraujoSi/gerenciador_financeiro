# 🤝 Contributing Guidelines

Thanks for helping improve this project! Please follow the rules and structure below to keep the codebase clean and consistent.

---

## 🧭 Code Style

- Use `**model_dump()` when the schema and model have matching fields.
- If extra logic or transformations are needed, assign each field manually.
- Follow the `PascalCase` for class names and `snake_case` for file names and variables.
- Always comment new code blocks in English.

---

## 🗃 Folder Structure

- `models/` → Contains SQLAlchemy models only.
- `schemas/` → Pydantic classes (Base, Create, Out).
- `repositories/` → Direct database queries.
- `controllers/` → Business logic and validations.
- `routes/` → FastAPI routes.
- `config/` → CORS and settings.

---

## 🌱 Creating New Features

1. Create a new branch using a clear name (e.g., `feature/pockets`).
2. Implement the feature step by step, following layered architecture.
3. Use English in function, variable, and file names.
4. Write detailed commits explaining what was done.
5. If new models or fields are added, update the database and test it locally.

---

## ✅ Testing

- Always test routes via Swagger or front-end.
- Confirm that tables are created and new fields appear correctly.
- If using SQLite, open the database in a browser to confirm structure.

---

## 📝 Commit Messages

Use clear and descriptive messages:

```
feat: add pocket_id to transactions
fix: correct missing pocket_type in category creation
refactor: apply Base schema usage in transaction schemas
```

---

## 📄 README and CONTRIBUTING

Keep `README.md` and `CONTRIBUTING.md` updated as the project evolves. It helps both you and others understand the standards, architecture, and logic used.

