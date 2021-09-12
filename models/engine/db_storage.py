#!/usr/bin/python3
"""contains dbstorage class"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """interacts with db"""
    __engine = None
    __session = None

    def __init__(self):
        """creates instance"""

        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'. format(user, passwd, host, db),
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the database"""

        n_list = [User, State, City, Amenity, Place, Review]
        n_dict = {}
        result = []

        if cls is None:
            for eachClass in n_list:
                result.extend(self.__session.query(eachClass).all())
        else:
            result = self.__session.query(cls).all()

        for r in result:
            id = r.__class__.__name__ + '.' + r.id
            n_dict[id] = r

        return(n_dict)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """ remove an object from the current session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(maker)
        self.__session = Session()

    def close(self):
        self.__session.invalidate()
