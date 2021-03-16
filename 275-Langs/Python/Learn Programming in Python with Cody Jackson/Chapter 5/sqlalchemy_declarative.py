from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tools(Base):
    __tablename__ = "tools"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=250), nullable=False)
    size = Column(String(length=25))
    price = Column(Integer)

engine = create_engine("sqlite:///sqlalchemy_example.db")

Base.metadata.create_all(engine)
