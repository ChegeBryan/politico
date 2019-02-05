""" Method for data manipulation in the mock db """
from flask import jsonify

from app.api.db.mock_db import MockDB
from app.api.model.party import Party
from app.api.util.dto import party_schema

def save_new_party(json_data):
    # Deserialize the data input against the party schema
    data = party_schema.load(json_data)

    party_name = data['party_name']
    hq_address = data['hq_address']

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


def save_changes(data):
    """ Write to the mock db """
    MockDB.PARTIES.append(data)
