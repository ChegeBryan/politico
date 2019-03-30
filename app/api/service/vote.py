""" Methods for vote data manipulation between controller and the database """

from flask import jsonify
from marshmallow import ValidationError


from app.api.util.dto import vote_load_schema
from app.api.model.vote import Vote
from app.api.model.user import User
from app.api.service.auth_helper import get_logged_in_user
from app.api.model import user


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

    data, status = get_logged_in_user(token)

    if status == 200:
        user_id = data.get_json()['user'].get('id')
    else:
        return data, status
