""" Tests for the vote endpoints """

from .base_test import BaseTestData
from app.api.db.vote_test_data import vote


class VoteAPITestCases(BaseTestData):
    """ Test class for votes endpoint """

    def test_vote_registration(self):
        """ Test api return correct status code and message when vote
        is registered successfully
        Returns: STATUS CODE 201 Created
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
        Returns: STATUS CODE 401 Unauthorized
        """
        # register a vote
        response = self.client.post(
            '/api/v2/votes', json=vote, headers={
                "Authorization": "Bearer {}".format("malformed_token")
            }
        )
        self.assertEqual(response.status_code, 401)

    def test_vote_duplication(self):
        """Test api returns correct error response when a user tries to vote
        twice for the same office
        Return: STATUS CODE 409 Conflict
        """
        # get user logged in token
        auth_token = self.user_token

        # register same vote created at setup
        response = self.client.post(
            '/api/v2/votes', json=vote, headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 409)
        self.assertEqual(json_body["error"], "Vote already cast for office.")
        self.assertEqual(response.status_code, 409)

    def test_office_candidate_referenced(self):
        """Test api returns correct error response when office & candidate
        combination referenced does not exists
        Return: STATUS CODE 404 Bad Request
        """
        # get user logged in token
        auth_token = self.user_token

        # register same vote created at setup
        response = self.client.post(
            '/api/v2/votes', json={
                "office": 234,
                "candidate": 345
            },
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 404)
        self.assertEqual(json_body["error"],
                         "Candidate and office referenced does not exist.")
        self.assertEqual(response.status_code, 404)
