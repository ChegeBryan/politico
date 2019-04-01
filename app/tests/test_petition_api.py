""" Tests for petition api endpoints """

from .base_test import BaseTestData


class PetitionAPITestCase(BaseTestData):
    """ petition endpoint api tests """

    def test_create_petition(self):
        """ Test api returns correct status code on success
        : return STATUS CODE 201 Ok Created
        """
        response = self.petition
        json_body = response.get_json()
        data = json_body["data"]
        self.assertEqual(json_body["status"], 201)
        self.assertEqual(data["office"], 1)
        self.assertEqual(data["created_by"], 2)
        self.assertEqual(data["contested_by"], 2)
        self.assertEqual(data["body"], "some string")
        self.assertIsInstance(data["evidence"], list)
        self.assertEqual(response.status_code, 201)

