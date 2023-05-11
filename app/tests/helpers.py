from contextlib import contextmanager


@contextmanager
def rollback_transaction(session):
    try:
        yield session.begin_nested()
    finally:
        session.rollback()
