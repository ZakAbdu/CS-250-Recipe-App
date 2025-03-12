from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_users():
    demo = User(
        user_name='Demo User',
        email='demo@aa.io',
        _password='password'
    )
    gordon = User(
        user_name='Gordon Ramsay',
        email='gordon@idiot.com',
        _password='password'
    )

    db.session.add(demo)
    db.session.add(gordon)
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()