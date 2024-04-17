from flask import abort, make_response, jsonify
from datetime import datetime
from config import db
from content.models import MovieProvider, MovieProvider_schema, MovieProviders_schema
from content.providers import Provider

def show_all():
    query_result = (
        db.session.query(MovieProvider, Provider)
        .join(Provider, Provider.tmdb_id == MovieProvider.provider_id)
        .all()
    )
    providers = build_object(query_result)
    return providers


def get_by_movie_id(movie_id):
    query_result = (
        db.session.query(MovieProvider, Provider)
        .join(Provider, Provider.tmdb_id == MovieProvider.provider_id)
        .filter(MovieProvider.movie_id == movie_id)
        .all()
    )
    providers = build_object(query_result)
    return providers


def get_id_by_movie_id(movie_id):
    providers = MovieProvider.query.filter(MovieProvider.movie_id == movie_id).all()
    provider_ids = [provider.provider_id for provider in providers]
    return provider_ids    


def build_object(query_data):
    providers = []
    for movie_provider, provider in query_data:
        providers.append({
            "id": movie_provider.id,
            "movie_id": movie_provider.movie_id,
            "provider_id": movie_provider.provider_id,
            "provider_name": provider.provider_name,
            "logo_path": "https://image.tmdb.org/t/p/original" + provider.logo_path,
            "link": movie_provider.link,
        })
    return providers