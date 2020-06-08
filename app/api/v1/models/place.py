#!/usr/bin/python
""" holds class Place"""
import models
from base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Table

class Place(BaseModel, Base):
    """Representation of Place """
    try:
      __tablename__ = 'places'
      name = Column(String(128), nullable=False)
      description = Column(String(1024), nullable=True)
      price = Column(Integer, nullable=False, default=0)
      adress = Column(String(20))
      phone = Column(String(20))
        
    except:
        name = ""
        description = ""
        max_guest = 0
        price = 0
        adress = ""
        phone = ""
        
    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
