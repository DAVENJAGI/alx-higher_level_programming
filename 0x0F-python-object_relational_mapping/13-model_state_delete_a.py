#!/usr/bin/python3
"""
This script changes the name of the State object with id = 2 to
New Mexico in the database hbtn_0e_6_usa
Usage
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    session.commit()
    session.close()
