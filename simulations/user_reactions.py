import random
import os, requests
from pyprobs import Probability as pr
from userdata.watch_history import show_all as get_watch_history
from userdata.user_reactions import insert_reaction as insert_reaction

# variables:
    # reactions per movie
    # 
# Read current watch history
# Each row represents a user watching a movie
    # How many reactions?
    # How close together are reactions? clusters?
    # Type of reactions?
        # Happy reactions, sad reactions, scared/shocked reactions, mad/bored/gross
        
        
def simulate_user_reactions(min, max):
    watched_movies = get_watch_history()
    prev_movie_id = 0
    for movie in watched_movies:
        # Select current movie id
        movie_id = movie["movie_id"]
        user_id = movie["user_id"]
        # Change reaction group for each different movie
        if movie_id != prev_movie_id:
            reactions = list(load_reaction_group())
            prev_movie_id = movie_id
        # Add some number of reactions for this user
        num_of_reactions = random.randint(min, max)
        for i in range(num_of_reactions):
            timestamp = round(random.randint(1,120), -1)
            rnum = random.randint(0, len(reactions)-1)
            reaction = reactions[rnum]
            insert_reaction(movie_id, user_id, timestamp, reaction)        


def load_reaction_group():
    reaction_group = random.randint(1, 5)
    if reaction_group == 5:
        return {
        "U+1F60D":"love",
        "U+1F923":"Laughing",
        "U+1F600":"Happy",
        "U+1F60E":"Cool",
        }
    if reaction_group == 4:
        return {
        "U+1F622":"Sad",
        "U+1F62D":"Crying",
        }
    if reaction_group == 3:
        return {
        "U+1F621":"Angry",
        "U+1F92E":"Disgusted",
        "U+1F971":"Bored",
        }
    if reaction_group == 2:
        return {
        "U+1F622":"Sad",
        "U+1F62D":"Crying",
        "U+1F971":"Bored",
        }
    if reaction_group == 1:
        return {
        "U+1F60E":"Cool",
        "U+1F631":"Shocked",
        "U+1F47B":"Spooky",
        "U+1F92F":"Mind Blown",
        }