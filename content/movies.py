from flask import abort, make_response
from datetime import datetime
from config import db
from content.models import Movie, Movie_schmea, Movies_schmea

def show_all():
    movies = Movie.query.all()
    return Movies_schmea.dump(movies)