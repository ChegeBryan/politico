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
