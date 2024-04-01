#!/usr/bin/python3
"""
Contains the class DBStorage
"""


class DBStorage:
    """interaacts with the MySQL database"""
    from models.instructor import Instructor
    from models.school import School
    from models.rating import School_Rating, Instructor_Rating
    from models.user import User

    classes = {"Instructor": Instructor,
            "School": School,
            "School_Rating": School_Rating,
            "Instructor_Rating": Instructor_Rating,
            "User": User}
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        from sqlalchemy import create_engine
        self.__engine = create_engine(
            'mysql+mysqldb://admin:admin@localhost:3306/index_db'
            )

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in DBStorage.classes:
            if cls is None or cls is DBStorage.classes[clss] or cls is clss:
                objs = self.__session.query(DBStorage.classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def user(self, username, password):
        """Method to retrive a user from the databas"""
        User = DBStorage.User
        if username and password:
            user = self.__session.query(User).filter(
                User.username == username,
                User.password == password
            ).first()
            return user
        else:
            return

    def get(self, cls, id):
        """Get on object based on its class and id"""
        # Check if class is a valid class
        if cls in DBStorage.classes.values():
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
        from sqlalchemy.orm import scoped_session, sessionmaker
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
