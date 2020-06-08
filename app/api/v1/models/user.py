#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class User(BaseModel, Base):
  """Representation of a user """
  __tablename__ = 'users'
  email = Column(String(128), nullable=False)
  password = Column(String(20), nullable=False)
  first_name = Column(String(20), nullable=True)
  last_name = Column(String(20), nullable=True)
  phone = Column(String(23))

  def __init__(self, *args, **kwargs):
     """initializes user"""
     super().__init__(*args, **kwargs)

