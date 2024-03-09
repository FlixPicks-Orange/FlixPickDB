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

Movie_schema = MovieSchema()
Movies_schema = MovieSchema(many=True)


# Movie Provider Relationship Model
class MovieProvider(db.Model):
    __tablename__ = "Movie_Providers"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    provider_id = db.Column(db.Integer)
    link = db.Column(db.String(255))
    
class MovieProviderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MovieProvider
        load_instance = True
        sqla_session = db.session

MovieProvider_schema = MovieProviderSchema()
MovieProviders_schema = MovieProviderSchema(many=True)


# Movie Genre Relationship Model
class MovieGenre(db.Model):
    __tablename__ = "Movie_Genres"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    genre_id = db.Column(db.Integer)
    
class MovieGenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MovieGenre
        load_instance = True
        sqla_session = db.session

MovieGenre_schema = MovieGenreSchema()
MovieGenres_schema = MovieGenreSchema(many=True)


# Streaming Providers Model
class Provider(db.Model):
    __tablename__ = "Providers"
    provider_id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer)
    display_priority = db.Column(db.Integer)
    provider_name = db.Column(db.String(255))
    logo_path = db.Column(db.String(255))
    region = db.Column(db.String(255))
    
class ProviderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Provider
        load_instance = True
        sqla_session = db.session

Provider_schema = ProviderSchema()
Providers_schema = ProviderSchema(many=True)


# Genres Model
class Genre(db.Model):
    __tablename__ = "Genre"
    genre_id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer)
    genre_name = db.Column(db.String(255))
    
class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True
        sqla_session = db.session

Genre_schema = GenreSchema()
Genres_schema = GenreSchema(many=True)