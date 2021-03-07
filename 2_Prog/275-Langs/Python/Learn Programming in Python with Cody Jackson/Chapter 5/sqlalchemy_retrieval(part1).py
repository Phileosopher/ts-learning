from sqlalchemy_declarative import Base, Tools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sqlalchemy_example.db")

Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
