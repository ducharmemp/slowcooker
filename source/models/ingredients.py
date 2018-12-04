from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from . import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    description = Column(Text)

    recipe_id = Column(Integer, ForeignKey("recipes.id"))
