#!/usr/bin/python3
"""
a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base

Base = declarative_base()


class City(Base):
    """class base description"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
