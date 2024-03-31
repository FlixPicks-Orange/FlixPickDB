from flask import abort, make_response
from sqlalchemy import and_
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
    watch_history = WatchHistory.query.filter(and_(
        WatchHistory.user_id == user_id,
        WatchHistory.supressed == False
        )).order_by(WatchHistory.watched.desc()).all()
    return WatchHistorys_schema.dump(watch_history)


def remove_from_watch_history(user_id, movie_id):
    watch_history = WatchHistory.query.filter(and_(
        WatchHistory.user_id == user_id,
        WatchHistory.movie_id == movie_id
        )).all()
    for entry in watch_history:
        entry.supressed = True
    db.session.commit()
    return 200


def clear_watch_history(user_id):
    watch_history = WatchHistory.query.filter(WatchHistory.user_id == user_id).all()
    for entry in watch_history:
        entry.supressed = True
    db.session.commit()
    return 200


def clear_all():
    db.session.query(WatchHistory).delete()
    db.session.commit()
    return 200