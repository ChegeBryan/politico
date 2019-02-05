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

