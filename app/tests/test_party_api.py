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
        self.assertIsInstance(json_body["data"], list)
        self.assertEqual(response.status_code, 201)

    def test_zero_length_party_name(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no party name
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/parties',
            json=self.null_party_name_holder
        )
        json_data = response.get_json()
        self.assertIn("Party name cannot be empty",
                      json_data["error"]["party_name"])
        self.assertEqual(response.status_code, 400)

    def test_zero_length_hq_address(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no Headquarters details
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/parties',
            json=self.null_party_hq_holder
        )
        json_data = response.get_json()
        self.assertIn("Please provide party Headquarters address.",
                         json_data["error"]["hq_address"])
        self.assertEqual(response.status_code, 400)

    def test_zero_length_party_fields(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no Headquarters details and party name
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/parties',
            json=self.null_party_entries_holder
        )
        json_data = response.get_json()
        self.assertEqual(json_data["error"]["hq_address"], [
                         "Please provide party Headquarters address."])
        self.assertIn("Party name cannot be empty",
                      json_data["error"]["party_name"])
        self.assertEqual(response.status_code, 400)

    def test_party_name_cannot_contain_integer(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no party name
        : return STATUS CODE 400 Bad Request
        """
        self.client = self.app.test_client()
        response = self.client.post(
            '/api/v1/parties',
            json=self.int_party_name_holder
        )
        json_data = response.get_json()
        self.assertEqual(json_data["error"], {
                         "party_name": ["Party name cannot contain number(s)."]})
        self.assertEqual(response.status_code, 400)





