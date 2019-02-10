""" Method for data manipulation in the mock db """
from flask import jsonify
from marshmallow import ValidationError

from app.api.db.mock_db import MockDB
from app.api.model.party import Party
from app.api.util.dto import party_schema, parties_schema


def save_new_party(json_data):
    # Deserialize the data input against the party schema
    # check if input values throw validation errors
    try:
        data = party_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    party_name = data['party_name']
    hq_address = data['hq_address']

    # Query database for party name
    party = Party.get_party_by_name(party_name)
    if party is None:
        # if name is not taken
        new_party = Party(
            party_name=party_name,
            hq_address=hq_address
        )
        save_changes(new_party)
        # 1. serialize the input for response
        # 2. return serialized and proper format json to api endpoint
        response = party_schema.dump(new_party)
        response_object = jsonify({
            "status": 201,
            "data": [response]
        })
        return response_object, 201
    else:
        # When name is taken
        return jsonify({
            "status": 409,
            "error": "Try a different Party name, Provided name is taken."
        }), 409


def get_party(_id):
    """Method to display out the party to the get /parties/<uuid:id>"""
    party = Party.get_party_by_id(_id)
    if party:
        # response when party exists
        return jsonify({
            "status": 200,
            "data": [party_schema.dump(party)]
        }), 200
    else:
        # response when party not found
        return jsonify({
            "status": 404,
            "error": "Resource /parties/{} not found".format(_id)
        }), 404


def get_parties():
    """Method to get all parties from list"""
    parties = parties_schema.dump(MockDB.PARTIES)
    return jsonify({
        "status": 200,
        "data": parties,
    }), 200


def edit_party(_id, json_data):
    """ Method to apply new changes to party details """
    try:
        data = party_schema.load(json_data, partial=True)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    party = Party.get_party_by_id(_id)
    if party:
        new_name = data["party_name"]
        party_edit = party.update_party(_id, new_name)
        return jsonify({
            "status": 200,
            "data": [party_schema.dump(party_edit)]
        })
    else:
        # response when party not found
        return jsonify({
            "status": 404,
            "error": "Resource requested for edit not found."
        }), 404


def delete_party(_id):
    """ Method to delete party and return response message """
    res = Party.delete_party(_id)
    if res:
        # response for successful deletion
        return jsonify({
            "status": 200,
            "data": [{
                "message": "Political Party deleted successfully."
            }]
        }), 200
    else:
        # response message when delete fails.
        return jsonify({
            "status": 404,
            "data": [{
                "message": "Political Party to delete not found."
            }]
        }), 404


def save_changes(data):
    """ Write to the mock db """
    MockDB.PARTIES.append(data)
