#!/usr/bin/python3
"""file that contains the class definition of a City."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """State class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
