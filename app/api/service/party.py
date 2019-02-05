""" Method for data manipulation in the mock db """

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


def save_changes(data):
    """ Write to the mock db """
    MockDB.PARTIES.append(data)
