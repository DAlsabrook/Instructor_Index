#!/usr/bin/python3
"""
Contains the class Rating
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property


class School_Rating(BaseModel, Base):
    """
    Representation of a Rating for schools
    """
    __tablename__ = 'school_ratings'

    # What school being rated
    school_id = Column(String(60), ForeignKey('schools.id'), nullable=False)

    # User given review
    review = Column(Text, nullable=False)
    # Rating categories given by user from 1-5
    facilities = Column(Integer, nullable=False)
    parking = Column(Integer, nullable=False)
    internet = Column(Integer, nullable=False)
    social = Column(Integer, nullable=False)
    happiness = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        # Get a UUID as primary key
        super().__init__(*args, **kwargs)

    @property
    def overall(self):
        ratings = [self.facilities, self.parking, self.internet,
                   self.social, self.happiness]
        return round(sum(ratings) / len(ratings), 1)


class Instructor_Rating(BaseModel, Base):
    """Representation of a Rating for instructors"""
    __tablename__ = 'instructor_ratings'

    # What instructor is being rated
    instructor_id = Column(String(60),
                           ForeignKey('instructors.id'), nullable=False)

    # User given reviews
    review = Column(Text, nullable=False)
    # Rating categories given by user from 1-5
    difficulty = Column(Integer, nullable=False)
    approachability = Column(Integer, nullable=False)
    availability = Column(Integer, nullable=False)
    helpfulness = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes city"""
        # Get a UUID as primary key
        super().__init__(*args, **kwargs)

    @property
    def overall(self):
        ratings = [self.difficulty, self.approachability,
                   self.availability, self.helpfulness]
        return round(sum(ratings) / len(ratings), 1)
