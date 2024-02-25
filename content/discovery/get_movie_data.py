import requests

def get_movies():
    api_key = '50cb1ca5b03be4ca02207aa9a63691a5'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_movies_list(page):
    api_key = '50cb1ca5b03be4ca02207aa9a63691a5'
    base_url = 'https://api.themoviedb.org/3'
    endpoint = f'{base_url}/discover/movie'
    params = {
        'api_key': api_key,
        'page': page,
        'language':'en-US',
        'region': 'US',
        'sort_by':'popularity.desc',
        'watch_region': 'US',
        'with_watch_providers': '8|9|15|337|1899',
        'primary_release_date.gte':'1980-01-01',
        'primary_release_date.lte':'2024-02-24'
    }
    response = requests.get(endpoint, params=params)
    return response.json()

def download_all_movies():
    all_movies = []
    page = 1    
    while page < 20:
        data = get_movies_list(page)
        movies = data.get('results', [])
        #movies = [movie['id'] for movie in data.get('results', [])]
        if not movies:
            break
        all_movies.extend(movies)
        page += 1
    return all_movies
    

def get_providers():
    api_key = '50cb1ca5b03be4ca02207aa9a63691a5'
    url = f'https://api.themoviedb.org/3/watch/providers/movie?api_key={api_key}&language=en-US'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def show_movie_providers(tmdb_id):
    api_key = '50cb1ca5b03be4ca02207aa9a63691a5'
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}/watch/providers?api_key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        return data["results"]["US"]
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def show_movie(tmdb_id):
    api_key = '50cb1ca5b03be4ca02207aa9a63691a5'
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None