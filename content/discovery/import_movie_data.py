import requests
from sqlalchemy import and_
from config import db
from content.models import Movie, Movie_schema
from content.models import MovieProvider, MovieProvider_schema
from content.models import MovieGenre, MovieGenre_schema

API_KEY = '50cb1ca5b03be4ca02207aa9a63691a5'
BASE_URL = "https://api.themoviedb.org/3"

## Import Movie Data For Specified TMDB_ID
def import_movie_from_tmdb(tmdb_id):
    endpoint = f'{BASE_URL}/movie/{tmdb_id}'
    params = {'api_key': API_KEY}
    response = requests.get(endpoint, params=params)
    movie_data = response.json()
    insert_movie(movie_data)
    find_movie = Movie.query.filter(Movie.tmdb_id == tmdb_id).one_or_none()
    if find_movie is not None:
        movie_id = find_movie.movie_id
        for genre in movie_data['genres']:
            insert_movie_genre(movie_id, genre['id'])
        import_movie_provider_from_tmdb(movie_id, tmdb_id)


## Import Movie Providers
def import_movie_provider_from_tmdb(movie_id, tmdb_id):
    endpoint = f'{BASE_URL}/movie/{tmdb_id}/watch/providers'
    params = {'api_key': API_KEY}
    response = requests.get(endpoint, params=params)    
    data = response.json()
    if data["results"]["US"]["flatrate"]:
        providers = data["results"]["US"]["flatrate"]
    elif data["results"]["US"]["buy"]:
        providers = data["results"]["US"]["buy"]
    elif data["results"]["US"]["rent"]:
        providers = data["results"]["US"]["rent"]
    for provider in providers:
        insert_movie_provider(movie_id, provider['provider_id'], tmdb_id)


## Insert Movie Into Database
def insert_movie(movie_data):
    existing = Movie.query.filter(Movie.tmdb_id == movie_data['id']).one_or_none()
    if existing is None:
        new_movie = Movie_schema.load({
            'tmdb_id': movie_data['id'],
            'title': movie_data['title'],
            'summary': movie_data['overview'],
            'release_date': movie_data['release_date'],
            'runtime': movie_data['runtime'],
            'adult': movie_data['adult'],
            'poster_path': movie_data['poster_path'],
            'backdrop_path': movie_data['backdrop_path'],
            'language': movie_data['original_language']
        }, session=db.session)
        db.session.add(new_movie)
        db.session.commit()


## Insert Movie_Genre Into Database
def insert_movie_genre(movie_id, genre_id):
    existing = MovieGenre.query.filter(and_(
            MovieGenre.movie_id == movie_id,
            MovieGenre.genre_id == genre_id
        )).one_or_none()
    if existing is None:
        new_genre = MovieGenre_schema.load({
            'movie_id': movie_id,
            'genre_id': genre_id
        }, session=db.session)
        db.session.add(new_genre)
        db.session.commit()


## Insert Movie_Provider Into Database
def insert_movie_provider(movie_id, provider_id, tmdb_id):
    existing = MovieProvider.query.filter(and_(
            MovieProvider.movie_id == movie_id,
            MovieProvider.provider_id == provider_id
        )).one_or_none()
    if existing is None:
        new_provider = MovieProvider_schema.load({
            'movie_id': movie_id,
            'provider_id': provider_id,
            'link': "https://www.themoviedb.org/movie/" + str(tmdb_id) + "/watch"
        }, session=db.session)
        db.session.add(new_provider)
        db.session.commit()