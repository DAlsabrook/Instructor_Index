#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import Base
from models.instructor import Instructor
from models.school import School
from models.rating import Rating
from models.user import User
from os import getenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Instructor": Instructor, "School": School,
           "Rating": Rating, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        # I added default port to the hosthost (:3306)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def get(self, cls, id):
        """Get on object based on its class and id"""
        # Check if class is a valid class
        if cls in classes.values():
            # Query to find if the class has an object with matching id
            obj = self.__session.query(cls).filter(cls.id == id).first()
            return obj
        else:
            # Return None if not a valid class
            return None

    def count(self, cls=None):
        """Return number of objects"""
        return len(self.all(cls))

    # Used in personal test files only
    def get_engine(self):
        """Returns the engine."""
        return self.__engine

    def get_session(self):
        """Returns the engine."""
        return self.__session

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
