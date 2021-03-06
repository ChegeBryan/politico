""" Tests for petition api endpoints """

from .base_test import BaseTestData

from app.api.db.petition_test_data import invalid_petition_data, petition

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

    def test_petition_input_data_validation(self):
        """Test api returns correct error response when petition input data
        fails validation
        : returns: STATUS CODE 400 Bad Request
        """

        response = self.client.post(
            '/api/v2/petitions', json=invalid_petition_data,
            headers={
                "Authorization": "Bearer {}".format(self.user_token)
            }
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 400)
        self.assertEqual(response.status_code, 400)

    def test_petition_endpoint_authentication(self):
        """Test api returns correct error response when petition POST
        petition is accessed without a authentication
        : returns: STATUS CODE 401 Unauthorized
        """

        response = self.client.post(
            '/api/v2/petitions', json=petition
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 401)
        self.assertEqual(response.status_code, 401)

    def test_petition_office_candidate_not_found(self):
        """Test api returns correct error response when office and candidate
        referenced does not exist
        : returns: STATUS CODE 404 Not found
       """

        response = self.client.post(
            '/api/v2/petitions',
            json={
                "office": 234,
                "contested_by": 2,
                "body": "some string",
                "evidence": ['https://image.url']
            },
            headers={
                "Authorization": "Bearer {}".format(self.user_token)
            }
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 404)
        self.assertEqual(json_body["message"],
                         "Office and candidate referenced does not exist.")
        self.assertEqual(response.status_code, 404)
