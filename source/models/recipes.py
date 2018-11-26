from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from . import Base


class RecipeStep(Base):
    __tablename__ = 'recipe_steps'

    id = Column(Integer, primary_key=True)
    position = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    parent_id = Column(Integer, ForeignKey('recipes.id'))

    def __repr__(self):
        return '<RecipeStep(position={self.position!r}, description={self.description!r})>'.format(
            self=self)


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    pictures = Column(Text)
    description = Column(Text, default="")

    steps = relationship(
        RecipeStep,
        lazy=False,
        order_by=RecipeStep.position,
        collection_class=ordering_list('position'))

    creator_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return '<Recipe(name={self.name!r})>'.format(self=self)
