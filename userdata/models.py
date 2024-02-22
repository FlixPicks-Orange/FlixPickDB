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
    title = db.Column(db.String(255))
    watched = db.Column(db.DateTime, default=datetime.utcnow)
    
class WatchHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WatchHistory
        load_instance = True
        sqla_session = db.session

WatchHistory_schmea = WatchHistorySchema()
WatchHistorys_schmea = WatchHistorySchema(many=True)