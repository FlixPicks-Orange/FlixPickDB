from flask import abort, make_response
from datetime import datetime
from config import db
from userdata.models import User, user_schmea, users_schema

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


def update_full(username, user):
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        update_user = user_schmea.load(user, session=db.session)
        existing_user.fname = update_user.fname
        existing_user.lname = update_user.lname
        existing_user.password = update_user.password
        existing_user.role = update_user.role
        existing_user.limit_subscriptions = update_user.limit_subscriptions
        db.session.merge(existing_user)
        db.session.commit()
        return user_schmea.dump(existing_user), 200
    else:
        abort(404, f"User with username {username} not found")


def update_password(username, data):
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        existing_user.password = data.get("password")
        db.session.merge(existing_user)
        db.session.commit()
        return user_schmea.dump(existing_user), 200
    else:
        abort(404, f"User with username {username} not found")


def update_role(username, data):
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        existing_user.role = data.get("role")
        db.session.merge(existing_user)
        db.session.commit()
        return user_schmea.dump(existing_user), 200
    else:
        abort(404, f"User with username {username} not found")


def update_last_login(username):
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        existing_user.last_login = datetime.utcnow()
        db.session.merge(existing_user)
        db.session.commit()
        return user_schmea.dump(existing_user), 200
    else:
        abort(404, f"User with username {username} not found")


def update_limit_subscriptions(username, data):
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        existing_user.limit_subscriptions = data.get("limit_subscriptions")
        db.session.merge(existing_user)
        db.session.commit()
        return user_schmea.dump(existing_user), 200
    else:
        abort(404, f"User with username {username} not found")