""" Office model """

import uuid

from app.api.db.mock_db import MockDB


class Office:
    """
    Office model
    """
    def __init__(self, officeName, officeType, isOccupied):
        self.officeId = uuid.uuid4()
        self.officeName = officeName
        self.officeType = officeType
        self.isOccupied = False

    def office_jsonified(self):
        """ Return a office object as json """
        return {
            "officeId": self.officeId,
            "officeName": self.officeName,
            "officeType": self.officeType,
            "isOccupied": self.isOccupied
        }

