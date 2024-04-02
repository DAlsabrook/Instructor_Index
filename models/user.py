#!/usr/bin/python3
"""
Contains the class User
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """Representation of a User"""
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    # Login info
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    @staticmethod
    def get(user_id):
        from models import storage
        return storage.get(User, user_id)

# create User first_name="" last_name="" username="" password=""
