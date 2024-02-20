
from card import Card  # Import Card from card.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi import status
from typing import List
from functions.config_quizz_card import currentCards
from card_data import card_data  # Import card_data
from card_quizz import list_card_by_frequency
from fastapi import Body

# Implementation of database
from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session

app = FastAPI(
    title="Learning Cards Application",
    description="This API aim to provide feature to manage a graphical interface for Learning Cards Application.")

# create the database
models.Base.metadata.create_all(bind=engine)

# pydentic validation
# card from card.py

valid_body = {
    "isValid": True
}

# getting the database


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/cards/", tags=["Cards"])
async def read_cards():
    return card_data


@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED, tags=["Cards"])
async def create_card(card: Card):
    card_dict = card.dict()
    card_data.append(card_dict)
    Card.add_to_list(card_data, list_card_by_frequency)
    return card


@app.get("/cards/quizz/", response_model=List[Card], status_code=status.HTTP_201_CREATED, tags=["Learning"])
async def get_quiz_cards(date: str | None = None):
    # Filtre et retourne uniquement les cartes de la catégorie FIRST
    quizz_cards = currentCards(list_card_by_frequency, card_data)
    return quizz_cards


@app.patch('/cards/{cardId}/answer/', status_code=status. HTTP_204_NO_CONTENT, tags=["Learning"])
async def check_reponse(cardId: int, isValid: dict = Body(valid_body), ):
    # Process the request body
    # You can access the fields of valid_body like valid_body["isValid"]
    return {"message": f"Card patched "}
