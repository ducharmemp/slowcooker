from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from passlib.hash import bcrypt

from . import Base, Recipe


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True, index=True)
    email = Column(Text, nullable=False, unique=True)
    # This should be salt and peppered
    password = Column(Text, nullable=False)

    recipes = relationship(Recipe)

    def __init__(self, name, password, email="", **kwargs):
        self.name = name
        self.email = email
        self.password = bcrypt.encrypt(password)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

