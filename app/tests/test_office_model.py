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

    def test_office_is_saved(self):
        """ Test party is saved on PARTIES list """
        save_changes(self.new_office)
        self.assertEqual(len(MockDB.OFFICES), 1)

    def test_multiple_offices_are_saved(self):
        """ Test PARTIES list has the saved parties """
        save_changes(self.new_office)
        add_office = Office('House of Respresentatives', 'Congress', False)
        save_changes(add_office)
        self.assertEqual(len(MockDB.OFFICES), 2)

    def tearDown(self):
        MockDB.OFFICES[:] = []
