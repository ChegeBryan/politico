""" Data that will be used on tests for the party endpoints """

import unittest

from app import create_app


class BaseTestData(unittest.TestCase):
    """
    base test data
    """
    def setUp(self):
        """ Initialize app and the tests data """
        self.app = create_app('testing')
