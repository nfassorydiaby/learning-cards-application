from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status



app = FastAPI()


class Card(BaseModel):
    id: int
    question: str
    answer: str
    tag: Optional[str] = None

fake_db = []

@app.get("/cards/")
async def read_cards():
    return fake_db

@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED)
async def create_card(card: Card):
    return card

