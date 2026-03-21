from typing import Any
from pydantic import BaseModel, HttpUrl


# --- API response models ---

class CodaDoc(BaseModel):
    id: str
    name: str
    browserLink: HttpUrl


class CodaPage(BaseModel):
    id: str
    name: str


class CodaCell(BaseModel):
    column: str
    value: Any


class CodaRow(BaseModel):
    id: str
    name: str | None = None
    values: dict[str, Any] = {}


# --- Tool input models ---

class UpsertRowInput(BaseModel):
    doc_id: str
    table_id: str
    cells: list[CodaCell]
    key_columns: list[str] = []
