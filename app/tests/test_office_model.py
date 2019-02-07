# tests for office model

import unittest
import uuid


from app.api.model.office import Office


class TestOfficeModel(unittest.TestCase):
    """ Test class for office model """
    def setUp(self):
        """
        Creation of office object
        :arg: officeId, officeName, officeType, isOccupied
        :return: office object
        """
        _id = uuid.uuid4()
        self.new_office = Office(
            'Senate',
            'Congress',
            False
        )

