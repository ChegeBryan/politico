""" Petition database model and methods """

import datetime as dt


class Petition:
    """Petition class methods that involve reading
    and writing to the database
    """

    def __init__(self, **kwargs):
        self.office = kwargs.get("office")
        self.contested_by = kwargs.get("contested_by")
        self.created_by = kwargs.get("created_by")
        self.body = kwargs.get("body")
        self.evidence = kwargs.get("evidence")
        self.created_on = dt.datetime.now()

    def add_petition(self):
        """SQl query to add petition to database

        Args:
            user_id (integer): user creating the petition
        """
        query = """INSERT INTO
          petitions (office_id, contested_by, created_by,
           body, evidence, created_on)
          VALUES (%s,%s,%s,%s,%s,%s) RETURNING id;
        """
        values = (self.office, self.contested_by, self.created_by, self.body,
                  self.evidence, self.created_on)
        return query, values
