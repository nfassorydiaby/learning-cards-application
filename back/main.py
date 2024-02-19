from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status
from datetime import datetime, timedelta
from typing import List, Dict
from card import Card  # Import Card from card.py
from category import Category  # Import Category from category.py
from card_data import card_data  # Import card_data

app = FastAPI(
    title="Learning Cards Application",
    description="This API aim to provide feature to manage a graphical interface for Learning Cards Application.")

@app.get("/cards/", tags=["Cards"])
async def read_cards():
    return card_data

@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED, tags=["Cards"])
async def create_card(card: Card):
    card_dict = card.dict() 
    card_data.append(card_dict) 
    return card

@app.get("/cards/quizz/", response_model=List[Card], status_code=status.HTTP_201_CREATED, tags=["Learning"])
async def get_quiz_cards(date: str | None = None):
    # Filtre et retourne uniquement les cartes de la catégorie FIRST
    today_cards: List[Dict] = [card for card in card_data if card["category"] == "FIRST"]
    return today_cards
