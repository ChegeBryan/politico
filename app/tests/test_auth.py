""" Test user login and authentication """
import unittest

from .base_test import BaseTestData


class UserAuthTesCases(BaseTestData):
    """
    Test cases class for testing user login and authentication
    """

    def test_registered_user_login(self):
        """
        Test if a registered user can login to the system.
        STATUS CODE: 200 Ok
        """
        # register a user
        register_user = self.user_data
        self.assertEqual(register_user.status_code, 201)

        # login registered user
        user_login = self.login_data
        json_body = user_login.get_json()
        self.assertEqual(json_body["status"], 200)
        self.assertEqual(json_body["message"], "Successfully logged in.")
        self.assertEqual(user_login.status_code, 200)






