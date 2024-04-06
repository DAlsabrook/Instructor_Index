#!/usr/bin/python3
"""
Contains the class School
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class School(BaseModel, Base):
    """Representation of a school"""
    __tablename__ = 'schools'
    name = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    instructors = relationship("Instructor", backref="school")
    ratings = relationship("School_Rating", backref="school")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    @property
    def overall(self):
        if self.ratings:
            return round(sum(rating.overall
                       for rating in self.ratings) / len(self.ratings), 1)
        return 0

    # Override to_dict method to include overall rating
    def to_dict(self):
        data = super().to_dict()
        data['overall'] = self.overall
        return data
