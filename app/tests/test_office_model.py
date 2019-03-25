# tests for office model

import unittest


from app.api.model.office import Office
from app.api.db.mock_db import MockDB
from app.api.service.office import save_changes


class TestOfficeModel(unittest.TestCase):
    """ Test class for office model """

    def setUp(self):
        """
        Creation of office object
        :arg: officeName, officeType, isOccupied
        :return: office object
        """
        self.new_office = Office(
            'Senate',
            'Congress',
            False
        )

    def test_office_object_creation(self):
        """
        Test office object is initialized properly
        """
        self.assertEqual(self.new_office.office_name, 'Senate')
        self.assertEqual(self.new_office.office_type, 'Congress')
        self.assertFalse(self.new_office.is_occupied, False)

