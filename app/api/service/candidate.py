""" Methods for candidate data manipulation
 between controller and the database
"""

from flask import jsonify
from marshmallow import ValidationError


from app.api.model.candidate import Candidate
from app.api.util.dto import candidate_load_schema, candidate_dump_schema
from app.api.db.database import AppDatabase as db


def save_new_candidate(office_id, json_data):
    """Create a candidate instance and save the data to database

    Args:
        office_id (integer): office the user is been registered as candidate to
        json_data (json): user details and party user belongs to.
    """

    # Deserialize the data input against the candidate schema
    # check if input values throw validation errors
    try:
        data = candidate_load_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    candidate = data['candidate']
    party = data['party']

    # create candidate object
    new_candidate = Candidate(
        candidate=candidate,
        party=party,
    )
    save_changes(office_id, new_candidate)

    # query database for the candidate
    candidate_by_id = Candidate.get_candidate_by_id(candidate)
    candidate_registered = db().get_single_row(*candidate_by_id)
    response = candidate_dump_schema.dump(candidate_registered)

    response_object = jsonify({
        "status": 201,
        "data": [response]
    })
    return response_object, 201


def save_changes(_id, data):
    """commit the candidate details to the database

    Args:
        _id (integer): office id from the endpoint url
        data ([object]): candidate instance
    """
    query, values = Candidate.add_candidate(data, office_id=_id)
    db().commit_changes(query, values)
