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

    def test_unregistered_user_login(self):
        """
        Test error is thrown when a unregistered user trys to login
        STATUS CODE: 404 Not Found
        """
        # login user
        user_login = self.client.post(
            '/api/v2/auth/signin',
            json={
                "email": "non_existent@politico.com",
                "password": "some_password"
            }
        )
        json_body = user_login.get_json()
        self.assertEqual(json_body["status"], 404)
        self.assertEqual(json_body["message"], "User does not exists.")
        self.assertEqual(user_login.status_code, 404)





