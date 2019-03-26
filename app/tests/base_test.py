""" Data that will be used on tests for the party endpoints """

import unittest

from app import create_app
from app.api.db.party_test_data import party_holder
from app.api.db.office_test_data import office_holder
from app.api.db.user_test_data import user, user_logins, admin_login
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

        # admin login
        self.admin_signin = self.client.post(
            "/api/v2/auth/signin", json=admin_login
        )
        # get the admin auth token
        self.admin_token = self.admin_signin.get_json()["data"][0]["token"]

        # for all posts use this variable
        # admin authorization header token
        self.post_data = self.client.post(
            "/api/v2/parties", json=party_holder, headers={
                "Authorization": "Bearer {}".format(self.admin_token)
            }
        )

        # office post client
        # admin authorization header token
        self.office_data = self.client.post(
            '/api/v2/offices', json=office_holder, headers={
                "Authorization": "Bearer {}".format(self.admin_token)
            }
        )

        # post a user
        self.user_data = self.client.post(
            '/api/v2/auth/signup', json=user
        )

        # login user
        self.login_data = self.client.post(
            '/api/v2/auth/signin', json=user_logins
        )

    def tearDown(self):
        """ destroy the database """
        with self.app.app_context():
            db = AppDatabase()
            db.drop_all()
