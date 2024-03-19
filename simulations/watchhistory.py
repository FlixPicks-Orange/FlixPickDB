import random
import os, requests

def generate():
    user_list = []
    r = requests.get(os.getenv('DB_URL') + "/users")
    
    packet = r.json()

    for entry in packet:
        user_list.append(entry.get("id"))

    for user in user_list:
        number_to_add = random.randint(3,10)
        random_numbers = [random.randint(1,20) for _ in range (number_to_add)]
        random_numbers = set(random_numbers)
        for number in random_numbers:
            package = {
            "movie_id": number,
            "title" : "Default",
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
            "title" : "Default",
            "user_id" : int(user)

            }
            response = requests.post(os.getenv('DB_URL') + "/watch_history", json=package)
            print(response)

#generate()