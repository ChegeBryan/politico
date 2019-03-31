""" Vote database model and methods """

import datetime as dt


class Vote:
    """ Vote class for and methods for database manipulation """

    def __init__(self, office, candidate):
        self.office = office
        self.candidate = candidate
        self.created_on = dt.datetime.now()

    def add_vote(self, user):
        """SQL query to insert a vote to database

        Args:
            user (integer): user who made the vote
        """
        query = """INSERT INTO
          votes(office_id, candidate_id, created_by, created_on)
        VALUES(%s, %s, %s, %s);
        """
        values = (self.office, self.candidate, user, self.created_on)

        return query, values

    @staticmethod
    def get_cast_vote(user_id, office_id):
        """SQL query to return vote cast by user for particular office

        Args:
            user_id (integer): id of user who made the vote
            office_id (integer): office user voted for
        """
        sql = """SELECT * FROM votes WHERE office_id=%s AND created_by=%s;"""
        query = sql, (office_id, user_id)

        return query

