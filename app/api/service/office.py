"""
Method for data manipulation between controller and models
in the mock db
"""
from flask import jsonify
from marshmallow import ValidationError

from app.api.db.mock_db import MockDB
from app.api.model.office import Office
from app.api.util.dto import office_schema, offices_schema


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
    officeName = data["officeName"]
    officeType = data["officeType"]
    isOccupied = data["isOccupied"]

    # create office object
    new_office = Office(officeName=officeName,
                        officeType=officeType, isOccupied=isOccupied)

    save_changes(new_office)
    # 1. serialize the input for response
    # 2. return serialized and proper format json to api endpoint
    response = office_schema.dump(new_office)
    response_object = jsonify({
        "status": 201,
        "data": [response]
    })
    return response_object, 201


def get_office(_id):
    """Method to display out the office to the get /offices/<uuid:id>"""
    office = Office.get_office_by_id(_id)
    if office:
        # response when office exists
        return jsonify({
            "status": 200,
            "data": [office_schema.dump(office)]
        }), 200
    else:
        # response when offices not found
        return jsonify({
            "status": 404,
            "error": "Resource /offices/{} not found".format(_id)
        }), 404


def get_offices():
    """Method to get all offices from list"""
    offices = offices_schema.dump(MockDB.OFFICES)
    return jsonify({
        "status": 200,
        "data": offices,
    }), 200


def save_changes(data):
    """ Write to the mock db """
    MockDB.OFFICES.append(data)
