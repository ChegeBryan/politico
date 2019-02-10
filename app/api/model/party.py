""" Party model """

import uuid

from app.api.db.mock_db import MockDB


class Party:
    """
    Party model class
    """

    def __init__(self, party_name, hq_address):
        self.party_id = uuid.uuid4()
        self.party_name = party_name
        self.hq_address = hq_address

    def party_jsonified(self):
        """ Return a party object on json like format """
        return {
            "party_id": self.party_id,
            "party_name": self.party_name,
            "hq_address": self.hq_address
        }

    @staticmethod
    def get_party_by_name(name):
        """Method to get a party in the PARTIES list by its name"""
        for party in MockDB.PARTIES:
            if party.party_name == name:
                return party

    @staticmethod
    def get_party_by_id(identifier):
        """Method to get a Party in the PARTIES list by its ID"""
        for party in MockDB.PARTIES:
            if party.party_id == identifier:
                return party

    @staticmethod
    def update_party(_id, name):
        """ Method to update the name and address of called party """
        for party in MockDB.PARTIES:
            if party.party_id == _id:
                party.party_name = name
                return party

    @staticmethod
    def delete_party(_id):
        """ Method to delete party from parties list """
        for party in MockDB.PARTIES:
            if party.party_id == _id:
                MockDB.PARTIES.remove(party)
                return True
            else:
                return False
