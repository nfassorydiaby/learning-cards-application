from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    isActive = Column(Boolean, default=True)


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50), index=True)
    question = Column(String(50), index=True)
    answer = Column(String(50), index=True)
    tag = Column(String(50), index=True)
    # user_id = Column(Integer, ForeignKey("users.id"))
    # create_date = Column(DateTime, index=True)
    # update_date = Column(DateTime, index=True)

# class QuizzCard(Base):
#     __tablename__ = "quizzCard"

#     id = Column(Integer, primary_key=True, index=True)
#     cardId = Column(UUID(as_uuid=True), ForeignKey("card.id"))
#     remainingDays = Column(Integer, index=True)
