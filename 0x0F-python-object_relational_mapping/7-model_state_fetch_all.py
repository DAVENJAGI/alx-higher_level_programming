#!/usr/bin/python3
"""
Ascript that lists all State objects from the database hbtn_0e_6_usa
takes 3 arguments: mysql username, mysql password and database name
script should connect to a MySQL server on localhost at port 3306
"""

from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql://{sys.argv[1]}:{sys.argv[1]}@localhost:3306/{sys.argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(state.id.asc()).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
