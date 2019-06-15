""" Test office application registration endpoint """

from .base_test import BaseTestData
from app.api.db.application_test_data import (
    application, unregistered_party_application,
    unregistered_office_application)


class ApplicationApiTestCase(BaseTestData):
    """ Test case class for office application endpoint """

    def test_office_application_registration(self):
        """Test api endpoint return correct status code on office
        application registration
        : return STATUS CODE 201 Ok Created
        """
        response = self.office_application
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 201)
        self.assertEqual(json_body["data"][0]["createdBy"], 2)
        self.assertEqual(json_body["data"][0]["party"], 1)
        self.assertEqual(json_body["data"][0]["office"], 1)
        self.assertTrue(json_body["data"][0]["requested_on"])
        self.assertEqual(response.status_code, 201)

    def test_duplicate_user_application_registration(self):
        """Test api endpoint return correct status code when
        the same user tries to apply for an office more than once
        : return STATUS CODE 400 Bad Request
        """
        # initial registration
        response = self.office_application
        self.assertEqual(response.status_code, 201)

        # user applies again for an office
        apply_again = self.client.post(
            '/api/v2/office/application', json=application, headers={
                "Authorization": "Bearer {}".format(self.user_token)
            }
        )
        json_body = apply_again.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"],
                         "User has an application registered already.")
        self.assertEqual(apply_again.status_code, 400)

    def test_unregistered_party_application_registration(self):
        """Test api endpoint return correct status code when
        the user applies for office application with a party that does
        not exist
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/office/application',
            json=unregistered_party_application,
            headers={
                "Authorization": "Bearer {}".format(self.user_token)
            }
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"],
                         "Party or office referenced does not exists.")
        self.assertEqual(response.status_code, 400)

    def test_unregistered_office_application_registration(self):
        """Test api endpoint return correct status code when
        the user applies for office application with an office that
        does not exist
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v2/office/application',
            json=unregistered_office_application,
            headers={
                "Authorization": "Bearer {}".format(self.user_token)
            }
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(json_body["error"],
                         "Party or office referenced does not exists.")
        self.assertEqual(response.status_code, 400)
