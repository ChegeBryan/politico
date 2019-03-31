""" Methods for vote data manipulation between controller and the database """

from flask import request, jsonify
from marshmallow import ValidationError


from app.api.util.dto import vote_load_schema, vote_dump_schema
from app.api.model.vote import Vote
from app.api.model.user import User
from app.api.service.auth_helper import get_logged_in_user
from app.api.model import user
from app.api.db.database import AppDatabase as db


def save_new_vote(token, json_data):
    """Saves a new vote created by the signed on user

    Args:
        token (bytes): user signed in token
        json_data (json): candidate and office data
    """
    try:
        data = vote_load_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    office = data['office']
    candidate = data['candidate']

    data, status = get_logged_in_user(request)

    if status == 200:
        # get the user id from the decoded token
        user_id = data.get_json()['user'].get('user_id')
        new_vote = Vote(
            office=office,
            candidate=candidate
        )
        save_changes(user_id, new_vote)

        cast_vote_query = Vote.get_cast_vote(user_id=user_id, office_id=office)
        cast_vote = db().get_single_row(*cast_vote_query)
        # serialize vote data
        response = vote_dump_schema.dump(cast_vote)
        response_object = jsonify({
            "status": 201,
            "data": [response]
        })
        return response_object, 201
    else:
        # json response for authentication error encountered
        return data, status


def save_changes(_id, data):
    """commit the vote details to the database

    Args:
        _id (integer): user id
        data ([object]): vote instance
    """

    query, values = Vote.add_vote(data, user=_id)
    db().commit_changes(query, values)