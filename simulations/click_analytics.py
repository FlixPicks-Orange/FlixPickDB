import random
import os, requests
from userdata.users import get_all_user_ids
from pyprobs import Probability as pr
# Source: https://stackoverflow.com/questions/14324472/get-a-random-boolean-by-percentage

def run_simulation(Operation, MinEntries, MaxEntries, ProbFrequency):
    if Operation == 'Random':
        generate_random(MinEntries, MaxEntries, ProbFrequency)
        return { "error": False, "message": "Simulated Watch History has been generated!" }
    else:
        return { "error": True, "message": "Unable to generate simulated Watch History" }

#Do this:
def generate_random(MinEntries, MaxEntries, ProbFrequency):
    user_list = get_all_user_ids()
    for user in user_list:
        
     

# def clear():
#     r = requests.delete(os.getenv('DB_URL') + "/watch_history/clear")
#     print(f"Clear response {r.status_code}")