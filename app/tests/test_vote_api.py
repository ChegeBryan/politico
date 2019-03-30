""" Tests for the vote endpoints """

from .base_test import BaseTestData
from app.api.db.vote_test_data import vote


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

    def test_auth_token_error(self):
        """Test api returns correct error code when the provided
        and error is encountered during token decoding not provide a valid token.
        """
        # register a vote
        response = self.client.post(
            '/api/v2/votes', json=vote, headers={
                "Authorization": "Bearer {}".format("malformed_token")
            }
        )
        self.assertEqual(response.status_code, 401)
