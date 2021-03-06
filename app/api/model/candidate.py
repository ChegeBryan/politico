""" Candidate database model and methods """

import datetime


class Candidate:
    """Candidate class and methods for database manipulation
    """

    def __init__(self, candidate, party):
        self.candidate = candidate
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

    @staticmethod
    def get_candidate_by_id(identifier):
        """SQL query to get a candidate from the database

        Args:
            identifier (integer): candidate id

        returns:
            query (string): select SQL for candidate with provided identifier
        """
        sql = """SELECT * FROM candidates WHERE candidate_id=%s;"""
        query = sql, (identifier,)
        return query

    @staticmethod
    def get_office_party_by_id(office_id, party_id):
        """SQL query to get a office from the database

        Args:
            office_id (integer): office id
            party_id (integer): party id

        returns:
            query (string): select SQL for office and party with ids
        """
        sql = """SELECT * FROM candidates WHERE office_id=%s AND party_id=%s;"""
        query = sql, (office_id, party_id)
        return query
