#! /usr/bin/env python2

# SQLAlchemy uses to communicate with various types of DBAPIs and databases.

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

import os
import sys

"""
    from item_catalog import app
    db=sqlalchemy(app)
"""


"""
creating an instance of declarative_base  for writing our class code
"""

Base = declarative_base()


def get_current_time():
    return datetime.datetime.now()


class MenuItem(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    image = Column(String(250), nullable=False)
    categories = Column(String(20), nullable=False)
    date = Column(DateTime, default=get_current_time,
    onupdate=get_current_time)
# automatically updates on creation and update

    def __init__(self, name):
        self.name = name

        """
        Return object data in easily serializeable format
        """
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': self.image,
            'categories': self.categories,
        }


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    picture = Column(String(150))
    user_id = Column(Integer, ForeignKey('menu_item.id'))
    user = relationship(MenuItem)


class Restaurant(Base):
    __tablename__ = 'restaurant'
    user_id = Column(Integer, ForeignKey('user.id'))
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(150))
    description = Column(String(250))
    user = relationship(User)

    @property
    def serialize(self):
        """
        Return serializeable format of the restaurant Object.
        """
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description': self.description,
        }

engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine)
