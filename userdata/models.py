from datetime import datetime
from config import db, ma

# User Model
class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    role = db.Column(db.String(32), default="Standard")
    registration_date = db.Column(db.DateTime,  default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    limit_subscriptions = db.Column(db.Boolean, default=True)
    survey_check = db.Column(db.Boolean, default=False)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schmea = UserSchema()
users_schema = UserSchema(many=True)


# Watch History Model
class WatchHistory(db.Model):
    __tablename__ = "WatchHistory"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    watched = db.Column(db.DateTime, default=datetime.utcnow)
    from_recommended = db.Column(db.Boolean, default=False)
    supressed = db.Column(db.Boolean, default=False)
    
class WatchHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WatchHistory
        load_instance = True
        sqla_session = db.session

WatchHistory_schema = WatchHistorySchema()
WatchHistorys_schema = WatchHistorySchema(many=True)


# Subscriptions Model
class Subscription(db.Model):
    __tablename__ = "Subscriptions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    provider_id = db.Column(db.Integer)
    
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription
        load_instance = True
        sqla_session = db.session

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)


# Recommendations Model
class Recommendations(db.Model):
    __tablename__ = "Recommendations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    recommended = db.Column(db.DateTime, default=datetime.utcnow)

class RecommendationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recommendations
        load_instance = True
        sqla_session = db.session

Recommendations_schema = RecommendationsSchema()
Recommendationss_schema = RecommendationsSchema(many=True)


# User Ratings Model
class UserRatings(db.Model):
    __tablename__ = "User_Ratings"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    user_liked = db.Column(db.Boolean)

class UserRatingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserRatings
        load_instance = True
        sqla_session = db.session

UserRating_schema = UserRatingsSchema()
UserRatings_schema = UserRatingsSchema(many=True)

class UserClicks(db.Model):
    __tablename__ = "User_Clicks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    page_id = db.Column(db.Integer)
    click_num = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class UserClicksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserClicks
        load_instance = True
        sqla_session = db.session

UserClick_schema = UserClicksSchema()
UserClicks_schema = UserClicksSchema(many=True)

"""class Interactions(db.Model):
    __tablename__ = "Interactions"
    
class InteractionsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Interactions
        load_instance = True
        sqla_session = db.session

interaction_schema = InteractionsSchema()
interactons_schema = InteractionsSchema(many=True)"""