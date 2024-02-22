
from multiprocessing import AuthenticationError
from card import Card
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi import status
from fastapi.params import Depends
from typing import List, Annotated
from category import Category
from uuid import UUID as UUID4
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

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


dbDependency = Annotated[Session, Depends(getDb)]


@app.get("/cards/", status_code=status.HTTP_200_OK, tags=["Cards"])
async def readCards(db: dbDependency):
    cards = db.query(models.Card).all()
    return cards


@app.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED, tags=["Cards"])
async def createCard(card: Card, db: dbDependency):
    dbCard = models.Card(**card.dict())
    db.add(dbCard)
    db.commit()
    return card


@app.get("/cards/quizz/", response_model=List[Card], status_code=status.HTTP_201_CREATED, tags=["Learning"])
async def getQuizCards(db: dbDependency, date: str | None = None):
    cards = db.query(models.Card).filter(models.Card.category < 7).all()
    quizzCards = []
    for card in cards:
        if card.remainingDays == 0:
            quizzCards.append(card)
        else:
            card.remainingDays -= 1
            db.query(models.Card).filter(models.Card.id == card.id).update({"remainingDays": card.remainingDays})
            db.commit()
    return quizzCards


@app.patch('/cards/{cardId}/answer/', status_code=status.HTTP_204_NO_CONTENT, tags=["Learning"])
async def checkResponse(db: dbDependency, cardId: UUID4, cardResponse: dict = Body(validBody)):
    card = db.query(models.Card).filter(models.Card.id == str(cardId)).first()

    if cardResponse['isValid']:
        currentCategoryIndex = list(Category).index(card.category)
        nextCategoryIndex = currentCategoryIndex + 1
        if nextCategoryIndex < len(Category):
            nextCategory = list(Category)[nextCategoryIndex]
        else:
            nextCategory = Category.DONE.value

        card.category = nextCategory
        card.remainingDays = nextCategoryIndex
        db.commit()
    else:
        card.category = Category.FIRST.value
        card.remainingDays = 0
        db.commit()

