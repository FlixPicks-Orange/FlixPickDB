from flask import abort, make_response
from datetime import datetime
from config import db
from userdata.models import Subscription, subscription_schema, subscriptions_schema
from userdata.models import UserRatings, UserRating_schema, UserRatings_schema
from userdata.models import Interactions, interaction_schema, interactons_schema

""" 
A Registered User who watched a trailer for more than 3 seconds shall be captured in the database
"""
"""def trailer_watched():
    pass

def wheel_submit():
    pass

def wheel_spins():
    pass

def most_used_provider():
    pass

def cineroll_count():
    pass"""