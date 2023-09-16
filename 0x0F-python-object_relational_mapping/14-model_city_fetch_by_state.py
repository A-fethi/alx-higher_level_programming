#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in (session.query(State, City)
                        .filter(State.id == City.state_id).all()):
        print(f'{state.name}: ({city.id}) {city.name}')
