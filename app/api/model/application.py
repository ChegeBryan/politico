""" Applications database model and methods """

import datetime


class Application:
    """Application class for and methods for database manipulation
    """

    def __init__(self, party, office):
        """application class properties registered when an instance of this
        class is created

        Args:
            party (int): id of a registered party
            office (int): id of a registered office
        """
        self.party = party
        self.office = office
        self.requested_on = datetime.datetime.now()

    def add_application(self, user_id):
        """SQL query to add a user application for office user

        Args:
            user_id (integer): user who made the application request
        """
        query = """
        INSERT INTO
          applications(applicant_id, office_id, party_id, requested_on)
          VALUES(%s, %s, %s, %s);
        """
        values = (user_id, self.office, self.party, self.requested_on)

        return query, values

    @staticmethod
    def get_application(user_id):
        """SQL query to get an application entry of a user

        Args:
            user_id (integer): user who made the application

        Returns:
            string: select application sql query
        """
        sql = """SELECT * FROM applications WHERE applicant_id=%s;"""
        query = sql, (user_id,)
        return query
