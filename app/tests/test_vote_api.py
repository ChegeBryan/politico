""" Tests for the vote endpoints """

from .base_test import BaseTestData


class VoteAPITestCases(BaseTestData):
    """ Test class for votes endpoint """

    def test_vote_registration(self):
        """ Test api return correct status code and message when vote
        is registered successfully
        """
        response = self.cast_vote
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 201)
        self.assertEqual(json_body["data"][0]["created_by"], 2)
        self.assertEqual(json_body["data"][0]["office"], 1)
        self.assertEqual(json_body["data"][0]["candidate"], 2)
        self.assertTrue(json_body["data"][0]["created_on"])
        self.assertEqual(response.status_code, 201)
