from flask import abort, make_response
from datetime import datetime
from config import db
from userdata.models import Recommendations, Recommendations_schema, Recommendationss_schema

def show_all():
    recommendations = Recommendations.query.all()
    return Recommendationss_schema.dump(recommendations)

def add(entry):
    new_item = Recommendations_schema.load(entry, session=db.session)
    db.session.add(new_item)
    db.session.commit()
    return Recommendations_schema.dump(new_item), 201

def lookup_by_id(user_id):
    recommendations = Recommendations.query.filter(Recommendations.user_id == user_id).all()
    return Recommendationss_schema.dump(recommendations), 201

def clear_all():
    db.session.query(Recommendations).delete()
    db.session.commit()
    return 200