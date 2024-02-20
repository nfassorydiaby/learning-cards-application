from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "mysql+pymysql://user:password@db/database"

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=create_engine(URL_DATABASE))

Base = declarative_base()
