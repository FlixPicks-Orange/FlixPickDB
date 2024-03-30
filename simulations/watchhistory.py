import random
import os, requests
from pyprobs import Probability as pr
# Source: https://stackoverflow.com/questions/14324472/get-a-random-boolean-by-percentage

def run_simulation(Operation, MinEntries, MaxEntries, RecFrequency):
    if Operation == 'UsePatterns':
        generate_pattern()
        return { "error": False, "message": "Simulated Watch History has been generated!" }
    elif Operation == 'Random':
        generate_random(MinEntries, MaxEntries, RecFrequency)
        return { "error": False, "message": "Simulated Watch History has been generated!" }
    else:
        return { "error": True, "message": "Unable to generate simulated Watch History" }


def generate_random(MinEntries, MaxEntries, RecFrequency):
    user_list = []
    r = requests.get(os.getenv('DB_URL') + "/users")
    packet = r.json()

    for entry in packet:
        user_list.append(entry.get("id"))

    for user in user_list:
        number_to_add = random.randint(MinEntries, MaxEntries)
        #random_numbers = [random.randint(1,20) for _ in range (number_to_add)]
        #random_numbers = set(random_numbers)
        #for number in random_numbers:
        for entry in range(number_to_add):
            # Generate Random Movie ID
            movie_id = random.randint(1, 380)
            # Pick True or False Based On Provided Frequency
            probabiltiy = RecFrequency / 100
            from_recommended = pr.prob(probabiltiy)
            #Insert Into Database
            package = {
            "movie_id": movie_id,
            "from_recommended" : from_recommended,
            "user_id" : int(user)
            }
            response = requests.post(os.getenv('DB_URL') + "/watch_history", json=package)
            print(response)


def generate_pattern():
    user_list = []
    r = requests.get(os.getenv('DB_URL') + "/users")
    packet = r.json()

    for entry in packet:
        user_list.append(entry.get("id"))
        
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
