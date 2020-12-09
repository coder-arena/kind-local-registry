from datetime import datetime
from typing import List, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel


class Entity(BaseModel):
    id: UUID = uuid4()
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class Item(Entity):
    name: str


class PaginatedItems(BaseModel):
    has_next: bool = False
    total: int = 0
    items: List[Item] = []


class User(Entity):
    name: str
    age: int
    gender: Literal['Male', 'Female'] = 'Male'
