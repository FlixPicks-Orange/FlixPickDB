import os, requests
from userdata.users import get_all_user_ids

def generate():
    user_list = get_all_user_ids()
    for user in user_list:
        numbers = list(range(1,380))
        for number in numbers:
            package = {
            "movie_id": number,
            "title" : "Default",
            "user_id" : int(user)
            }
            response = requests.post(os.getenv('DB_URL') + "/recommendations", json=package)
            print(response)

def clear():
    r = requests.delete(os.getenv('DB_URL') + "/recommendations/clear")
    print(f"Clear response {r.status_code}")