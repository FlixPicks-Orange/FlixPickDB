import os, requests
def generate():
    user_list = []
    r = requests.get(os.getenv('DB_URL') + "/users")
    
    packet = r.json()

    for entry in packet:
        user_list.append(entry.get("id"))

    for user in user_list:
        numbers = list(range(1,21))
        
        for number in numbers:
            package = {
            "movie_id": number,
            "title" : "Default",
            "user_id" : int(user)

            }
            response = requests.post(os.getenv('DB_URL') + "/recommendations", json=package)
            print(response)