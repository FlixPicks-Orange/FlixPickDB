from datetime import datetime
from config import db, ma


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    registration_date = db.Column(db.DateTime,  default=datetime.utcnow)
    role = db.Column(db.String(32), default="Standard")

    
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session


user_schmea = UserSchema()
users_schema = UserSchema(many=True)
