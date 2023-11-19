#!/usr/bin/python3
"""
Ascript that lists all State objects from the database hbtn_0e_6_usa
takes 3 arguments: mysql username, mysql password and database name
script should connect to a MySQL server on localhost at port 3306
"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(state.id.asc()).all():
        print("{}: {}".format(state.id, state.name))
