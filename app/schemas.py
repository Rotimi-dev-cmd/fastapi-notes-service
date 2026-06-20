from datetime import datetime
from pydantic import BaseModel, ConfigDict


class NoteBase(BaseModel):
    title: str
    body: str = ""
    pinned: bool = False


class NoteCreate(NoteBase):
    pass


class NoteUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    pinned: bool | None = None


class NoteOut(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
