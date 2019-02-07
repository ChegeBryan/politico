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

