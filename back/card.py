from category import Category
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from cardId import CardId


class Card(BaseModel):
    id: Optional[UUID] = Field(default_factory=CardId.generate)
    category: Optional[Category] = Category.FIRST
    question: str
    answer: str
    tag: Optional[str] = None
