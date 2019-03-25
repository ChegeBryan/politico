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

    def office_jsonified(self):
        """ Return a office object as json """
        return {
            "officeName": self.officeName,
            "officeType": self.officeType,
            "isOccupied": self.isOccupied
        }

    @staticmethod
    def get_office_by_id(identifier):
        """Method to get office in the OFFICES list by its ID"""
        return get_item(identifier, MockDB.OFFICES)
