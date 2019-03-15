""" Test user login and authentication """
import unittest

from app.api.db.user_test_data import (
    user_malformed_login_email, user_no_email, user_no_password, user_no_fields)
from .base_test import BaseTestData


class UserAuthTestCases(BaseTestData):
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
        self.assertTrue(json_body["data"][0]["token"])
        self.assertEqual(user_login.status_code, 200)

    def test_unregistered_user_login(self):
        """
        Test error is thrown when a unregistered user tries to login
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

    def test_password_missmatch(self):
        """
        Test error is thrown when a unregistered user tries to login
        STATUS CODE: 404 Not Found
        """
        # login user
        user_login = self.client.post(
            '/api/v2/auth/signin',
            json={
                "email": "email@exampl.com",
                "password": "different_password"
            }
        )
        json_body = user_login.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], "Incorrect user email or password.")
        self.assertEqual(user_login.status_code, 400)

    def test_malformed_login_email(self):
        """Test api returns an error when user attempts to login with \
        a malformed email
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signin', json=user_malformed_login_email
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], {
                         'email': ['Not a valid email address.']})
        self.assertEqual(response.status_code, 400)

    def test_missing_login_email(self):
        """Test api returns an error when user attempts to login with \
        missing email field in the request.
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signin', json=user_no_email
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], {
                         'email': ['Missing data for required field.']})
        self.assertEqual(response.status_code, 400)

    def test_missing_login_password(self):
        """Test api returns an error when user attempts to login with \
        missing email field in the request.
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signin', json=user_no_password
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], {
                         'password': ['Missing data for required field.']})
        self.assertEqual(response.status_code, 400)

    def test_missing_login_fields(self):
        """Test api returns an error when user attempts to login with \
        missing email field in the request. \
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signin', json=user_no_fields
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], {
            'email': ['Missing data for required field.'],
            'password': ['Missing data for required field.']})
        self.assertEqual(response.status_code, 400)

    def test_blacklisted_token_valid_logout(self):
        """ Test valid user logout
        : return STATUS CODE: 200 Ok
        """
        # register a user
        signup = self.user_data
        self.assertEqual(signup.status_code, 201)

        # login registered user
        signin = self.login_data
        json_body = signin.get_json()
        auth_token = json_body["data"][0]["token"]
        self.assertTrue(signin.status_code, 200)

        signout = self.client.post(
            '/api/v2/auth/signout', headers={
                "Authorization": "Bearer {}".format(auth_token)}
        )
        json_body = signout.get_json()
        self.assertEqual(json_body["status"], 200)
        self.assertEqual(json_body["message"], "Successfully logged out.")
        self.assertEqual(signout.status_code, 200)

    def test_invalid_token_logout(self):
        """ Test user cannot logout with invalid token
        :return: STATUS CODE: 403 Forbidden
        """
        # register user
        signup = self.user_data
        self.assertEqual(signup.status_code, 201)

        # login registered user
        signin = self.login_data
        self.assertTrue(signin.status_code, 200)

        signout = self.client.post(
            '/api/v2/auth/signout', headers={
                "Authorization": "Bearer {}".format('eyJ0.eXAi.OiJ4')}
        )
        json_body = signout.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"],
                         "Invalid token. PLease login again.")
        self.assertEqual(signout.status_code, 400)

    def test_missing_auth_token_logout(self):
        """ Test user user cannot logout without providing a token
        in the header
        :return: STATUS CODE: 400 Bad Request
        """
        # register user
        signup = self.user_data
        self.assertEqual(signup.status_code, 201)

        # login registered user
        signin = self.login_data
        self.assertTrue(signin.status_code, 200)

        # signout without providing an Authorization header
        signout = self.client.post(
            '/api/v2/auth/signout'
        )
        json_body = signout.get_json()
        self.assertEqual(json_body["status"], 403)
        self.assertEqual(json_body["message"], "Please provide a valid token.")
        self.assertEqual(signout.status_code, 403)

    def test_blacklisted_token_invalid_logout(self):
        """ Test user user cannot logout using a blacklisted token
        :return: STATUS CODE: 401 Unauthorized
        """
        # register user
        signup = self.user_data
        self.assertEqual(signup.status_code, 201)

        # login registered user
        signin = self.login_data
        json_body = signin.get_json()
        auth_token = json_body["data"][0]["token"]
        self.assertTrue(signin.status_code, 200)

        # signout without providing an Authorization header
        signout = self.client.post(
            '/api/v2/auth/signout', headers={
                "Authorization": "Bearer {}".format(auth_token)}
        )
        json_body = signout.get_json()
        self.assertEqual(json_body["status"], 200)
        self.assertEqual(json_body["message"], "Successfully logged out.")
        self.assertEqual(signout.status_code, 200)

        # signout again with a blacklisted token
        signout = self.client.post(
            '/api/v2/auth/signout', headers={
                "Authorization": "Bearer {}".format(auth_token)}
        )
        json_body = signout.get_json()
        self.assertEqual(json_body["status"], 401)
        self.assertEqual(json_body["error"], "User is logged out, Please log in again.")
        self.assertEqual(signout.status_code, 401)
