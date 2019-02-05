""" Tests for party api endpoints """

from .base_test import BaseTestData


class PartyAPITestCase(BaseTestData):
    """
    Class for testing api methods
    """

    def test_api_can_create_party(self):
        """
        Test api return correct status code on success
        : return STATUS CODE 201 Ok Created
        """

        #  app testing client
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/parties',
            json=self.party_holder
        )
        json_body = response.get_json()
        self.assertTrue(json_body["data"] == [{"party_name": "example name", "hq_address": "example location"}])
        self.assertEqual(response.status_code, 201)
