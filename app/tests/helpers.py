from contextlib import contextmanager


@contextmanager
def rollback_transaction(session):
    # rollback all after finish a test
    try:
        yield session.begin_nested()
    finally:
        session.rollback()
