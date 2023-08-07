from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///storage.sql")

session = scoped_session(sessionmaker(engine))

Base = declarative_base()