""" Party model """

import uuid

class Party:
    """
    Party model class
    """
    def __init__(self, party_name, hq_address):
        self.party_id = str(uuid.uuid4())
        self.party_name = party_name
        self.hq_address = hq_address

    def party_jsonified(self):
        """ Return a party object on json like format """
        return {
            "party_id": self.party_id,
            "party_name": self.party_name,
            "hq_address": self.hq_address
        }

