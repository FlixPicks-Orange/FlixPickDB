from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import Movie, Movie_schema, Movies_schema
from content.movie_providers import get_by_movie_id as get_providers_by_movie_id
from content.movie_genres import get_by_movie_id as get_genres_by_movie_id

def show_all():
    query_result = Movie.query.all()
    movies = build_object(query_result)
    return movies


def get_by_movie_id(movie_id):
    query_result = Movie.query.filter(Movie.movie_id == movie_id).all()
    movies = build_object(query_result)
    return movies


def build_object(query_data):
    movies = []
    for movie in query_data:
        providers = get_providers_by_movie_id(movie.movie_id)
        genres = get_genres_by_movie_id(movie.movie_id)
        movies.append({
            "movie_id": movie.movie_id,
            "tmdb_id": movie.tmdb_id,
            "title": movie.title,
            "summary": movie.summary,
            "release_date": movie.release_date,
            "runtime": movie.runtime,
            "adult": movie.adult,
            "poster_path": "https://image.tmdb.org/t/p/original" + movie.poster_path,
            "backdrop_path": "https://image.tmdb.org/t/p/original" + movie.backdrop_path,
            "language": movie.language,
            "moive_providers": providers,
            "movie_genres": genres
        })
    return movies