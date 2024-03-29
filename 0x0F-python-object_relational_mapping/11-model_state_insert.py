#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_object = State(name="Louisiana")
    session.add(new_object)
    session.commit()
    print(new_object.id)
    session.close()
