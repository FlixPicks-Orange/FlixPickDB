import random
import os, requests
from userdata.users import get_all_user_ids
from content.movie_providers import get_id_by_movie_id as get_movie_providers
from pyprobs import Probability as pr
# Source: https://stackoverflow.com/questions/14324472/get-a-random-boolean-by-percentage

def run_simulation(Operation, MinEntries, MaxEntries, ProbFrequency):
    if Operation == 'UsePatterns':
        generate_pattern()
        return { "error": False, "message": "Simulated Watch History has been generated!" }
    elif Operation == 'Random':
        generate_random(MinEntries, MaxEntries, ProbFrequency)
        return { "error": False, "message": "Simulated Watch History has been generated!" }
    else:
        return { "error": True, "message": "Unable to generate simulated Watch History" }


def generate_random(MinEntries, MaxEntries, ProbFrequency):
    if MaxEntries < MinEntries: MaxEntries = MinEntries
    user_list = get_all_user_ids()
    for user in user_list:
        number_to_add = random.randint(MinEntries, MaxEntries)
        for entry in range(number_to_add):
            movie_id = random.randint(1, 380)
            #available_providers = [8, 15, 337, 9, 1899]
            #which_one = random.randint(0, 4)
            #provider_id = available_providers[which_one]
            available_providers = get_movie_providers(movie_id)
            which_one = random.randint(0, len(available_providers) - 1)
            provider_id = available_providers[which_one]
            from_recommended = pr.prob(ProbFrequency/100)
            package = {
            "movie_id": movie_id,
            "provider_id": provider_id,
            "from_recommended" : from_recommended,
            "user_id" : int(user)
            }
            response = requests.post(os.getenv('DB_URL') + "/watch_history", json=package)
            print(response)


def generate_pattern():
    user_list = get_all_user_ids()
    for user in user_list:
        group = random.randint(1,4)
        if group == 1:
            movielist = [100,101,102,103,104,105]
        if group == 2:
            movielist = [100,101,102,103]
        if group == 3:
            movielist = [200, 201, 202,203,204,205]
        if group == 4:
            movielist = [200, 201,202,203]
        for number in movielist:
            package = {
            "movie_id": number,
            "from_recommended" : False,
            "user_id" : int(user)
            }
            response = requests.post(os.getenv('DB_URL') + "/watch_history", json=package)
            print(response)


def clear():
    r = requests.delete(os.getenv('DB_URL') + "/watch_history/clear")
    print(f"Clear response {r.status_code}")
