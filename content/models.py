from datetime import datetime
from config import db, ma

# Movies Model
class Movie(db.Model):
    __tablename__ = "Movie"
    movie_id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    summary = db.Column(db.String(1000))
    release_date = db.Column(db.Date)
    runtime = db.Column(db.Integer)
    adult = db.Column(db.Boolean, default=False)
    poster_path = db.Column(db.String(255))
    backdrop_path = db.Column(db.String(255))
    language = db.Column(db.String(255))
    
class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        load_instance = True
        sqla_session = db.session

Movie_schmea = MovieSchema()
Movies_schmea = MovieSchema(many=True)