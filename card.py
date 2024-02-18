from category import Category
from card_data import card_data
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status
from datetime import datetime, timedelta
from typing import List, Dict

class Card(BaseModel):
    id: Optional[int] = None  
    category: Category
    question: str
    answer: str
    tag: Optional[str] = None