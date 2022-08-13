#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    if len(session.query(State).all()) > 0:
        state_1 = session.query(State).order_by(State.id).all()
        print("{}: {}".format(state_1[0].id, state_1[0].name))
    session.close()
