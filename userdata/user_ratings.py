from flask import abort, make_response
from sqlalchemy import and_
from config import db
from userdata.models import UserRatings, UserRating_schema, UserRatings_schema


def show_all():
    ratings = UserRatings.query.all()
    return UserRatings_schema.dump(ratings)


def show_all_by_user(user_id):
    ratings = UserRatings.query.filter(
        UserRatings.user_id == user_id).all()
    return UserRatings_schema.dump(ratings)


def show_by_user_and_movie(user_id, movie_id):
    rating = UserRatings.query.filter(and_(
        UserRatings.user_id == user_id,
        UserRatings.movie_id == movie_id
        )).one_or_none()
    if rating is None: abort(404, "Rating not found for user")
    else: return UserRating_schema.dump(rating)


def add_rating_like(user_id, movie_id):
    existing = UserRatings.query.filter(and_(
        UserRatings.user_id == user_id,
        UserRatings.movie_id == movie_id
        )).one_or_none()
    if existing is None:
        return insert_rating(user_id, movie_id, True)
    else:
        existing.user_liked = True
        db.session.commit()
        return UserRating_schema.dump(existing), 201
    

def add_rating_dislike(user_id, movie_id):
    existing = UserRatings.query.filter(and_(
        UserRatings.user_id == user_id,
        UserRatings.movie_id == movie_id
        )).one_or_none()
    if existing is None:
        return insert_rating(user_id, movie_id, False)
    else:
        existing.user_liked = False
        db.session.commit()
        return UserRating_schema.dump(existing), 201


def insert_rating(user_id, movie_id, user_liked):
    new_entry = UserRating_schema.load({
        "user_id": user_id,
        "movie_id": movie_id,
        "user_liked": user_liked
        }, session=db.session)
    db.session.add(new_entry)
    db.session.commit()
    return UserRating_schema.dump(new_entry), 201


def remove_from_user_ratings(user_id, movie_id):
    db.session.query(UserRatings).filter(and_(
        UserRatings.user_id == user_id,
        UserRatings.movie_id == movie_id
        )).delete()
    db.session.commit()
    return 200


def clear_user_ratings(user_id):
    db.session.query(UserRatings).filter(
        UserRatings.user_id == user_id
        ).delete()
    db.session.commit()
    return 200


def clear_all():
    db.session.query(UserRatings).delete()
    db.session.commit()
    return 200

# Get All Records
# Get All For User
# Get For User and Movie
# Add to Liked
# Add to Disliked
    # Helper: Add Entry Generic
# Remove Entry For User
# Remove All Entries for user
# Empty Table