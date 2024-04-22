from flask import abort, make_response, jsonify
from sqlalchemy import and_
from datetime import datetime
from config import db
from userdata.models import WatchHistory, WatchHistory_schema, WatchHistorys_schema
from userdata.models import User
from content.movie_genres import get_by_movie_id as get_movie_genre
#import content.movies, content.providers, content.genres

# https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.filter

def show_all():
    history = WatchHistory.query.order_by(WatchHistory.movie_id).all()
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


def get_watched_genres_for_user(user_id):
    watch_history = WatchHistory.query.filter(and_(
        WatchHistory.user_id == user_id,
        WatchHistory.supressed == False
        )).order_by(WatchHistory.watched.desc()).all()
    genre_list = TagCounter()
    for watched_movie in watch_history:
        for genre in get_movie_genre(watched_movie.movie_id):  
            genre_list.add(genre.get('genre_name'))
    return jsonify(genre_list.get_tag_names())
    
#def get_providers_used():
    


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




class TagCounter:
    def __init__(self):
        self.tags = {}
    
    def add(self, tag):
        if tag in self.tags:
            self.tags[tag] += 1
        else:
            self.tags[tag] = 1
    
    def get_count(self, tag):
        return self.tags.get(tag, 0)
    
    def get_tag_names(self):
        return sorted(self.tags, key=lambda x: self.tags[x], reverse=True)
    
    def get_list_of_tags(self):
        return sorted(self.tags.items(), key=lambda x: x[1], reverse=True)