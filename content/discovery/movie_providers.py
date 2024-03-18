import requests
from content.movies import show_all as show_all_movies

API_KEY = '50cb1ca5b03be4ca02207aa9a63691a5'
BASE_URL = "https://api.themoviedb.org/3"


# FIND PROVIDERS WHERE NOT SPECIFIED FOR EACH MOVIE IN THE DB
def find_missing_providers():
    all_movies = show_all_movies()
    updates = []
    for movie in all_movies:
        if not movie["moive_providers"]:
            providers = get_providers_for_movie(movie["movie_id"], movie["tmdb_id"])
            updates.extend(providers)
    return updates

# FIND PROVIDERS FOR SPECIFIC MOVIE
def get_providers_for_movie(movie_id, tmdb_id):
    endpoint = f'{BASE_URL}/movie/{tmdb_id}/watch/providers'
    params = {'api_key': API_KEY}
    response = requests.get(endpoint, params=params)    
    data = response.json()
    results = []
    if data["results"]:
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