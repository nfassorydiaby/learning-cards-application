from category import Category
from card_data import card_data
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status
from datetime import datetime, timedelta
from typing import List, Dict

class Card(BaseModel):
    id: Optional[int] = Field(default=None, example=0)  # Set default value to None
    category: Category = Category.FIRST
    question: str
    answer: str
    tag: Optional[str] = None

    def set_category(self):
        currentCategoryIndex = Category.__members__[self.category].value
        nextCategoryIndex = (currentCategoryIndex + 1) % len(Category)
        nextCategory = list(Category)[nextCategoryIndex]
        self.category = nextCategory