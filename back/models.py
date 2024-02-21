from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
import uuid


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)


class Card(Base):
    __tablename__ = "cards"

    id = Column(String(255), primary_key=True,
                index=True, default=uuid.uuid4)

    category = Column(String(50), index=True)
    question = Column(String(50), index=True)
    answer = Column(String(50), index=True)
    tag = Column(String(50), index=True)
    # user_id = Column(Integer, ForeignKey("users.id"))
    # create_date = Column(DateTime, index=True)
    # update_date = Column(DateTime, index=True)
