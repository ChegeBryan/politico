""" Methods for petition data manipulation
 between controller and the database
"""

from flask import jsonify, request
from marshmallow import ValidationError
from psycopg2 import IntegrityError


from app.api.model.petition import Petition
from app.api.util.dto import petition_load_schema, petitions_dump_schema
from app.api.service.auth_helper import get_logged_in_user
from app.api.db.database import AppDatabase as db


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

    # check endpoint authorization
    res, status = get_logged_in_user(request)

    if status == 200:
        # get the user id from the decoded token
        created_by = res.get_json()['user'].get('user_id')

        new_petition = Petition(
            office=office,
            contested_by=contested_by,
            created_by=created_by,
            body=body,
            evidence=evidence
        )

        try:
            # save the petition and return the id created thereafter
            petition_id = save_changes(new_petition)
        except IntegrityError:
            return jsonify({
                "status": 404,
                "message": "Office and candidate referenced does not exist."
            }), 404

        petition_query = Petition.get_petition_by_id(petition_id)
        petition = db().get_single_row(*petition_query)

        # serialize the petition details
        serialized_petition = petitions_dump_schema.dump(petition)
        response_object = jsonify({
            "status": 201,
            "data": serialized_petition
        })
        return response_object, 201
    # if status code == 401
    return res, status


def save_changes(data):
    """commit the petition details to the database

    Args:
        data (object): petition details
    """
    query, values = Petition.add_petition(data)
    petition_id = db().commit_changes_returning_id(query, values)

    return petition_id
