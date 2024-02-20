
from multiprocessing import AuthenticationError
from card import Card  # Import Card from card.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi import status
from fastapi.params import Depends

from typing import List, Annotated
from functions.config_quizz_card import currentCards

from config_quizz_card import setCurrentCards
from category import Category  # Import Category from category.py

from card_data import card_data  # Import card_data
from fastapi import Body
import auth

# Implementation of database
from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session

app = FastAPI(
    title="Learning Cards Application",
    description="This API aim to provide feature to manage a graphical interface for Learning Cards Application.")
app.include_router(auth.router)
# create the database
models.Base.metadata.create_all(bind=engine)

# pydentic validation
# card from card.py


validBody = {
    "isValid": True
}

# getting the database


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/cards/", tags=["Cards"])
async def read_cards():
    return card_data


@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED, tags=["Cards"])
async def create_card(card: Card, db: db_dependency):

    card_dict = card.dict()
    card_data.append(card_dict)
    card.addToList()

    # add card to the database
    db_card = models.Card(**card.dict())
    db.add(db_card)
    db.commit()

    return card


@app.get("/cards/quizz/", response_model=List[Card], status_code=status.HTTP_201_CREATED, tags=["Learning"])
async def get_quiz_cards(date: str | None = None):
    # Filtre et retourne uniquement les cartes de la catégorie FIRST
    quizzCards = getCurrentCards()
    return quizzCards


@app.patch('/cards/{cardId}/answer/', status_code=status.HTTP_204_NO_CONTENT, tags=["Learning"])
async def check_reponse(cardId: int, cardResponse: dict = Body(validBody), ):
    card = Card.getCard(cardId)
    category = card.manageCategory(cardResponse.isValid)
    setCurrentCards(cardId, category)
