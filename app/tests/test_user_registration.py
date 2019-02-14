""" Tests for user registration """

from .base_test import BaseTestData

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



