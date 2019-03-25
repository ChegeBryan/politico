""" Method for data manipulation in the mock db """
from flask import jsonify
from marshmallow import ValidationError

from app.api.model.party import Party
from app.api.util.dto import party_schema, parties_schema
from app.api.db.database import AppDatabase as db


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
    logo_url = data['logo_url']

    # Query database for party by name
    party_by_name = Party.get_party_by_name(party_name)
    party = db().get_single_row(*party_by_name)
    if party is None:
        # if name is not taken
        new_party = Party(
            party_name=party_name,
            hq_address=hq_address,
            logo_url=logo_url
        )
        save_changes(new_party)
        # 1. serialize the input for response
        # 2. return serialized and proper format json to api endpoint
        party_saved = db().get_single_row(*party_by_name)
        response = party_schema.dump(party_saved)
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
    """Method to return the party from the database with the provided id

    Args:
        _id (integer): the party unique identifier

    Returns:
        1. json : the party found details in json format
        2. json : error if the party is not found
    """
    party_query = Party.get_party_by_id(_id)
    party = db().get_single_row(*party_query)
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
    """Method to return all the parties from the database

    Returns:
        1. json : the parties found details in json format
    """
    parties_query = Party.get_parties_query()
    parties = db().get_all_rows(parties_query)
    response = parties_schema.dump(parties)

    return jsonify({
        "status": 200,
        "data": response
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
    party_to_edit_query = Party.get_party_by_id(_id)
    party_to_edit = db().get_single_row(*party_to_edit_query)
    if party_to_edit:
        new_name = data["party_name"]
        # construct update party name query
        query, values = Party.update_party(_id, new_name)
        # persist changes to the database
        db().commit_changes(query, values)

        # query back the database for the edited party.
        party_edited = db().get_single_row(*party_to_edit_query)
        return jsonify({
            "status": 200,
            "data": [party_schema.dump(party_edited)]
        })
        # response when party not found
    else:
        return jsonify({
            "status": 404,
            "error": "Resource requested for edit not found."
        }), 404


def delete_party(_id):
    """delete the selected party

    Returns:
        1. json : response message o details in json format
    """
    # check if party to delete exists
    party_to_delete_query = Party.get_party_by_id(_id)
    party_to_delete = db().get_single_row(*party_to_delete_query)
    if party_to_delete:

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
    query, values = Party.add_party(data)
    db().commit_changes(query, values)
