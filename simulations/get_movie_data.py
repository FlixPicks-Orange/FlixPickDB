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