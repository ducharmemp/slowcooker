from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from source.config import CONFIG

Base = declarative_base()
ENGINE = create_engine('{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'.format(**CONFIG['database']['uri']), **CONFIG['database']['config'])
_session_cls = sessionmaker(bind=ENGINE)

from .recipes import Recipe
from .users import User

# Base.metadata.create_all(ENGINE)


def init_database():
    Base.metadata.bind = ENGINE
    Base.metadata.drop_all()
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
