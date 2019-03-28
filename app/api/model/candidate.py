""" Candidate database model and methods """

import datetime


class Candidate:
    """Candidate class and methods for database manipulation
    """

    def __init__(self, candidate, office=None, party=None):
        self.candidate = candidate
        self.office = office
        self.party = party
        self.created_on = datetime.datetime.now()
