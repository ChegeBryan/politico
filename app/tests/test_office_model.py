# tests for office model

import unittest
import uuid


from app.api.model.office import Office
from app.api.db.mock_db import MockDB
from app.api.service.office import save_changes


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

    def test_office_object_creation(self):
        """
        Test office object is initialized properly
        """
        self.assertTrue(self.new_office.officeId)
        self.assertEqual(self.new_office.officeName, 'Senate')
        self.assertEqual(self.new_office.officeType, 'Congress')
        self.assertFalse(self.new_office.isOccupied, False)

    def test_office_is_saved(self):
        """ Test party is saved on PARTIES list """
        save_changes(self.new_office)
        self.assertEqual(len(MockDB.OFFICES), 1)
