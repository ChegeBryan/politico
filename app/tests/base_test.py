""" Data that will be used on tests for the party endpoints """

import unittest

from app import create_app
from app.api.db.party_test_data import party_holder
from app.api.db.office_test_data import office_holder
from app.api.db.user_test_data import user
from app.api.db.mock_db import MockDB
from app.api.db.database import AppDatabase


class BaseTestData(unittest.TestCase):
    """
    base test data
    """

    def setUp(self):
        """ Initialize app and the tests data """
        self.app = create_app('testing')
        with self.app.app_context():
            self.client = self.app.test_client()

        # for all posts use this variable
        self.post_data = self.client.post(
            "/api/v1/parties", json=party_holder)

        # office post client
        self.office_data = self.client.post(
            '/api/v1/offices', json=office_holder
        )

        # post a user
        self.user_data = self.client.post(
            '/api/v2/auth/signup', json=user
        )

    def tearDown(self):
        """ Empty party list for each test """
        MockDB.PARTIES[:] = []
        MockDB.OFFICES[:] = []
        with self.app.app_context():
            db = AppDatabase()
            db.drop_all()
