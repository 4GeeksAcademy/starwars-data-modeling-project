import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    secondname = Column(String(250), nullable=False)
    location = Column(String(250), ForeignKey('location.id'), nullable=False)
    gender = Column(String(250), nullable=False)
    weapon = Column(String(250), ForeignKey('weapon.id'), nullable=False)
    species = Column(String(250), ForeignKey('species.id'), nullable=False)

class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    dimensions = Column(Integer, nullable=False)
    location = Column(String(250), ForeignKey('location.id'), nullable=False)

class Location(Base):
    __tablename__ = 'location'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    terrain = Column(String(250), nullable=False)
    weapon = Column(String(250), ForeignKey('weapon.id'), nullable=False)
    species = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

class Weapon(Base):
    __tablename__ = 'weapon'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    affiliation = Column(String(250), nullable=False)
    location = Column(String(250), ForeignKey('location.id'), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    dimensions = Column(Integer, nullable=False)
    location = Column(String(250), ForeignKey('location.id'), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
