from flask import abort, make_response
from config import db
from models import User, user_schmea, users_schema

# https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.filter

def show_all():
    users = User.query.all()
    return users_schema.dump(users)


def add(user):
    email = user.get("email")
    username = user.get("username")
    existing_user = User.query.filter(User.username == username).one_or_none()
    existing_user1 = User.query.filter(User.email == email).one_or_none()
    
    if existing_user is None and existing_user1 is None:
        new_user = user_schmea.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schmea.dump(new_user), 201
    else:
        abort(422, f"User with user {username} already exists")


def lookup_by_id(id):
    user = User.query.filter(User.id == id).one_or_none()
    if user is not None:
        return user_schmea.dump(user)
    else:
        abort(404, f"User id {id} not found")


def lookup_by_email(email):
    user = User.query.filter(User.email == email).one_or_none()
    if user is not None:
        return user_schmea.dump(user)
    else:
        abort(404, f"User with email {email} not found")


def lookup_by_username(username):
    user = User.query.filter(User.username == username).one_or_none()
    if user is not None:
        return user_schmea.dump(user)
    else:
        abort(404, f"User with username {username} not found")