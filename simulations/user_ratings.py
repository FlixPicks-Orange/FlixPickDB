import random
import os, requests
from userdata.user_ratings import add_rating_like, add_rating_dislike
import userdata.watch_history
from pyprobs import Probability as pr

#almost there
def run_simulation(ProbRating, ProbLikes):
    watch_history = userdata.watch_history.show_all()
    for entry in watch_history:
        if pr.prob(ProbRating/100):
            movie_id = random.randint(1, 380)
            if pr.prob(ProbLikes/100): add_rating_like(entry["user_id"], entry["movie_id"])
            else: add_rating_dislike(entry["user_id"], entry["movie_id"])
    return { "error": False, "message": "Simulated User Ratings have been generated!" }
    
def clear():
    r = requests.delete(os.getenv('DB_URL') + "/user_ratings/clear")
    print(f"Clear response {r.status_code}")