""" Test the blacklist model """

import unittest

from app.api.model.blacklist import BlacklistToken


class BlacklistTokenTestCases(unittest.TestCase):
    """ Test cases class for the blacklist token model class """

    def setUp(self):
        """ create a token instance """
        dummy_token = "gutgntogntggtgintgjrngernssd"
        self.blacklist_token = BlacklistToken(
            token=dummy_token
        )

    def test_blacklist_object_creation(self):
        """ Test the blacklist token class creates the token passed properly """
        self.assertTrue(self.blacklist_token.blacklisted_on)
        self.assertEqual(self.blacklist_token.token[0],
                         "gutgntogntggtgintgjrngernssd")


