""" Methods for candidate data manipulation
 between controller and the database
"""

from flask import jsonify
from marshmallow import ValidationError
from psycopg2 import IntegrityError


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
    office = office_id

    # check if the office and part provied are have a candidate under a certain
    # party
    party_represented = check_party_is_registered(office_id=office,
                                                  party_id=party)
    # check if the candidate provided is already registered
    # in another office
    registered_candidate = check_user_is_registered(candidate)
    if party_represented is None and registered_candidate is None:

        new_candidate = Candidate(
            candidate=candidate,
            party=party
        )
        try:
            save_changes(_id=office_id, data=new_candidate)
        except IntegrityError:
            # json when integrityError in the database is raised caused by
            # foreign key referencing
            response_object = jsonify({
                "status": 409,
                "error": "Party, office or user referenced does not exists."
            })
            return response_object, 409
    else:
        response_object = jsonify({
            "status": 409,
            "error": "Party or user exists under an office."
        })
        return response_object, 409

    # query serialize the results from the database
    candidate_by_id = Candidate.get_candidate_by_id(candidate)
    candidate_registered = db().get_single_row(*candidate_by_id)
    response = candidate_dump_schema.dump(candidate_registered)

    response_object = jsonify({
        "status": 201,
        "data": [response]
    })
    return response_object, 201


def check_party_is_registered(office_id, party_id):
    """check from the database if a party is already registered for an office

    Args:
        office_id (integer): office to check
        party_id (integer): party to check
    """
    office_party_query = Candidate.get_office_party_by_id(office_id, party_id)
    office_party = db().get_single_row(*office_party_query)
    if office_party:
        return office_party


def check_user_is_registered(candidate_id):
    """Check if a candidate is already registered as a candidate

    Args:
        candidate_id (integer): the candidate unique identifier
    """
    # query database for the candidate
    candidate_by_id = Candidate.get_candidate_by_id(candidate_id)
    candidate_registered = db().get_single_row(*candidate_by_id)

    if candidate_registered:
        return candidate_registered


def save_changes(_id, data):
    """commit the candidate details to the database

    Args:
        _id (integer): office id from the endpoint url
        data ([object]): candidate instance
    """
    query, values = Candidate.add_candidate(data, office_id=_id)
    db().commit_changes(query, values)
