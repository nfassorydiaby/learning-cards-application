
from multiprocessing import AuthenticationError
from card import Card  # Import Card from card.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi import status
from fastapi.params import Depends
from typing import List, Annotated
from configQuizzCard import getCurrentCards
from configQuizzCard import setCurrentCards
from category import Category  # Import Category from category.py
from uuid import UUID as UUID4
from card_data import card_data  # Import card_data
from fastapi import Body
# import auth

# Implementation of database
from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session

app = FastAPI(
    title="Learning Cards Application",
    description="This API aim to provide feature to manage a graphical interface for Learning Cards Application.")

# app.include_router(auth.router)
# create the database
models.Base.metadata.create_all(bind=engine)

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


@app.get("/cards/", status_code=status.HTTP_200_OK, tags=["Cards"])
async def read_cards(db: db_dependency):
    cards = db.query(models.Card).all()
    return cards
    # return card_data


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
async def get_quiz_cards(db: db_dependency, date: str | None = None):
    # card firlered by category under 7
    cards = db.query(models.Card).filter(models.Card.category < 7).all()
    # get all cards whose frequency is 0 or you reduice the frequency by 1
    quizzCards = []
    for card in cards:
        if card.frequency == 0:
            quizzCards.append(card)
        else:
            card.frequency -= 1
            print(card.frequency)
            # update the card in the database
            db.query(models.Card).filter(models.Card.id ==
                                         card.id).update({"frequency": card.frequency})
            db.commit()

    return quizzCards


@app.patch('/cards/{cardId}/answer/', status_code=status.HTTP_204_NO_CONTENT, tags=["Learning"])
async def check_reponse(db: db_dependency, cardId: UUID4, cardResponse: dict = Body(validBody), ):
   # Récupérer la carte par son ID
    card = db.query(models.Card).filter(models.Card.id == cardId).first()
    print("cardID :", cardId)
    print("card :", card)
    # Si la réponse de la carte est valide, nous incrémentons la fréquence de la carte
    if cardResponse['isValid']:
        prochaine_categorie = Category(card.category).value + 1
        if prochaine_categorie <= len(Category):
            prochaine_categorie_str = Category(prochaine_categorie).name
        else:
            prochaine_categorie_str = Category.DONE.value
        card.category = prochaine_categorie_str
        # Mettre à jour la fréquence de la carte en catégorie - 1
        card.frequency = prochaine_categorie - 1
        db.commit()
    else:
        card.category = Category.FIRST.value
        card.frequency = 0
        db.commit()
