# FastAPI Notes Service

A small REST microservice for managing notes, built with **Python**, **FastAPI**,
**SQLAlchemy**, and **Pydantic**. Demonstrates clean separation between ORM models,
schemas, database session management, and routing.

## Features

- Full CRUD for notes
- SQLAlchemy ORM models with a SQLite backend (swap `DATABASE_URL` for Postgres)
- Pydantic v2 request/response validation
- Dependency-injected database sessions
- Auto-generated OpenAPI docs at `/docs`

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload    # http://localhost:8000
```

Interactive API docs: http://localhost:8000/docs

## Project structure

```
app/
├── main.py          # FastAPI app + router registration
├── database.py      # engine, session factory, Base
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas
└── routers/
    └── notes.py     # CRUD endpoints
```

## API

| Method | Route              | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/notes`           | List notes        |
| POST   | `/notes`           | Create a note     |
| GET    | `/notes/{id}`      | Get a note        |
| PUT    | `/notes/{id}`      | Update a note     |
| DELETE | `/notes/{id}`      | Delete a note     |

## License

MIT
