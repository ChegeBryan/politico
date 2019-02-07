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

    def test_office_object_creation(self):
        """
        Test office object is initialized properly
        """
        self.assertTrue(self.new_office.officeId)
        self.assertEqual(self.new_office.officeName, 'Senate')
        self.assertEqual(self.new_office.officeType, 'Congress')
        self.assertFalse(self.new_office.isOccupied, False)
