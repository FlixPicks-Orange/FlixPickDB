from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import Movie, MovieGenre, MovieProvider
from content.movie_providers import get_by_movie_id as get_providers_by_movie_id
from content.movie_genres import get_by_movie_id as get_genres_by_movie_id

def show_all():
    query_result = Movie.query.all()
    movies = build_object(query_result)
    return movies


def get_by_title(movie_title):
    query_result = Movie.query.filter(Movie.title.like(f"%{movie_title}%")).all()
    movies = build_object(query_result)
    if not movies:
        abort(404, f"{movie_title} not found in moives list.")
    else:
        return movies


def get_by_movie_id(movie_id):
    query_result = Movie.query.filter(Movie.movie_id == movie_id).all()
    movies = build_object(query_result)
    if not movies:
        abort(404, f"Movie {movie_id} not found")
    else:
        return movies


def get_by_tmdb_id(movie_id):
    query_result = Movie.query.filter(Movie.tmdb_id == movie_id).all()
    movies = build_object(query_result)
    if not movies:
        abort(404, f"Movie {movie_id} not found")
    else:
        return movies


def find_movies_by_genre_id(genre_id):
    query_result = (
        Movie.query
        .join(MovieGenre, MovieGenre.movie_id == Movie.movie_id)
        .filter(MovieGenre.genre_id == genre_id)
        .all()
        )
    movies = build_object(query_result)
    if not movies:
        abort(404, f"Movies not found for specified genre.")
    else:
        return movies


def find_movies_by_provider_id(provider_id):
    query_result = (
        Movie.query
        .join(MovieProvider, MovieProvider.movie_id == Movie.movie_id)
        .filter(MovieProvider.provider_id == provider_id)
        .all()
        )
    movies = build_object(query_result)
    if not movies:
        abort(404, f"Movies not found for specified provider.")
    else:
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