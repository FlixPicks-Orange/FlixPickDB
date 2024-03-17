from flask import abort, make_response
from config import db
from content.models import Genre, Genre_schema, Genres_schema

def show_all():
    genres = Genre.query.all()
    return Genres_schema.dump(genres)

def lookup_by_id(genre_id):
    genre = Genre.query.filter(Genre.genre_id == genre_id).one_or_none()
    if genre is not None:
        return Genre_schema.dump(genre)
    else:
        abort(404, f"Genre id {genre_id} not found")

def get_provider_name(genre_id):
    genre = Genre.query.filter(Genre.genre_id == genre_id).one_or_none()
    if genre is not None:
        return { 'genre_name': genre.genre_name }
    else:
        abort(404, f"Genre id {genre_id} not found.")