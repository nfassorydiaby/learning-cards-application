from category import Category
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status
from datetime import datetime, timedelta
from typing import List, Dict
from uuid import UUID, uuid4
from cardId import CardId
from card_data import card_data  # Import card_data
from card_quizz import list_card_by_frequency

class Card(BaseModel):
    id: Optional[UUID] = Field(default_factory=CardId.generate)
    category: Category = Category.FIRST
    question: str
    answer: str
    tag: Optional[str] = None

    def addToList(self):
        list_card_by_frequency.append({"id": self.id, "remainingDays": 0})

    def setCategory(self):
        currentCategoryIndex = Category.__members__[self.category].value
        nextCategoryIndex = (currentCategoryIndex + 1) % len(Category)
        nextCategory = list(Category)[nextCategoryIndex]
        self.category = nextCategory

