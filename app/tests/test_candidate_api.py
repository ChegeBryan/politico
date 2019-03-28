""" Tests for candidate registration endpoint """

from .base_test import BaseTestData


class CandidateAPITestCases(BaseTestData):
    """ Test case class for candidate registration API """

    def test_candidate_registration(self):
        """Test api return the correct status code on success
        candidate registration
        : return STATUS CODE 201 Ok Created
        """
        response = self.register_candidate
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 201)
        self.assertEqual(json_body["data"][0]["party"], 1)
        self.assertEqual(json_body["data"][0]["office"], 1)
        self.assertEqual(json_body["data"][0]["candidate"], 2)
        self.assertTrue(json_body["data"][0]["registered_on"])
        self.assertEqual(response.status_code, 201)
