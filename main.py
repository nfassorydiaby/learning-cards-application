from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status
from datetime import datetime, timedelta
from typing import List, Dict




app = FastAPI(
    title="Learning Cards Application",
    description="This API aim to provide feature to manage a graphical interface for Learning Cards Application.")

class Category(str, Enum):
    FIRST = "FIRST"
    SECOND = "SECOND"
    THIRD = "THIRD"
    FOURTH = "FOURTH"
    FIFTH = "FIFTH"
    SIXTH = "SIXTH"
    SEVENTH = "SEVENTH"
    DONE = "DONE"

class Card(BaseModel):
    id: Optional[int] = None  
    category: Category
    question: str
    answer: str
    tag: Optional[str] = None

card_data = [
    {
        "id": 1,
        "category": Category.FIRST.value,
        "question": "What is pair programming ?",
        "answer": "A practice to work in pair on same computer.",
        "tag": "Teamwork"
    },
    {
        "id": 2,
        "category": Category.SECOND.value,
        "question": "str",
        "answer": "str",
        "tag": "Teamwork"
    },
    {
        "id": 3,
        "category": Category.THIRD.value,
        "question": "str",
        "answer": "str",
        "tag": "Teamwork"
    },
]

@app.get("/cards/", tags=["Cards"])
async def read_cards():
    return card_data

@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED, tags=["Cards"])
async def create_card(card: Card):
    if card_data:
        max_id = max(item["id"] for item in card_data)
    else:
        max_id = 0
    card.id = max_id + 1 
    card_dict = card.dict() 
    card_data.append(card_dict) 
    return card

@app.get("/cards/quizz/")
async def get_quiz_cards():
    # Filtre et retourne uniquement les cartes de la catégorie FIRST
    today_cards: List[Dict] = [card for card in card_data if card["category"] == "FIRST"]
    return today_cards
