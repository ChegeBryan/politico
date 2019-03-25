""" Office model """

from app.api.db.mock_db import MockDB
from app.api.model.helper import get_item


class Office:
    """
    Office model
    """

    def __init__(self, office_name, office_type, is_occupied):
        self.office_name = office_name
        self.office_type = office_type
        self.is_occupied = False

    def add_office(self):
        """ add an office object to the parties table

        Returns:
            tuple : insert sql query, values(the object initialization
                    attributes)
        """
        query = """INSERT INTO
          offices(office_name, office_type, is_occupied)
          VALUES (%s,%s,%s);
          """
        values = (self.office_name, self.office_type, self.is_occupied)

        return query, values

    @staticmethod
    def get_office_by_id(identifier):
        """Method to get office in the OFFICES list by its ID"""
        return get_item(identifier, MockDB.OFFICES)
