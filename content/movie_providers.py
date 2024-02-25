from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import MovieProvider, MovieProvider_schema, MovieProviders_schema

def show_all():
    movies = MovieProvider.query.all()
    return MovieProviders_schema.dump(movies)