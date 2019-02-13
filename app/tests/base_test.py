""" Data that will be used on tests for the party endpoints """

import unittest

from app import create_app
from .party_test_data import party_holder
from app.api.model.office import Office
from app.api.db.mock_db import MockDB


class BaseTestData(unittest.TestCase):
    """
    base test data
    """
    def setUp(self):
        """ Initialize app and the tests data """
        self.app = create_app('testing')
        self.client = self.app.test_client()

        # for all posts use this variable
        self.post_data = self.client.post(
            "/api/v1/parties", json=party_holder)

        # data to use for office test
        self.office = Office('senator', 'congress', False)
        self.office_holder = self.office.office_jsonified()
        self.invalid_office_name = Office('sene', "congress", False)
        self.invalid_office_name_holder = self.invalid_office_name.office_jsonified()
        self.invalid_office_type = Office('senator', "cong", False)
        self.invalid_office_type_holder = self.invalid_office_type.office_jsonified()
        # office post client
        self.office_data = self.client.post(
            '/api/v1/offices', json=self.office_holder
        )

    def tearDown(self):
        """ Empty party list for each test """
        MockDB.PARTIES[:] = []
        MockDB.OFFICES[:] = []
