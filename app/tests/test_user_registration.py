""" Tests for user registration """

from .base_test import BaseTestData
from app.api.db.user_test_data import (
    user_null_values, user_names_integer, user_invalid_email,
    user_invalid_passporturl, user_same_email, user_same_passport)

class UserRegistrationTestCases(BaseTestData):
    """
    Class for testing api methods
    """

    def test_user_registration(self):
        """Test api return correct status code on successful user registration
        : return STATUS CODE 201 Ok Created
        """
        response = self.user_data
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 201)
        self.assertEqual(response.status_code, 201)

    def test_zero_length_fields(self):
        """Test api returns an error when user attempts to register user with no field values
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signup', json=user_null_values
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(response.status_code, 400)

    def test_person_names_contain_integer(self):
        """Test api returns an error when user attempts to register user with no person names that contain integers
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signup', json=user_names_integer
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], {
                         "firstname": ["Person name cannot contain number(s)."],
                         "lastname": ["Person name cannot contain number(s)."],
                         "othername": ["Person name cannot contain number(s)."]
                         })
        self.assertEqual(response.status_code, 400)

    def test_invalid_email(self):
        """Test api returns an error when user attempts to register user with an invalid email
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signup', json=user_invalid_email
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], {
                         'email': ['Not a valid email address.']})
        self.assertEqual(response.status_code, 400)

    def test_invalid_passporturl(self):
        """Test api returns an error when user attempts to register user with no invalid passport url
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/auth/signup', json=user_invalid_passporturl
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"], {
                         'passportUrl': ['Not a valid URL.']})
        self.assertEqual(response.status_code, 400)

    def test_duplicate_user_registration_email(self):
        """
        Test api returns error message on attempt to register party
        with a user with the same email address
        :return STATUS CODE 409 Conflict
        """
        response = self.user_data
        self.assertEqual(response.status_code, 201)
        response_2 = self.client.post(
            'api/v2/auth/signup', json=user_same_email
        )
        json_body = response_2.get_json()
        self.assertEqual(json_body["status"], 409)
        self.assertTrue(json_body["error"] == "Try a different email.")

    def test_duplicate_user_registration_passport(self):
        """
        Test api returns error message on attempt to register party
        with a user with the same passport url
        :return STATUS CODE 409 Conflict
        """
        response = self.user_data
        self.assertEqual(response.status_code, 201)
        response_2 = self.client.post(
            'api/v2/auth/signup', json=user_same_passport
        )
        json_body = response_2.get_json()
        self.assertEqual(json_body["status"], 409)
        self.assertTrue(json_body["error"] == "Try a different passport uri.")


