from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import MovieGenre, MovieGenre_schema, MovieGenres_schema

def show_all():
    movies = MovieGenre.query.all()
    return MovieGenres_schema.dump(movies)