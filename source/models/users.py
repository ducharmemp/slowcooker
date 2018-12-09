from enum import IntEnum

from sqlalchemy import Column, Integer, Text, Table, ForeignKey
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from passlib.hash import argon2

from . import Base, Recipe


class RecipeStatus(IntEnum):
    USER_SAVED = 1
    USER_CREATED = 2


class UserRecipe(Base):
    __tablename__ = 'user_recipes'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    status = Column(Enum(RecipeStatus))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True, index=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)

    recipes = relationship('UserRecipe')
    # saved_recipes = relationship('UserRecipes', primaryjoin='and_(User.id == UserRecipe.user_id, UserRecipe.status == RecipeStatus.USER_SAVED)')

    def __init__(self, name, password, email="", **kwargs):
        self.name = name
        self.email = email
        self.password = argon2.hash(password)

    def validate_password(self, password):
        return argon2.verify(password, self.password)

