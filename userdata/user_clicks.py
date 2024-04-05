from flask import abort, make_response
from sqlalchemy import and_
from datetime import datetime
from config import db
from userdata.models import UserClicks, UserClick_schema, UserClicks_schema
def show_all():
    clicks = UserClicks.query.all()
    return UserClicks_schema.dump(clicks)