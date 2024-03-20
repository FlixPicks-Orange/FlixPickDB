from flask import abort, make_response
from datetime import datetime
from config import db
from userdata.models import Recommendations, Recommendation_schema, Recommendations_schema

def show_all():
    recommendations = Recommendations.query.all()
    return Recommendations_schema.dump(recommendations)

def add(entry):
    new_item = Recommendation_schema.load(entry, session=db.session)
    db.session.add(new_item)
    db.session.commit()
    return Recommendation_schema.dump(new_item), 201

def get_user_recommendations_by_userID(user_id):
    recommendations = Recommendations.query.filter(Recommendations.user_id == user_id).all()
    return Recommendations_schema.dump(recommendations)