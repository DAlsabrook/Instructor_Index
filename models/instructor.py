#!/usr/bin/python3
"""
Contains the class Instructor
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Instructor(BaseModel, Base):
    """
    Representation of a Instructor

    Instance creation:
        instructor_name = Instructor(name='Tom', school_id=atlas.id)
        "atlas.id" being an instance of a school
    """
    __tablename__ = 'instructors'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    ratings = relationship("Instructor_Rating", backref="instructor")
    # What school they teach at
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    @property
    def overall(self):
        if self.ratings:
            return round(sum(rating.overall
                       for rating in self.ratings) / len(self.ratings), 1)
        return 0
