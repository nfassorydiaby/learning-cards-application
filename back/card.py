from category import Category
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from card_quizz import list_card_by_frequency


class Card(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    category: Optional[Category] = Category.FIRST
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

    def manageCategory(self, cardResponse) -> str:
        if cardResponse:
            self.setCategory()
        else:
            self.category = Category.FIRST

        return self.category
