from flask import abort, make_response
from sqlalchemy import and_
from datetime import datetime
from config import db
from userdata.models import UserClicks, UserClick_schema, UserClicks_schema
def show_all():
    clicks = UserClicks.query.all()
    return UserClicks_schema.dump(clicks)

def add(entry):
    new_item = UserClick_schema.load(entry, session=db.session)
    db.session.add(new_item)
    db.session.commit()
    return UserClick_schema.dump(new_item), 201
