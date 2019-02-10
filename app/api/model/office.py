""" Office model """

import uuid

from app.api.db.mock_db import MockDB
from app.api.model.helper import get_item


class Office:
    """
    Office model
    """

    def __init__(self, officeName, officeType, isOccupied):
        self._id = uuid.uuid4()
        self.officeName = officeName
        self.officeType = officeType
        self.isOccupied = False

    def office_jsonified(self):
        """ Return a office object as json """
        return {
            "officeId": self._id,
            "officeName": self.officeName,
            "officeType": self.officeType,
            "isOccupied": self.isOccupied
        }

    @staticmethod
    def get_office_by_id(identifier):
        """Method to get office in the OFFICES list by its ID"""
        return get_item(identifier, MockDB.OFFICES)
