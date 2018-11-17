from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from . import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    # This should be salt and peppered
    password = Column(Text)

    recipes = relationship(Recipe)

