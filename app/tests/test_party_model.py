# test part model

import unittest


from app.api.model.party import Party
from app.api.service.party import save_changes


class TestPartyModel(unittest.TestCase):
    """ Test class for political party model """

    def setUp(self):
        """
        Creation of party object
        :arg: party_id, party_name, hq_address
        :return: party object
        """
        self.new_party = Party(
            'party name',
            'party location',
            'http://some.logo.url'
        )

    def test_party_object_creation(self):
        """
        Test party object is initialized properly
        """
        self.assertEqual(self.new_party.party_name, 'party name')
        self.assertEqual(self.new_party.hq_address, 'party location')
        self.assertEqual(self.new_party.logo_url, 'http://some.logo.url')

