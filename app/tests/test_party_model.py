# test part model

import unittest
import uuid


from app.api.model.party import Party

class TestPartyModel(unittest.TestCase):
    """ Test class for political party model """
    def setUp(self):
        """
        Creation of party object
        :arg: party_id, party_name, hq_address
        :return: party object
        """
        __id = str(uuid.uuid4())
        self.new_party = Party(
            'party name',
            'party location'
        )

    def test_party_object_creation(self):
        """
        Test party object is initialized properly
        """
        self.assertTrue(self.new_party.party_id)
        self.assertEqual(self.new_party.party_name, 'party name')
        self.assertEqual(self.new_party.hq_address, 'party location')
