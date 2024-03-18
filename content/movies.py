from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import Movie, MovieGenre, MovieProvider
from content.movie_providers import get_by_movie_id as get_providers_by_movie_id
from content.movie_genres import get_by_movie_id as get_genres_by_movie_id
from content.discovery.popular_movies import find_popular_movies
from content.discovery.import_movie_data import import_movie_from_tmdb

def show_all():
    query_result = Movie.query.all()
    movies = build_json_result(query_result)
    return movies


def get_by_title(movie_title):
    query_result = Movie.query.filter(Movie.title.like(f"%{movie_title}%")).all()
    movies = build_json_result(query_result)
    if not movies: return None
    else: return movies


def get_by_movie_id(movie_id):
    query_result = Movie.query.filter(Movie.movie_id == movie_id).all()
    movies = build_json_result(query_result)
    if not movies: return None
    else: return movies


def get_by_tmdb_id(movie_id):
    query_result = Movie.query.filter(Movie.tmdb_id == movie_id).all()
    movies = build_json_result(query_result)
    if not movies: return None
    else: return movies


def find_movies_by_genre_id(genre_id):
    query_result = (
        Movie.query
        .join(MovieGenre, MovieGenre.movie_id == Movie.movie_id)
        .filter(MovieGenre.genre_id == genre_id)
        .all()
        )
    movies = build_json_result(query_result)
    if not movies: return None
    else: return movies


def find_movies_by_provider_id(provider_id):
    query_result = (
        Movie.query
        .join(MovieProvider, MovieProvider.movie_id == Movie.movie_id)
        .filter(MovieProvider.provider_id == provider_id)
        .all()
        )
    movies = build_json_result(query_result)
    if not movies: return None
    else: return movies


def show_popular_movies():
    movie_list = []
    popular_movies = find_popular_movies()
    for movie in popular_movies:
        found_movie = get_by_tmdb_id(movie['id'])
        if found_movie is not None: movie_list.extend(found_movie)
        else:
            import_movie_from_tmdb(movie['id'])
            found_movie = get_by_tmdb_id(movie['id'])
            if found_movie is not None: movie_list.extend(found_movie)
    return movie_list
            
        


def build_json_result(query_data):
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