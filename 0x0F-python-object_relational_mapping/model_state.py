#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """Class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
