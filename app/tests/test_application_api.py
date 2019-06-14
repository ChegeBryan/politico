""" Test office application registration endpoint """

from .base_test import BaseTestData


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
