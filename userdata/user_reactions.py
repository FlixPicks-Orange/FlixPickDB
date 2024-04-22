from flask import abort, make_response, jsonify
from sqlalchemy import func
from config import db
from userdata.models import UserReactions, UserReaction_schema, UserReactions_schema

def show_all():
    reactions = UserReactions.query.all()
    return UserReactions_schema.dump(reactions)

def insert_reaction(user_id, movie_id, timestamp, emoticon):
    known_emoticons = {
        "U+1F60D":"Love",
        "U+1F923":"Laughing",
        "U+1F600":"Happy",
        "U+1F60E":"Cool",
        "U+1F621":"Angry",
        "U+1F92E":"Disgusted",
        "U+1F622":"Sad",
        "U+1F62D":"Crying",
        "U+1F631":"Shocked",
        "U+1F47B":"Spooky",
        "U+1F92F":"Mind Blown",
        "U+1F971":"Bored",
    }
    reaction = known_emoticons[emoticon]
    reaction = UserReaction_schema.load({
        "user_id": user_id,
        "movie_id": movie_id,
        "timestamp": int(timestamp),
        "emoticon": emoticon,
        "reaction": reaction
    })
    db.session.add(reaction)
    db.session.commit()
    return UserReaction_schema.dump(reaction), 201


def movie_reaction_summary(movie_id): 
    summary = db.session.query(
        UserReactions.reaction,
        UserReactions.timestamp,
        func.count().label('reaction_count')
    ).filter(
        UserReactions.movie_id == movie_id
    ).group_by(
        #UserReactions.reaction,
        UserReactions.timestamp
    ).all()
    
    summary_list = []
    for row in summary:
        #time = round(row[1], -1)
        summary_dict = {
    #        'reaction': row[0],
            'timestamp': row[1],
            'reaction_count': row[2]
        }
        summary_list.append(summary_dict)

    return jsonify(summary_list)