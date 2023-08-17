from app.services.crud_user import create_user


def create_user_db(db):
    user_db = create_user(db, "testuser@yopmail.com", "test user", "123456789", "password")
    return user_db
