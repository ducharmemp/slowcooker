from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from source.config import CONFIG

Base = declarative_base()
ENGINE = create_engine(
    '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'.format(
        **CONFIG['database']['uri']),
    **CONFIG['database']['config'])
_session_cls = sessionmaker(bind=ENGINE)


# Base.metadata.create_all(ENGINE)


def init_database(clean=False):
    Base.metadata.bind = ENGINE
    clean and Base.metadata.drop_all()
    Base.metadata.create_all()


@contextmanager
def connection(*args, **kwargs) -> Session:
    ctx_session = _session_cls(*args, **kwargs)
    try:
        yield ctx_session
    except Exception:
        ctx_session.rollback()
        raise
    finally:
        ctx_session.close()

from .ingredients import Ingredient
from .recipes import Recipe, RecipeStep
from .users import User
