from flask import abort, make_response
from datetime import datetime
from config import db
from userdata.models import WatchHistory, WatchHistory_schmea, WatchHistorys_schmea
from userdata.models import User

# https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.filter

def show_all():
    history = WatchHistory.query.all()
    return WatchHistorys_schmea.dump(history)


def add(entry):
    new_item = WatchHistory_schmea.load(entry, session=db.session)
    db.session.add(new_item)
    db.session.commit()
    return WatchHistory_schmea.dump(new_item), 201

def lookup_by_id(id):
    watch_history = WatchHistory.query.filter(WatchHistory.user_id == id).all()
    return WatchHistorys_schmea.dump(watch_history)