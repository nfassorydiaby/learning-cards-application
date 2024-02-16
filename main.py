from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status



app = FastAPI()


class Card(BaseModel):
    id: Optional[int] = None  
    question: str
    answer: str
    tag: Optional[str] = None

card_data = [
    {
        "id": 1,
        "question": "What is pair programming ?",
        "answer": "A practice to work in pair on same computer.",
        "tag": "Teamwork"
    },
    {
        "id": 2,
        "question": "str",
        "answer": "str",
        "tag": "Teamwork"
    },
    {
        "id": 3,
        "question": "str",
        "answer": "str",
        "tag": "Teamwork"
    },
]

@app.get("/cards/")
async def read_cards():
    return card_data

@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED)
async def create_card(card: Card):
    if card_data:
        max_id = max(item["id"] for item in card_data)
    else:
        max_id = 0
    card.id = max_id + 1 
    card_dict = card.dict() 
    card_data.append(card_dict) 
    return card


