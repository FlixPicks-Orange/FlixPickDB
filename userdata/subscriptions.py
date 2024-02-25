from flask import abort, make_response, jsonify
from sqlalchemy import and_
from config import db
from userdata.models import Subscription, subscription_schema, subscriptions_schema

# https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.filter

def show_all():
    all_subscriptions = Subscription.query.all()
    return subscriptions_schema.dump(all_subscriptions)

# lookup all subs for user
def lookup_by_id(user_id):
    subscriptions = Subscription.query.filter(Subscription.user_id == user_id).all()
    return subscriptions_schema.dump(subscriptions), 200
        
# add sub for user
def add(user_id, provider_id):
    existing = Subscription.query.filter(and_(
            Subscription.user_id == user_id,
            Subscription.provider_id == provider_id
        )).one_or_none()
    if existing is None:
        new_item = subscription_schema.load({
            'user_id': user_id,
            'provider_id': provider_id
            }, session=db.session)
        db.session.add(new_item)
        db.session.commit()
        return subscription_schema.dump(new_item), 201
    else:
        response = {
            'error': 'Duplicate Entry',
            'message': 'Subscription provided already exists.'
        }
        return make_response(jsonify(response), 409)

# remove sub for user
def delete(user_id, provider_id):
    existing = Subscription.query.filter(and_(
            Subscription.user_id == user_id,
            Subscription.provider_id == provider_id
        )).one_or_none()
    if existing:
        Subscription.query.filter(Subscription.id == existing.id).delete()
        db.session.commit()
        response = make_response(jsonify(message="Subscription removed successfully"), 200)
        return response
    else:
        abort(404, f"Subscription not found")