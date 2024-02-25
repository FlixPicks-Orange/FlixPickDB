import requests
from content.models import Movie, movie_schema, movies_schema

API_KEY = '50cb1ca5b03be4ca02207aa9a63691a5'
BASE_URL = "https://api.themoviedb.org/3"

def find_movie_info():
    all_movies = Movie.query.all()
    collection = []
    #count = 0
    for movie in all_movies:
        #data = request_movie_info(movie.tmdb_id)
        #data = request_genres(movie.tmdb_id)
        data = request_providers(movie.movie_id, movie.tmdb_id)
        collection.extend(data)
        #if count > 20:
        #    break
        #count += 1
    return collection        


def request_providers(movie_id, tmdb_id):
    endpoint = f'{BASE_URL}/movie/{tmdb_id}/watch/providers'
    params = {'api_key': API_KEY}
    response = requests.get(endpoint, params=params)    
    data = response.json()
    results = []
    if data["results"]:
        #providers = data["results"]["US"]
        if data["results"]["US"]["flatrate"]:
            providers = data["results"]["US"]["flatrate"]
        elif data["results"]["US"]["buy"]:
            providers = data["results"]["US"]["buy"]
        elif data["results"]["US"]["rent"]:
            providers = data["results"]["US"]["rent"]
        else:
            results.append({
                'movie_id': movie_id,
                'tmdb_id': tmdb_id,
                'provider_id': '0',
                'provider_name': 'unknown',
                'link': "https://www.themoviedb.org/movie/" + str(tmdb_id) + "/watch"
            })
        for provider in providers:
            results.append({
                'movie_id': movie_id,
                'tmdb_id': tmdb_id,
                'provider_id': provider["provider_id"],
                'provider_name': provider["provider_name"],
                'link': "https://www.themoviedb.org/movie/" + str(tmdb_id) + "/watch"
            })
    else:
        results.append({
            'movie_id': movie_id,
            'tmdb_id': tmdb_id,
            'provider_id': '0',
            'provider_name': 'unknown',
            'link': "https://www.themoviedb.org/movie/" + str(tmdb_id) + "/watch"
        })

    return results
    
    #results = []
    #for genre in genres:
    #    results.append({
    #        'movie_id': movie_id,
    #        'tmdb_id': tmdb_id,
    #        'link': genre["link"]
    #    })



def request_genres(tmdb_id):
    endpoint = f'{BASE_URL}/movie/{tmdb_id}'
    params = {'api_key': API_KEY}
    response = requests.get(endpoint, params=params)
    data = response.json()
    genres = data.get("genres")
    results = []
    for genre in genres:
        results.append({
            'movie_id': tmdb_id,
            'genre_id': genre.get("id")
        })
    return results


def request_movie_info(tmdb_id):
    endpoint = f'{BASE_URL}/movie/{tmdb_id}'
    params = {'api_key': API_KEY}
    response = requests.get(endpoint, params=params)
    data = response.json()
    movie_info = {
        'tmdb_id': tmdb_id,
        'runtime': data.get("runtime"),
        'release_date': data.get("release_date")
    }
    return movie_info