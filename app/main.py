from fastapi import FastAPI

from . import models
from .database import engine
from .routers import notes

# Create tables on startup (use Alembic migrations in production).
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes Service", version="1.0.0")

app.include_router(notes.router)


@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok"}
