""" Methods for petition data manipulation
 between controller and the database
"""

from flask import jsonify, request
from marshmallow import ValidationError


from app.api.model.petition import Petition
from app.api.util.dto import petition_load_schema
from app.api.service.auth_helper import get_logged_in_user


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

    # get petition details from the validated json input
    office = data["office"]
    contested_by = data["contested_by"]
    body = data["body"]
    evidence = data["evidence"]

    created_by = get_logged_in_user(request)

    new_petition = Petition(
        office=office,
        contested_by=contested_by,
        created_by=created_by,
        body=body,
        evidence=evidence
    )
