from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import Movie, movie_schema, movies_schema

def show_all():
    movies = Movie.query.all()
    return movies_schema.dump(movies)