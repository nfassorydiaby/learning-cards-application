from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from back.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    tag = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    create_date = Column(DateTime, index=True)
    update_date = Column(DateTime, index=True)
