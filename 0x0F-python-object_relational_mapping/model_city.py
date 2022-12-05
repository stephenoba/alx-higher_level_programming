#!/usr/bin/python3
"""
class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base

class City(Base):
    """
    City table mapping
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer,
            Foreignley('states.id'),
            nullable=False)

    def __repr__(self):
        """
        model representation"
        """
        return "<City(id={}, name={)>".format(self.id, self.name)
