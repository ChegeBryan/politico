""" Methods for vote data manipulation between controller and the database """

from flask import jsonify
from marshmallow import ValidationError


from app.api.util.dto import vote_load_schema
from app.api.model import vote


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

