from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status
from datetime import datetime, timedelta
from typing import List, Dict
from card import Card  # Import Card from card.py
from config_quizz_card import currentCards
from category import Category  # Import Category from category.py
from card_data import card_data  # Import card_data
from card_quizz import list_card_by_frequency
from fastapi import Body

app = FastAPI(
    title="Learning Cards Application",
    description="This API aim to provide feature to manage a graphical interface for Learning Cards Application.")

validBody = {
    "isValid": True
}

@app.get("/cards/", tags=["Cards"])
async def read_cards():
    return card_data

@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED, tags=["Cards"])
async def create_card(card: Card):
    cardDict = card.dict() 
    card_data.append(cardDict)
    card.addToList() 
    return card

@app.get("/cards/quizz/", response_model=List[Card], status_code=status.HTTP_201_CREATED, tags=["Learning"])
async def get_quiz_cards(date: str | None = None):
    # Filtre et retourne uniquement les cartes de la catégorie FIRST
    quizzCards = currentCards()
    return quizzCards

@app.patch('/cards/{cardId}/answer/', status_code=status. HTTP_204_NO_CONTENT, tags=["Learning"])
async def check_reponse(cardId: int, isValid: dict = Body(validBody), ):
    # Process the request body
    # You can access the fields of valid_body like valid_body["isValid"]
    return {"message": f"Card patched "}