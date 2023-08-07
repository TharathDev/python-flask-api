# 3rd party libraries import
from sqlalchemy import Column, Integer, String

# local import
from db import Base

# relation import
from .base_model import BaseModel


class UserModel(BaseModel, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False, index=True)
    __username = Column("username", String(24), nullable=False, index=True)
    __password = Column("password", String(256), nullable=False)
    phone = Column(Integer)
    email = Column(String(24))

    def __init__(self, schema={}):
        super().__init__()

        for key, value in schema.items():
            if (hasattr(self, key)):
                setattr(self, key, value)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
