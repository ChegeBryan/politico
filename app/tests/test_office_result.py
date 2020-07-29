""" Test for election office results """

from .base_test import BaseTestData


class OfficeResultsAPITestCases(BaseTestData):
    """ Test cases for office results """

    def test_get_office_results(self):
        """Test api returns the correct status code and response message
        : return STATUS CODE 200 Ok
        """
        response = self.office_results
        json_data = response.get_json()
        data = json_data["data"][0]
        self.assertEqual(json_data["status"], 200)
        self.assertEqual(data["office"], 1)
        self.assertEqual(data["candidate"], 2)
        self.assertEqual(data["result"], 1)

    def test_no_results_found(self):
        """Test API returns the correct response message and status code
        when the office referenced has no votes or does not exist
        :return STATUS CODE 404 Not Found
        """
        # get logged in user token
        auth_token = self.user_token

        response = self.client.get(
            '/api/v2/office/232/result', headers={
                'Authorization': 'Bearer {}'.format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data['status'], 404)
        self.assertEqual(json_data['message'], "Results requested not found.")
        self.assertEqual(response.status_code, 404)

    def test_result_endpoint_authentication(self):
        """Test result endpoint is protected
        : return STATUS CODE 402 Unauthorized
        """

        response = self.client.get(
            '/api/v2/office/1/result'
        )
        json_data = response.get_json()
        self.assertEqual(json_data['status'], 401)
        self.assertEqual(response.status_code, 401)
