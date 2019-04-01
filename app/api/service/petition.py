""" Methods for petition data manipulation
 between controller and the database
"""

from flask import jsonify
from marshmallow import ValidationError


from app.api.model.petition import Petition
from app.api.util.dto import petition_load_schema


def save_new_petition(json_data):
    """Save the petition to the petition table and return appropriate
    response to endpoint

    Args:
        json_data (json): petition details.
    """
    try:
        data = petition_load_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
