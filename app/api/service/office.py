"""
Method for data manipulation between controller and models
in the mock db
"""
from flask import jsonify

from app.api.db.mock_db import MockDB
from app.api.model.office import Office
from app.api.util.dto import office_schema


def save_new_office(json_data):
    """ Method to save new office to list """
    # Deserialize the data input against the office schema
    data = office_schema.load(json_data)
    officeName = data["officeName"]
    officeType = data["officeType"]
    isOccupied = data["isOccupied"]

    # create office object
    new_office = Office(officeName=officeName, officeType=officeType, isOccupied=isOccupied)

    save_changes(new_office)
    # 1. serialize the input for response
    # 2. return serialized and proper format json to api endpoint
    response = office_schema.dump(new_office)
    response_object = jsonify({
        "status": 201,
        "data": [response]
    })
    return response_object, 201

def save_changes(data):
    """ Write to the mock db """
    MockDB.OFFICES.append(data)

