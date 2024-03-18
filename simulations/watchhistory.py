import sqlite3 as sql
import random
import os, requests

def generate():
    user_list = []
    r = requests.get("http://localhost:3000/api/users")
    
    packet = r.json()

    for entry in packet:
        user_list.append(entry.get("id"))

    for user in user_list:
        number_to_add = random.randint(1,50)
        random_numbers = [random.randint(1,60) for _ in range (number_to_add)]
        for number in random_numbers:
            package = {
            "movie_id": number,
            "title" : "Default",
            "user_id" : int(user)

            }
            response = requests.post("http://localhost:3000/api/watch_history", json=package)
            print(response)

generate()