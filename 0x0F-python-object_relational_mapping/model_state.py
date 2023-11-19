#!/usr/bin/python3
"""
a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationships
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """class base description"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)

#    cities = relationship('City', backref='satte')

    def __repr__(self):
        """To define how  to print the outpus"""
        return f"State(id={self.id}, name={self.name})"


engine = create_engine("sqlite:///user:root@localhost:3306")
Base.metadata.create_all(engine)
