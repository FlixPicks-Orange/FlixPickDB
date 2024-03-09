from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import MovieGenre, MovieGenre_schema, MovieGenres_schema
from content.models import Genre

def show_all():
    query_result = (
        db.session.query(MovieGenre, Genre)
        .join(Genre, Genre.tmdb_id == MovieGenre.genre_id)
        .all()
    )
    genres = build_object(query_result)
    return genres


def get_by_movie_id(movie_id):
    query_result = (
        db.session.query(MovieGenre, Genre)
        .join(Genre, Genre.tmdb_id == MovieGenre.genre_id)
        .filter(MovieGenre.movie_id == movie_id)
        .all()
    )
    genres = build_object(query_result)
    return genres


def build_object(query_data):
    genres = []
    for movie_genre, genre in query_data:
        genres.append({
            "id": movie_genre.id,
            "movie_id": movie_genre.movie_id,
            "genre_id": movie_genre.genre_id,
            "genre_name": genre.genre_name
        })
    return genres