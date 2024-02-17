from flask import abort, make_response
from datetime import datetime
from config import db
from userdata.models import WatchHistory, WatchHistory_schmea

def show_all():
    history = WatchHistory.query.all()
    return WatchHistory_schmea.dump(history)