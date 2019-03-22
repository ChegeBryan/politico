# test part model

import unittest


from app.api.model.party import Party
from app.api.db.mock_db import MockDB
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

    def test_party_is_saved(self):
        """ Test party is saved on PARTIES list """
        save_changes(self.new_party)
        self.assertEqual(len(MockDB.PARTIES), 1)

    def test_multiple_parties_are_saved(self):
        """ Test PARTIES list has the saved parties """
        save_changes(self.new_party)
        add_party = Party('another party',
                          'another location',
                          'http://some.logo.url'
                        )
        save_changes(add_party)
        self.assertEqual(len(MockDB.PARTIES), 2)

    def tearDown(self):
        MockDB.PARTIES[:] = []
