"""
Method for data manipulation between controller and models
in the mock db
"""
from flask import jsonify
from marshmallow import ValidationError

from app.api.model.office import Office
from app.api.util.dto import office_schema, offices_schema
from app.api.db.database import AppDatabase as db


def save_new_office(json_data):
    """ Method to save new office to list """
    # Deserialize the data input against the office schema
    # check for validation errors
    try:
        data = office_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    office_name = data["office_name"]
    office_type = data["office_type"]
    is_occupied = data["is_occupied"]

    # create office object
    new_office = Office(
        office_name=office_name,
        office_type=office_type,
        is_occupied=is_occupied
    )

    return_id = save_changes(new_office)
    # 1. serialize the input for response
    # 2. return serialized and proper format json to api endpoint
    saved_office_query = Office.get_office_by_id(return_id)
    saved_office = db().get_single_row(*saved_office_query)
    response = office_schema.dump(saved_office)
    response_object = jsonify({
        "status": 201,
        "data": [response]
    })
    return response_object, 201


def get_office(_id):
    """Method to return the office from the database with the provided id

    Args:
        _id (integer): the office unique identifier

    Returns:
        1. json : the office found details in json format
        2. json : error if the office is not found
    """
    office_query = Office.get_office_by_id(_id)
    office = db().get_single_row(*office_query)
    if office:
        # response when office exists
        return jsonify({
            "status": 200,
            "data": [office_schema.dump(office)]
        }), 200

    # response when offices not found
    return jsonify({
        "status": 404,
        "error": "Resource /offices/{} not found".format(_id)
    }), 404


def get_offices():
    """Method to return all the offices from the database

    Returns:
        1. json : the offices found details in json format
    """
    offices_query = Office.get_offices_query()
    offices = db().get_all_rows(offices_query)
    response = offices_schema.dump(offices)
    return jsonify({
        "status": 200,
        "data": response,
    }), 200


def save_changes(data):
    """ Write to the mock db """
    query, values = Office.add_office(data)
    identifier = db().commit_changes_returning_id(query, values)
    return identifier
