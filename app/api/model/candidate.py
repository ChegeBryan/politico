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

    def add_candidate(self, office_id):
        """SQL query to add a candidate to the candidates table

        Args:
            office_id (integer): office to register a candidate to
        """
        query = """
        INSERT INTO
          candidates(office_id, candidate_id, party_id, created_on)
          VALUES(%s, %s, %s, %s);
        """
        values = (office_id, self.candidate, self.party, self.created_on)

        return query, values
