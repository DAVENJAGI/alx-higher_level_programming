#!/usr/bin/python3
"""
Ascript that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///user:{sys.argv[1]}@localhost:3306")

states = session.query(State).order_by(state.id.asc()).all()

for state in states:
    print(state)

    session.close()
