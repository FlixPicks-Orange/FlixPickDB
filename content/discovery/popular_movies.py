import requests

API_KEY = '50cb1ca5b03be4ca02207aa9a63691a5'
BASE_URL = "https://api.themoviedb.org/3"

def find_popular_movies():
    #endpoint = f'{BASE_URL}/movie/popular'
    #params = {
    #    'api_key': API_KEY,
    #    'region': 'US',
    #    'page': 1
    #    }
    movie_results = []
    page = 1    
    while page <= 4:
        endpoint = f'{BASE_URL}/discover/movie'
        params = {
            'api_key': API_KEY,
            'page': page,
            'language':'en-US',
            'region': 'US',
            'sort_by':'popularity.desc',
            'watch_region': 'US',
            'with_watch_providers': '8|9|15|337|1899',
            'with_watch_monetization_types': 'flatrate',
            'primary_release_date.gte':'1980-01-01',
            'primary_release_date.lte':'2024-02-24'
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        movies = data.get('results', [])
        movie_results.extend(movies)
        page += 1
    return movie_results
