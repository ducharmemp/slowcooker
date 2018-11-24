from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    steps = Column(Text)
    pictures = Column(Text)
    description = Column(Text)
    # comments = relationship()

    creator_id = Column(Integer, ForeignKey("users.id"))
