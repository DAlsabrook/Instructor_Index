#!/usr/bin/python3
"""
Contains the class User
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a User"""
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    # Login info
    user_name = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args):
        """initializes city"""
        super().__init__(*args)
