from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()

ENGINE = create_engine("sqlite://", pool_pre_ping=True)
_session_cls = sessionmaker(bind=ENGINE)


def init_database():
    Base.metadata.bind(ENGINE)
    Base.metadata.create_all()


@contextmanager
def connection(*args, **kwargs) -> Session:
    ctx_session = _session_cls(*args, **kwargs)
    try:
        yield ctx_session
        ctx_session.commit()  # TODO: Determine if this is the correct place to commit
    except Exception:
        ctx_session.rollback()
        raise
    finally:
        ctx_session.close()