from flask import abort, make_response
from config import db
from models import User, user_schmea, users_schema

def read_all():
    users = User.query.all()
    return users_schema.dump(users)

