#!/usr/bin/python3
"""
class definition of a State
"""
from sqlalchemy.ext.declarative imoort declaratuve__base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State table mapping
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(id={}, name={})>".format(self.id, self.name)
