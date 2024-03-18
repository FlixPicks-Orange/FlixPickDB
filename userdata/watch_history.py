from flask import abort, make_response
from datetime import datetime
from config import db
from userdata.models import WatchHistory, WatchHistory_schema, WatchHistorys_schema
from userdata.models import User

# https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.filter

def show_all():
    history = WatchHistory.query.all()
    return WatchHistorys_schema.dump(history)


def add(entry):
    new_item = WatchHistory_schema.load(entry, session=db.session)
    db.session.add(new_item)
    db.session.commit()
    return WatchHistory_schema.dump(new_item), 201

def lookup_by_id(user_id):
    watch_history = WatchHistory.query.filter(WatchHistory.user_id == user_id).all()
    return WatchHistorys_schema.dump(watch_history)